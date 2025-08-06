FROM python:3.12

# Install pip and essential build tools
RUN apt-get update && apt-get install -y python3-pip build-essential

# Ensure python and pip point to correct binaries
RUN ln -sf /usr/bin/python3 /usr/bin/python && ln -sf /usr/bin/pip3 /usr/bin/pip

WORKDIR /main

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app code
COPY . .

# Run Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
