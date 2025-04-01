const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const users = [
    {id:1, name: 'User1'},
    {id:2, name: 'User2'},
    {id:3, name: 'User3'},
]

app.get('/Hello', (req, res) => {
    res.send('Hello World!!')
})

app.get('/api/users', (req, res) => {
    res.json({ok: true, users: users})
})

app.get('/api/users/user', (req, res) => {
    let user = "";
    const { user_id, name } = req.query;

    if (req.query.name == null) {
        user = users.filter(data => data.id == user_id);
    } else {
        user = users.filter(data => data.id == user_id && data.name == name);
    }
    res.json({ok: false, users: user})
})

app.get('/api/users/:id', (req, res) => {
    let user_id = req.params.id

    const user = users.filter(data => data.id == user_id);
    res.json({ok: false, users: user})
})

app.post('/api/users/userBody', (req, res) => {
    const id = req.body.id;
    const user  = users.filter(data => data.id == id);
    res.json({ok: false, users: user})
})

app.post('/api/users/add', (req, res) => {
    const { id, name } = req.body;
    const user = users.concat({id, name});
    res.json({ok: true, users: user})
})
    

app.put('/api/users/update', (req, res) => {
    const { id, name } = req.body;
    const user = users.map( data => {
       if (data.id == id) data.name = name
       return {
           id: data.id,
           name: data.name
       }
    })
    res.json({ok: true, users: user})
})

app.patch('/api/users/update/:id', (req, res) => {
    const { id } = req.params;
    const { name } = req.body;
    const user = users.map( data => {
       if (data.id == id) data.name = name
       return {
           id: data.id,
           name: data.name
       }
    })
    res.json({ok: true, users: user})
})

app.delete('/api/users/delete', (req, res) => {
    const { id } = req.body;
    const user = users.filter(data => data.id != id);
    res.json({ok: true, users: user})
})

module.exports = app;
