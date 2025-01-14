import mongoose from 'mongoose';
const { Schema, model } = mongoose;

const authSchema = new Schema({
  _id: String,
  password_hash: String,
});

// Use email as _id
const Auth = model('Auth', authSchema);
export default Auth;
