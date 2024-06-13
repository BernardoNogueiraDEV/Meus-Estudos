function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (fano.value.length == 0 || Number(fano.value) > ano){
        window.alert('Verifique os dados e tente novamente!')
    }else{
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var gênero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked){
            gênero = 'Homem'
            if(idade >= 0 && idade <= 11 ){
                //criança
                img.setAttribute('src', 'criançaM.png')
            }else if (idade < 21){
                //jovem
                img.setAttribute('src', 'jovemM.png')
            }else if (idade < 50){
                //adulto
                img.setAttribute('src', 'adultoM.png')
            }else{
                //idoso
                img.setAttribute('src', 'senhor.png')
            }
        }else if (fsex[1].checked){
            gênero = 'Mulher'
            if(idade >= 0 && idade <= 11 ){
                //criança
                img.setAttribute('src', 'criançaF.png')
            }else if (idade < 21){
                //jovem
                img.setAttribute('src', 'jovemF.png')
            }else if (idade < 50){
                //adulto
                img.setAttribute('src', 'adultoF.png')
            }else{
                //idoso
                img.setAttribute('src', 'senhora.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos.`
        res.appendChild(img)
    }
}