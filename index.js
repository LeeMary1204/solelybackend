const app = require("./app")
const connectDatabase = require("./config/database")
const scheduleJob = require('./scheduleJob')


connectDatabase()

scheduleJob()


const server = app.listen(8777, () => {
  console.log(`Server is working on http://localhost:8777`)
})