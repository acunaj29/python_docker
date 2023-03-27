FROM python:slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENV NAME World
CMD ["python", "app.py"]