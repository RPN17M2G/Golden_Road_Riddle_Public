# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /app

COPY package.json .

#Install contents of package.json
RUN npm install 

#Expost local host port
EXPOSE 3000

# add app
COPY . .

# start app
CMD ["npm", "start"]