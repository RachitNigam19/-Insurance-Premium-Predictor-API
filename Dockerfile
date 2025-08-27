# base 
FROM python:3.12.3

# working directory 
WORKDIR /app

# requirements.txt
COPY requirements.txt .

# install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy rest of the files 
COPY . .

# Expose port 
EXPOSE 8000

# run command 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]