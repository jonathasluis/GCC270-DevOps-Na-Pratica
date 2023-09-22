FROM python:3.11.5-alpine3.17
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["sh", "-c", "sleep 5 && python app.py"]