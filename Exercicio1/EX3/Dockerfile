FROM node:alpine
COPY . /app
WORKDIR /app
RUN npm install express --no-save
EXPOSE 3000
CMD ["node" , "app.js"]