# Fitness Circuit Designer with Heart Monitor Integration

Our team's submission for MakeUofT 2025 for wearable technology.
This is a Streamlit-based web application that helps users design custom fitness circuits based on their exercise preferences, fitness levels, and workout duration. Additionally, this system is integrated with a heart monitor that reads ECG data and displays it in real-time on the interface.

---

## Features
- Customizable workout routines based on:
  - Focus areas (Upper Body, Lower Body, Core, Cardio, Mobility, Full Body)
  - Activity level (Sedentary, Moderate, Active)
  - Age, Height, Weight, and Sex
  - Total workout duration
- Real-time heart monitoring:
  - Displays ECG data on the screen for live heart rate tracking during the workout.

---

## Technologies Used
- **Streamlit**: For the web application interface.
- **Python**: Core programming language.
- **Heart Monitor Integration**:
  - Reads ECG data and displays it on the dashboard.
  - Designed for compatibility with most commercial heart rate monitors.

---

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <project-folder>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Connect the heart monitor:
    - Ensure the heart monitor is paired with your system.
    - Check the connection settings in the `index.py` file if necessary.

---

## Usage
1. Start the Streamlit application:
    ```sh
    streamlit run index.py
    ```

2. Open your browser and navigate to the local host URL provided by Streamlit.

3. Input your profile details:
    - Age, Height, Weight, and Sex
    - Select focus areas and activity level
    - Choose the workout duration

4. Click on **Generate Workout** to see a customized fitness circuit. The routine is generated using a simple for loop to filter exercises based on your selection.

5. Real-time ECG data from the heart monitor will be displayed on the screen during the workout.

---

## Future Enhancements
- Add more exercises and categories.
- Enhance ECG visualization with detailed heart rate analytics.
- Improve user experience with additional customization options.

---

## Acknowledgements
- Streamlit for the web application framework

---

## Contact
For any questions or issues, feel free to reach out via GitHub or email.

---

Enjoy your personalized fitness routine and stay healthy!
