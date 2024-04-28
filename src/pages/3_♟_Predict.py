import streamlit as st
import pandas as pd
import numpy as np
import joblib  
import os 
from sklearn.preprocessing import LabelEncoder
from catboost import CatBoostClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier
from  PIL import Image
from src.auth import login_form, is_authenticated

st.set_page_config(
    page_icon= "🔮",
    page_title= "Predict",
    layout = "wide"
)

def main():
    login_form()
    if is_authenticated():
        col1, col2 = st.columns(2)
        with col1:
            st.title(f"**Predict income 💰**")
            st.write(
                """
                This app helps you predict individuals income above or below threshold amount(50k).
                """
            )
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            # select models
            selected_model = st.selectbox(label='Select Model', options=['Catboost', 'Random Forest'], key= 'selected_model')
        with col2:
            # display GIF
            gif_path = 'assets/images/money-count.gif'
            st.image(
            gif_path, use_column_width=True
            )

        

        #  session state
        if 'final_prediction' not in st.session_state:
            st.session_state.final_prediction = None

        # Create a form for user input
    
        with st.form(key='user_input_form', clear_on_submit=True):
            st.header('**User Input**⚪')
            cola,colb  = st.columns(2)
            with cola:
                st.header('**Numerical Columns**⚫')
            with colb:
                st.header('**String Columns**🔴')
                
            col3, col4, col5, col6 = st.columns(4)
            with col3:
                age = st.number_input(label='Age', min_value= 0, value= 'min')
                employment_stat = st.number_input(label='Has Own Business Or Is Self Employed', min_value= 0, max_value= 2, value='min')
                wage_per_hour = st.number_input(label='Wage Per Hour', min_value=0 , value = 'min')
                working_week_per_year = st.number_input(label='Weeks Worked In A Year', min_value= 0, max_value=52, value= 'min')
                industry_code = st.number_input(label='Industry_code', min_value= 0 , max_value=51 , value='min')
                occupation_code = st.number_input(label='Occupation_code', min_value= 0, value= 'min')

            with col4:
                total_employed = st.number_input(label='Num Persons Worked For Employer', min_value=0 , value= 'min')
                gains = st.number_input(label='Gains', min_value= 0)
                losses = st.number_input(label='Losses', min_value=0)
                stocks_status = st.number_input(label='Divdends From Stocks', min_value= 0, value = 'min')
                mig_year = st.number_input(label='Migration Year', min_value= 94, max_value=95 , value = 'min')
                importance_of_record = st.number_input(label='Weight Of Instance', min_value= 100)

            with col5:
                gender = st.selectbox(label='Gender', options=['Male', 'Female'])
                education = st.selectbox(label='Education', options=[' High school graduate' ,' 12th grade no diploma', ' Children',
                                                                    ' Bachelors degree(BA AB BS)', ' 7th and 8th grade', ' 11th grade',
                                                                    ' 9th grade', ' Masters degree(MA MS MEng MEd MSW MBA)', ' 10th grade',
                                                                    ' Associates degree-academic program' ,' 1st 2nd 3rd or 4th grade',
                                                                    ' Some college but no degree' ,' Less than 1st grade',
                                                                    ' Associates degree-occup /vocational',
                                                                    ' Prof school degree (MD DDS DVM LLB JD)', ' 5th or 6th grade',
                                                                    ' Doctorate degree(PhD EdD)'
                                                                    ]
                )
                marital_status = st.selectbox(label='Marital_status', options=[' Widowed', ' Never married', ' Married-civilian spouse present',
                                                                            ' Divorced' ,' Married-spouse absent', ' Separated',
                                                                            ' Married-A F spouse present'
                                                                            ]
                )
                race = st.selectbox(label='Race', options=[' White', ' Black', ' Asian or Pacific Islander',
                                                        ' Amer Indian Aleut or Eskimo' ,' Other'
                                                        ]
                )
                is_hispanic = st.selectbox(label='Hispanic Origin', options=[' All other' ,' Mexican-American' ,' Central or South American',
                                                                            ' Mexican (Mexicano)', ' Puerto Rican' ,' Other Spanish' , ' Cuban',
                                                                            ' Do not know' ,' Chicano'
                                                                            ]
                )
                household_summary = st.selectbox(label='Household Summary In Household', options=[' Householder' ,' Child 18 or older' ,' Child under 18 never married',
                                                                                                ' Spouse of householder', ' Nonrelative of householder',
                                                                                                ' Other relative of householder' ,' Group Quarters- Secondary individual',
                                                                                                ' Child under 18 ever married'
                                                                                                ]
                )
            with col6:
                tax_status = st.selectbox(label='Tax Filer Status', options=[' Head of household', ' Single' , ' Nonfiler' ,' Joint both 65+',
                                                                            ' Joint both under 65', ' Joint one under 65 & one 65+'
                                                                            ]
                )
                citizenship = st.selectbox(label='Citizenship', options=['Native' ,' Foreign born- Not a citizen of U S ',
                                                                        ' Foreign born- U S citizen by naturalization',
                                                                        ' Native- Born abroad of American Parent(s)',
                                                                        ' Native- Born in Puerto Rico or U S Outlying'
                                                                        ]
                )
                work_class = st.selectbox(label='Class Of Worker', options=[' Federal government', ' Private', ' Local government',
                                                                            ' Self-employed-incorporated', ' Self-employed-not incorporated',
                                                                            ' State government', ' Without pay', ' Never worked'
                                                                            ]
                )
            submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            pipeline, encoder = select_model(selected_model)
            
            # Single-row DataFrame directly from user input values 
            df = pd.DataFrame({
                      'age': age,
                      'employment_stat': employment_stat,
                      'wage_per_hour': wage_per_hour,
                      'working_week_per_year': working_week_per_year,
                      'industry_code': industry_code,
                      'occupation_code': occupation_code,
                      'total_employed': total_employed,
                      'gains': gains,
                      'losses': losses,
                      'stocks_status': stocks_status,
                      'mig_year': mig_year,
                      'gender': gender,
                      'education': education,
                      'marital_status': marital_status,
                      'race': race,
                      'work_class': work_class,
                      'is_hispanic': is_hispanic,
                      'household_summary': household_summary,
                      'tax_status': tax_status,
                      'importance_of_record': importance_of_record,
                      'citizenship': citizenship
            }, index=[0]) 

            make_prediction(pipeline, df)
           
            # prediction and probability
            if st.session_state.final_prediction is not None:
                col7, col8 = st.columns(2)
                with col7:
                    if st.session_state.final_prediction == "Below Limit😟":
                        # display GIF
                        emoji_path = 'assets/images/worried_face_emoji.png'
                        st.image(emoji_path,width = 400)
                    else:
                        # display GIF
                        emoji_path = 'assets/images/grinning_emoji.png'
                        st.image(emoji_path, width =400)
                with col8:
                    st.write(f'**🏧 Income Prediction: {st.session_state.final_prediction}**')
                    st.write(f'**✨ Probability of income above limit is: {st.session_state.final_probability:.1f}%**')
        
    else:
        st.error("Please log in to access the App.")

# Load CatBoost model
@st.cache_resource()
def load_catboost():
    Catboost = joblib.load('models/catboost_pipeline_thresh 1.pkl')
    return Catboost

# Load Random Forest model
@st.cache_resource()
def load_rf():
    try:
        rf = joblib.load('models/rf_pipeline_thresh 2.pkl')
        return rf
    except Exception as e:
        st.error(f"An error occurred loading the Random Forest model: {e}")
        return None

# Function to select the appropriate model based on user input
def select_model(selected_model):
    pipeline, encoder = None, None
    try:  
        if selected_model == 'Catboost':
            pipeline = load_catboost()
        elif selected_model == 'Random Forest':
            pipeline = load_rf()
    except Exception as e:  # handling errors
        st.error(f"An error occurred loading the model: {e}")
    return pipeline, encoder

data = pd.DataFrame(pd.read_csv("data/Train.csv"))

# Function to make prediction using the selected model
def make_prediction(pipeline, data):
    if pipeline is not None:
        df = pd.DataFrame(data)
        df.to_csv('./Datasets/History.csv', mode='a', header=False, index=False if os.path.exists('./Datasets/History.csv') else True)
        if not os.path.exists('./Datasets'):
            os.mkdir("./Datasets")
        
        try:  
            prediction = pipeline.predict(df)[0]
            income_probability = pipeline.predict_proba(df)[0][1]  
            prediction_label = "Below Limit😟" if prediction == 1 else "Above Limit😀"
            st.session_state.final_prediction = prediction_label
            st.session_state.final_probability = 100 * income_probability
        except Exception as e:  # handling errors
            st.error(f"An error occurred making the prediction: {e}")

if __name__ == "__main__":
    main()
