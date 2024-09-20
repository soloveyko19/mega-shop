FROM node:22.8-alpine

RUN mkdir /src

COPY ./src/package*.json /src/

WORKDIR /src

RUN npm i 

COPY ./src/ ./

RUN npm run build

CMD sh ./server/start.sh
