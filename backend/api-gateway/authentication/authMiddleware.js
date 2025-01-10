module.exports = (req, res, next) => {
    // Example: check for a token (mocked here)
    const token = req.headers['authorization'];
    if (token === 'valid-token') {
      req.user = { id: 1, name: 'John Doe', role: 'admin' }; // Mock user
      return next();
    }
    res.status(401).send('Unauthorized');
  };
  