const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
});

app.get('/Hello', (req, res) => {
    res.send('Hello World!!')
})

//select all rows from st_info table
app.get('/select', (req, res) => {
    let result = connection.query('SELECT * FROM st_info');
    console.log(result);
    res.send(result);
})

// insert data to st_info table
app.get('/insert', (req, res) => {
    const { st_id, name, dept } = req.query;
    const result = connection.query("INSERT INTO st_info values (?, ?, ?)",
        [st_id, name, dept]);
        res.redirect('/select');
    })

// update data to st_info table
app.get('/update', (req, res) => {
    const { st_id, name, dept } = req.query;
    const result = connection.query("UPDATE st_info SET NAME = ?, DEPT = ? WHERE ST_ID = ?",
        [name, dept, st_id]);
        res.redirect('/select');
    })

// delete data from st_info table
app.get('/delete', (req, res) => {
    const st_id= req.query.st_id;
    const result = connection.query("delete from st_info WHERE ST_ID = ?",
        [st_id]);
        res.redirect('/select');
    })

module.exports = app;
