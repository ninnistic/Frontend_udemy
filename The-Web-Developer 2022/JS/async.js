const login = async (username, password) => {
  if(!username || !password) throw 'Missing Credentials'
  if(password === 'shaggyfeetarcute') return 'Welcome'
  throw 'Invalid Password'
}

login('ninni')
.then(msg => {
  console.log("LOGGED IN!")
  console.log(msg)
})
.catch(err => {
  console.log("ERROR!")
  console.log(err)
})