import express from 'express';
import register from '../authentication/register.js';
import tools from '../tools/tools.js';

const router = express.Router();

// Define routes
router.get('/', (req, res) => {
  res.send('API Gateway Home');
});

// Authentication routes
router.post('/register', register); // Use imported function directly

// Tools routes
router.use('/tools', tools);

export default router; // Export router as ES Module
