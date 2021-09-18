'use strict'

var express = require('express'),
    app = express(),
    http = require('http').createServer(app),
    io = require('socket.io')(http),
    port = process.env.PORT || 3000,
    sourceDir = express.static(`${__dirname}/src`)

app
    .use(sourceDir)
    .get('/', (req, res) => {
        res.sendFile(`${sourceDir}/index.html`)
    })

http.listen(port, () => {
    console.log(`Connect: http://localhost:${port}`)
})

io.on('connection', (socket) => {
    socket.broadcast.emit('new user', { message: 'Ha entrado un usuario al Chat' })

    socket.on('new message', (message) => {
        io.emit('user says', message)
    })

    socket.on('disconnect', () => {
        console.log('Ha salido un usuario del Chat')
        socket.broadcast.emit('bye bye user', { message: 'Ha salido un usuario del Chat' })
    })
})