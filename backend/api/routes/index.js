var express = require('express');
var router = express.Router();
var passport = require('passport');
var axios = require('axios');
var userModel = require('../models/user');
var User = require('../controllers/user');
const multer = require('multer');
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });
const FormData = require('form-data');

router.get('/', function (req, res) {
  res.jsonp('Im here. My name is api')
})

// done
router.post('/register', function (req, res) {
  var d = new Date().toISOString().substring(0, 19);
  User.checkUserExistence(req.body.username)
    .then(user => {
      if (!user) {
        userModel.register(new userModel({
          username: req.body.username,
          dateCreated: d,
          dateAccessed: d
        }), req.body.password, function async (err, user) {
          if (err) {
            res.status(401).jsonp({ error: err, message: "Register error: " + err });
          } else {
            // Get the hash from the saved user
            const newUser = {
              username: req.body.username,
              password_hash: user.hash,  // The hash is stored in the user object
              name: req.body.name,
              email: req.body.email,
              type: "registered"
            }
            const apiBaseUrl = process.env.USERS_MICRO_SERVICE // Ensure this is set in your .env file
            axios.post(`${apiBaseUrl}/users`, newUser)
              .then(response => {
                console.log('Microservice Response:', response.data);
                res.jsonp('User registed with sucess!');
              })
              .catch(error => {
                console.error('Error posting to microservice:', error);
                // You might want to handle this error appropriately
                res.status(500).jsonp({ error: "Microservice error: " + error });
              });
          }
        });
      }
    })
    .catch(erro => {
      res.status(500).jsonp({ error: "Server error: " + erro });
    });
});

// done
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

// done
router.post('/logout', function (req, res) {
  req.logout(function (err) {
    if (err) return res.status(500).json({ error: err });
    res.json({ message: "Logged out successfully" });
  });
});

// done
router.get('/profile', passport.authenticate(['local', 'anonymous'], { session: false }), async (req, res) => {
  if (req.isAuthenticated()) {
    // request ao micro serviço a info do user
    const apiBaseUrl = process.env.USERS_MICRO_SERVICE // Ensure this is set in your .env file
    // Make the GET request to the external API
    const response = await axios.get(`${apiBaseUrl}/users/${req.user.username}`);
    res.status(200).jsonp({ email: response.data.email, name:response.data.name,status:response.data.plan});
  } else {
    res.status(401).jsonp({ error: "Not authenticated" });
  }
});

// done
router.get('/user/status', passport.authenticate(['local', 'anonymous'], { session: false }), (req, res) => {
  if (req.isAuthenticated()) {
    res.json({ status: 'loggedIn', sessionId:req.sessionID  });
  } else {
    res.json({ status: 'anonymous', sessionId:req.sessionID  });
  }
});

//done
router.get('/tools', passport.authenticate(['local', 'anonymous'], { session: false }), async (req, res) => {
  try {
    // Use the API base URL from your environment variables
    const apiBaseUrl = process.env.TOOL_MICRO_SERVICE // Ensure this is set in your .env file
    // Make the GET request to the external API
    console.log(`${apiBaseUrl}/tools`)
    const response = await axios.get(`${apiBaseUrl}/tools`);
    // Optionally process the response.data here if needed
    const staticTools = response.data;
    return res.status(200).json(staticTools)
  
  } catch (error) {
    // Handle errors and send an appropriate response
    console.error('Error fetching tools:', error.message);

    res.status(error.response?.status || 500).json({
      error: 'Failed to fetch tools',
      details: error.response?.data || error.message,
    });
  }
});

// done
router.get('/projects', passport.authenticate(['local', 'anonymous'], { session: false }), async (req, res) => {
  try {
    // logica de enviar const = axios.get wtv
    // localhost:3003/projects/owner/<user_id></user_id>
    if(req.isAuthenticated()){

      const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
      const response = await axios.get(`${apiBaseUrl}/projects/owner/${req.user.username}`);
      return res.status(200).json(response.data);

    }else{
    const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
    const response = await axios.get(`${apiBaseUrl}/projects/owner/anonymous-${req.sessionID}`);
    return res.status(200).json(response.data);
    }
  
  } catch (error) {
    // Handle errors and send an appropriate response
    console.error('Error fetching projects:', error.message);

    res.status(error.response?.status || 500).json({
      error: 'Failed to fetch projects',
      details: error.response?.data || error.message,
    });
  }
});

// done (testar para registados)
router.post('/projects', passport.authenticate(['local', 'anonymous'], { session: false }), async (req, res) => {
  if (req.isAuthenticated()) {
    const { name, owner } = req.body;
      // Create a new project
      const newProjectWrapper = {
        name: name || 'Untitled', // Default to 'Untitled' if no name is provided
        owner: req.user.username, // Use user ID if authenticated, otherwise use session ID
        tools:[]
      };
      const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
      const response = await axios.post(`${apiBaseUrl}/projects`,newProjectWrapper);
      const newProject = response.data;
      res.json(newProject);
  } else {
    try{
      const { name, owner } = req.body;
      // Create a new project
      const newProjectWrapper = {
        name: name || 'Untitled', // Default to 'Untitled' if no name is provided
        owner: `anonymous-${req.sessionID}`, // Use user ID if authenticated, otherwise use session ID
        tools:[]
      };
      const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
      const response = await axios.post(`${apiBaseUrl}/projects`,newProjectWrapper);
      const newProject = response.data;
      res.json(newProject);
    }catch(e){
      console.error(e)
    }
  }
});

// todo testar isto
router.post(
  '/projects/images',
  upload.single('image'),
  passport.authenticate(['local', 'anonymous'], { session: false }),
  async (req, res) => {
    const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
    if (req.isAuthenticated()) {
      try {
        // Handle the anonymous user case
        // Extract `projectId` and process the image file

        const projectId = req.body.projectId;
        if (!projectId) {
          return res.status(400).json({ error: 'Project ID is required.' });
        }

        // Assume `req.file` has the uploaded image (if using middleware like multer)
        const file = req.file;
        if (!file) {
          return res.status(400).json({ error: 'No image provided.' });
        }
        const formData = new FormData();
        formData.append("image", file.buffer, file.originalname);
        const response = await axios.post(`${apiBaseUrl}/projects/images/${projectId}`, formData, {
          headers: {
          "Content-Type": "multipart/form-data",
        }
        });
        // apagar imagem do upload
        // Return the dummy URI for now
        return res.status(200).json({ uri: response.data.image});
      } catch (e) {
        console.error('Error uploading file for anonymous user:', e);
        return res.status(500).json({ error: 'Internal server error.' });
      }
    } else {
      try {
        // Handle the anonymous user case
        // Extract `projectId` and process the image file

        const projectId = req.body.projectId;
        if (!projectId) {
          return res.status(400).json({ error: 'Project ID is required.' });
        }

        // Assume `req.file` has the uploaded image (if using middleware like multer)
        const file = req.file;
        if (!file) {
          return res.status(400).json({ error: 'No image provided.' });
        }
        const formData = new FormData();
        formData.append("image", file.buffer, file.originalname);
        const response = await axios.post(`${apiBaseUrl}/projects/images/${projectId}`, formData, {
          headers: {
          "Content-Type": "multipart/form-data",
        }
        });
        return res.status(200).json(response.data);
      } catch (e) {
        console.error('Error uploading file for anonymous user:', e);
        return res.status(500).json({ error: 'Internal server error.' });
      }
    }
  }
);

// todo - `GET localhost:3003/projects/images/<project_id>`: obter as imagens do projeto 
router.get('/projects/images', passport.authenticate(['local', 'anonymous'], { session: false }), async (req, res) => {
  const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
    
      try{
        const { projectId } = req.query;
        const uris = await axios.get(`${apiBaseUrl}/projects/images/${projectId}`);
        res.status(200).json(uris.data)

      }catch(e){
        console.error(e)
      }
      
});

// pedir bytes de image uma a uma
router.get('/projects/images/:id', passport.authenticate(['local', 'anonymous'], { session: false }), async (req, res) => {
  const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
  axios.get(`${apiBaseUrl}/projects/images/data/${req.params.id}`, { responseType: 'arraybuffer' })
      .then(response => {
          res.contentType(response.headers.get('content-type'))
          res.status(200).send(response.data)
      })
      .catch(error => res.status(500).jsonp(error))
});

// done (testar para autenticado)
router.put('/projects', passport.authenticate(['local', 'anonymous'], { session: false }), async (req, res) => {
  if (req.isAuthenticated()) {
    const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
    const response = await axios.put(`${apiBaseUrl}/projects/${req.body.id}`)
    res.status(200).json(`Sucess on saving ${req.body.id}`);
  } else {
    try{
      const apiBaseUrl = process.env.PROJECTS_MICRO_SERVICE
      const response = await axios.put(`${apiBaseUrl}/projects/${req.body.id}`,req.body)
      res.status(200).json(`Sucess on saving ${req.body.id}`);
    }catch(e){
      console.error(e)
    }
  }
});

module.exports = router;
