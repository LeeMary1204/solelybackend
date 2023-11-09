const mongoose = require("mongoose")

const jobSchema = new mongoose.Schema({
  job: {
    type: String,
  },
  company: {
    type: String,
  },
  descriptionURL: {
    type: String,
  },
  date: {
    type: String,
  },
  role: {
    type: String,
  },
  jobType: {
    type: String,
  }
})

module.exports = mongoose.model("Job", jobSchema)