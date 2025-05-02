FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Install required system packages (combine apt commands to reduce image layers)
RUN apt-get update && \
    apt-get install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command
CMD ["python3", "app.py"]
