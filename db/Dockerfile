FROM mysql

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_HOST=mysql

COPY ./mysql.sql /docker-entrypoint-initdb.d/
