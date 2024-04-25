#### BUILDER ####
FROM node:18-bullseye as builder

WORKDIR /home/node

COPY package.json .
RUN npm install

COPY . .
RUN npm run build

#### FINAL ####
FROM node:18-bullseye

WORKDIR /home/node

COPY package.json .
COPY package-lock.json .
RUN npm install --omit=dev

COPY --from=builder /home/node/.nuxt ./.nuxt
COPY --from=builder /home/node/.output ./.output

