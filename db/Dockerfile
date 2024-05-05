FROM mysql

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_HOST=localhost

COPY ./mysql.sql /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/mysql.sql

# Start MySQL and keep the container running
#CMD ["mysqld", "--defaults-file=/etc/mysql/my.cnf", "--init-file=/docker-entrypoint-initdb.d/mysql.sql"]
