# build environment
FROM node:13.6.0 as build
WORKDIR /app
COPY /package.json /app
RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent
RUN npm run build
ENV PATH ./node_modules/.bin:$PATH



# production environment
FROM nginx:1.17.4-alpine
COPY --from=build /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY /nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
