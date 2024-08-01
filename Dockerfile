# Use an official Python runtime as a parent image
FROM python:3
# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app

# Expose port 8000
EXPOSE 8000
# Define the command to run the app
CMD ["python", "calculator.py"]