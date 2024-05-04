FROM python:alpine3.17

WORKDIR /app

ENV MONGO_URI="mongodb+srv://mohmed123:mohmed123@cluster0.yi9werh.mongodb.net/gain?retryWrites=true&w=majority&appName=Cluster0"
ENV ENV="production"
ENV TESTING_MONGO_URI="mongodb+srv://mohmed123:mohmed123@cluster0.yi9werh.mongodb.net/testgain?retryWrites=true&w=majority&appName=Cluster0"

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]
