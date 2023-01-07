FROM python:3.7-alpine

ENV user_service=http://user-service:8001

ADD main.py .
ADD requirements.txt .

RUN pip install -r requirements.txt
EXPOSE 8002
CMD ["python", "-m", "uvicorn", "main:app","--host", "0.0.0.0", "--port", "8002"]