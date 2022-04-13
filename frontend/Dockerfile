# The first image is for compiling the client files, the second is for serving.

# BUILD IMAGE
FROM node:16-alpine as build-stage

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Build
COPY . .
RUN npm run build

# -----------------------------------------------------------------------------
# SERVING IMAGE
FROM nginx:1.19.3-alpine
COPY nginx.nginx /etc/nginx/conf.d/default.conf

# Copy built files
COPY --from=build-stage /app/build /usr/share/nginx/html

# 80 for HTTP
EXPOSE 80

# Run nginx
CMD nginx -g 'daemon off;'
