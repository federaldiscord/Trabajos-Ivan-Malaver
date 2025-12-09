// Clase Contacto para mantener la estructura de datos
class Contact {
    constructor(id, name, email, phone, createdAt) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.phone = phone;
        this.createdAt = createdAt || new Date().toISOString();
    }
}

class App {
    constructor() {
        this.storageKey = 'contacts_app_items_v1';
        this.contacts = this.load() || [];
        this.nextId = this.calculateNextId();

        // Referencias al DOM
        this.mainTableBody = document.querySelector('#mainTable tbody');
        this.modal = document.getElementById('modal');
        this.modalTitle = document.getElementById('modalTitle');
        this.modalTableBody = document.querySelector('#modalTable tbody');
        this.searchInput = document.getElementById('searchInput');

        this.form = document.getElementById('contactForm');
        this.inputId = document.getElementById('contactId'); // Usamos ID en lugar de index
        this.inputName = document.getElementById('name');
        this.inputEmail = document.getElementById('email');
        this.inputPhone = document.getElementById('phone');

        this.errName = document.getElementById('errName');
        this.errEmail = document.getElementById('errEmail');
        this.errPhone = document.getElementById('errPhone');
        this.formMessage = document.getElementById('formMessage');

        // Eventos generales
        document.getElementById('searchInput').addEventListener('input', () => this.handleSearch());
        document.getElementById('btnExport').addEventListener('click', () => this.exportJSON());
        document.getElementById('btnImport').addEventListener('click', () => document.getElementById('fileImport').click());
        document.getElementById('fileImport').addEventListener('change', (e) => this.importJSON(e));
        document.getElementById('btnClearAll').addEventListener('click', () => this.clearAll());

        this.form.addEventListener('submit', (e) => this.onSubmit(e));
        
        // Manejo de la URL para el routing
        window.addEventListener('hashchange', () => this.router());
        document.addEventListener('DOMContentLoaded', () => this.router());

        // Inicializar la tabla y las funciones que vienen de otros archivos
        this.renderMainTable();
    }

    // --- UTILS ---

    calculateNextId() {
        if (!this.contacts || this.contacts.length === 0) return 1;
        const max = this.contacts.reduce((m, c) => Math.max(m, Number(c.id) || 0), 0);
        return max + 1;
    }

    load() {
        try {
            const raw = localStorage.getItem(this.storageKey);
            return raw ? JSON.parse(raw) : [];
        } catch (e) {
            console.error('load error', e);
            return [];
        }
    }

    save() {
        localStorage.setItem(this.storageKey, JSON.stringify(this.contacts));
    }

    formatDate(iso) {
        try { const d = new Date(iso); return d.toLocaleString(); } catch (e) { return iso }
    }
    
    // Función de saneamiento de HTML
    escapeHtml(s) {
        if (!s && s !== 0) return '';
        return String(s)
            .replaceAll('&', '&amp;')
            .replaceAll('<', '&lt;')
            .replaceAll('>', '&gt;')
            .replaceAll('"', '&quot;')
            .replaceAll("'", '&#39;');
    }

    // --- MODAL Y ROUTING (URL) ---

    router() {
        const hash = window.location.hash.substring(1); // Obtiene la parte después de #
        this.closeModal(); // Cerrar por defecto
        
        // Patrón para /add
        if (hash === 'add') {
            this.openModal('add');
        }
        
        // Patrón para /edit/ID
        const editMatch = hash.match(/^edit\/(\d+)$/);
        if (editMatch) {
            const contactId = Number(editMatch[1]);
            this.openModal('edit', contactId);
        }
        
        // Cualquier otro hash (o hash vacío) se comporta como /list (cierra modal)
        if (hash === 'list') {
            window.location.hash = ''; // Limpiar el hash para dejar la URL limpia
        }
    }

    openModal(mode = 'add', contactId = null) {
        this.clearFormErrors();
        this.modal.setAttribute('aria-hidden', 'false');
        this.modalTitle.textContent = mode === 'add' ? 'Nuevo contacto' : 'Editar contacto';

        if (mode === 'add') {
            this.inputId.value = '';
            this.inputName.value = '';
            this.inputEmail.value = '';
            this.inputPhone.value = '';
            this.formMessage.textContent = '';
        } else if (mode === 'edit' && contactId !== null) {
            const contact = this.contacts.find(c => Number(c.id) === contactId);
            if (contact) {
                this.inputId.value = contactId;
                this.inputName.value = contact.name;
                this.inputEmail.value = contact.email;
                this.inputPhone.value = contact.phone || '';
                this.formMessage.textContent = '';
            } else {
                // Si no encuentra el ID, vuelve a la lista
                window.location.hash = 'list';
                return;
            }
        }

        this.renderModalTable();
        this.inputName.focus();
    }

    closeModal() {
        this.modal.setAttribute('aria-hidden', 'true');
    }
    
    // --- VALIDACIÓN Y FORM SUBMIT ---
    
    clearFormErrors() {
        this.errName.textContent = '';
        this.errEmail.textContent = '';
        this.errPhone.textContent = '';
        this.formMessage.textContent = '';
    }

    validateForm(name, email) {
        let ok = true;
        this.clearFormErrors();
        if (!name) { this.errName.textContent = 'El nombre es obligatorio'; ok = false; }
        if (!email) { this.errEmail.textContent = 'El email es obligatorio'; ok = false; }
        else if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { this.errEmail.textContent = 'Email inválido'; ok = false; }
        return ok;
    }

    onSubmit(e) {
        e.preventDefault();
        const contactId = this.inputId.value; // Será vacío para crear, o el ID para editar
        const name = this.inputName.value.trim();
        const email = this.inputEmail.value.trim();
        const phone = this.inputPhone.value.trim();

        if (!this.validateForm(name, email)) return;
        
        if (contactId === '') {
            // Llama a la función de Create.js
            this.createContact(name, email, phone);
        } else {
            // Llama a la función de Update.js
            this.updateContact(Number(contactId), name, email, phone);
        }
    }

    // --- MÉTODOS DE EXPORTACIÓN/IMPORTACIÓN ---

    exportJSON() {
        try {
            const data = JSON.stringify(this.contacts, null, 2);
            const blob = new Blob([data], { type: 'application/json' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'contacts.json';
            document.body.appendChild(a);
            a.click();
            a.remove();
            URL.revokeObjectURL(url);
        } catch (e) { console.error('Error exportando:', e); }
    }

    importJSON(e) {
        const file = e.target.files && e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (ev) => {
            try {
                const arr = JSON.parse(ev.target.result);
                if (!Array.isArray(arr)) throw new Error('JSON inválido');
                // map to Contact objects with required fields
                this.contacts = arr.map(item => new Contact(item.id || this.nextId++, item.name || '', item.email || '', item.phone || '', item.createdAt || new Date().toISOString()));
                this.nextId = this.calculateNextId();
                this.save();
                this.renderMainTable();
                this.formMessage.textContent = 'Importación completada';
                setTimeout(() => this.formMessage.textContent = '', 3000);
            } catch (err) { this.formMessage.textContent = 'Error importando JSON: ' + err.message; }
        };
        reader.readAsText(file);
        e.target.value = ''; // limpiar input
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    // Exponer la instancia de App globalmente
    window.app = new App();
});
