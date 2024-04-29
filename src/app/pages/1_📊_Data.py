import pandas as pd
import numpy as np
import streamlit as st

def main():
    st.set_page_config(
        page_title="Home",
        page_icon=":)",
        layout="wide",
    )

    st.title("DATA PAGE")
    st.write("This page contains all datasets that were used in this project")

    # Load datasets
    train_data = pd.read_csv("data/Train.csv")
    test_data = pd.read_csv("data/Test.csv")

    data_columns = st.columns([1.1])

    #with data_columns:
        # Create a selectbox to choose between datasets
    selected_dataset = st.selectbox("Select Dataset", ["Train_data", "Test_data"])

    # Display the chosen dataset
    if selected_dataset == "Train_data":
        st.write("Displaying Train_data:")
        st.write(train_data)
    else:
        st.write("Displaying Test_data:")
        st.write(test_data)

if __name__ == "__main__":
    main()
