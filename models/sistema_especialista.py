class ExpertSystem:
    def __init__(self):
        # Regras para ajuste de similaridade
        self.rules = {
            'high': {
                'threshold': 0.7,
                'boost': 1.2  # Aumenta em 20% para alta similaridade
            },
            'medium': {
                'threshold': 0.4,
                'boost': 1.1  # Aumenta em 10% para média similaridade
            },
            'low': {
                'threshold': 0.2,
                'boost': 1.0  # Sem boost para baixa similaridade
            },
            'none': {
                'threshold': 0.0,
                'boost': 1.0  # Sem boost para nenhuma similaridade
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