require('dotenv').config();
const express = require('express');
const cors = require('cors');
const pool = require('./db'); // Import the existing pool connection

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Basic route for health check
app.get('/', (req, res) => {
  res.send('Welcome to the VR ADHD Therapy Backend');
});

// Users route (to handle registration and sign-in)
const usersRouter = require('./routes/registration');
app.use('/api/registration', usersRouter);

// Example of using pool in a route (if needed)
app.get('/api/test-db', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW()');
    res.json(result.rows);
  } catch (err) {
    console.error('Database query error', err.stack);
    res.status(500).send('Server error');
  }
});

// Listen on the specified port
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
