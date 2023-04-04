// const allImages = document.getElementsByTagName('img');

// for (let img of allImages) {
//     img.src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Silky_bantam.jpg/440px-Silky_bantam.jpg'
// }

// const squareImages = document.getElementsByClassName('square');

// for (let img of squareImages) {
//     img.src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Silky_bantam.jpg/440px-Silky_bantam.jpg'
// }


// Finds first h1 element:
// document.querySelector('h1');

// Finds first element with ID of red:
// document.querySelector('#red');

// Finds first element with class of 
// document.querySelector('.big');


const links = document.querySelectorAll('p a');

for (let link of links) {
    console.log(link.href)
}