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
            res.status(401).jsonp({ error: err, message: "Register error: " + err });
          } else {
            // MANDAR AO BACK
            res.jsonp('Utilizador registado com sucesso!')
          }
        });
      }
    })
    .catch(erro => {
      res.status(500).jsonp({ error: "Server error: " + erro });
    });
});

router.post('/login', (req, res, next) => {
  passport.authenticate('local', async (err, user, info) => {
    if (err) {
      console.error('Authentication error:', err);
      return res.status(500).json({ message: 'Internal server error' });
    }

    if (!user) {
      // If authentication failed, return the error message provided by Passport
      return res.status(401).json({ message: info?.message || 'Invalid credentials' });
    }

    // Log the user in and update their dateAccessed
    req.logIn(user, async (loginErr) => {
      if (loginErr) {
        console.error('Login error:', loginErr);
        return res.status(500).json({ error:"Failed to log in server error",message: 'Failed to log in' });
      }

      try {
        const date = new Date().toISOString().substring(0, 19); // Current timestamp
        await User.updateUser(user.username, { dateAccessed: date }); // Update user's last accessed date
        res.status(200).json({ message: 'Login successful', sessionId:req.sessionID});
      } catch (updateErr) {
        console.error('Error updating user access date:', updateErr);
        res.status(500).json({ message: 'Error updating user access date' });
      }
    });
  })(req, res, next);
});

router.post('/logout', function (req, res) {
  req.logout(function (err) {
    if (err) return res.status(500).json({ error: err });
    res.json({ message: "Logged out successfully" });
  });
});

router.get('/profile', passport.authenticate(['local', 'anonymous'], { session: false }), (req, res) => {
  if (req.isAuthenticated()) {
    // request ao micro serviço a info do user
    res.status(200).jsonp({ email: req.user.username, name:"jmf",status:"premium"});
  } else {
    console.log("Not Auth")
    res.status(401).jsonp({ error: "Not authenticated" });
  }
});

router.get('/mixed', passport.authenticate(['local', 'anonymous'], { session: false }), (req, res) => {
  if (req.isAuthenticated()) {
    return res.json({ message: `Welcome back, ${req.user.username}.`, sessionId:req.sessionID });
  }
  res.json({ message: 'Hello anonymous user!', sessionId:req.sessionID});
});

router.get('/user/status', passport.authenticate(['local', 'anonymous'], { session: false }), (req, res) => {
  if (req.isAuthenticated()) {
    console.log("loggedIn")
    res.json({ status: 'loggedIn', sessionId:req.sessionID  });
  } else {
    res.json({ status: 'anonymous', sessionId:req.sessionID  });
  }
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

router.get('/projects', passport.authenticate(['local', 'anonymous'], { session: false }), (req, res) => {
  try {
    // logica de enviar const = axios.get wtv
    return res.status(200).json([]);
  
  } catch (error) {
    // Handle errors and send an appropriate response
    console.error('Error fetching projects:', error.message);

    res.status(error.response?.status || 500).json({
      error: 'Failed to fetch projects',
      details: error.response?.data || error.message,
    });
  }
});

router.post('/projects', passport.authenticate(['local', 'anonymous'], { session: false }), (req, res) => {
  if (req.isAuthenticated()) {
    // todo
  } else {
    try{
      const { name, owner } = req.body;
      // Create a new project
      const newProjectWrapper = {
        name: name || 'Untitled', // Default to 'Untitled' if no name is provided
        owner: `anonymous-${req.sessionID}`, // Use user ID if authenticated, otherwise use session ID
      };

      // send to backend
      // retrieve from backend
      const newProject = {
        id: "umId",
        name: name || 'Untitled', // Default to 'Untitled' if no name is provided
        owner: `anonymous-${req.sessionID}`, // Use user ID if authenticated, otherwise use session ID
      };
      // Return the newly created project
      res.json(newProject);
    }catch(e){
      console.log(e)
    }
  }
});

module.exports = router;
