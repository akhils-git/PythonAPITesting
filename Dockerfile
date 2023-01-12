FROM python:3.8-alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -U Flask
CMD ["python", "index.py"]