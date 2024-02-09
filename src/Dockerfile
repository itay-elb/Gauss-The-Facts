FROM python
WORKDIR /app
COPY src/requirements.txt /app/
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
EXPOSE 5000
