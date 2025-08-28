import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Get the working directory of the script
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load saved models
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/parkinsons_model.sav', 'rb'))
# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Function to check if inputs are valid numbers
def are_inputs_valid(inputs):
    try:
        return [float(x) for x in inputs if x.strip() != '']
    except ValueError:
        return None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    
    # code to ensure valid inputs
    def are_inputs_valid(inputs):
        try:
            return [float(x) for x in inputs if x.strip() != '']
        except ValueError:
            return None

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = are_inputs_valid(user_input)

        # Ensure all inputs are valid before making a prediction
        if user_input is not None and len(user_input) == 8:
            diab_prediction = diabetes_model.predict([user_input])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        else:
            st.error("Please fill all fields with valid numeric values.")

    st.success(diab_diagnosis)

    # Recommendation Box for Diabetes
    if diab_diagnosis:
        with st.expander("Recommendations for Diabetes"):
            if diab_prediction[0] == 1:
                st.write("### Do's:")
                st.write("- Monitor your blood sugar levels regularly.")
                st.write("- Follow a balanced, low-carb diet.")
                st.write("- Exercise regularly to maintain a healthy weight.")
                st.write("- Take prescribed medications and insulin as advised.")
                st.write("- Stay hydrated and avoid sugary drinks.")

                st.write("### Don'ts:")
                st.write("- Do not skip meals.")
                st.write("- Avoid foods high in sugar and fats.")
                st.write("- Don't neglect your regular checkups.")
            else:
                st.write("### Do's:")
                st.write("- Maintain a healthy lifestyle with a balanced diet and exercise.")
                st.write("- Keep an eye on your blood sugar levels periodically.")
                st.write("- Stay hydrated and maintain a healthy weight.")

                st.write("### Don'ts:")
                st.write("- Avoid sugary snacks and drinks.")
                st.write("- Don't ignore any symptoms related to diabetes.")
                st.write("- Avoid sedentary behavior and excessive stress.")


    # Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_diagnosis = ''

    # function to validate and convert inputs to float
    def are_inputs_valid(inputs):
        try:
            return [float(x) for x in inputs if x.strip() != '']
        except ValueError:
            return None

    # button to trigger prediction
    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = are_inputs_valid(user_input)

        # Ensure inputs are valid before making prediction
        if user_input is not None and len(user_input) == 13:
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        else:
            st.error("Please fill all fields with valid numeric values.")

    st.success(heart_diagnosis)

    # Recommendations Box for Heart Disease
    if heart_diagnosis:
        with st.expander("Recommendations for Heart Disease"):
            if heart_prediction[0] == 1:
                st.write("### Do's:")
                st.write("- Follow a heart-healthy diet, including plenty of fruits and vegetables.")
                st.write("- Engage in regular physical activity, such as walking or swimming.")
                st.write("- Take medications prescribed by your doctor.")
                st.write("- Monitor your blood pressure and cholesterol levels.")
                st.write("- Stay hydrated and reduce salt intake.")

                st.write("### Don'ts:")
                st.write("- Avoid smoking or exposure to secondhand smoke.")
                st.write("- Don't consume foods high in saturated fats and cholesterol.")
                st.write("- Avoid excessive alcohol consumption.")
                st.write("- Don't ignore chest pain or other heart-related symptoms.")
            else:
                st.write("### Do's:")
                st.write("- Maintain a healthy diet rich in fiber, fruits, and vegetables.")
                st.write("- Exercise regularly to keep your heart healthy.")
                st.write("- Monitor your blood pressure, cholesterol, and weight.")
                st.write("- Limit salt intake and stay hydrated.")

                st.write("### Don'ts:")
                st.write("- Don't smoke or consume too much alcohol.")
                st.write("- Avoid stress and long periods of inactivity.")
                st.write("- Don't neglect regular medical checkups.")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    # function to validate and convert inputs to float
    def are_inputs_valid(inputs):
        try:
            return [float(x) for x in inputs if x.strip() != '']
        except ValueError:
            return None

    # button to trigger prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = are_inputs_valid(user_input)

        # Ensure inputs are valid before making prediction
        if user_input is not None and len(user_input) == 22:
            parkinsons_prediction = parkinsons_model.predict([user_input])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        else:
            st.error("Please fill all fields with valid numeric values.")

    st.success(parkinsons_diagnosis)

    # Recommendations Box for Parkinson's Disease
    if parkinsons_diagnosis:
        with st.expander("Recommendations for Parkinson's Disease"):
            if parkinsons_prediction[0] == 1:
                st.write("### Do's:")
                st.write("- Consult a neurologist regularly for medication management.")
                st.write("- Engage in physical therapy and exercises to improve mobility.")
                st.write("- Consider speech therapy to maintain clear communication.")
                st.write("- Follow a healthy diet to support brain function and overall health.")

                st.write("### Don'ts:")
                st.write("- Don't neglect your symptoms or stop medication without consulting your doctor.")
                st.write("- Avoid excessive alcohol consumption and recreational drugs.")
                st.write("- Don't lead a sedentary lifestyle; regular movement is essential.")
                st.write("- Don't ignore mental health symptoms such as anxiety or depression.")

            else:
                st.write("### Do's:")
                st.write("- Maintain a balanced diet with plenty of antioxidants.")
                st.write("- Stay active and engage in regular exercise, like walking or swimming.")
                st.write("- Monitor your health with regular checkups and screenings.")
                st.write("- Stay mentally engaged by reading, solving puzzles, or learning new skills.")

                st.write("### Don'ts:")
                st.write("- Don't smoke, as it may worsen overall health.")
                st.write("- Avoid overexerting yourself physically.")
                st.write("- Don't skip regular health checkups to monitor other conditions.")
