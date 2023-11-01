
FROM python:3.10

WORKDIR /app
COPY . /app

#Firestore local
# RUN pip install mock==4.0.3
# RUN pip install google-cloud-firestore==2.0.2
RUN pip install mysql-connector-python
RUN pip install PyJWT
# RUN apt-get update && apt-get install -y netcat-traditional
# ENV DOCKER_UPDATED=true
# ENV FUNCTION_NAME=query_data
# Function requirements
RUN pip install -r requirements-dev.txt
RUN pip install -U autopep8
RUN pip install -U pycodestyle

EXPOSE 5000

CMD ["python", "main.py"] 
