const express = require('express');
const app = express();

let healthy = false;
let startupTime = Date.now();

// Simulate slow startup - takes 60 seconds to become healthy
setTimeout(() => {
  healthy = true;
  console.log('Application is now healthy');
}, 60000);

app.get('/', (req, res) => {
  res.send(`Hello World! App running for ${Math.floor((Date.now() - startupTime) / 1000)} seconds`);
});

app.get('/health', (req, res) => {
  console.log(`Health check called. Healthy: ${healthy}`);
  if (healthy) {
    res.status(200).json({
      status: 'healthy',
      uptime: Math.floor((Date.now() - startupTime) / 1000),
      timestamp: new Date().toISOString()
    });
  } else {
    res.status(503).json({
      status: 'not ready',
      uptime: Math.floor((Date.now() - startupTime) / 1000),
      timestamp: new Date().toISOString(),
      message: 'Still initializing...'
    });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server starting on port ${PORT}. Will be healthy in 60 seconds...`);
});
