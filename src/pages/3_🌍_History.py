import streamlit as st
import pandas as pd 
from src.auth import login_form, is_authenticated    


st.set_page_config(
    page_icon="⏳",
    page_title="History",
    layout="wide"  
)

def history_page():
    login_form()
    if is_authenticated():
       st.title("**HISTORY**")
       def user_predict_history():
           file_path = "Datasets/History.csv"
           try:
               history_df = pd.read_csv(file_path, header=None) 
               history_df.columns = history_df.iloc[0]
               history_df = history_df.iloc[1:]
           except pd.errors.ParserError as e:
               st.error(f"Error parsing CSV: {e}")
               return None
           return history_df

       if __name__ == "__main__":
            if st.button("Refresh Data"):
               history_df = user_predict_history()
               if history_df is not None:
                  st.dataframe(history_df)
               else:
                  st.write("Unable to display history data due to errors.")
    else:
     st.error("Please log in to access the App. Username: admin Password: Admin01")

if __name__ == "__main__":
    history_page()
