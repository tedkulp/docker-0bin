FROM python:3.6-alpine

WORKDIR /app

RUN set -x \
    && pip install --no-cache-dir --disable-pip-version-check \
        bottle \
        'cherrypy<9' \
        clize \
        lockfile

COPY app/ ./

COPY --chown=root:root default_settings.py /app/zerobin

EXPOSE 80
VOLUME /data
CMD ["python", "zerobin.py"]
