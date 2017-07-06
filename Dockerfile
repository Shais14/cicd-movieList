FROM alpine:3.5
RUN apk add --update python py-pip
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY movies /src/movies
COPY templates /src/templates
COPY static /src/static
CMD python /src/app.py