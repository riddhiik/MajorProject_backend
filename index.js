require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');

const app = express();
const PORT = process.env.PORT || 5000;

// PostgreSQL connection setup
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

pool.connect()
  .then(() => console.log('Connected to PostgreSQL database'))
  .catch(err => console.error('Database connection error', err.stack));

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.send('Welcome to the VR ADHD Therapy Backend');
});

// Users route (to handle registration and sign-in)
const usersRouter = require('./routes/users');
app.use('/api/users', usersRouter);

// Listen on the specified port
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
