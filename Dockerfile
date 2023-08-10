FROM python:alpine3.18
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8181
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8181"]
