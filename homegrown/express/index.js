const express = require('express')


const app = express()
const port = 3000


app.get('/test', (req, res) => {
    console.log('HEADERS:', JSON.stringify(req.headers));
    console.log('BODY:', JSON.stringify(req.body));
    res.send('Hello world')
})

app.listen(port, () => {
    console.log(`APP ACTIVE ON PORT: ${port}`);
})