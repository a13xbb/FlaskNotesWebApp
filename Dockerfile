FROM python:3.10.10-alpine3.16
WORKDIR /backend
COPY requirements.txt /backend
RUN apk update
RUN apk add --upgrade py3-greenlet
RUN apk --no-cache add musl-dev linux-headers g++ build-base openssl-dev python3-dev
RUN pip3 install -r requirements.txt
ADD /instance /backend/instance
ADD /website /backend/website
COPY /main.py /backend
CMD python main.py
EXPOSE 5000