# Stage 1: Build
FROM node:16 AS build

WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy the frontend files
COPY . ./

# Inject the backend API URL into the build process
ARG VITE_API_URL
ENV VITE_API_URL=${VITE_API_URL}

# Build the frontend
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
