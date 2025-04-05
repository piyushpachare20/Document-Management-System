# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Set the command to run the FastAPI application
CMD ["uvicorn", "app_fast_api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]