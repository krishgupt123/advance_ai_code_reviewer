# Frontend Dockerfile
FROM python:3.9

WORKDIR /app  

# Copy and install dependencies
COPY requirements.txt /app/requirements.txt  
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy frontend source code
COPY . /app  

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
