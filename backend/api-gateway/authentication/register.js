import mongoose from 'mongoose';
import 'dotenv/config';


import Auth from './model/Auth.js';
import bcrypt from 'bcrypt';

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true });

export default async (req, res) => {
  try {
    const { email, password } = req.body;

    // Check if the user already exists
    const existingUser = await Auth.findById(email);
    if (existingUser) {
      return res.status(409).send({ message: 'User already exists' });
    }

    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create a new user in the database
    const newUser = new Auth({ _id: email, password_hash: hashedPassword });    
    await newUser.save();

    // Send this data to a user service 
    // await axios.post(process.env.USER_SERVICE_URL + '/users', { email });

    res.status(201).send({ message: 'User registered successfully' });
  } catch (error) {
    console.error('Error during registration:', error);
    res.status(500).send({ message: 'Internal server error' });
  }
};
