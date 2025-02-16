import streamlit as st
import random
import numpy as np
from openai import OpenAI

calisthenics_exercises = [
    {
        "category": "Upper Body",
        "exercises": [
            "Push-Ups",
            "Dips",
            "Pull-Ups",
            "Inverted Rows",
            "Bicep Dips",
            "Tricep Dips"
        ]
    },
    {
        "category": "Lower Body",
        "exercises": [
            "Bodyweight Squats",
            "Jump Squats",
            "Foward Lunges",
            "Side Lunges",
            "Hip Thrusts",
            "Box Jumps",
            "Calf Raises"
        ]
    },
    {
        "category": "Core",
        "exercises": [
            "Plank",
            "Leg Raises",
            "Russian Twists",
            "Leg Raises",
            "Bicycle Crunches"
        ]
    },
    {
        "category": "Full Body",
        "exercises": [
            "Burpees",
            "Mountain Climbers",
            "Bear Crawls",
            "High Knees",
            "Jump Lunges"
        ]
    },
    {
        "category": "Mobility",
        "exercises": [
            "Leg Swings",
            "Arm Circles",
            "Shoulder Stretch",
            "Spinal Twists",
        ]
    },
    {
        "category": "Cardio",
        "exercises": [
            "Jumping Jacks",
            "Running on the Spot"
            "Jump Rope"
        ]
    }
]

def generate_workout(exercise_selection, total_time, age, experience_level):
    
    # Find the exercises for the given focus
    client = OpenAI(api_key="sk-de117b858d9640248b4c0841954eeed7")

   # Assuming the variables exercise_selection, total_time, age, experience_level, and calisthenics_exercises are defined

    prompt = f"""
    Create a workout, a calisthenics circuit, for the user. Focus: {exercise_selection}. Duration: {total_time} minutes. Make sure each exercise lasts for at least 30 seconds.
    Additionally, you must take into account these factors when thinking about the endurance and length of each exercise: Age {age}. Experience Level: {experience_level}.
    Depending on the focus, you can only choose exercises from this list: {calisthenics_exercises}
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a fitness assistant. Please maintain a respectful and enthusiastic attitude as you give a detailed fitness circuit based on the user's profile"},
            {"role": "user", "content": prompt},
        ]
    )

    print(response.choices[0].message.content)

def main():
    st.title("Fitness Circuit Designer")

    age = st.slider("Current Age", 14, 65, 14)
    workout_duration = st.slider("How much time are you willing to put into today's workout? (Minutes)", 1, 10, 1)

    # Input fields for height and weight
    height = st.number_input("Enter your height (cm):", min_value=135, max_value=220, step=1)
    weight = st.number_input("Enter your weight (lbs):", min_value=60, max_value=400, step=1)

    exercise_options = ["Upper Body", "Lower Body", "Full Body", "Mobility", "Core", "Cardio"] #maybe add cardio and isometrics
    exercise_selection = st.multiselect("Select your focus areas:", exercise_options)

    sex_selection = st.selectbox("Enter your sex:", [
        "  ",
        "Male",
        "Female"
    ])

    # Dropdown for experience level
    experience_level = st.selectbox("How many days of the week do you spend working out?:", [
        "Sedentary (1 Day or None)",
        "Moderate (2-4 Times Per Week)",
        "Active (5+ Times Per Week)"
    ])

    if experience_level == "Sedentary (1 Day or None)":
        experience_level_readable = "Sedentary"
    elif experience_level ==  "Moderate (2-4 Times Per Week)":
        experience_level_readable = "Moderate"
    elif experience_level == "Active (5+ Times Per Week)":
        experience_level_readable = "Active"

    # Display the inputs creatively using columns
    if height and weight and experience_level and sex_selection != "  " and exercise_selection:
        st.markdown("---")
        st.subheader("Your Profile")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Height", f"{height} cm")
            st.metric("Weight", f"{weight} lbs")
            st.metric("Age", f"{age} years")
        with col2:
            st.metric("Sex", sex_selection)
            st.metric("Activity Level", experience_level_readable)
            st.metric("Workout Duration", f"{workout_duration} min")

        st.subheader("Selected Exercise Focus:")
        st.write(", ".join(exercise_selection) if exercise_selection else "None")

        st.markdown("---")

        if st.button("Generate Workout"):
            st.subheader("Your Workout Routine")
            generate_workout(workout_duration, exercise_selection, age, experience_level)

    st.markdown("---")


if __name__ == "__main__":
    main()

