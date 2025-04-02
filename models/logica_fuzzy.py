class FuzzyLogic:
    def __init__(self):
        # Pesos para diferentes aspectos da similaridade
        self.weights = {
            'areas': 0.4,        # Áreas de conhecimento têm maior peso
            'habilidades': 0.3,  # Habilidades têm peso médio
            'competencias': 0.3  # Competências têm peso médio
        }
        
        # Pesos para diferentes níveis de similaridade
        self.similarity_thresholds = {
            'high': 0.7,
            'medium': 0.4,
            'low': 0.2
        }

    def calculate_similarity(self, user_frame, course_frame):
        # Calcula similaridade para cada aspecto
        area_similarity = self._calculate_set_similarity(
            set(user_frame['areas']), 
            set(course_frame['areas'])
        )
        
        habilidade_similarity = self._calculate_set_similarity(
            set(user_frame['habilidades']), 
            set(course_frame['habilidades'])
        )
        
        competencia_similarity = self._calculate_set_similarity(
            set(user_frame['competencias']), 
            set(course_frame['competencias'])
        )
        
        # Calcula a similaridade total ponderada
        total_similarity = (
            area_similarity * self.weights['areas'] +
            habilidade_similarity * self.weights['habilidades'] +
            competencia_similarity * self.weights['competencias']
        )
        
        return total_similarity

    def _calculate_set_similarity(self, set1, set2):
        if not set1 or not set2:
            return 0.0
            
        # Calcula a similaridade usando o coeficiente de Jaccard
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        
        if union == 0:
            return 0.0
            
        return intersection / union

    def get_similarity_level(self, similarity_score):
        if similarity_score >= self.similarity_thresholds['high']:
            return 'high'
        elif similarity_score >= self.similarity_thresholds['medium']:
            return 'medium'
        elif similarity_score >= self.similarity_thresholds['low']:
            return 'low'
        return 'none' 