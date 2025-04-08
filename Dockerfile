# Use an official Python 3.12 image
FROM python:3.11.7

# Set the working directory inside the container
WORKDIR /app



# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project into the container
COPY . .

#Copy the environment variables
COPY .env .env

#Expose a port if you have a server (optional)
EXPOSE 8000

# Finally, set the command. 
# Adjust if you have a different entry point or want to run a web server
CMD ["python", "main.py"]
