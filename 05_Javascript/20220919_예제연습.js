// 클릭 시 alert 출력
const alertMessage = function () {
  alert('JS파일 테스트')
}
const myButton = document.querySelector('#my-button')
myButton.addEventListener('click', alertMessage)


// Input에 사용자가 입력 시 document에 입력한 내용 출력
const myTextInput = document.querySelector('#my-text-input')
myTextInput.addEventListener('input', function(event){
  const myPtag = document.querySelector('#my-paragraph')
  myPtag.innerText = event.target.value
})

// 원하는 색상 영어 입력 시 h2 태그의 텍스트 색상 변경
const colorInput = document.querySelector('#change-color-input')
const changeColor = function (event) {
  const h2Tag = document.querySelector('h2')
  h2Tag.style.color = event.target.value
}
color.Input.addEventListener('input', changeColor)