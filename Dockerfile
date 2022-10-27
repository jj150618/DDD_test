FROM python:3.7.15

EXPOSE 80

WORKDIR /app

COPY requirements.txt .

COPY src .

COPY .env .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]