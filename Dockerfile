FROM python:3.6-alpine

WORKDIR /app

RUN set -x \
    && pip install --no-cache-dir --disable-pip-version-check \
        bottle \
        'cherrypy<9' \
        clize \
        lockfile \
    && apk add --no-cache --virtual .build-dependencies \
        curl \
        tar \
    && curl -sLO https://github.com/sametmax/0bin/tarball/master \
    && tar -xzf master --strip-components=1 \
    && rm master \
    && apk del .build-dependencies

COPY --chown=root:root default_settings.py /app/zerobin

EXPOSE 80
VOLUME /data
CMD ["python", "zerobin.py"]
