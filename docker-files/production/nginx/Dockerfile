# build stage
FROM node:12.18 as build-stage
WORKDIR /app
COPY ./package* /app/
COPY  ./vue.config.js /app
COPY ./app.json /app
COPY ./frontend /app/frontend
RUN npm install && npm cache clean --force
RUN npm run build


# production stage
FROM nginx:1.17.4-alpine
COPY --from=build-stage /app/frontend/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY docker-files/production/nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
