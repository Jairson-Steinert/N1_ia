import sys
import os

# Adiciona o diretório do projeto ao path
path = '/home/seu-usuario/N1_ia'  # Substitua 'seu-usuario' pelo seu nome de usuário
if path not in sys.path:
    sys.path.append(path)

# Importa a aplicação Flask
from app import app as application 