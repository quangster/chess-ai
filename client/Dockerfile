FROM node:20.12.2-alpine
WORKDIR /app

COPY package.json ./

RUN npm install

COPY tailwind.config.js ./
COPY /public ./public
COPY /src ./src

EXPOSE 3000

CMD ["npm", "start"]