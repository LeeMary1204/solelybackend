const express = require("express")
const cors = require('cors')
const app = express()
const bodyParser = require("body-parser")


const errorMiddleware = require("./middleware/error")

// cors解决跨域问题
app.use(cors())
app.use(express.json())
// bodyParser handle form data
app.use(bodyParser.urlencoded({ extended: true }))

const jobRouter = require("./routers/jobRouter")
app.use("/api", jobRouter)

// Middleware for Errors
app.use(errorMiddleware)

module.exports = app