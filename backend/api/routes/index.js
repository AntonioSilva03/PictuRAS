var express = require('express');
var router = express.Router();
var jwt = require('jsonwebtoken');
var passport = require('passport');
var userModel = require('../models/user');
var auth = require('../Auth/auth');
var User = require('../controllers/user');

router.get('/', function (req, res) {
  res.jsonp('Im here. My name is api')
})

router.post('/register', function (req, res) {
  var d = new Date().toISOString().substring(0, 19);
  User.checkUserExistence(req.body.email)
    .then(user => {
      if (user) {
        if (user.email === req.body.email) {
          res.status(400).jsonp({ error: 'Já existe um utilizador com este email!' });
        }
        } else {
        userModel.register(new userModel({
          username: req.body.username,
          email: req.body.email,
          dateCreated: d,
          dateAccessed: d
        }), req.body.password, function (err, user) {
          if (err) {
            res.jsonp({ error: err, message: "Register error: " + err });
          } else {
            passport.authenticate("local")(req, res, function () {
              jwt.sign({ username: req.user.username, sub: 'PictuRAS2025' }, "PictuRAS2025", { expiresIn: 3600 }, function (e, token) {
                if (e) res.status(500).jsonp({ error: "Erro na geração do token: " + e });
                else {
                  res.status(201).jsonp({ token: token });
                }
              });
            });
          }
        });
      }
    })
    .catch(erro => {
      res.status(500).jsonp({ error: "Server error: " + erro });
    });
});

router.post('/login', passport.authenticate('local'), function (req, res) {
  jwt.sign({
    username: req.user.username,
    sub: 'PictuRAS2025'
  },
    "PictuRAS2025",
    { expiresIn: 3600 },
    function (e, token) {
      if (e) res.status(500).jsonp({ error: "Erro na geração do token: " + e });
      else {
        res.status(201).jsonp({ token: token });
      }
    });
    var date = new Date().toISOString().substring(0, 19);
    User.updateUser(req.user.username, {dateAccessed: date})
});

router.get('/profile', auth.verificaAcesso, function (req, res, next) {
  User.getUserByUserName(req.user.username)
    .then(dados => res.jsonp(dados))
    .catch(erro => res.status(500).jsonp(erro));
});

router.put('/profile', auth.verificaAcesso, function (req, res) {
  User.updateUser(req.user.username, req.body)
    .then(dados => res.jsonp(dados))
    .catch(erro => res.status(500).jsonp(erro));
});

module.exports = router;


module.exports = router;
