import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

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

        # Criar universo de discurso para similaridade
        self.universe = np.linspace(0, 1, 100)
        
        # Criar variáveis fuzzy
        self.similarity = ctrl.Antecedent(self.universe, 'similarity')
        
        # Definir funções de pertinência
        self.similarity['low'] = fuzz.trimf(self.universe, [0, 0, 0.4])
        self.similarity['medium'] = fuzz.trimf(self.universe, [0.2, 0.5, 0.8])
        self.similarity['high'] = fuzz.trimf(self.universe, [0.6, 1, 1])

    def calculate_similarity(self, user_frame, course_frame):
        # Calcula similaridade para cada aspecto usando lógica fuzzy
        area_similarity = self._calculate_fuzzy_similarity(
            set(user_frame['areas']), 
            set(course_frame['areas'])
        )
        
        habilidade_similarity = self._calculate_fuzzy_similarity(
            set(user_frame['habilidades']), 
            set(course_frame['habilidades'])
        )
        
        competencia_similarity = self._calculate_fuzzy_similarity(
            set(user_frame['competencias']), 
            set(course_frame['competencias'])
        )
        
        # Calcula a similaridade total ponderada usando operador fuzzy
        total_similarity = self._fuzzy_weighted_average({
            'areas': area_similarity,
            'habilidades': habilidade_similarity,
            'competencias': competencia_similarity
        })
        
        return total_similarity

    def _calculate_fuzzy_similarity(self, set1, set2):
        if not set1 or not set2:
            return 0.0
            
        # Calcula a similaridade usando funções de pertinência fuzzy
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        
        if not union:
            return 0.0
            
        # Calcula similaridade base
        similarity = len(intersection) / len(union)
        
        # Aplica inferência fuzzy
        similarity_level = fuzz.interp_membership(
            self.universe,
            self.similarity['high'].mf,
            similarity
        )
        
        return similarity_level

    def _fuzzy_weighted_average(self, similarities):
        # Calcula a média ponderada usando operador fuzzy
        total_weight = sum(self.weights.values())
        weighted_sum = sum(similarities[key] * self.weights[key] 
                          for key in similarities)
        return weighted_sum / total_weight

    def get_similarity_level(self, similarity_score):
        # Aplica funções de pertinência para determinar o nível de similaridade
        if similarity_score >= self.similarity_thresholds['high']:
            return 'high'
        elif similarity_score >= self.similarity_thresholds['medium']:
            return 'medium'
        elif similarity_score >= self.similarity_thresholds['low']:
            return 'low'
        return 'none' 