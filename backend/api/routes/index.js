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
    res.status(200).jsonp({ message: "Login successful", user: req.user,sessionId:req.sessionID});
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

router.get('/mixed', passport.authenticate(['local', 'anonymous'], { session: false }), (req, res) => {
  if (req.isAuthenticated()) {
    return res.json({ message: `Welcome back, ${req.user.username}.`, sessionId:req.sessionID });
  }
  res.json({ message: 'Hello anonymous user!', sessionId:req.sessionID});
});

router.get('/tools', passport.authenticate(['local', 'anonymous'], { session: false }), (req, res) => {
  try {
    return res.status(200).json([
        {
            "name": "contrast",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "contrast",
                    "type": "float",
                    "value": 0,
                    "min_value":-100,
                    "max_value":100
                }
            ]
        },
        {
            "name": "border",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "border_width",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1920
                },
                {
                    "name": "border_height",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1080
                },
                {
                    "name": "border_color",
                    "type": "hex",
                    "value": "#000000"
                }
            ]
        },
        {
            "name": "brightness",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "brightness",
                    "type": "float",
                    "value": 0,
                    "min_value": -1,
                    "max_value": 1
                }
            ]
        },
        {
            "name": "crop",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "width",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1920
                },
                {
                    "name": "height",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1080
                },
                {
                    "name": "x_top_left",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 1920
                },
                {
                    "name": "y_top_left",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "min_value": 1080
                }
            ]
        },
        {
            "name": "ocr",
            "input_type": "image",
            "output_type": "text",
            "parameters": []
        },
        {
            "name": "rotate",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "angle",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 360
                }
            ]
        },
        {
            "name": "scale",
            "input_type": "image",
            "output_type": "image",
            "parameters": [
                {
                    "name": "width",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 8
                },
                {
                    "name": "height",
                    "type": "int",
                    "value": 0,
                    "min_value": 0,
                    "max_value": 8
                }
            ]
        }
    ]);
  
  } catch (error) {
    // Handle errors and send an appropriate response
    console.error('Error fetching tools:', error.message);

    res.status(error.response?.status || 500).json({
      error: 'Failed to fetch tools',
      details: error.response?.data || error.message,
    });
  }
});

module.exports = router;
