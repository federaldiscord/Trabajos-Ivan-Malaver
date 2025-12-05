// Read.js - Lógica para leer, buscar y renderizar las tablas

// 1. Manejar la búsqueda
App.prototype.handleSearch = function() {
    // Simplemente llama al renderizado principal, que usa el valor del input de búsqueda
    this.renderMainTable();
};

// 2. Renderizar la tabla principal
App.prototype.renderMainTable = function() {
    const term = (this.searchInput?.value || '').toLowerCase().trim();
    this.mainTableBody.innerHTML = '';

    const filtered = this.contacts.filter(c => {
        if (!term) return true;
        // Buscar por nombre o email
        return (c.name || '').toLowerCase().includes(term) || (c.email || '').toLowerCase().includes(term);
    });

    if (filtered.length === 0) {
        const tr = document.createElement('tr');
        tr.innerHTML = `<td colspan="6" style="text-align:center">No hay contactos</td>`;
        this.mainTableBody.appendChild(tr);
    }

    filtered.forEach((c) => {
        const tr = document.createElement('tr');
        // Usamos this.escapeHtml() y this.formatDate() del App.js
        tr.innerHTML = `
            <td>${this.escapeHtml(c.id)}</td>
            <td>${this.escapeHtml(c.name)}</td>
            <td>${this.escapeHtml(c.email)}</td>
            <td>${this.escapeHtml(c.phone || '')}</td>
            <td>${this.escapeHtml(this.formatDate(c.createdAt))}</td>
            <td class="actions">
                <!-- Los botones ahora usan el ID y navegan al hash #edit/ID -->
                <a href="#edit/${c.id}" class="btn">Editar</a>
                <button class="btn" data-action="delete" data-id="${c.id}">Eliminar</button>
            </td>
        `;
        this.mainTableBody.appendChild(tr);
    });

    // Delegación de eventos de eliminación y edición
    this.mainTableBody.querySelectorAll('button[data-action="delete"]').forEach(btn => {
        const contactId = Number(btn.dataset.id);
        btn.addEventListener('click', () => this.deleteContact(contactId));
    });
};

// 3. Renderizar la tabla dentro del modal (es solo de lectura/información)
App.prototype.renderModalTable = function() {
    this.modalTableBody.innerHTML = '';
    this.contacts.forEach((c) => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${this.escapeHtml(c.id)}</td>
            <td>${this.escapeHtml(c.name)}</td>
            <td>${this.escapeHtml(c.email)}</td>
            <td>${this.escapeHtml(this.formatDate(c.createdAt))}</td>
        `;
        this.modalTableBody.appendChild(tr);
    });
};