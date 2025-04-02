class CourseDatabase:
    def __init__(self):
        self.courses = [
            {
                'nome': 'Ciência da Computação',
                'descricao': 'Curso focado no desenvolvimento de software e sistemas computacionais.',
                'areas': ['Tecnologia', 'Ciências Exatas'],
                'habilidades': ['Análise de Dados', 'Resolução de Problemas', 'Pensamento Crítico'],
                'competencias': ['Desenvolvimento', 'Análise', 'Pesquisa']
            },
            {
                'nome': 'Medicina',
                'descricao': 'Formação médica completa para atuação na área da saúde.',
                'areas': ['Saúde', 'Ciências Biológicas'],
                'habilidades': ['Comunicação', 'Trabalho em Equipe', 'Pensamento Crítico'],
                'competencias': ['Gestão', 'Coordenação', 'Supervisão']
            },
            {
                'nome': 'Administração',
                'descricao': 'Gestão empresarial e desenvolvimento de negócios.',
                'areas': ['Ciências Sociais', 'Gestão'],
                'habilidades': ['Liderança', 'Gestão de Projetos', 'Negociação'],
                'competencias': ['Gestão', 'Planejamento', 'Coordenação']
            },
            {
                'nome': 'Psicologia',
                'descricao': 'Estudo do comportamento humano e processos mentais.',
                'areas': ['Ciências Humanas', 'Saúde'],
                'habilidades': ['Comunicação', 'Empatia', 'Análise de Dados'],
                'competencias': ['Consultoria', 'Coordenação', 'Pesquisa']
            },
            {
                'nome': 'Engenharia Civil',
                'descricao': 'Projeto e construção de estruturas e infraestruturas.',
                'areas': ['Engenharias', 'Ciências Exatas'],
                'habilidades': ['Análise de Dados', 'Gestão de Projetos', 'Resolução de Problemas'],
                'competencias': ['Planejamento', 'Coordenação', 'Supervisão']
            },
            {
                'nome': 'Arquitetura e Urbanismo',
                'descricao': 'Projeto e planejamento de espaços e edificações.',
                'areas': ['Artes', 'Engenharias'],
                'habilidades': ['Criatividade', 'Gestão de Projetos', 'Comunicação'],
                'competencias': ['Planejamento', 'Coordenação', 'Desenvolvimento']
            },
            {
                'nome': 'Direito',
                'descricao': 'Estudo das leis e aplicação da justiça.',
                'areas': ['Direito', 'Ciências Sociais'],
                'habilidades': ['Comunicação', 'Pensamento Crítico', 'Negociação'],
                'competencias': ['Consultoria', 'Coordenação', 'Gestão']
            },
            {
                'nome': 'Pedagogia',
                'descricao': 'Formação para atuação na área educacional.',
                'areas': ['Educação', 'Ciências Humanas'],
                'habilidades': ['Comunicação', 'Liderança', 'Trabalho em Equipe'],
                'competencias': ['Ensino', 'Coordenação', 'Gestão']
            }
        ]

    def get_all_courses(self):
        return self.courses

    def get_course_by_name(self, name):
        for course in self.courses:
            if course['nome'].lower() == name.lower():
                return course
        return None

    def get_courses_by_area(self, area):
        return [course for course in self.courses if area in course['areas']]

    def get_courses_by_skill(self, skill):
        return [course for course in self.courses if skill in course['habilidades']]

    def get_courses_by_competency(self, competency):
        return [course for course in self.courses if competency in course['competencias']] 