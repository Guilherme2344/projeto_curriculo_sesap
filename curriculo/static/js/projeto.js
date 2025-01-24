if (window.location.pathname === '/curriculo/enviar-curriculo') {
    document.getElementById('botao-add').addEventListener('click', function() {
        // Ativa o campo de input de arquivo
        document.getElementById('arquivo').click();
    });

    // Alteração do nome do arquivo no botão
    document.getElementById('arquivo').addEventListener('change', function() {
        const file = this.files[0];
        const button = document.getElementById('botao-add');
        
        if (file) {
            const fileName = file.name;
            const size = file.size;

            // Limita o nome do arquivo a 100 caracteres
            if (fileName.length > 100) {
                button.textContent = fileName.substring(0, 100) + '...';
            } else {
                button.textContent = fileName;
            }

            // Verifica o tamanho do arquivo
            if (size > 1048576) { // 1MB em bytes
                alert('O arquivo supera o limite de 1MB');
                this.value = ""; // Limpa o campo de input de arquivo
                button.textContent = '+ Adicionar Arquivo'; // Restaura o texto do botão
            }
        }
        
        // Verifica se o botão de envio deve ser ativado
        toggleSubmitButton();
    });

    // Formatação do telefone
    document.getElementById('telefone').addEventListener('input', function(event) {
        let telefone = event.target.value;

        // Remove qualquer caractere não numérico
        telefone = telefone.replace(/\D/g, '');

        // Formata o número de telefone
        telefone = telefone.replace(/^(\d{2})(\d{0,5})(\d{0,4})/, '($1) $2-$3');

        // Limita o número de caracteres
        if (telefone.length > 15) {
            telefone = telefone.substring(0, 15);
        }

        // Atualiza o valor do campo
        event.target.value = telefone;
    });

    document.getElementById('observacoes').addEventListener('input', function() {
        this.style.height = 'auto'; // Reseta a altura para calcular a altura correta
        this.style.height = (this.scrollHeight) + 'px'; // Ajusta a altura conforme o conteúdo
    });

    // Função para verificar se todos os campos obrigatórios estão preenchidos
    function toggleSubmitButton() {
        const form = document.querySelector('form');
        const submitButton = document.getElementById('botao-enviar');
        const requiredFields = form.querySelectorAll('[required]');
        
        let allFilled = true;

        // Verifica se todos os campos obrigatórios estão preenchidos
        requiredFields.forEach(function(field) {
            if (!field.value) {
                allFilled = false;
            }
        });

        // Verifica se o arquivo foi selecionado
        const fileInput = document.getElementById('arquivo');
        if (!fileInput.files.length || fileInput.value === "") {
            allFilled = false;  // Desabilita o botão caso o arquivo não tenha sido selecionado
        }

        // Ativa ou desativa o botão de envio
        submitButton.disabled = !allFilled;
    }

    // Verifica os campos obrigatórios sempre que o valor mudar
    document.querySelectorAll('[required]').forEach(function(input) {
        input.addEventListener('input', toggleSubmitButton);
    });

    // Chama a função uma vez ao carregar a página
    window.addEventListener('load', toggleSubmitButton);
}