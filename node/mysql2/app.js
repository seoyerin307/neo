const mysql = require("mysql2/promise");
const env = require('dotenv').config({ path:"../../.env"});

const db = async() => {
    try {
    // database connection
        let connection = await mysql.createConnection({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database
})

let [rows, fields] = await connection.query('select * from st_info');
console.log(rows);

let data = {
    st_id:"202599"
    name:"Moon"
    dept:"Computer"
}

let inserId = data.st_id;

//insert query
[rows, fields] = await connection.query("insert into st_info values ?", data);
console.log("\nData is insertId~!!");

// select * query for inserted data
[rows, fields] = await connection.query("select * from st_info where st_id = ?", [insertId]);
console.log(rows);

// update query
[rows, fields] = await connection.query("update st_info set name = ?, dept = ? where st_id = ?", ["Game", isnertId]);
console.log("\nData is Updated!!");

// select * query for updated data
[rows, fields] = await connection.query("select * from st_info where st_id = ?", [insertId]);
console.log(rows);

// delete query
[rows, fields] = await connection.query("delete from st_info where st_id = ?", [insertId]);
console.log('\nData is Deleted!!');

// select * query for deleted data
[rows, fields] = await connection.query("select * from st_info where st_id = ?", [insertId]);
console.log(rows);

    } catch (error) {
        console.log(err);
    }
}

db();

