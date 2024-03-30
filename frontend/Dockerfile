#### BUILDER ####
FROM node:18-bullseye as builder

WORKDIR /home/node

COPY package.json .
RUN npm install

COPY . .
RUN npm run build

RUN chown -R node: .nuxt
RUN chown -R node: .output
RUN chmod -R u+rwx .nuxt
RUN chmod -R u+rwx .output

#### FINAL ####
FROM node:18-bullseye

WORKDIR /home/node

COPY --from=builder /home/node/.nuxt ./.nuxt
COPY --from=builder /home/node/.output ./.output

COPY package.json .
RUN npm install
