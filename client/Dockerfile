FROM node:20.12.2
WORKDIR /app

COPY package*.json ./

RUN npm install

COPY public/ ./public
COPY tailwind.config.js ./
COPY src/ ./src

EXPOSE 3000

CMD ["npm", "start"]