class CourseFrame:
    def __init__(self):
        self.weights = {
            'areas': 0.4,
            'habilidades': 0.3,
            'competencias': 0.3
        }

    def create_user_frame(self, areas, habilidades, competencias):
        return {
            'areas': areas,
            'habilidades': habilidades,
            'competencias': competencias
        }

    def create_course_frame(self, course):
        return {
            'areas': course['areas'],
            'habilidades': course['habilidades'],
            'competencias': course['competencias']
        }

    def calculate_match(self, user_frame, course_frame):
        # Calcular correspondência para cada categoria
        areas_match = len(set(user_frame['areas']) & set(course_frame['areas'])) / len(set(user_frame['areas'] | course_frame['areas'])) if user_frame['areas'] else 0
        habilidades_match = len(set(user_frame['habilidades']) & set(course_frame['habilidades'])) / len(set(user_frame['habilidades'] | course_frame['habilidades'])) if user_frame['habilidades'] else 0
        competencias_match = len(set(user_frame['competencias']) & set(course_frame['competencias'])) / len(set(user_frame['competencias'] | course_frame['competencias'])) if user_frame['competencias'] else 0

        # Calcular score ponderado
        total_score = (
            areas_match * self.weights['areas'] +
            habilidades_match * self.weights['habilidades'] +
            competencias_match * self.weights['competencias']
        )

        return total_score 