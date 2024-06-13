var peso = document.getElementById('peso1')
var altura = document.getElementById('altura1')
var res = document.getElementById('res')
function calcular(){
    var peso1 = Number(peso.value)
    var altura1 = Number(altura.value)
    var imc = peso1 / (altura1 * altura1)
    imc = imc.toFixed(0).replace(',')
    if(imc < 18.5){
        res.innerHTML += `Seu IMC é de ${imc}, portanto voçê está abaixo do peso`
    }else if (imc < 25){
        res.innerHTML += `Seu IMC é de ${imc}, voçê está com o peso normal`
    }else if(imc < 30){
        res.innerHTML += `Seu IMC é de ${imc}, voçê está com sobrepeso`
    }else if(imc < 35){
        res.innerHTML += `Seu IMC é de ${imc}, voçê está com obesidade Grau I`
    }else if (imc < 40){
        res.innerHTML += `Seu IMC é de ${imc}, voçê está com obesidade Grau II (severa)`
    }else{
        res.innerHTML += `Seu IMC é de ${imc}, voçê está com obesidade Grau III (mórbita)`
    }

}
