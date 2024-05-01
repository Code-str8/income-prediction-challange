# 💸💰Income Prediction ML Azubian Challenge💰💸

<span style="font-weight:500">This repository contains a cutting-edge machine learning project spearheaded by Team Xenon from the Azubi Cohort 5. The project focuses on predicting income levels and seamlessly integrating the model into a robust web application using the powerful FAST API framework.</span>

<span style="font-style:italic">(Place reference image path here)</span>

<span style="font-weight:500">This project harnesses the power of machine learning to forecast income levels, addressing the pressing challenges of income inequality and providing invaluable insights for policymakers and stakeholders.</span>

### Summary

| Jupyter Notebook | Power BI Dashboard| Published Article| Deployed Streamlit App | Dockerized FastAPI |
| ------------- | ------------- | ------------- | ------------- | ------------- |
|[Notebook with analysis and model development](https://github.com/Code-str8/income-prediction-challange/blob/main/dev/Income_Prediction.ipynb)| [Interactive Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZDNjMmExZjYtMWU2NS00NTBjLTk4Y2EtYmQ2MWU2OWMwODMyIiwidCI6IjQ0ODdiNTJmLWYxMTgtNDgzMC1iNDlkLTNjMjk4Y2I3MTA3NSJ9) | [Published Article on Medium]() |[Link to Deployed Streamlit App](https://teamXenon-income-prediction-streamlit.hf.space/) |[Link to Dockerized FastAPI](https://hub.docker.com/repository/docker/codestr8/income-prediction-challange/general)|


## FastAPI Interface
After clicking on the link to the working FastAPI, click on "Try It Out", provide the required details, and click on the **"EXECUTE"** button.

<p align="center">
  <img src="assets/images/api 2.PNG" width="800">
</p>

### Before Prediction

<p align="center">
  <img src="assets/images/api 3.PNG" width="800">
</p>

### After Prediction
<p align="center">
  <img src="assets/images/api 4.PNG" width="800">
</p>

# Repository Contents:
- 🌍[Project Overview](#project-overview)
- ⚙️[Project Setup](#project-setup)
- 🪪📰[Data Fields](#data-fields)
- 🤔🤑[Business Understanding](#business-understanding)
- 📊[Data Understanding](#data-understanding)
- 🔢🎰[Data Preparation](#data-preparation)
- 🤖[Modeling](#modeling)
- 🔁[Evaluation](#evaluation)
- 🚀[Deployment](#deployment)
- 🧑‍💻[Author](#author)
- 🏅[Acknowledgements](#acknowledgements)

###How our local repository looks like at the backend ⚙️

<p align="center">
  <img src="assets/images/Repo.png" width="800">
</p>


# 🌍Project Overview:
**i. Data Collection and Preprocessing:** Team Xenon loaded and preprocessed an extensive dataset containing income-related data to train and evaluate the cutting-edge income prediction model.

<p align="center">
  <img src="assets/images/api 3.PNG" width="800">
</p>

**ii. Machine Learning Model:** The team implemented a state-of-the-art machine learning model meticulously tailored for predicting income levels. This model has been fine-tuned to achieve industry-leading accuracy in forecasting income thresholds.

**iii. FAST API Integration:** The trained machine learning model has been seamlessly integrated into a web application using the powerful FAST API framework. This innovative web application empowers users to input individual data and receive instant predictions regarding income levels.

**iv. Usage and Deployment:** This README file provides detailed instructions on how to utilize and deploy this web application, ensuring a user-friendly experience for both developers and policymakers.

# ⚙️Project Setup:
To set up the project environment, follow these steps:

i. Clone the repository:

```bash 
git clone https://github.com/Code-str8/income-prediction-challange.git
```

ii. Create a virtual environment and install the required dependencies:

- **Windows:**
  ```bash
  python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt
  ```

- **Linux & MacOS:**
  ```bash
  python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  
  ```

## 🪪📰Data Fields
The data used in this project consists of a diverse collection of income-related attributes obtained from [source](your_data_source_link).

| Column Name                | Data Type   | Description                                      |
|----------------------------|-------------|--------------------------------------------------|
| Age                        | Numeric     | Age of the individual                            |
| Gender                     | Categorical | Gender of the individual                        |
| Education                  | Categorical | Education level of the individual               |
| Class Of Worker            | Categorical | Class of worker                                 |
| Education Institute        | Categorical | Enrollment status in an educational institution in the last week  |
| Marital Status             | Categorical | Marital status                                  |
| Race                       | Categorical | Race                                            |
| Hispanic Origin            | Categorical | Hispanic origin                                 |
| Employment Commitment      | Categorical | Full or part-time employment status             |
| Unemployment Reason        | Categorical | Reason for unemployment                         |
| Employment Stat            | Categorical | Owns a business or is self-employed             |
| Wage Per Hour               | Numeric     | Wage per hour                                   |
| Labor Union Membership     | Categorical | Member of a labor union                         |
| Weeks Worked In A Year      | Numeric     | Weeks worked in a year                          |
| Industry Code              | Categorical | Industry category                               |
| Major Industry Code        | Categorical | Major industry category                         |
| Occupation Code            | Categorical | Occupation category                             |
| Major Occupation Code       | Categorical | Major occupation category                       |
| Num Persons Worked For Employer | Numeric | Number of persons worked for employer         |
| Household and Family Stat   | Categorical | Detailed household and family status            |
| Household Summary          | Categorical | Detailed household summary                      |
| Under 18 Family            | Categorical | Family members under 18                         |
| Veterans Admin Questionnaire| Categorical | Filled income questionnaire for Veterans Admin |
| Vet Benefit                | Categorical | Veteran benefits                                |
| Tax Filer Status           | Categorical | Tax filer status                                |
| Gains                      | Numeric     | Gains from financial investments                |
| Losses                     | Numeric     | Losses from financial investments               |
| Stocks Status              | Categorical | Dividends from stocks                           |
| Citizenship                | Categorical | Citizenship status                             |
| Migration Year             | Numeric     | Year of migration                               |
| Country Of Birth - Individual | Categorical | Individual's birth country                     |
| Country Of Birth - Father   | Categorical | Father's birth country                          |
| Country Of Birth - Mother   | Categorical | Mother's birth country                          |
| Migration Code Change In MSA | Categorical | Migration code - Change in MSA                   |
| Migration Prev Sunbelt      | Categorical | Migration previous Sunbelt                      |
| Migration Code Move Within Reg | Categorical | Migration code - Move within region              |
| Migration Code Change In Reg | Categorical | Migration code - Change in region                |
| Residence 1 Year Ago        | Categorical | Lived in this house one year ago                |
| Old Residence Region        | Categorical | Region of previous residence                   |
| Old Residence State         | Categorical | State of previous residence                    |
| Importance Of Record        | Numeric     | Weight of the instance                          |
| Income Above 50k           | Categorical | Binary indicator if income is above $50,000     |

# Machine Learning Lifecycle
Team Xenon employed the cutting-edge CRISP-DM (Cross-Industry Standard Process for Data Mining) methodology in this project, ensuring a systematic and rigorous approach to data mining and machine learning.

<p align="center">
  <img src="assets/images/data mining.jpg" width="800">
</p>

Here are the steps undertaken by the team:

## 🤔🤑Business Understanding:

The team commenced by gaining a deep understanding of the problem domain, which involved predicting income levels.
They defined the project goals and objectives, such as addressing income inequality through data-driven insights, aligning with industry best practices.

## 📊Data Understanding:</span>

The dataset was meticulously collected from [Zindi](https://zindi.africa/competitions/income-prediction-challenge-for-azubian), which included various income-related attributes. After an in-depth overview of the initial columns, the team formulated hypotheses and key analytical questions to guide the comprehensive understanding of the dataset.

**Hypothesis:**

Null Hypothesis (H0): There is no significant association between the individual's age and income level.

Alternative Hypothesis (H1): There is a significant association between the individual's age and income level.

### Research Questions:

*How do age and gender influence income levels?*

*Does educational attainment correlate with higher income levels?*

*Is there a difference in income levels between different racial or ethnic groups?*

*How does employment status impact an individual's income level?*

*Are there regional variations in income levels, and if so, what factors contribute to these differences?*



## 🔢🎰Data Preparation
### Feature Engineering
Team Xenon performed a rigorous feature engineering process, including unique value exploration, column renaming, missing value imputation, column dropping, target column extraction, and balancing the target column to address class imbalance, leveraging cutting-edge techniques to ensure data integrity and quality.

### Balancing The Target Variable
There was a significant class imbalance in the target variable, with a relatively small number of participants in the high-income category compared to the low-income category. This significant disparity in class distribution may have had implications for modeling and predictive accuracy. Class imbalances can lead to models that are biased toward the majority class, potentially impacting the model's ability to accurately predict the minority class (Above Limit). Team Xenon addressed this class imbalance through state-of-the-art oversampling techniques.

## 🤖Modeling
The training dataset for this income prediction problem contains numerous categorical features, some of which have a large number of unique values. This can pose challenges in terms of encoding and model performance. To address these issues, Team Xenon opted for the cutting-edge CatBoost classifier as their modeling solution:

**1. Automatic Categorical Feature Handling:** CatBoost offers a unique advantage by automatically handling categorical features. Unlike traditional models that require extensive feature encoding using techniques like One-Hot Encoding or Label Encoding, CatBoost can directly work with categorical data. This simplifies the preprocessing step and ensures that the team can utilize categorical features without manual intervention.

**2. Handling Missing Values:** CatBoost excels in handling missing values. It utilizes an algorithm called Symmetric Weighted Quantile Sketch (SWQS) to automatically manage missing data. This not only simplifies the preprocessing process but also reduces the risk of overfitting, contributing to improved overall model performance.

**3. Streamlined Feature Scaling:** Another benefit of CatBoost is its built-in feature scaling. It takes care of scaling all columns uniformly, saving the team the effort of manual conversion. This helps streamline the data preparation phase.

**4. Built-in Cross-Validation:** CatBoost includes a built-in cross-validation method, simplifying the task of selecting the best hyperparameters for the model. This ensures that the model's performance is optimized without the need for extensive manual tuning.

**5. Regularization Techniques:** CatBoost supports both L1 and L2 regularization methods. These techniques are valuable for reducing overfitting and enhancing the model's ability to generalize well to unseen data.

By choosing CatBoost, Team Xenon aimed to efficiently address the challenges posed by the dataset, particularly the extensive set of categorical features with many unique values, which would have posed challenges during encoding. CatBoost not only simplifies the modeling process but also enhances the model's performance. It's a robust solution for the income prediction problem.

### Dataset Splitting
The team split the preprocessed training dataset into training and evaluation sets (80% training, 20% evaluation) using the industry-standard train_test_split technique.

## 🔁Model Training and Evaluation
Team Xenon achieved an impressive Accuracy of 89.38% and an F1-Score of 0.89, demonstrating the effectiveness of their modeling approach and the team's expertise in machine learning.

## Saving The Model and Key Components
The trained model, unique values, encoder, and scaler were meticulously saved in a single pickle file for later use, ensuring seamless deployment and ease of integration.

## 🚀Deployment
Team Xenon utilized the cutting-edge Streamlit framework for a user-friendly interface and the powerful FAST API for scalable predictions. This innovative architecture allows for flexibility in deployment, scalability, high performance, and easy integration.

<p align="center">
  <img src="assets/images/streamlit.png" width="800">
</p>

## Why Streamlit + FastAPI?
- Asynchronous processing
- Scalability
- High performance
- Easy integration

Streamlit allows for a user-friendly interface, while FastAPI ensures scalability and high performance for global-scale predictions, providing a best-in-class solution for income prediction.

<p align="center">
  <img src="assets/images/Render.png" width="800">
</p>

## Linking The Streamlit App with The FASTAPI
The Streamlit app was seamlessly connected with the FastAPI backend for seamless integration. A POST request was sent to the FastAPI server, the prediction response was obtained, and the prediction result was displayed to the user in real-time.

## App Layout - Homepage, Solution & EDA
The app comprises four pages: Homepage, Solution, EDA, and Prediction Page. Each page serves a specific purpose, from introducing the user to the problem to providing an interactive PowerBI dashboard and allowing for instantaneous predictions.

<p align="center">
  <img src="assets/images/home page.PNG" width="800">
</p>

<p align="center">
  <img src="assets/images/dashboard page.PNG" width="800">
</p>


## App Layout - Prediction Page
The Prediction Page empowers users to input data such as age, gender, education, and more. They can submit the data and receive an instant prediction response. The page provides detailed descriptions of the different inputs and allows users to view and select them intuitively.

<p align="center">
  <img src="assets/images/predict page.PNG" width="800">
</p>

## FastAPI Backend
The FastAPI backend is a robust and scalable solution that accepts user input data, preprocesses it, utilizes a trained machine learning model to predict income categories, calculates prediction probability, formats the prediction result, and returns the prediction response in real-time.

<p align="center">
  <img src="assets/images/api 1.PNG" width="800">
</p>

# 🧑‍💻Author

`Team Xenon`

`Data Analysts/Data Scientists`

`Azubi Cohort 5`

# 🏅Acknowledgments:
Team Xenon would like to express their gratitude to the open-source community and the data providers who contributed to the dataset used in this project. Their efforts have made advancements in income prediction possible and paved the way for this groundbreaking work.

<p align="center">
  <img src="assets/images/azubi.jpg" width="800">
</p>

Feel free to explore the code, use the web application, and contribute to the project's development. Data-driven insights can contribute to a more equitable society, and together, we can make a difference.
