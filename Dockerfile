FROM python:3.11.5

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 1234

CMD ["uvicorn", "main:app", "--port", "1234", "--reload", "--host", "0.0.0.0"]