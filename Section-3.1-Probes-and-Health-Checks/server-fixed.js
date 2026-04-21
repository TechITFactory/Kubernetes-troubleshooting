const express = require('express');
const app = express();

let healthy = true; // Start healthy immediately
let ready = false;
let startupTime = Date.now();

// Simulate faster startup - ready in 10 seconds
setTimeout(() => {
  ready = true;
  console.log('Application is now ready to serve traffic');
}, 10000);

app.get('/', (req, res) => {
  res.send(`Hello World! App running for ${Math.floor((Date.now() - startupTime) / 1000)} seconds`);
});

// Liveness probe - basic health check
app.get('/alive', (req, res) => {
  console.log('Liveness check called');
  if (healthy) {
    res.status(200).json({
      status: 'alive',
      uptime: Math.floor((Date.now() - startupTime) / 1000),
      timestamp: new Date().toISOString()
    });
  } else {
    res.status(503).json({
      status: 'dead',
      timestamp: new Date().toISOString()
    });
  }
});

// Readiness probe - comprehensive readiness check
app.get('/ready', (req, res) => {
  console.log(`Readiness check called. Ready: ${ready}`);
  if (ready && healthy) {
    res.status(200).json({
      status: 'ready',
      uptime: Math.floor((Date.now() - startupTime) / 1000),
      timestamp: new Date().toISOString()
    });
  } else {
    res.status(503).json({
      status: 'not ready',
      uptime: Math.floor((Date.now() - startupTime) / 1000),
      timestamp: new Date().toISOString(),
      message: ready ? 'Healthy but not ready' : 'Still initializing...'
    });
  }
});

// Legacy health endpoint for backward compatibility
app.get('/health', (req, res) => {
  res.redirect('/ready');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server starting on port ${PORT}. Will be ready in 10 seconds...`);
});
