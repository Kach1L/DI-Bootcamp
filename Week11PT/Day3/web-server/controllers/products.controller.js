const { products } = require("../config/products.js");

const getAllProducts = (req, res) => {
  res.json(products);
};

const getProduct = ((req, res) => {
    console.log("params=>", req.params);
    const { id } = req.params;
    const user = users.find((item) => item.id == id);
    if (!user) return res.status(404).json({ msg: "user not found" });
    res.json(user);
  });

module.exports = {
  getAllProducts,
  getProduct
};