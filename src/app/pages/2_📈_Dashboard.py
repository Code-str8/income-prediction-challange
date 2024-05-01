import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.set_page_config(
        page_title="Home",
        page_icon=":)",
        layout="wide",
    )

    st.title('Dashboard')
    st.markdown('This page provides visuals on Bivariate, Multivariate and KPIs analysis')

    # Load the data using pandas
    train_data = pd.read_csv("data/Train.csv")

    selectbox_column, visualization_column = st.columns([1, 4])
    visualization_category = selectbox_column.selectbox(
        "Select Visualization Category",
        ["Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis", "KPIs"])

    # Add columns to the dashboard page
    col1, col2 = st.columns(2)

    # variables for storing figures
    fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13 = [None] * 10

    #  a custom color palette
    custom_palette = px.colors.qualitative.Pastel

    # a Seaborn color palette
    seaborn_palette = sns.color_palette(custom_palette, as_cmap=True)

    # the color scale for plots
    color_scale = 'Viridis'

    if visualization_category == "Univariate Analysis":
        with col1:
            fig1 = px.histogram(train_data, x='age', nbins=10, title='Distribution of Age')
            fig1.update_layout(xaxis_title='Age', yaxis_title='Frequency')
            fig1.update_traces(marker_color=custom_palette[0])
            st.plotly_chart(fig1, use_container_width=True)
            fig1.update_layout(template="plotly_dark")  # Move this line inside the block

            fig2 = px.histogram(train_data, x='gender', title='Gender Distribution')
            fig2.update_layout(xaxis_title='Gender', yaxis_title='Count', xaxis={'categoryorder': 'total descending'})
            fig2.update_traces(marker_color=custom_palette[1])
            st.plotly_chart(fig2, use_container_width=True)
            fig2.update_layout(template="plotly_dark")  # Move this line inside the block

        with col2:
            fig3 = px.histogram(train_data, x='marital_status', title='Marital Status Distribution')
            fig3.update_layout(xaxis_title='Distribution of Marital Status', yaxis_title='Count',
                               xaxis={'categoryorder': 'total descending'})
            fig3.update_traces(marker_color=custom_palette[2])
            st.plotly_chart(fig3, use_container_width=True)
            fig3.update_layout(template="plotly_dark")  # Move this line inside the block

    elif visualization_category == "Bivariate Analysis":
        with col1:
            fig4 = sns.boxplot(data=train_data, x='income_above_limit', y='age', palette='pastel')
            fig4.set_title('Age vs. Income Level')
            st.pyplot(fig4.figure)

            fig5 = sns.countplot(data=train_data, x='education', hue='income_above_limit', palette='pastel')
            fig5.set_title('Education vs. Income Level')
            plt.xticks(rotation=90)
            st.pyplot(fig5.figure)

        with col2:
            fig6 = sns.countplot(data=train_data, x='marital_status', hue='income_above_limit', palette='pastel')
            fig6.set_title('Marital Status vs. Income Level')
            plt.xticks(rotation=90)
            st.pyplot(fig6.figure)

    elif visualization_category == "Multivariate Analysis":
        selected_features = ['age', 'wage_per_hour', 'working_week_per_year', 'gains', 'losses']
        fig7 = sns.pairplot(train_data[selected_features])
        fig7.fig.suptitle('Pair Plot of Selected Numerical Variables')
        st.pyplot(fig7)

        numerical_columns = train_data.select_dtypes(include=np.number).columns
        correlation_matrix = train_data[numerical_columns].corr()
        fig, ax = plt.subplots()
        fig8 = sns.heatmap(correlation_matrix, annot=True, cmap='viridis', cbar=True, ax=ax)
        ax.set_title('Correlation Heatmap of Numerical Variables')
        st.pyplot(fig8.figure)
        

    elif visualization_category == "KPIs":
        with col1:
            fig9 = sns.stripplot(data=train_data, x='income_above_limit', y='age', palette='pastel')
            fig9.set_title('Age vs. Income Level')
            st.pyplot(fig9.figure)

            fig10 = sns.countplot(data=train_data, x='gender', hue='income_above_limit', palette='pastel')
            fig10.set_title('Gender vs. Income Level')
            plt.xticks(rotation=45)
            st.pyplot(fig10.figure)

            fig11 = sns.countplot(data=train_data, x='race', hue='income_above_limit', palette='pastel')
            fig11.set_title('Race vs. Income Level')
            plt.xticks(rotation=45)
            st.pyplot(fig11.figure)

        with col2:
            fig12 = sns.countplot(data=train_data, x='employment_stat', hue='income_above_limit', palette='pastel')
            fig12.set_title('Employment Status vs. Income Level')
            plt.xticks(rotation=45)
            st.pyplot(fig12.figure)

            fig13 = sns.countplot(data=train_data, x='residence_1_year_ago', hue='income_above_limit', palette='pastel')
            fig13.set_title('Residence vs. Income Level')
            plt.xticks(rotation=45)
            st.pyplot(fig13.figure)

    #  fig4 to fig13 are already defined Seaborn figures
    #for fig in [fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13]:
        #if fig:
           # fig.set_facecolor('#1E1E1E')

if __name__ == "__main__":
    main()
