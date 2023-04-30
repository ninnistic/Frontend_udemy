async function rainbow(){
  await delayedColorChange('red', 1000)
  delayedColorChange('orange', 1000)
}
// await를 쓰지 않으면 그냥 orange로 바뀜 -> 동시에 실행 됨
// 즉 await를 쓰면 빨간색으로 바뀔 떄 까지 기다렸다가 -> 완료되면 주황으로 바뀜


async function makeTwoRequests() {
  // Error handling
  // try문에 오류가 될 코드를 적으면 catch에서 어떻게 처리할지를 담당한다. 
  try {
    let data1 = await fakeRequest('/page1');
    console.log(data1);
    let data2 = await fakeRequest('/page2');
    console.log(data2);
  }catch(e) {
    console.log('Error I caught it!, error is', e)
  }
}