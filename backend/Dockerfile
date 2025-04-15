# Backend Dockerfile
FROM python:3.9

WORKDIR /app  

# Copy and install dependencies
COPY requirements.txt /app/requirements.txt  
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy backend source code
COPY . /app  

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
