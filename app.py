from flask import Flask, render_template, request, jsonify
from models.frame import CourseFrame
from models.logica_fuzzy import FuzzyLogic
from models.sistema_especialista import ExpertSystem
from data.course_database import CourseDatabase
from data.constants import AREAS_CONHECIMENTO, HABILIDADES, COMPETENCIAS

app = Flask(__name__)

# Inicializar os componentes do sistema
course_frame = CourseFrame()
fuzzy_logic = FuzzyLogic()
expert_system = ExpertSystem()
course_db = CourseDatabase()

@app.route('/')
def index():
    return render_template('index.html', 
                         areas=AREAS_CONHECIMENTO,
                         habilidades=HABILIDADES,
                         competencias=COMPETENCIAS)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    
    # Coleta as seleções do usuário
    selected_areas = data.get('areas', [])
    selected_habilidades = data.get('habilidades', [])
    selected_competencias = data.get('competencias', [])
    
    # Cria o frame do usuário
    user_frame = course_frame.create_user_frame(
        areas=selected_areas,
        habilidades=selected_habilidades,
        competencias=selected_competencias
    )
    
    # Obtém todos os cursos
    courses = course_db.get_all_courses()
    
    # Calcula a similaridade para cada curso
    recommendations = []
    for course in courses:
        course_frame_data = course_frame.create_course_frame(course)
        
        # Calcula similaridade
        similarity = fuzzy_logic.calculate_similarity(user_frame, course_frame_data)
        
        # Aplica regras do sistema especialista
        adjusted_similarity = expert_system.apply_rules(similarity)
        recommendation_level = expert_system.get_recommendation_level(adjusted_similarity)
        
        # Adiciona a recomendação apenas se houver alguma similaridade
        if adjusted_similarity > 0:
            recommendations.append({
                'nome': course['nome'],
                'descricao': course['descricao'],
                'similaridade': adjusted_similarity,
                'nivel': recommendation_level,
                'areas': course['areas'],
                'habilidades': course['habilidades'],
                'competencias': course['competencias']
            })
    
    # Ordena as recomendações por similaridade
    recommendations.sort(key=lambda x: x['similaridade'], reverse=True)
    
    # Retorna apenas as top 5 recomendações
    return jsonify(recommendations[:5])

if __name__ == '__main__':
    app.run(debug=True)