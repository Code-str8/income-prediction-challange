# Use the official Python image as a parent image
FROM python:3.11.6

# Set the working directory within the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY ./requirements.txt /tmp/requirements.txt

# Install the Python dependencies
RUN pip install -r /tmp/requirements.txt

# Copy your FastAPI application code into the container
COPY . /app

# Expose port 80 for the FastAPI application
EXPOSE 80

# Define the command to run your FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
