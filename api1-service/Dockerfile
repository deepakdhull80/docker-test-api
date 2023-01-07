FROM python:3.7-alpine

ADD main.py .
ADD requirements.txt .

RUN pip install -r requirements.txt
EXPOSE 8001
CMD ["python", "-m", "uvicorn", "main:app","--host", "0.0.0.0", "--port", "8001"]