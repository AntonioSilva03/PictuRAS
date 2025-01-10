const express = require('express');
const router = express.Router();

// Import middleware and other utilities
const authMiddleware = require('../authentication/authMiddleware');
const authzMiddleware = require('../authorization/authzMiddleware');

// Define routes
router.get('/', (req, res) => {
  res.send('API Gateway Home');
});

// Authentication routes
router.post('/login', require('../authentication/login'));
router.post('/register', require('../authentication/register'));

// Protected route (authentication + authorization example)
router.get(
  '/protected',
  authMiddleware, // Authentication middleware
  authzMiddleware(['admin']), // Authorization middleware for 'admin' role
  (req, res) => {
    res.send('This is a protected route for admins only.');
  }
);

module.exports = router;
