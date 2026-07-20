FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN apt update && apt-get install -y iproute2
COPY app/main.py /app/
EXPOSE 80
CMD python3 -m uvicorn main:app --host 0.0.0.0 --port 80