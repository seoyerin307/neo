var express = require('express');
var mysql = require('mysql');
const env = require('dotenv').config({ path: "../../.env" });
var app = express();

var connection = mysql.createConnection({
    host: process.env.NODE_MYSQL_HOST,
    user: process.env.NODE_MYSQL_USER,
    password: process.env.NODE_MYSQL_PASSWORD,
    database: process.env.NODE_MYSQL_DATABASE
});


connection.connect(function(err) {
    if (err) {
        console.error('Databases is connected~!!\n\n');
    } else {
        console.log('Databases is connected~!!\n\n');
    }
});

app.get('/', function (req, res) {
    connection.query('SELECT * FROM st_info', function (err, rows, fields) {
        connection.end();
        if (err) {
            res.send(rews);
            console.log("The solution is : ", rows);
         } eles {
            console.log("Error while performing Query~!!\n\n');
        }
    })
})

app.listen(8000, function() {
    console.log("8000 Port : Server Started~!!\n\n")
})