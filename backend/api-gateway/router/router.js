import express from 'express';
import register from '../authentication/register.js'; // Use import for ES Module

const router = express.Router();

// Define routes
router.get('/', (req, res) => {
  res.send('API Gateway Home');
});

// Authentication routes
router.post('/register', register); // Use imported function directly

export default router; // Export router as ES Module
