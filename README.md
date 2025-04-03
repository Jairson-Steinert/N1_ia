# Sistema de Recomendação de Cursos

Um sistema inteligente que recomenda cursos baseado nas preferências, habilidades e competências do usuário, utilizando lógica fuzzy e sistema especialista.

## 🚀 Funcionalidades

- Interface interativa e intuitiva
- Seleção de áreas de conhecimento
- Seleção de habilidades
- Seleção de competências
- Recomendações personalizadas
- Sistema de progresso visual
- Validação de seleções
- Opção de reiniciar o processo
- Disponível online através do PythonAnywhere

## 🌐 Acesso Online

O sistema está disponível online através do PythonAnywhere:
```
https://jairson.pythonanywhere.com
```

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Flask
- Lógica Fuzzy
- Sistema Especialista
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- PythonAnywhere (Hosting)

## 📋 Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Jairson-Steinert/N1_ia.git
cd N1_ia
```

2. Crie um ambiente virtual (recomendado):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

As dependências incluem:
- Flask==3.0.2
- Werkzeug==3.0.1
- NumPy==1.26.4
- scikit-fuzzy==0.4.2
- Pandas==2.2.1
- python-dotenv==1.0.1
- Gunicorn==21.2.0

4. Execute o aplicativo localmente:
```bash
python app.py
```

5. Acesse o sistema no navegador:
```
http://localhost:5000
```

**Nota**: Se encontrar algum erro durante a instalação das dependências, certifique-se de que:
- Python 3.11 ou superior está instalado
- pip está atualizado (`pip install --upgrade pip`)
- Em sistemas Windows, você pode precisar instalar o Visual C++ Build Tools

## 🎯 Como Usar

1. **Seleção de Áreas de Conhecimento**
   - Escolha as áreas que mais te interessam
   - Selecione pelo menos uma opção para avançar

2. **Seleção de Habilidades**
   - Identifique suas habilidades ou as que deseja desenvolver
   - Selecione pelo menos uma opção para avançar

3. **Seleção de Competências**
   - Escolha suas competências principais
   - Selecione pelo menos uma opção para avançar

4. **Recomendações**
   - Clique em "Recomendar" para receber sugestões personalizadas
   - Visualize os cursos mais adequados ao seu perfil

5. **Reiniciar**
   - Use o botão "Reiniciar" para começar novamente
   - Todas as seleções serão limpas

## 🏗️ Estrutura do Projeto

```
N1_ia/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/
│   └── index.html
├── models/
│   ├── frame.py
│   ├── logica_fuzzy.py
│   └── sistema_especialista.py
└── data/
    ├── constants.py
    └── course_database.py
```

## 🤖 Como Funciona

O sistema utiliza uma combinação de:

1. **Lógica Fuzzy**
   - Calcula a similaridade entre o perfil do usuário e os cursos disponíveis
   - Considera diferentes pesos para áreas, habilidades e competências

2. **Sistema Especialista**
   - Aplica regras específicas para ajustar as recomendações
   - Considera requisitos e pré-requisitos dos cursos

3. **Frame Semântico**
   - Estrutura as informações do usuário e dos cursos
   - Facilita a comparação e recomendação

## 📦 Deploy

O sistema está hospedado no PythonAnywhere. Para fazer deploy de atualizações:

1. Push das alterações para o GitHub:
```bash
git add .
git commit -m "Descrição das alterações"
git push origin main
```

2. No console do PythonAnywhere:
```bash
cd /home/Jairson/N1_ia
git pull origin main
```

3. Na interface web do PythonAnywhere:
- Acesse a seção "Web"
- Clique no botão "Reload" para aplicar as alterações

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Contribuição

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
