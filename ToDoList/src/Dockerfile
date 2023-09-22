FROM python:3.11.5-alpine3.17
COPY . /app
COPY ini.sh /usr/src/app/ini.sh
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000
# Dê permissões de execução ao arquivo .sh
RUN chmod +x /usr/src/app/ini.sh

# Execute o arquivo .sh como parte do comando CMD
CMD /usr/src/app/ini.sh