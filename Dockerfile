# Use official Python 3.12 slim image as base
FROM python:3.12-slim

# Prevent Python from writing .pyc files and enable stdout/stderr to be unbuffered
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /app

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip to latest version
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy all application files into the container
COPY . .

# Expose port 8000 to access the Django development server
EXPOSE 8000

# Default command to run the Django development server
# Binding to 0.0.0.0 allows access from outside the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
