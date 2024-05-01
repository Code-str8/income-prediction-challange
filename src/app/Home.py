import streamlit as st

# Create a function to authenticate users
def authenticate(username, password):
    # Define a dictionary with usernames as keys and passwords as values
    users = {
        "Tietaar": "abc123",
        "Alexander": "bcd234",
        "Michelle": "cde345",
        "Reginald": "def456",
        "Manenyi": "efg567",
        "Adeleye": "fgh678"
    }

    # Check if the username exists and the password matches
    if username in users and users[username] == password:
        return True
    else:
        return False


# Create Streamlit app
def main():
    st.set_page_config(
        page_title="Home",
        page_icon=":)",
        layout="wide",
    )

    st.title("Welcome to Xenon Income Prediction App👋👋👋")
    

    # Create input fields for username and password
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    # Check if the user has submitted the login form
    if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            # Once authenticated, show the rest of the app            
            show_app()
        else:
            st.error("Invalid username or password")

# Define the rest of the app to show after authentication
def show_app():
    st.subheader("About App:")
    st.markdown(
        """_This app aims at using  machine learning models to predict whether employees earn above or below certain salary limits._"""
    )
    st.subheader("Key Features:")
    st.markdown(
        """
        * **Data_page:** _Contains all the datasets that was used in analyzing and training machine learning models._
        * **Dashboard:** _This page contains all the visuals that were created during our analysis._
        * **Predict_page:** _This page allows you to predict the salary limit of employees._
        * **History_page:** _The History page serves as an archive for all predictions that were done in the predict page._
        """
    )

    st.subheader("Partners:")
    st.markdown(
        """
        * **Maanenyi Idriss Nyande:** maangott@gmail.com
        * **Michelle Addawoo:** michelle.addawoo@azubiafrica.org
        * **Alexander Ndunda:** ndunda.alex@gmail.com
        * **Reginald Ffoulkes:** niidoku@hotmail.com
        * **Emmanuel Adeleye Iyanu:** iyanu1106@gmail.com
        * **Nyar Tietaar Louis:** nyarlouis@gmail.com.
        """
    )

    st.markdown(
        """_Dreams inspire but actions make. Keep trying, Keep coding. The world is full of endless possibilities_"""
    )

    # Logout button
    if st.button("Logout"):
        st.sidebar.text_input("Username", value="")
        st.sidebar.text_input("Password", value="", type="password")
        st.sidebar.button("Login")

if __name__ == "__main__":
    main()
