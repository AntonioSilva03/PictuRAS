import express from 'express';
import 'dotenv/config';


import apiRouter from './router/router.js';


const app = express();

// Middleware for parsing JSON
app.use(express.json());

// Use the API router
app.use('/api', apiRouter);

// Root route
app.get('/', (req, res) => {
  res.send('Welcome to the API Gateway');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
