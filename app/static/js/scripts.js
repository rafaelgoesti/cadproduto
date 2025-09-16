let currentEditId = null;
let currentDeleteId = null;

function openEditModal(id, nome, descricao, preco, categoria, imagem) {
    currentEditId = id;
    
    document.getElementById('editNome').value = nome;
    document.getElementById('editDescricao').value = descricao;
    document.getElementById('editPreco').value = preco;
    document.getElementById('editCategoria').value = categoria;
    
    const editForm = document.getElementById('editForm');
    editForm.action = `/editar/${id}`;
    
    if (imagem) {
        document.getElementById('editImagePreview').src = `/static/uploads/${imagem}`;
    } else {
        document.getElementById('editImagePreview').src = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIGhlaWdodD0iMjAwIiB2aWV3Qm94PSIwIDAgMjAwIDIwMCI+PHJlY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNlMWUxZTEiLz48dGV4dCB4PSI1MCUiIHk9IjUwJSIgZG9taW5hbnQtYmFzZWxpbmU9Im1pZGRsZSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9IkFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjI0IiBmaWxsPSIjOTk5Ij5Qcm9kdXRvPC90ZXh0Pjwvc3ZnPg==";
    }
    
    document.getElementById('editModal').style.display = 'block';
}

function openDeleteModal(id, nome) {
    currentDeleteId = id;
    
    document.getElementById('deleteProductName').textContent = nome;
    
    const deleteForm = document.getElementById('deleteForm');
    deleteForm.action = `/excluir/${id}`;
    
    document.getElementById('deleteModal').style.display = 'block';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Fechar modal clicando fora dele
window.addEventListener('click', function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
});

// Preview da imagem no modal de edição
document.addEventListener('DOMContentLoaded', function() {
    const editImageInput = document.getElementById('editImagem');
    if (editImageInput) {
        editImageInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    document.getElementById('editImagePreview').src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Preview da imagem no formulário principal
    const mainImageInput = document.getElementById('imagem');
    if (mainImageInput) {
        mainImageInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const preview = document.getElementById('imagePreview');
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }
});