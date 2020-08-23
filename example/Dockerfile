FROM python:3.6.3
MAINTAINER trianta@research.att.com

RUN mkdir /app
WORKDIR /app

ADD ./example-model /app/example-model
ADD ./requirements.txt /app
ADD ./packages /app/packages

RUN pip install --no-cache-dir -r /app/requirements.txt && \
    pip install --no-cache-dir acumos_dcae_model_runner 

ENV DCAEPORT=10000
EXPOSE $DCAEPORT

ENTRYPOINT ["acumos_dcae_model_runner"]
CMD ["/app/example-model"]
