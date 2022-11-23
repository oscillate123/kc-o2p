FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY index.js /app/index.js

EXPOSE 3000

CMD ["node", "index.js"]