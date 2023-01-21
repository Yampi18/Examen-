var matrizfila = new Array();

for (let x = 0; x <= 4; x++){
    matrizfila[x] = new Array();
    for (let y = 0; y<= 4; y++ ){
        matrizfila[x][y] = x * y;
    }
}

for(let elementomatriz in matrizfila){
    console.log(elementomatriz + "=" + matrizfila[elementomatriz]);
}

console.log("El elemento 9 se encuentra en la posicion 4x4")