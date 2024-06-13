var inicio = document.querySelector('input#inicio')
    var fim = document.querySelector('input#fim')
    var passo = document.querySelector('input#passo')
    
var res = document.querySelector('div#res')
function contar(){
    if(inicio.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        window.alert('Insira números válidos!')
        return;
    }else{
    var inicio1 = Number(inicio.value)
    var fim1 = Number(fim.value)
    var passo1 = Number(passo.value)
    if(passo1 <= 0){
        window.alert('Passo inválido! Considerando PASSO 1')
        passo1 = 1
    }
    if(inicio1 <= fim1){
        for(let i = inicio1; i<= fim1; i+= passo1){
            res.innerHTML += `${i} \u{1F449}`
        }
    }else{
        for(let c = inicio1; c>= fim1; c-= passo1){
            res.innerHTML += `${c} \u{1F449}`
        }
    }res.innerHTML += `\u{1F3C1}`
    }
}


