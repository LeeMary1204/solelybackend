const mongoose = require("mongoose")

const uri = "mongodb+srv://root:root@cluster0.laene46.mongodb.net/solelywebsite?retryWrites=true&w=majority"

const connectDatabase = () => {
  mongoose
    .connect(uri)
    .then((data) => {
      console.log(`Mongodb connected with server: ${data.connection.host}`)
    }).catch((err) => {
      console.log(err.message)
    })
}

module.exports = connectDatabase