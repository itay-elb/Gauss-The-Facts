FROM python
WORKDIR /app
COPY requirements.txt /app/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python","app.py"]