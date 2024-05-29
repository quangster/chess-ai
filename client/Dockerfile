FROM node:20.12.2-alpine as builder
WORKDIR /app

COPY package.json ./

RUN npm install

COPY tailwind.config.js ./
COPY /public ./public
COPY /src ./src

RUN npm run build

FROM nginx
COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]