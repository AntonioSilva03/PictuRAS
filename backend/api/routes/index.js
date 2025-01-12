var express = require('express');
var router = express.Router();
var passport = require('passport');
var userModel = require('../models/user');
var User = require('../controllers/user');

router.get('/', function (req, res) {
  res.jsonp('Im here. My name is api')
})

router.post('/register', function (req, res) {
  var d = new Date().toISOString().substring(0, 19);
  User.checkUserExistence(req.body.username)
    .then(user => {
      if (user) {
        if (user.username === req.body.username) {
          res.status(400).jsonp({ error: 'Já existe um utilizador com este email!' });
        }
        } else {
        userModel.register(new userModel({
          username: req.body.username,
          dateCreated: d,
          dateAccessed: d
        }), req.body.password, function (err, user) {
          if (err) {
            res.jsonp({ error: err, message: "Register error: " + err });
          } else {
            res.jsonp('Utilizador registado com sucesso!')
          }
        });
      }
    })
    .catch(erro => {
      res.status(500).jsonp({ error: "Server error: " + erro });
    });
});

router.post('/login', passport.authenticate('local'), function (req, res) {
    var date = new Date().toISOString().substring(0, 19);
    User.updateUser(req.user.username, {dateAccessed: date})
    res.status(200).jsonp({ message: "Login successful", user: req.user });
});

router.post('/logout', function (req, res) {
  req.logout(function (err) {
    if (err) return res.status(500).json({ error: err });
    res.json({ message: "Logged out successfully" });
  });
});

router.get('/profile', function (req, res) {
  if (req.isAuthenticated()) {
    res.jsonp({ user: req.user });
  } else {
    res.status(401).jsonp({ error: "Not authenticated" });
  }
});

module.exports = router;
