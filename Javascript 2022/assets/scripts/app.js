const defaultResult = 0;
let currentResult = defaultResult;
let logEntries = [];

function getUserNumberInput() {
   return parseInt(userInput.value)
}

function createAndWriteOutput(operator, resultBeforeCalc, calcNumber) {
   const calcDescription =  `${resultBeforeCalc} ${operator} ${calcNumber}`
   outputResult(currentResult, calcDescription)
}

function add() {
   const enteredNumber = getUserNumberInput ();
   const initialResult = currentResult;  
   currentResult += enteredNumber;
   createAndWriteOutput('+', initialResult, enteredNumber)
   logEntries.push(enteredNumber);
   //.push 배열에 변수이름을 넣어, 값을 넣을 수 있다.
   // like, logEntries = [enteredNumber]; 와 같다. 
   console.log(logEntries[1]); 
}
/*내부 상수와 외부 전역의 값을 섞어서 사용하지 않고,
오로지 전역값만을 사용해 이벤트 리스너로 사용되는 점에서는 괜찮다. */ 
/* 이런 함수는...return 해서는 안된다.. : 할수는 있는데, 하면 전역변수의 값을 바로 수정해 버릴것  */

function subtract() {
   const enteredNumber = getUserNumberInput();
   const initialResult = currentResult;  
   currentResult -= enteredNumber;
   createAndWriteOutput('-', initialResult, enteredNumber)
}

function multiply() {
   const enteredNumber = getUserNumberInput();
   const initialResult = currentResult;  
   currentResult *= enteredNumber;
   createAndWriteOutput('*', initialResult, enteredNumber)
}

function divide() {
   const enteredNumber = getUserNumberInput();
   const initialResult = currentResult;  
   currentResult /= enteredNumber;
   createAndWriteOutput('/', initialResult, enteredNumber)
}



addBtn.addEventListener('click', add);
/* addEventListener = 브라우저에 내장된 함수 */
/* 브라우저에게, click을 하면 add라는 함수를 실행하도록 해줘~ 하는 것 */
/* 즉, 브라우저에게 add라는 함수의 주소를 알려주고, 버튼이 클릭되면 함수를 호출하도록 한다.*/
subtractBtn.addEventListener('click', subtract);
multiplyBtn.addEventListener('click', multiply);
divideBtn.addEventListener('click', divide);
