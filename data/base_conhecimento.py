from models.frame import CursoFrame

def criar_base_conhecimento():
    cursos = [
        # Cursos de Exatas e Computação
        CursoFrame("Engenharia de Software", ["Exatas", "Computação"], 5, ["Lógica", "Resolução de Problemas", "Trabalho em Equipe"], ["Engenharia de Software", "Ciência da Computação"]),
        CursoFrame("Ciência da Computação", ["Exatas", "Computação"], 5, ["Lógica", "Raciocínio Matemático", "Resolução de Problemas"], ["Ciência da Computação", "Engenharia de Software"]),
        CursoFrame("Engenharia Civil", ["Exatas"], 5, ["Raciocínio Matemático", "Resolução de Problemas"], ["Engenharia Civil", "Arquitetura"]),
        CursoFrame("Estatística", ["Exatas"], 4, ["Raciocínio Matemático", "Análise"], ["Estatística", "Matemática"]),
        CursoFrame("Física", ["Exatas"], 4, ["Raciocínio Matemático", "Resolução de Problemas"], ["Física", "Matemática"]),
        CursoFrame("Matemática", ["Exatas"], 5, ["Raciocínio Matemático", "Análise"], ["Matemática", "Estatística"]),
        CursoFrame("Engenharia Mecânica", ["Exatas"], 5, ["Resolução de Problemas", "Raciocínio Matemático"], ["Engenharia Mecânica", "Engenharia de Produção"]),
        CursoFrame("Sistemas de Informação", ["Exatas", "Computação"], 4, ["Resolução de Problemas", "Lógica", "Trabalho em Equipe"], ["Sistemas de Informação", "Ciência da Computação"]),
       
        # Cursos de Biológicas
        CursoFrame("Medicina", ["Biológicas", "Ciências da Saúde"], 6, ["Análise", "Observação", "Trabalho em Equipe"], ["Medicina", "Biotecnologia"]),
        CursoFrame("Biotecnologia", ["Biológicas", "Ciências da Saúde"], 5, ["Análise", "Observação", "Resolução de Problemas"], ["Biotecnologia", "Medicina"]),
        CursoFrame("Biologia", ["Biológicas"], 4, ["Análise", "Observação"], ["Biologia", "Medicina"]),
        CursoFrame("Psicologia", ["Biológicas", "Humanas"], 4, ["Análise", "Interpretação", "Trabalho em Equipe"], ["Psicologia", "Filosofia"]),
       
        # Cursos de Humanas
        CursoFrame("Direito", ["Humanas", "Sociais Aplicadas"], 5, ["Argumentação", "Interpretação", "Tomada de Decisão"], ["Direito", "Filosofia"]),
        CursoFrame("Filosofia", ["Humanas"], 4, ["Argumentação", "Interpretação"], ["Filosofia", "Psicologia"]),
        CursoFrame("Ciências Sociais", ["Humanas"], 4, ["Argumentação", "Interpretação"], ["Ciências Sociais", "Sociologia"]),
        CursoFrame("Letras", ["Humanas"], 4, ["Interpretação", "Argumentação"], ["Letras", "Literatura"]),
        CursoFrame("História", ["Humanas"], 4, ["Interpretação", "Argumentação"], ["História", "Arqueologia"]),
       
        # Cursos de Artes
        CursoFrame("Design Gráfico", ["Artes", "Comunicação"], 4, ["Criatividade", "Expressão", "Estética"], ["Design Gráfico", "Publicidade"]),
        CursoFrame("Arquitetura", ["Artes", "Exatas"], 5, ["Criatividade", "Estética", "Resolução de Problemas"], ["Arquitetura", "Design"]),
        CursoFrame("Moda", ["Artes"], 4, ["Criatividade", "Estética"], ["Moda", "Design de Interiores"]),
        CursoFrame("Publicidade", ["Artes", "Comunicação"], 4, ["Criatividade", "Comunicação", "Expressão"], ["Publicidade", "Design Gráfico"]),
        CursoFrame("Teatro", ["Artes"], 4, ["Expressão", "Criatividade", "Estética"], ["Teatro", "Dança"]),
        CursoFrame("Música", ["Artes"], 4, ["Criatividade", "Expressão", "Estética"], ["Música", "Teatro"]),
        CursoFrame("Dança", ["Artes"], 4, ["Expressão", "Criatividade", "Estética"], ["Dança", "Teatro"]),
        CursoFrame("Design de Interiores", ["Artes"], 4, ["Criatividade", "Estética"], ["Design de Interiores", "Moda"]),
        CursoFrame("Belas Artes", ["Artes"], 5, ["Criatividade", "Estética"], ["Belas Artes", "Artes Visuais"]),
       
        # Cursos de Sociais Aplicadas
        CursoFrame("Administração", ["Sociais Aplicadas"], 4, ["Tomada de Decisão", "Liderança", "Comunicação"], ["Administração", "Gestão de Projetos"]),
        CursoFrame("Marketing", ["Sociais Aplicadas"], 4, ["Comunicação", "Liderança", "Tomada de Decisão"], ["Marketing", "Administração"]),
        CursoFrame("Gestão de Pessoas", ["Sociais Aplicadas"], 4, ["Liderança", "Comunicação", "Tomada de Decisão"], ["Gestão de Pessoas", "Administração"]),
        CursoFrame("Economia", ["Exatas", "Sociais Aplicadas"], 4, ["Raciocínio Matemático", "Tomada de Decisão", "Análise"], ["Economia", "Administração"]),
       
        # Cursos relacionados à Comunicação
        CursoFrame("Jornalismo", ["Humanas", "Comunicação"], 4, ["Comunicação", "Argumentação", "Interpretação"], ["Jornalismo", "Publicidade"]),
        CursoFrame("Relações Públicas", ["Humanas", "Comunicação"], 4, ["Comunicação", "Argumentação", "Interpretação"], ["Relações Públicas", "Jornalismo"]),
       
        # Cursos relacionados a Liderança e Gestão
        CursoFrame("Gestão de Projetos", ["Sociais Aplicadas"], 4, ["Liderança", "Comunicação", "Tomada de Decisão"], ["Gestão de Projetos", "Administração"]),
        CursoFrame("Recursos Humanos", ["Sociais Aplicadas"], 4, ["Liderança", "Comunicação", "Tomada de Decisão"], ["Recursos Humanos", "Gestão de Pessoas"]),
       
        # Cursos de Ciências da Saúde
        CursoFrame("Enfermagem", ["Biológicas", "Ciências da Saúde"], 4, ["Trabalho em Equipe", "Observação", "Análise"], ["Enfermagem", "Medicina"]),
        CursoFrame("Educação Física", ["Biológicas", "Saúde"], 4, ["Trabalho em Equipe", "Resolução de Problemas"], ["Educação Física", "Saúde"]),
       
        # Cursos de Ciências Humanas
        CursoFrame("Antropologia", ["Humanas", "Biológicas"], 4, ["Observação", "Análise"], ["Antropologia", "Sociologia"]),
        CursoFrame("Arqueologia", ["Humanas", "Exatas"], 4, ["Observação", "Análise"], ["Arqueologia", "História"]),
       
        # Cursos de Ciências Contábeis
        CursoFrame("Ciências Contábeis", ["Sociais Aplicadas"], 4, ["Raciocínio Matemático", "Tomada de Decisão", "Análise"], ["Ciências Contábeis", "Administração"]),
    ]

    return cursos 
