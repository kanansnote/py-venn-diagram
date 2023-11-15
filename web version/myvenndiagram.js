document.getElementById('start').addEventListener('click',
function() {
  document.getElementById('intro').style.display = 'none';
  document.getElementById('desktop').style.display = 'block';
});

document.getElementById('to-mobile').addEventListener('click',
function() {
  document.getElementById('desktop').style.display = 'none';
  document.getElementById('mobile').style.display = 'block';
});

document.getElementById('to-desktop').addEventListener('click',
function() {
  document.getElementById('mobile').style.display = 'none';
  document.getElementById('desktop').style.display = 'block';
});