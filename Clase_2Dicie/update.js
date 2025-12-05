// Update.js - Lógica para actualizar un contacto existente

// Añadir método al prototipo de la clase App
App.prototype.updateContact = function(id, newName, newEmail, newPhone) {
    // 1. Encontrar el índice del contacto por ID
    const index = this.contacts.findIndex(c => Number(c.id) === id);
    
    if (index === -1) {
        console.error(`Error: No se encontró contacto con ID: ${id}`);
        this.formMessage.textContent = 'Error: Contacto no encontrado para actualizar.';
        return;
    }

    // 2. Actualizar las propiedades
    const existing = this.contacts[index];
    existing.name = newName;
    existing.email = newEmail;
    existing.phone = newPhone;
    
    // 3. Guardar estado
    this.save();
    
    // 4. Actualizar vista principal
    this.renderMainTable();
    
    // 5. Cerrar modal (redirigir a #list)
    window.location.hash = 'list';

    // Opcional: mostrar mensaje de éxito en la vista principal
    console.log(`Contacto actualizado con ID: ${id}`);
};