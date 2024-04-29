import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

def main():
    st.set_page_config(
        page_title="Home",
        page_icon=":)",
        layout="wide",
    )

st.title('Dashboard')
st.markdown('This page provides visuals on Bivariate, Multivariate and KPIs analysis')

# Load the data using pandas
train_data = pd.read_csv(r"C:\Users\ndund\OneDrive\Documents\PYTHON\income-prediction-challange\data\Train.csv")


selectbox_column, visualization_column = st.columns([1, 4])
visualization_category = selectbox_column.selectbox(
    "Select Visualization Category",
    ["Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis", "KPIs"])


# Add columns to the dashboard page
col1, col2 = st.columns(2)

# Define a custom color palette
custom_palette = px.colors.qualitative.Pastel

# Set the color scale for plots
color_scale = 'Viridis'

if visualization_category == "Univariate Analysis":
    with col1:
        fig1 = px.histogram(train_data, x='age', nbins=10,  title='Distribution of Age')
        fig1.update_layout(xaxis_title='Age', yaxis_title='Frequency')
        fig1.update_traces(marker_color=custom_palette[0])
        st.plotly_chart(fig1, use_container_width=True)

        
        fig2 = px.histogram(train_data, x='gender', title='Gender Distribution')
        fig2.update_layout(xaxis_title='Gender', yaxis_title='Count', xaxis={'categoryorder':'total descending'})
        fig2.update_traces(marker_color=custom_palette[1])
        st.plotly_chart(fig2, use_container_width=True)

    with col2:
        fig3 = px.histogram(train_data, x='marital_status', title='Marital Status Distribution')
        fig3.update_layout(xaxis_title='Distribution of Marital Status', yaxis_title='Count', xaxis={'categoryorder':'total descending'})
        fig3.update_traces(marker_color=custom_palette[2])
        st.plotly_chart(fig3, use_container_width=True)

elif visualization_category == "Bivariate Analysis":
    with col1:
        fig4 = px.box(train_data, x='income_above_limit', y='age', title='Age vs. Income Level')
        fig4.update_layout(xaxis_title='Income Level', yaxis_title='Age')
        fig4.update_traces(marker_color=custom_palette[3])
        st.plotly_chart(fig4, use_container_width=True)

        fig5 = px.bar(train_data, x='education', color='income_above_limit', title='Education vs. Income Level', barmode='group')
        fig5.update_layout(xaxis_title='Education', yaxis_title='Count', legend_title='Income Level')
        fig5.update_traces(marker_color=custom_palette[4])
        st.plotly_chart(fig5, use_container_width=True)

    with col2:
        fig6 = px.histogram(train_data, x='marital_status', color='income_above_limit', title='Marital Status vs. Income Level', barmode='group')
        fig6.update_layout(xaxis_title='Marital Status', yaxis_title='Count', legend_title='Income Level')
        fig6.update_traces(marker_color=custom_palette[5])
        st.plotly_chart(fig6, use_container_width=True)

elif visualization_category == "Multivariate Analysis":
    selected_features = ['age', 'wage_per_hour', 'working_week_per_year', 'gains', 'losses']
    fig7 = px.scatter_matrix(train_data[selected_features], title='Pair Plot of Selected Numerical Variables')
    fig7.update_traces(marker=dict(colorscale=color_scale))
    fig7.update_layout(title_x=0.5)
    st.plotly_chart(fig7, use_container_width=True)

    numerical_columns = train_data.select_dtypes(include=np.number).columns
    correlation_matrix = train_data[numerical_columns].corr()
    fig8 = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.index,
        colorscale=color_scale,
        colorbar=dict(title='Correlation'),
        hoverongaps=False))
    fig8.update_layout(title='Correlation Heatmap of Numerical Variables')
    st.plotly_chart(fig8, use_container_width=True)

elif visualization_category == "KPIs":
    with col1:
        fig9 = px.scatter(train_data, x='income_above_limit', y='age', title='Age vs. Income Level',
                          labels={'income_above_limit': 'Income Level', 'age': 'Age'})
        fig9.update_xaxes(tickangle=45)
        fig9.update_traces(marker_color=custom_palette[6])
        st.plotly_chart(fig9, use_container_width=True)

        fig10 = px.histogram(train_data, x='gender', color='income_above_limit',
                             title='Gender vs. Income Level',
                             labels={'gender': 'Gender', 'income_above_limit': 'Income Level', 'count': 'Count'})
        fig10.update_layout(barmode='group')
        fig10.update_traces(marker_color=custom_palette[7])
        st.plotly_chart(fig10, use_container_width=True)

        fig11 = px.histogram(train_data, x='race', color='income_above_limit',
                             title='Race vs. Income Level',
                             labels={'race': 'Race', 'income_above_limit': 'Income Level', 'count': 'Count'})
        fig11.update_layout(barmode='group')
        fig11.update_traces(marker_color=custom_palette[8])
        st.plotly_chart(fig11, use_container_width=True)

    with col2:
        fig12 = px.histogram(train_data, x='employment_stat', color='income_above_limit',
                             title='Employment Status vs. Income Level',
                             labels={'employment_stat': 'Employment Status', 'income_above_limit': 'Income Level',
                                     'count': 'Count'})
        fig12.update_layout(barmode='group')
        fig12.update_traces(marker_color=custom_palette[9])
        st.plotly_chart(fig12, use_container_width=True)

        fig13 = px.histogram(train_data, x='residence_1_year_ago', color='income_above_limit',
                             title='Residence vs. Income Level',
                             labels={'residence_1_year_ago': 'Residence 1 Year Ago', 'income_above_limit': 'Income Level',
                                     'count': 'Count'})
        fig13.update_layout(barmode='group')
        fig13.update_traces(marker_color=custom_palette[10])
        st.plotly_chart(fig13, use_container_width=True)

# Apply the updated theme to all plots
pio.templates.default = "plotly_dark"

# Update the layout to match the theme
fig1.update_layout(template="plotly_dark")
fig2.update_layout(template="plotly_dark")
fig3.update_layout(template="plotly_dark")
fig4.update_layout(template="plotly_dark")
fig5.update_layout(template="plotly_dark")
fig6.update_layout(template="plotly_dark")
fig7.update_layout(template="plotly_dark")
fig8.update_layout(template="plotly_dark")
fig9.update_layout(template="plotly_dark")
fig10.update_layout(template="plotly_dark")
fig11.update_layout(template="plotly_dark")
fig12.update_layout(template="plotly_dark")
fig13.update_layout(template="plotly_dark")

# Run the main function
if __name__ == "__main__":
    main()
