# Projeto Currículo UGTSIC

## Tecnologias Utilizadas
- Front-End: HTML, CSS e JS
- Back-End: Python com Django
- Protótipos de Páginas: Figma
- Modelo relacional de DB: MySQL Workbench
- Modelor ER de DB: ERDPlus
- Ambiente de Desenvolvimento: VS Code
- Banco de Dados: SQLite

## Requisitos
- Conexão Wi-Fi.
- PC com Windows.
- Python instalado no pc.

## Tutorial de ativação do projeto
1. Após baixar e extrair a pasta do projeto, entre na pasta e extraia o conteúdo do arquivo "venv.rar".
2. Após extraído, entre na pasta "curriculo_admin" e extraia o banco de dados "db.rar". (OBS: caso apareça um arquivo de banco de dados ".sqlite3" sem você ter antes extraído o conteúdo de "db.rar", exclua esse banco de dados e extraia normalmente o "db.rar")
3. Após tudo isso, execute o prompt de comando do computador e navegue para a pasta do projeto.
4. Ao entrar na pasta pelo cmd, execute a linha de comando "venv\Scripts\activate".
5. Após o ambiente virtual estiver ativo, execute a linha de comando "pip install django Django==4.2.7".
6. Após isso, execute a linha de comando "python manage.py runserver 127.0.0.1:8080".
7. Após o comando ser executado, abra seu navegador e digite o seguinte endereço: "http://127.0.0.1:8080/curriculo/enviar-curriculo".
8. Se tudo deu certo, a página de enviar currículo irá aparecer normalmente.

## Tutorial bônus (Visualizar espaço do usuário admin)
1. Caso queira visualizar o ambiente de configuração do admin na web, digite o seguinte endereço: "http://127.0.0.1:8080/admin".
2. Aparecerá uma tela de login. O usuário é "admin" e a senha é "admin123"
3. Após isso, a tela do admin do django aparecerá. Nesse espaço, ao clicar em "Candidatos", podem ser feitas operações CRUD.

# OBSERVAÇÕES IMPORTANTES!!!
- Para visualizar o e-mail enviado, basta ir no console do cmd para isso. A estrutura aparecerá com vários (bastante mesmo) caracteres aleatórios, mas basta apenas rolar a página pra cima pra encontrar o formato de como o e-mail foi enviado. Esse formato foi escolhido por causa de segurança, já que a outra maneira de enviar e-mail (a maneira real de envio) deve-se colocar o e-mail e a senha reais. É importante ressaltar que o código que fiz não envia realmente um e-mail, apenas simula a estrutura de um e-mail enviado caso configurado da maneira funcional.
- O uso da IA ChatGPT foi utilizado, em sua maioria, para obter os códigos necessários de JavaScript, uma vez que possuo conhecimento muito básico nessa linguagem. Ela também foi usada para outros propósitos, como pegar o ip do pc, como enviar e-mail, dentre outras coisas específicas que eu não tinha conhecimento.
- Gostaria de deixar claro que os códigos em HTML e CSS foram feitos em uma proporção de 99% de código feita por mim e apenas 1% de código do ChatGPT. Quanto aos códigos em Python, essa proporção vai para 90% e 10%, respectivamente. Esses dados aproximados servem apenas para ilustrar que grande parte do código foi feita por mim.
- As páginas são responsivas.
- Há dois currículos já cadastrados no banco de dados.
- Os modelos e diagrama das páginas e do projeto podem ser encontrados na pasta "modelos_diagramas".
-  O projeto foi desenvolvido para ser o mais fiel possível a um projeto funcional real.
- As páginas são bem minimalistas com o objetivo de facilitar sua utilização pelos usuários.
- A organização das pastas e arquivos do projeto foi feita para ser melhor de navegar.
