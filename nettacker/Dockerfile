FROM python:3.9

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clone OWASP Nettacker
RUN git clone https://github.com/OWASP/Nettacker.git /app/nettacker

WORKDIR /app/nettacker

# Install Nettacker dependencies using setup.py
RUN pip install --no-cache-dir .

# Install missing dependencies manually (if needed)
RUN pip install multiprocess

# Expose API port
EXPOSE 5000

# Start Nettacker API
CMD ["python3", "nettacker.py", "--api"]
