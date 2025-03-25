

    
    # Use Python 3.9 as the base image
    FROM python:3.9
    
    # Set the working directory in the container
    WORKDIR /app
    
    # Copy all files from the project into the container
    COPY . .
    
    # Install required dependencies
    RUN pip install -r requirements.txt
    
    # Run the application
    CMD ["python", "app.py"]
    