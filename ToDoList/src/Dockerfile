FROM python:3.11.5-alpine3.17
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

# Execute o arquivo .sh como parte do comando CMD
CMD flask db migrate && flask db upgrade && python app.py