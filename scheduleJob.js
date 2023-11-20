const { execSync } = require('child_process')
const schedule = require('node-schedule')
const { deleteAll } = require('./controllers/jobController')

const login = () => {
  const path = './login.py'
  execSync(`python ${path}`)
}

const runPythonInNodeEnvSync = () => {
  const role = '"frontend developer"'
  const jobType = '"internship"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}

const runPythonInNodeEnvSync1 = () => {
  const role = '"software developer"'
  const jobType = '"internship"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}

const runPythonInNodeEnvSync2 = () => {
  const role = '"fullstack developer"'
  const jobType = '"internship"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}


const runPythonInNodeEnvSync3 = () => {
  const role = '"frontend developer"'
  const jobType = '"entry level"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}

const runPythonInNodeEnvSync4 = () => {
  const role = '"software developer"'
  const jobType = '"entry level"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}

const runPythonInNodeEnvSync5 = () => {
  const role = '"fullstack developer"'
  const jobType = '"entry level"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}

const runPythonInNodeEnvSync6 = () => {
  const role = '"frontend developer"'
  const jobType = '"mid-senior level"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}

const runPythonInNodeEnvSync7 = () => {
  const role = '"software developer"'
  const jobType = '"mid-senior level"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}

const runPythonInNodeEnvSync8 = () => {
  const role = '"fullstack developer"'
  const jobType = '"mid-senior level"'
  const path = './getJobs.py'
  execSync(`python ${path} ${role} ${jobType}`)
}

const sleep = (n) => {
  var start = new Date().getTime()
  while (true) {
    if (new Date().getTime() - start > n) {
      break
    }
  }
}

const scheduleObjectSyntax = () => {
  schedule.scheduleJob('0 0 0 * * *', () => {
    deleteAll()
    sleep(10000)

    // console.log('login start')
    // login()
    // console.log('login end')
    // sleep(1000)

    console.log('runPythonInNodeEnvSync start')
    runPythonInNodeEnvSync()
    console.log('runPythonInNodeEnvSync end')
    sleep(1000)

    console.log('runPythonInNodeEnvSync1 start')
    runPythonInNodeEnvSync1()
    console.log('runPythonInNodeEnvSync1 end')
    sleep(1000)

    console.log('runPythonInNodeEnvSync2 start')
    runPythonInNodeEnvSync2()
    console.log('runPythonInNodeEnvSync2 end')
    sleep(1000)

    console.log('runPythonInNodeEnvSync3 start')
    runPythonInNodeEnvSync3()
    console.log('runPythonInNodeEnvSync3 end')
    sleep(1000)

    console.log('runPythonInNodeEnvSync4 start')
    runPythonInNodeEnvSync4()
    console.log('runPythonInNodeEnvSync4 end')
    sleep(1000)

    console.log('runPythonInNodeEnvSync5 start')
    runPythonInNodeEnvSync5()
    console.log('runPythonInNodeEnvSync5 end')
    sleep(1000)

    console.log('runPythonInNodeEnvSync6 start')
    runPythonInNodeEnvSync6()
    console.log('runPythonInNodeEnvSync6 end')
    sleep(1000)

    console.log('runPythonInNodeEnvSync7 start')
    runPythonInNodeEnvSync7()
    console.log('runPythonInNodeEnvSync7 end')
    sleep(1000)

    console.log('runPythonInNodeEnvSync8 start')
    runPythonInNodeEnvSync8()
    console.log('runPythonInNodeEnvSync8 end')
  })
}



module.exports = scheduleObjectSyntax

