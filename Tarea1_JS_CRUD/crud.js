const data = [];

    function create(item) {
    if (!item || typeof item !== 'string') {
        throw new Error('El elemento debe ser un texto válido.');
    }
    data.push(item.trim());
    return data;
    }

    function read() {
    return [...data];
    }

    function update(index, newItem) {
    if (index < 0 || index >= data.length) {
        throw new Error('Índice fuera de rango.');
    }
    if (!newItem || typeof newItem !== 'string') {
        throw new Error('El nuevo elemento debe ser un texto válido.');
    }
    data[index] = newItem.trim();
    return data;
    }

    function deleteItem(index) {
    if (index < 0 || index >= data.length) {
        throw new Error('Índice fuera de rango.');
    }
    data.splice(index, 1);
    return data;
    }

console.log('Crear elementos:');
create('manzana');
create('pera');
create('banana');
console.log(read());

console.log('\nActualizar el índice 1:');
update(1, 'naranja');
console.log(read());

console.log('\nEliminar el índice 0:');
deleteItem(0);
console.log(read());
