const box1 = document.querySelector('.box-one');
const box2 = document.querySelector('.box-two');
const box3 = document.querySelector('.box-three');


const content1 = document.querySelector('.content-one');
const content2 = document.querySelector('.content-two');
const content3 = document.querySelector('.content-three');


box1.addEventListener('mouseover', function(event) {
    setTimeout(function() {
        var pre = parseInt(content1.style.left);
        content1.style.left = pre + 180 + "px";
    }, 5);

});

box1.addEventListener('mouseout', function(event) {
    content1.style.left = "350px";
});



box2.addEventListener('mouseover', function(event) {
    setTimeout(function() {
        content2.style.left = "550px";
    }, 5);

});

box2.addEventListener('mouseout', function(event) {
    content2.style.left = "800px";
});



box3.addEventListener('mouseover', function(event) {
    setTimeout(function() {
        content3.style.left = "900px";
    }, 5);

});

box3.addEventListener('mouseout', function(event) {
    content3.style.left = "1100px";
});