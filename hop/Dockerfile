FROM apache/hop:latest

USER root

RUN apk add --no-cache bash curl

COPY ojdbc17.jar /opt/hop/lib/
COPY ojdbc11.jar /opt/hop/lib/

RUN chmod 644 /opt/hop/lib/ojdbc11.jar

WORKDIR /app

