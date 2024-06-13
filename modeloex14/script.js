
function calcular(){
    
    var n1 = document.getElementById('nota1')
    var n2 = document.getElementById('nota2')
    var n3 = document.getElementById('nota3')
    var res = document.getElementById('res')
    var m = n1 + n2 + n3 / 3; 
    var media = Number(n1.value)
    var media = Number(n2.value)
    var media = Number(n3.value)
    
    if(media >= 6){
        res.innerHTML += 'Aprovado!'
    }else if(media >= 5){
        res.innerHTML += 'Recuperação!'
    }else{
        res.innerHTML += 'Reprovado!'
    }
}