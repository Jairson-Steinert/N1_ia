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

## 🛠️ Tecnologias Utilizadas

- Python
- Flask
- Lógica Fuzzy
- Sistema Especialista
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-recomendacao-cursos.git
cd sistema-recomendacao-cursos
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
- Flask 3.0.2 - Framework web
- Werkzeug 3.0.1 - Utilitários WSGI
- NumPy 1.26.4 - Computação numérica
- scikit-fuzzy 0.4.2 - Lógica fuzzy
- Pandas 2.2.1 - Manipulação de dados
- python-dotenv 1.0.1 - Variáveis de ambiente
- Gunicorn 21.2.0 - Servidor WSGI

4. Execute o aplicativo:
```bash
python app.py
```

5. Acesse o sistema no navegador:
```
http://localhost:5000
```

**Nota**: Se encontrar algum erro durante a instalação das dependências, certifique-se de que:
- Python 3.8 ou superior está instalado
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
sistema-recomendacao-cursos/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   └── css/
│       └── style.css
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

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Contribuição

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte, envie um email para seu-email@exemplo.com ou abra uma issue no repositório. 