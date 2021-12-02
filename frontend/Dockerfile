# pull official base image
FROM node:17.1.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
# RUN npm install react-scripts@4.0.3 -g --silent

ENV NODE_OPTIONS --openssl-legacy-provider

# add app
COPY . ./

# start app
EXPOSE 3000
CMD ["yarn", "start"]
