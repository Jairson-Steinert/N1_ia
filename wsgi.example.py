import os
import sys

# Configurar ambiente virtual
VIRTUALENV = '/home/seu-usuario/.virtualenvs/N1_ia'  # Substitua 'seu-usuario' pelo seu nome de usuário
python_home = VIRTUALENV
python_version = '3.11'

# Adicionar diretórios ao path
prefixes = [python_home, os.path.join(python_home, 'lib', 'python' + python_version)]
for prefix in prefixes:
    for lib in ['site-packages', 'lib-dynload']:
        path = os.path.join(prefix, lib)
        if os.path.isdir(path):
            if path not in sys.path:
                sys.path.insert(0, path)

# Adicionar diretório do projeto ao path
project_home = '/home/seu-usuario/N1_ia'  # Substitua 'seu-usuario' pelo seu nome de usuário
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Importar a aplicação Flask
from app import app as application 