const Job = require("../models/jobModel")

exports.getJobsByFilter = async (req, res, next) => {

  const { roles, types, company } = req.body

  var list = []
  Job.find().then((response) => {
    list = [...response]

    var result = list.filter(element => {
      return element.company.toLowerCase().indexOf(company.toLowerCase()) != -1 && roles.includes(element.role) && types.includes(element.jobType)
    })
    res.status(200).json({
      success: true,
      result,
    })
  })
}


exports.getAllJobs = async (req, res, next) => {

  await Job.find().then(jobs => {

    res.status(200).json({
      success: true,
      jobs,
    })
  }).catch(err => {
    console.error(err)
  })
}


exports.deleteAll = (req, res, next) => {
  // const response = await Job.deleteMany({ _id: { $ne: null } }).exec()
  console.log('delete All data start')
  Job.deleteMany({})
  console.log('delete All data end')
}