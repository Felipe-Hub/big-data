FROM python:3.6-slim
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","main.py"]