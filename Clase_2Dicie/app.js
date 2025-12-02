// app.js - CRUD con búsqueda, export/import, validación y modal

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

        // DOM
        this.mainTableBody = document.querySelector('#mainTable tbody');
        this.modal = document.getElementById('modal');
        this.modalTitle = document.getElementById('modalTitle');
        this.modalTableBody = document.querySelector('#modalTable tbody');

        this.btnAdd = document.getElementById('btnAdd');
        this.modalClose = document.getElementById('modalClose');
        this.btnCancel = document.getElementById('btnCancel');
        this.btnExport = document.getElementById('btnExport');
        this.btnImport = document.getElementById('btnImport');
        this.fileImport = document.getElementById('fileImport');
        this.btnClearAll = document.getElementById('btnClearAll');

        this.searchInput = document.getElementById('searchInput');

        this.form = document.getElementById('contactForm');
        this.inputIndex = document.getElementById('contactIndex');
        this.inputName = document.getElementById('name');
        this.inputEmail = document.getElementById('email');
        this.inputPhone = document.getElementById('phone');

        this.errName = document.getElementById('errName');
        this.errEmail = document.getElementById('errEmail');
        this.errPhone = document.getElementById('errPhone');
        this.formMessage = document.getElementById('formMessage');

        // eventos
        this.btnAdd.addEventListener('click', () => this.openModal('add'));
        this.modalClose.addEventListener('click', () => this.closeModal());
        this.btnCancel.addEventListener('click', () => this.closeModal());
        this.form.addEventListener('submit', (e) => this.onSubmit(e));
        this.searchInput.addEventListener('input', () => this.renderMainTable());
        this.btnExport.addEventListener('click', () => this.exportJSON());
        this.btnImport.addEventListener('click', () => this.fileImport.click());
        this.fileImport.addEventListener('change', (e) => this.importJSON(e));
        this.btnClearAll.addEventListener('click', () => this.clearAll());

        // render inicial
        this.renderMainTable();
    }

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

    renderMainTable() {
        const term = (this.searchInput?.value || '').toLowerCase().trim();
        this.mainTableBody.innerHTML = '';

        const filtered = this.contacts.filter(c => {
            if (!term) return true;
            return (c.name || '').toLowerCase().includes(term) || (c.email || '').toLowerCase().includes(term);
        });

        if (filtered.length === 0) {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td colspan="6" style="text-align:center">No hay contactos</td>`;
            this.mainTableBody.appendChild(tr);
        }

        filtered.forEach((c, idx) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
        <td>${escapeHtml(c.id)}</td>
        <td>${escapeHtml(c.name)}</td>
        <td>${escapeHtml(c.email)}</td>
        <td>${escapeHtml(c.phone || '')}</td>
        <td>${escapeHtml(this.formatDate(c.createdAt))}</td>
        <td class="actions">
          <button class="btn" data-action="edit" data-index="${this.contacts.indexOf(c)}">Editar</button>
          <button class="btn" data-action="delete" data-index="${this.contacts.indexOf(c)}">Eliminar</button>
        </td>
      `;
            this.mainTableBody.appendChild(tr);
        });

        // delegación de eventos en la tabla
        this.mainTableBody.querySelectorAll('button').forEach(btn => {
            const action = btn.dataset.action;
            const index = Number(btn.dataset.index);
            if (action === 'edit') btn.addEventListener('click', () => this.openModal('edit', index));
            if (action === 'delete') btn.addEventListener('click', () => this.deleteContact(index));
        });
    }

    renderModalTable() {
        // muestra una tabla dentro del modal con los contactos actuales
        this.modalTableBody.innerHTML = '';
        this.contacts.forEach((c) => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
        <td>${escapeHtml(c.id)}</td>
        <td>${escapeHtml(c.name)}</td>
        <td>${escapeHtml(c.email)}</td>
        <td>${escapeHtml(this.formatDate(c.createdAt))}</td>
      `;
            this.modalTableBody.appendChild(tr);
        });
    }

    openModal(mode = 'add', index = null) {
        this.clearFormErrors();
        this.modal.setAttribute('aria-hidden', 'false');
        this.modalTitle.textContent = mode === 'add' ? 'Nuevo contacto' : 'Editar contacto';

        if (mode === 'add') {
            this.inputIndex.value = '';
            this.inputName.value = '';
            this.inputEmail.value = '';
            this.inputPhone.value = '';
            this.formMessage.textContent = '';
        } else if (mode === 'edit' && index !== null) {
            const c = this.contacts[index];
            this.inputIndex.value = index;
            this.inputName.value = c.name;
            this.inputEmail.value = c.email;
            this.inputPhone.value = c.phone || '';
            this.formMessage.textContent = '';
        }

        // Al abrir el modal siempre mostramos la(s) tabla(s)
        this.renderModalTable();
        this.inputName.focus();
    }

    closeModal() {
        this.modal.setAttribute('aria-hidden', 'true');
    }

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
        const idx = this.inputIndex.value;
        const name = this.inputName.value.trim();
        const email = this.inputEmail.value.trim();
        const phone = this.inputPhone.value.trim();

        if (!this.validateForm(name, email)) return;

        if (idx === '') {
            // create
            const contact = new Contact(this.nextId++, name, email, phone, new Date().toISOString());
            this.contacts.push(contact);
        } else {
            // update
            const existing = this.contacts[Number(idx)];
            existing.name = name;
            existing.email = email;
            existing.phone = phone;
        }

        this.save();
        this.renderMainTable();
        this.closeModal();
    }

    deleteContact(index) {
        if (!confirm('¿Eliminar este contacto?')) return;
        this.contacts.splice(index, 1);
        this.save();
        this.renderMainTable();
    }

    clearAll() {
        if (!confirm('¿Borrar todos los contactos? Esta acción no se puede deshacer.')) return;
        this.contacts = [];
        this.nextId = 1;
        this.save();
        this.renderMainTable();
    }

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
        } catch (e) { alert('Error exportando: ' + e); }
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
                alert('Importación completada');
            } catch (err) { alert('Error importando JSON: ' + err.message); }
        };
        reader.readAsText(file);
        // limpiar el input para permitir re-importar el mismo archivo si se desea
        e.target.value = '';
    }
}

function escapeHtml(s) {
    if (!s && s !== 0) return '';
    return String(s)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
