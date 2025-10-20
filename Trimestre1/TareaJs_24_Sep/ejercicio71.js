// Subarray Máximo: Encuentra el subarray con la suma máxima.

function subarrayMaximo(array) {
    let maxActual = array[0];
    let maxGlobal = array[0];

    for (let i = 1; i < array.length; i++) {
        maxActual = Math.max(array[i], maxActual + array[i]);
        maxGlobal = Math.max(maxGlobal, maxActual);
    }

    return maxGlobal;
}

console.log(subarrayMaximo([-2, 1, -3, 4, -1, 2, 1, -5, 4])); 
