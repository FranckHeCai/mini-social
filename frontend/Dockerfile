# Use Node 20 Alpine base image
FROM node:20-alpine

# Enable Corepack and activate the specific pnpm version
# RUN corepack enable && corepack prepare pnpm@10.11.1 --activate
RUN corepack enable

# Set working directory
WORKDIR /app

# Copy package files first for caching
COPY package.json pnpm-lock.yaml ./

# Install dependencies with frozen lockfile
RUN pnpm install

# Copy the rest of the source code
COPY . .

# Expose port
EXPOSE 3000

# Run the Nuxt server
CMD ["pnpm", "run", "dev"]
