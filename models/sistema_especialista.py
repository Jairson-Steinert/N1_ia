class ExpertSystem:
    def __init__(self):
        # Regras para ajuste de similaridade
        self.rules = {
            'high': {
                'threshold': 0.5,  # Reduzido de 0.7
                'boost': 1.1  # Reduzido de 1.2
            },
            'medium': {
                'threshold': 0.3,  # Reduzido de 0.4
                'boost': 1.05  # Reduzido de 1.1
            },
            'low': {
                'threshold': 0.1,  # Reduzido de 0.2
                'boost': 1.0
            },
            'none': {
                'threshold': 0.0,
                'boost': 1.0
            }
        }

    def apply_rules(self, similarity_score):
        """
        Aplica regras do sistema especialista para ajustar a similaridade
        """
        # Determina o nível de similaridade baseado no score
        level = self.get_recommendation_level(similarity_score)
        
        # Aplica o boost correspondente ao nível
        adjusted_score = similarity_score * self.rules[level]['boost']
        
        # Garante que o score não ultrapasse 1.0
        return min(adjusted_score, 1.0)

    def get_recommendation_level(self, similarity_score):
        """
        Determina o nível de recomendação baseado no score de similaridade
        """
        if similarity_score >= self.rules['high']['threshold']:
            return 'high'
        elif similarity_score >= self.rules['medium']['threshold']:
            return 'medium'
        elif similarity_score >= self.rules['low']['threshold']:
            return 'low'
        return 'none' 