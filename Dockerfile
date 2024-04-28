# Use the official Python image as a parent image
FROM python:3.12-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies
RUN pip install -r /app/requirements.txt

# Copy your FastAPI application code into the container
COPY ./src/main.py /app/main.py

# Copy the model and key components into the container
COPY ./models/LabelEncoder.pkl /app/models/LabelEncoder.pkl
COPY ./models/catboost_pipeline_thresh.pkl /app/models/catboost_pipeline_thresh.pkl
COPY ./models/rf_pipeline_thresh.pkl /app/models/rf_pipeline_thresh.pkl

# Expose port 7860 for the FastAPI application
EXPOSE 7860

# Define the command to run your FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
