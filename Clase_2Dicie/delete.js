// Delete.js - Lógica para eliminar (individual y total) contactos

// 1. Eliminar contacto individual
App.prototype.deleteContact = function(id) {
    if (!confirm(`¿Eliminar contacto con ID ${id}?`)) return;
    
    // 1. Encontrar el índice del contacto por ID
    const index = this.contacts.findIndex(c => Number(c.id) === id);
    
    if (index === -1) {
        console.error(`Error: No se encontró contacto con ID: ${id}`);
        // No hay un buen lugar para mostrar un error en la UI aquí, solo lo logueamos
        return;
    }
    
    // 2. Eliminar del array
    this.contacts.splice(index, 1);
    
    // 3. Guardar estado
    this.save();
    
    // 4. Actualizar vista principal
    this.renderMainTable();
    
    console.log(`Contacto eliminado con ID: ${id}`);
};

// 2. Borrar todos los contactos
App.prototype.clearAll = function() {
    // Usamos el mismo patrón de modal customizado para no usar alert/confirm
    if (!confirm('¿Borrar todos los contactos? Esta acción no se puede deshacer.')) return;
    
    // 1. Limpiar array
    this.contacts = [];
    
    // 2. Resetear el contador de ID
    this.nextId = 1;
    
    // 3. Guardar estado
    this.save();
    
    // 4. Actualizar vista principal
    this.renderMainTable();
    
    console.log('Todos los contactos han sido eliminados.');
};