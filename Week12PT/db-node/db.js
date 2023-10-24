const knex = require("knex");
// const dotenv = require("dotenv");
// dotenv.config();
require("dotenv").config();

const db = knex({
  client: "pg",
  connection: {
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME,
  },
});

// INSERT
// db("products")
//   .insert([
//     { name: "iPad", price: 700 },
//     { name: "iKey", price: 500 },
//   ])

// UPDATE
// db("products")
//   .where({ id: 2 })
//   .update({ price: 5555 })
//   .returning(["id", "price", "name"])
// DELETE
// db("products")
//   .where({ id: 2 })
//   .del()
//   .returning(["id", "price", "name"])
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((err) => {
//     console.log(err);
//   });

// SELECT
// db.from("products").select("*")
//   .then((rows) => {
//     console.log("rows=>", rows);
//   })
//   .catch((e) => {
//     console.log(e);
//   });

// db.raw("select * from products where id = ? or name = ?", [2, "iPa"]).then(
//   (data) => {
//     console.log("rows=>", data.rows);
//   }
// );
