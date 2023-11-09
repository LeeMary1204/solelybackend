const express = require("express")
const {
  getJobsByFilter,
  getAllJobs,
  registerJob
} = require("../controllers/jobController")

const router = express.Router()

router.route("/getAllJobs").get(getAllJobs)
router.route("/getJobsByFilter").post(getJobsByFilter)

module.exports = router