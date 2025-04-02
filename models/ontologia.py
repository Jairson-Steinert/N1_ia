class DomainOntology:
    def __init__(self):
        self.areas_conhecimento = {
            "Ciências Exatas": {
                "aplicações": ["Engenharia", "Pesquisa Científica", "Modelagem Matemática", "Análise de Dados"],
                "relacionamentos": [
                    {"area": "Engenharias", "tipo": "aplicação", "peso": 0.8},
                    {"area": "Tecnologia", "tipo": "complementar", "peso": 0.6}
                ]
            },
            "Ciências Biológicas": {
                "aplicações": ["Medicina", "Biotecnologia", "Conservação", "Pesquisa Biomédica"],
                "relacionamentos": [
                    {"area": "Saúde", "tipo": "aplicação", "peso": 0.9},
                    {"area": "Medicina", "tipo": "aplicação", "peso": 0.8}
                ]
            },
            "Tecnologia": {
                "aplicações": ["Desenvolvimento de Software", "Cibersegurança", "Inteligência Artificial", "Cloud Computing"],
                "relacionamentos": [
                    {"area": "Engenharias", "tipo": "complementar", "peso": 0.7},
                    {"area": "Ciências Exatas", "tipo": "base", "peso": 0.6}
                ]
            },
            "Engenharias": {
                "aplicações": ["Infraestrutura", "Automação", "Projetos", "Inovação"],
                "relacionamentos": [
                    {"area": "Tecnologia", "tipo": "aplicação", "peso": 0.8},
                    {"area": "Ciências Exatas", "tipo": "base", "peso": 0.7}
                ]
            },
            "Saúde": {
                "aplicações": ["Clínica", "Saúde Pública", "Pesquisa Médica", "Gestão Hospitalar"],
                "relacionamentos": [
                    {"area": "Ciências Biológicas", "tipo": "base", "peso": 0.9},
                    {"area": "Medicina", "tipo": "complementar", "peso": 0.8}
                ]
            },
            "Medicina": {
                "aplicações": ["Clínica", "Cirurgia", "Pesquisa", "Saúde Pública"],
                "relacionamentos": [
                    {"area": "Ciências Biológicas", "tipo": "base", "peso": 0.9},
                    {"area": "Saúde", "tipo": "complementar", "peso": 0.8}
                ]
            }
        }

    def get_all_areas(self):
        return list(self.areas_conhecimento.keys())

    def get_aplicacoes(self, area):
        if area in self.areas_conhecimento:
            return self.areas_conhecimento[area]["aplicações"]
        return []

    def get_related_areas_with_weights(self, area):
        if area in self.areas_conhecimento:
            return self.areas_conhecimento[area]["relacionamentos"]
        return []

    def get_area_info(self, area):
        if area in self.areas_conhecimento:
            return {
                "aplicações": self.areas_conhecimento[area]["aplicações"],
                "relacionamentos": self.areas_conhecimento[area]["relacionamentos"]
            }
        return {"aplicações": [], "relacionamentos": []} 