import streamlit as st
import random
import numpy as np
import openai

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
    selected_exercises = []
    print("Selected Exercises:")
    for category in exercise_selection:
        for item in calisthenics_exercises:
            if item["category"] == category:
                print(f"\n{category} Exercises:")
                for exercise in item["exercises"]:
                    print(f"- {exercise}")
                    # Add the exercise to the routine list
                    selected_exercises.append(exercise)

    # Calculate time per exercise (simple division, can be enhanced)
    time_per_exercise = total_time * 60 // len(selected_exercises) if selected_exercises else 0
    routine = [(exercise, time_per_exercise) for exercise in selected_exercises]

    return routine

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
            routine = generate_workout(exercise_selection, workout_duration, age, experience_level)
            st.subheader("Your Workout Routine")
            for exercise, secs in routine:
                st.markdown(f"- **{exercise}** for {secs} seconds")


    st.markdown("---")


if __name__ == "__main__":
    main()

