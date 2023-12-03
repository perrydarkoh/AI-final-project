import streamlit as st
from joblib import load
import pandas as pd

# Load the best model
model = load('best_model.joblib')

def predict(input_data):
    # Convert the input data into a DataFrame with the correct feature names
    feature_names = ['extra_paid_classes', 'grade_2', 'grade_1']
    input_df = pd.DataFrame([input_data], columns=feature_names)
    return model.predict(input_df)

def main():
    # Add a homepage section
    st.title('Students Learning Type Suggestion')
    st.write(
        "Welcome to the Students Learning Type Suggestion website! "
        "This tool helps you understand what type of learning approach "
        "is suitable for a student based on their characteristics."
    )
    
    # Define input fields for the features
    extra_paid_classes = st.selectbox('Extra Paid Classes', ['Yes', 'No'])
    extra_paid_classes = 1 if extra_paid_classes == 'Yes' else 0

    # Limit the maximum value for grade inputs to 20
    grade_2 = st.number_input('Grade 2', min_value=0.0, max_value=20.0, format='%f')
    grade_1 = st.number_input('Grade 1', min_value=0.0, max_value=20.0, format='%f')

    if st.button('Predict'):
        input_data = {
            'extra_paid_classes': extra_paid_classes,
            'grade_2': grade_2,
            'grade_1': grade_1,
        }

        result = predict(input_data)
        result_value = result[0]

        # Display the prediction
        if 0 <= result_value < 50:
            st.error(f'The predicted output is: **{result_value}** (The student could use more attention from teachers)')
        elif 50 <= result_value < 70:
            st.warning(f'The predicted output is: **{result_value}** (The student could use extra learning materials)')
        elif result_value >= 70:
            st.success(f'The predicted output is: **{result_value}** (The student is doing a good job and should keep it up)')

if __name__ == '__main__':
    main()
