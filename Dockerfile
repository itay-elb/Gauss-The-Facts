from python
WORKDIR /app
COPY requirements.txt /app/
COPY /src .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python","app.py"]