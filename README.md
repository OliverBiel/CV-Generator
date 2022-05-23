# CV-Generator


## Bem-vindo!
Esse projeto têm como objetivo gerar e alterar um currículo.
Foi utilizado Django no backend juntamente com um container PostgreSQL no Docker e o frontend foi feito em HTML e CSS puro.

## Instalacao Backend

- Após clonar o repositório crie uma venv na pasta do repositório com o seguinte comando:

*Necessário ter python instalado!

```bash
python -m venv venv 
```
- Em seguida inicialize a venv da seguinte forma:

```bash
source venv/bin/activate
```
*Certifique-se que o terminal utilizado está na pasta aonde foi criada a venv.

- Tendo criado e ativado a venv basta instalar os requirements, com a terminal na pasta raiz do projeto execute o comando:
```bash
pip install -r requirements.txt
```
- É necessário ter um banco postgres para poder fazer a conexão com o django, o mesmo pode ser criado como desejar. No meu caso criei um container utilizando [Docker](https://hub.docker.com/_/postgres).
- Tendo criado o banco, basta criar um arquivo .env na pasta CVGenerator/CVGenerator/ com as seguintes variáveis:
```bash
SECRET_KEY=chave de seguranca do django (Caso voce nao possua uma, basta pesquisar no google um gerador de secret key para django)
DB_NAME=nome do DB
DB_USER=user do DB
DB_PSWD=senha do DB
DB_HOST=ip do host do DB
DB_PORT=porta do DB - Por padrao a porta do postgres e 5432, esta como default no projeto, so e necessario utilizar essa variável se voce tiver mudado a porta padrao.
```
- Depois basta rodar os comandos, com a venv ativada:
```python
python manage.py makemigrations

#apos rodar o comando acima, rode o seguinte:
python manage.py migrate
```

## Como utilizar
### Inicializando o backend

- Se tudo ocorreu corretamente basta rodar o comando com a venv ativada:
```python
python manage.py runserver
```
- Pronto, o backend da aplicação já esta rodando. Para acessar basta clicar no link que aparece no terminal.

### Adicionando os seus dados
- Para adicionar os seus dados basta colocar "/admin" (sem aspas) no fim da url.
- Os campos foram divididos da seguinte maneira:
-  Academics:
	- Name: Refere-se ao tipo de curso, se é graduação, um curso de extensão e etc.
	- Institution: A instituição onde foi feito o curso.
	- Start_date: Data do começo do curso
	- End_date: Data de término do curso (Esse campo pode ser nulo caso deseje).
- Contacts:
	- Name: Apenas para melhor visualização na página de administração.
	- Logo: Eu optei por utilizar o [FontAwesome](https://fontawesome.com/) para os ícones de contato, portanto nesse campo deve-se colocar a classe do ícone que você escolher. Por exemplo: [No ícone do instagram](https://fontawesome.com/search?q=insta&s=solid%2Cbrands) a classe é: fa-brands fa-instagram. **PS: Cole no HTML o link do seu kit que o FontAwesome disponibiliza.**
	- Info: Refere-se a informação de contato em si; o número, o e-mail etc.
- Experiences:
	- Position: Cargo que você ocupou.
	- Company: Empresa
	- Start_date: Data de entrada no trabalho.
	- End_date: Data de desligamento (Esse campo pode ser nulo caso deseje).
	- Job_func: Nesse campo você deve selecionar e/ou adicionar as funções que você desempenhou nesse trabalho.
- My profiles (Esse campo só deve conter 1 item, é a descrição do seu perfil):
	- Name: Coloque seu nome da forma que deseja que fique no currículo
	- Photo: A foto que você deseja no currículo
	- Description: Aqui você descreve o seu perfil de maneira clara e objetiva.

### Baixando o currículo em PDF
- Após preencher os dados, para baixar o currículo basta apertar "Ctrl + p" e caso o CSS não tenha sido aplicado é só ir em mais opções e marcar a opção "Gráficos de segundo plano" e é só salvar onde desejar.



## Contato
- [Linkedin](https://www.linkedin.com/in/gabriel-oliveira-4bb406190)