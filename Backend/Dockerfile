# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container at /code
COPY requirements.txt /code/requirements.txt

# Install any dependencies specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# Copy the rest of the application code into the container at /code
COPY . /code/

# Make the start script executable
RUN chmod +x /code/start_servers.sh

# Set the start script as the entrypoint
ENTRYPOINT ["/code/start_servers.sh"]

# # Make port 8000 available to the world outside this container
# EXPOSE 8800

# # Run the manage.py runserver command when the container launches
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8800"]
