FROM python:3.11.4-alpine@sha256:995c7fcdf9a10e0e1a4555861dac63436b456822a167f07b6599d4f105de6fa0

ARG user=dt-reimport
ARG group=dt-reimport

RUN addgroup -g 1000 -S ${group} && \
    adduser -u 1000 -S ${user} -G ${group}

WORKDIR /usr/local/dt-reimport
RUN mkdir ./dt_reimport && mkdir ./bin
COPY --chown=dt-reimport:dt-reimport ./ ./
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="/usr/local/dt-reimport/bin:$PATH"

USER ${user}
