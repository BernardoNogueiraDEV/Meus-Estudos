let valores = [1,2,4,3,5]
valores.sort()
/*for(pos = 0; pos < valores.length; pos++){
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}*/
for(let pos in valores){
    console.log(valores[pos])
}
