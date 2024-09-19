const express = require('express');
const router = express.Router();
const pool = require('../db'); // Import database connection

// Registration Route
router.post('/register', async (req, res) => {
  const { kid_name, gender, age, dob, parent_name, email, password, phone_number } = req.body;
  
  try {
    const newUser = await pool.query(
      `INSERT INTO users (kid_name, gender, age, dob, parent_name, email, password, phone_number)
       VALUES ($1, $2, $3, $4, $5, $6, $7, $8) RETURNING *`,
      [kid_name, gender, age, dob, parent_name, email, password, phone_number]
    );
    res.status(201).json(newUser.rows[0]);
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
});

// Sign-in Route
router.post('/signin', async (req, res) => {
  const { email, password } = req.body;
  
  try {
    const user = await pool.query(
      'SELECT * FROM users WHERE email = $1 AND password = $2',
      [email, password]
    );
    
    if (user.rows.length > 0) {
      res.status(200).json({ message: 'Sign-in successful', user: user.rows[0] });
    } else {
      res.status(401).send('Invalid credentials');
    }
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
});

module.exports = router;
