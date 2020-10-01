# build environment
FROM node:13.6.0 as build
WORKDIR /app
ENV PATH /app/front-end/node_modules/.bin:$PATH
COPY ../../../package.json /app/package.json
RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent
COPY ../../../front-end/ /app/front-end
RUN npm run build

# production environment
FROM nginx:1.17.4-alpine
COPY --from=build /app/front-end/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
