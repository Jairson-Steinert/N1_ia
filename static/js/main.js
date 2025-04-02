document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('preferenciasForm');
    const recomendacoesDiv = document.getElementById('recomendacoes');
    const loadingDiv = document.getElementById('loading');
    const mensagemInicialDiv = document.getElementById('mensagemInicial');

    // Adicionar efeito de hover nos selects
    const selects = document.querySelectorAll('.form-select');
    selects.forEach(select => {
        select.addEventListener('mouseenter', function() {
            this.style.borderColor = '#0d6efd';
        });
        select.addEventListener('mouseleave', function() {
            if (!this.matches(':focus')) {
                this.style.borderColor = '#e9ecef';
            }
        });
    });

    // Adicionar contador de seleções para cada seção
    const sections = [
        { id: 'areas_conhecimento', title: 'Áreas de Conhecimento', minRequired: 1 },
        { id: 'habilidades', title: 'Habilidades', minRequired: 1 },
        { id: 'competencias', title: 'Competências', minRequired: 1 }
    ];

    sections.forEach(section => {
        const container = document.querySelector(`[data-section="${section.id}"]`);
        if (!container) return;

        const counter = document.createElement('div');
        counter.className = 'selection-status mt-2';
        container.appendChild(counter);

        function updateCounter() {
            const checked = container.querySelectorAll('input[type="checkbox"]:checked').length;
            const status = checked >= section.minRequired ? 'text-success' : 'text-danger';
            counter.innerHTML = `
                <div class="d-flex align-items-center ${status}">
                    <i class="fas ${checked >= section.minRequired ? 'fa-check-circle' : 'fa-exclamation-circle'} me-2"></i>
                    <span>${checked} ${checked === 1 ? 'item selecionado' : 'itens selecionados'}</span>
                </div>
            `;
        }

        // Adicionar evento de mudança para cada checkbox
        container.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', updateCounter);
        });

        updateCounter();
    });

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Validar seleções mínimas
        const validations = sections.map(section => {
            const container = document.querySelector(`[data-section="${section.id}"]`);
            const checked = container ? container.querySelectorAll('input[type="checkbox"]:checked').length : 0;
            return {
                section: section.title,
                valid: checked >= section.minRequired,
                selected: checked
            };
        });

        const invalid = validations.filter(v => !v.valid);
        if (invalid.length > 0) {
            const messages = invalid.map(v => 
                `${v.section}: selecione pelo menos ${v.section.minRequired} ${v.section.minRequired === 1 ? 'opção' : 'opções'} (selecionado: ${v.selected})`
            );
            
            // Mostrar mensagem de erro mais amigável
            mensagemInicialDiv.innerHTML = `
                <div class="alert alert-warning" role="alert">
                    <i class="fas fa-exclamation-triangle me-2"></i>
                    <strong>Por favor, complete sua seleção:</strong>
                    <ul class="mb-0 mt-2">
                        ${messages.map(msg => `<li>${msg}</li>`).join('')}
                    </ul>
                </div>
            `;
            mensagemInicialDiv.classList.remove('d-none');
            return;
        }

        // Mostrar loading com animação
        loadingDiv.classList.remove('d-none');
        recomendacoesDiv.classList.add('d-none');
        mensagemInicialDiv.classList.add('d-none');

        // Coletar dados do formulário
        const data = sections.reduce((acc, section) => {
            const container = document.querySelector(`[data-section="${section.id}"]`);
            acc[section.id] = Array.from(container.querySelectorAll('input[type="checkbox"]:checked'))
                .map(checkbox => checkbox.value);
            return acc;
        }, {});

        try {
            const response = await fetch('/recomendar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            const recomendacoes = await response.json();
            loadingDiv.classList.add('d-none');

            if (recomendacoes && recomendacoes.length > 0) {
                const listGroup = recomendacoesDiv.querySelector('.list-group');
                listGroup.innerHTML = '';

                recomendacoes.forEach((rec, index) => {
                    const item = document.createElement('div');
                    item.className = 'list-group-item';
                    item.style.animationDelay = `${index * 0.1}s`;
                    item.innerHTML = `
                        <div class="curso-header d-flex justify-content-between align-items-start mb-3">
                            <h5 class="curso-titulo mb-0">
                                <i class="fas fa-graduation-cap me-2"></i>
                                ${rec.curso}
                            </h5>
                            <span class="badge bg-success score-badge">
                                <i class="fas fa-chart-line me-1"></i>
                                ${(rec.pontuacao * 100).toFixed(1)}%
                            </span>
                        </div>
                        <div class="curso-info mb-3">
                            <span class="badge bg-primary me-2">
                                <i class="fas fa-clock me-1"></i>
                                ${rec.duracao} anos
                            </span>
                        </div>
                        <div class="curso-detalhes">
                            <div class="mb-3">
                                <h6 class="mb-2"><i class="fas fa-book me-2"></i>Áreas de Conhecimento</h6>
                                <div class="tags">
                                    ${rec.areas_conhecimento.map(area => 
                                        `<span class="badge bg-info">${area}</span>`
                                    ).join(' ')}
                                </div>
                            </div>
                            <div class="mb-3">
                                <h6 class="mb-2"><i class="fas fa-star me-2"></i>Habilidades</h6>
                                <div class="tags">
                                    ${rec.habilidades.map(hab => 
                                        `<span class="badge bg-secondary">${hab}</span>`
                                    ).join(' ')}
                                </div>
                            </div>
                            <div>
                                <h6 class="mb-2"><i class="fas fa-trophy me-2"></i>Competências</h6>
                                <div class="tags">
                                    ${rec.competencias.map(comp => 
                                        `<span class="badge bg-warning text-dark">${comp}</span>`
                                    ).join(' ')}
                                </div>
                            </div>
                        </div>
                    `;
                    listGroup.appendChild(item);
                });

                recomendacoesDiv.classList.remove('d-none');
            } else {
                mensagemInicialDiv.innerHTML = `
                    <div class="alert alert-info" role="alert">
                        <i class="fas fa-info-circle me-2"></i>
                        <strong>Nenhuma recomendação encontrada</strong>
                        <p class="mb-0 mt-2">Tente selecionar diferentes combinações de opções para encontrar cursos que combinem com seu perfil.</p>
                    </div>
                `;
                mensagemInicialDiv.classList.remove('d-none');
            }
        } catch (error) {
            console.error('Erro ao buscar recomendações:', error);
            loadingDiv.classList.add('d-none');
            mensagemInicialDiv.innerHTML = `
                <div class="alert alert-danger" role="alert">
                    <i class="fas fa-exclamation-circle me-2"></i>
                    <strong>Ops! Algo deu errado</strong>
                    <p class="mb-0 mt-2">Não foi possível processar sua solicitação. Por favor, tente novamente mais tarde.</p>
                </div>
            `;
            mensagemInicialDiv.classList.remove('d-none');
        }
    });
}); 