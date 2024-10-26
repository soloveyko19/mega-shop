FROM node:22.8-alpine

ARG NUXT_API_URL_CLIENT
ENV NUXT_API_URL_CLIENT=${NUXT_API_URL_CLIENT}

RUN mkdir /src

COPY ./src/package*.json /src/

WORKDIR /src

RUN npm i 

COPY ./src/ ./

RUN npm run build

CMD npm run start
