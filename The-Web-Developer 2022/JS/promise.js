const fakeRequest = (url) => {
  return new Promise((resolve, reject) => {
    const rand = Math.random();
    setTimeout(() => {
      if(rand < 0.7){
        resolve('YOUR FAKE DATA HERE');
      }
      reject('REQUEST ERROR!')
    }
  })
}

fakeRequest('/dogs/1')
.then(() => {
  console.log("DONE WITH REQUEST")
})
.catch((err) => {
  console.timeLog("OH NO", err)
})