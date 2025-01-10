module.exports = (req, res) => {
    const { username, password } = req.body;
    // Mock authentication
    if (username === 'admin' && password === 'password') {
      return res.json({ token: 'valid-token' }); // Mock token
    }
    res.status(401).send('Invalid credentials');
  };
      