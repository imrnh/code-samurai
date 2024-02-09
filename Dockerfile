FROM postgres:latest

# Install Python, pip, and python3-venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get install -y libpq-dev && \  
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# Create a virtual environment and activate it
RUN python3 -m venv venv

# Install Python dependencies within the virtual environment
RUN /bin/bash -c "source venv/bin/activate && pip install --no-cache-dir -r requirements.txt"

COPY . .

EXPOSE 8000

ENV MY_NAME=IMRAN_HOSSEN

CMD [ "venv/bin/python3", "main.py" ]