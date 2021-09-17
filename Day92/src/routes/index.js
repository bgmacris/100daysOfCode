const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.render('index', { title: 'SERVER' });
})

router.get('/help', (req, res) => {
    res.render('help', { title: 'HELP' });
})

module.exports = router;