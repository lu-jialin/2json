FROM alpine

RUN apk add --no-cache python3 py3-yaml py3-tomli py3-tomli-w

COPY src/2json.py /bin/
RUN chmod +x /bin/2json.py

CMD ["2json.py" , "-h"]
