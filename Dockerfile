# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World
RUN export FLASK_APP="server.py"
RUN export FLASK_DEBUG=1

# Run app.py when the container launches
# CMD ["python", "server.py”]
CMD ["python", "server.py"]
# CMD ["flask", "run"]