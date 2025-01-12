import createError from 'http-errors'; //Helps http error creation 
import cookieParser from 'cookie-parser'; //Parses cookies sent with client requests
import logger from 'morgan'; //Logs http errors for monitoring and debug
import session from 'express-session'; //Manages session state on server (not persistent if server goes down, is it enough?)
import passport from 'passport'; // Enables user authentication 
import { Strategy as LocalStrategy } from 'passport-local'; //Passport strategy for user/pass auth 
import express from 'express';
import cors from 'cors'; // Import the CORS middleware
import 'dotenv/config';
import mongoose from "mongoose";

import apiRouter from './router/router.js';

const app = express();

app.use(logger('dev'));
app.use(cookieParser());
app.use(session({
  secret: 'RAS2025',
  resave: false,
  saveUninitialized: true,
  cookie: { secure: true } 
}));
app.use(passport.initialize());
app.use(passport.session());

//Passport config
import UnknownUser from './authentication/model/Auth.js';
passport.use(new LocalStrategy(UnknownUser.authenticate()));
passport.serializeUser(UnknownUser.serializeUser());
passport.deserializeUser(UnknownUser.deserializeUser());
// Enable CORS for all origins
app.use(cors());
// Middleware for parsing JSON
app.use(express.json());


mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  serverSelectionTimeoutMS: 5000
});

var db = mongoose.connection;
db.on('error', console.error.bind(console, 'Erro de conexão ao MongoDB'));
db.once('open', () => {
  console.log("Conexão ao MongoDb realizada com sucesso");
});


// Use the API router
app.use('/api', apiRouter);

app.use(function (req, res, next) {
  next(createError(404));
});

// Root route
app.get('/', (req, res) => {
  res.send('Welcome to the API Gateway');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
