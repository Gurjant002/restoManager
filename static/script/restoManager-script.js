columna = document.querySelectorAll('#col-num');
for (var i = 0; i < columna.length; i++)
    newNum = parseInt(columna[i].textContent)

inputNum = document.querySelector('#floatingNum')
inputNum.value = 1+newNum
