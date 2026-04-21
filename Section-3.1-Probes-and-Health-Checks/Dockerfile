FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json first for better Docker layer caching
COPY package.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY server.js ./

# Expose the port the app runs on
EXPOSE 3000

# Create a non-root user for security
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001

# Change ownership of the app directory
RUN chown -R nodejs:nodejs /app
USER nodejs

# Health check (optional - Docker level)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

# Start the application
CMD ["node", "server.js"]
