// Create.js - Lógica para crear un nuevo contacto

// Añadir método al prototipo de la clase App
App.prototype.createContact = function(name, email, phone) {
    // 1. Crear nuevo contacto
    const contact = new Contact(this.nextId++, name, email, phone, new Date().toISOString());
    
    // 2. Insertar en el array
    this.contacts.push(contact);
    
    // 3. Guardar estado
    this.save();
    
    // 4. Actualizar vista principal
    this.renderMainTable();
    
    // 5. Cerrar modal (redirigir a #list)
    window.location.hash = 'list';

    // Opcional: mostrar mensaje de éxito en la vista principal
    // (Implementación simple: log a consola)
    console.log(`Contacto creado con ID: ${contact.id}`);
};