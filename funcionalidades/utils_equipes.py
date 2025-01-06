overview_equipes = """
<div>
    <h4>Visão Geral das Equipes</h4>
    <p>A <strong>visão geral das equipes</strong> serve como um painel unificado para acompanhar o <strong>desempenho,
     o acesso</strong> e a <strong>organização</strong> das equipes e de seus membros. Esse painel inclui informações
      essenciais como:</p>

    <h5>Estrutura das Equipes</h5>
    <p>As equipes são divididas conforme a organização, podendo ser por <strong>centros administrativos</strong> 
    (filiais ou departamentos) ou <strong>macro serviços</strong> (grandes áreas como limpeza, manutenção, jardinagem, etc.).</p>

    <h5>Hierarquia de Acesso</h5>
    <p>Com <strong>permissões claras</strong> para gestores, supervisores e funcionários operacionais.</p>

    <h5>Indicadores de Produtividade</h5>
    <p>Fornece <strong>métricas de produtividade</strong> por colaborador e por equipe, permitindo uma visão tanto 
    individual quanto coletiva.</p>

    <h5>Relatórios em Tempo Real</h5>
    <p>Facilita <strong>decisões e otimizações</strong> baseadas em dados atualizados. Essa visão unificada permite 
    que gestores e coordenadores monitorem e ajustem as operações, garantindo que os recursos humanos estejam alocados 
    conforme as prioridades do serviço.</p>
</div>
"""

individuali_permission = """
<div>
  <h4>Permissões Individuais</h4>
  <p>
    As <strong>permissões individuais</strong> controlam o nível de acesso de cada colaborador ao ZeladorX, com base nas responsabilidades e necessidades de informação de cada um. Abaixo, apresento uma estrutura sugerida:
  </p>

  <h5>Gestores</h5>
  <ul>
    <li>Acesso total a <strong>relatórios</strong>, configurações do sistema, e funcionalidades de controle administrativo.</li>
    <li>Capacidade de <strong>revisar, editar e aprovar</strong> registros de produtividade e status das tarefas.</li>
    <li>Permissão para <strong>criar e editar equipes</strong> e distribuir permissões.</li>
  </ul>

  <h5>Supervisores</h5>
  <ul>
    <li>Acesso para visualizar e editar informações das equipes que coordenam.</li>
    <li>Permissão para <strong>revisar a produtividade individual</strong> dos membros da equipe e atribuir tarefas.</li>
    <li>Controle de status e atualização dos processos e registros de serviços realizados.</li>
  </ul>

  <h5>Funcionários Operacionais</h5>
  <ul>
    <li>Acesso para visualizar suas próprias tarefas, checklists e métricas de produtividade.</li>
    <li>Permissão para registrar a conclusão das tarefas e <strong>reportar problemas</strong>.</li>
    <li>Sem acesso às informações e estatísticas de outros colaboradores.</li>
  </ul>

  <div style="background-color: #f9f9f9; border-left: 4px solid #007bff; padding: 15px; margin: 20px 0;">
    <h5><strong>Mais de 120 permissões exclusivas</strong></h5>
    <p>
      Essas são nossas sugestões de estrutura hierárquica de permissões. No entanto, o <strong>ZeladorX</strong> vai além, oferecendo <strong>mais de 60 permissões diferentes</strong>. 
      Cada botão, tela, tabela ou funcionalidade pode ser configurado para acesso exclusivo, garantindo total controle e segurança no uso do sistema.
    </p>
  </div>
  
  <p>
    Essa estrutura hierárquica garante que cada colaborador acesse somente as informações necessárias para seu papel, mantendo a <strong>segurança</strong> e o <strong>foco nas funções principais</strong>.
  </p>
  
    <div>
        <img  src="static/index/permissoes de usuario.png" alt="Estrutura de permissões no ZeladorX" class="img-fluid">
    </div>
    <br>
</div>
"""

productivity = """
<div>
    <h4>Cálculo de Produtividade Individual</h4>
    <p>Para medir a <strong>produtividade individual</strong> de cada colaborador, podemos considerar diversos fatores e métricas, que podem variar conforme o tipo de serviço:</p>

    <h5>Tarefas Completas vs. Tarefas Atribuídas</h5>
    <p>Mede a quantidade de tarefas concluídas em relação ao total de tarefas atribuídas no período, oferecendo uma visão básica da eficiência.</p>

    <h5>Tempo de Conclusão por Tarefa</h5>
    <p>Registra o tempo gasto em cada tarefa e compara com o tempo médio esperado. Este cálculo permite identificar áreas de melhoria e o ritmo de cada colaborador.</p>

    <h5>Taxa de Erro ou Reabertura de Tarefas</h5>
    <p>Quantifica o número de tarefas que precisam ser reabertas ou corrigidas. Isso ajuda a entender a qualidade do serviço prestado.</p>

    <h5>Pontuação de Qualidade</h5>
    <p>Atribui uma pontuação baseada em avaliações de supervisores ou clientes, refletindo a satisfação com o serviço realizado.</p>
    
    <div>
        <img src='static/index/agendado x acompanhado.png' alt='outra foto' class='img-fluid'>
    </div>

    <p>Essas métricas podem ser combinadas para formar um <strong>índice de produtividade individual</strong>, ajustando pesos conforme a prioridade de cada indicador.</p>
</div>
"""

organization = """
<div>
    <h4>Organização dos Times: Centros Administrativos e Macro Serviços</h4>
    <p>Existem várias opções de estrutura para organizar os times, dependendo das necessidades e da estrutura da empresa. Abaixo, apresentamos três opções principais:</p>

    <h5>Opção 1: Organização por Centro Administrativo</h5>
    <ul>
        <li>Estrutura ideal para empresas com operações em várias localidades ou filiais, como centros regionais, unidades ou departamentos específicos.</li>
        <li>Facilita o controle local, com relatórios de produtividade e gestão de equipe segmentados por cada centro.</li>
        <li>Gestores regionais têm acesso dedicado às suas unidades, otimizando a supervisão e resposta rápida a problemas locais.</li>
    </ul>

    <h5>Opção 2: Organização por Macro Serviço</h5>
    <ul>
        <li>Equipes são agrupadas conforme o tipo de serviço que prestam, como "Limpeza", "Manutenção", "Jardinagem", etc.</li>
        <li>Esse formato favorece empresas com operações especializadas, centralizando o controle e monitoramento de produtividade por área de serviço.</li>
        <li>A gestão é realizada por supervisores de área, permitindo um acompanhamento específico das necessidades e padrões de cada tipo de serviço.</li>
    </ul>

    <h5>Opção 3: Organização Híbrida (Centro Administrativo + Macro Serviço)</h5>
    <ul>
        <li>Uma combinação dos dois métodos, onde cada unidade ou centro administrativo é subdividido em macro serviços.</li>
        <li>Ideal para grandes organizações com serviços diversos em cada unidade, oferecendo relatórios segmentados e detalhados, tanto por localidade quanto por especialidade.</li>
        <li>Flexibiliza a alocação de recursos e facilita a análise comparativa de produtividade entre localidades e serviços.</li>
    </ul>
    <div>
        <img src='static/index/superuser.png' alt='outra foto' class='img-fluid'>
    </div>
</div>
"""

escales = """
<div>
    <h4>Estrutura de Escalas por Centro Administrativo ou Macro Serviço</h4>
    <p>A definição de escalas no ZeladorX pode ser adaptada conforme a complexidade da operação, permitindo uma organização por centro administrativo, macro serviço ou uma abordagem combinada:</p>

    <h5>Por Centro Administrativo</h5>
    <p>Cada unidade ou local de trabalho possui sua própria escala, permitindo uma gestão específica para cada localidade. Isso facilita o ajuste das escalas conforme as necessidades de cada centro, atendendo às particularidades de cada ambiente.</p>

    <h5>Por Macro Serviço</h5>
    <p>Escalas específicas para grandes áreas, como limpeza, jardinagem e manutenção, proporcionando uma visão mais focada no tipo de serviço. Essa abordagem facilita a alocação de recursos conforme as demandas e especialidades necessárias em cada área de atuação.</p>

    <h5>Estrutura Combinada</h5>
    <p>As equipes são agrupadas tanto por centros administrativos quanto por macro serviços, permitindo uma organização das escalas de forma integrada. A gestão combinada permite um balanceamento dinâmico, atendendo de forma otimizada às demandas específicas de cada unidade e especialidade.</p>
</div>
"""

how_functions = """
<div>
    <h4>Integração das Funcionalidades no ZeladorX</h4>
    <p>O ZeladorX une a organização das equipes, as permissões individuais, o cálculo de produtividade e a estrutura de escalas para apoiar gestores e colaboradores no dia a dia. Veja como essas partes se conectam para facilitar as operações:</p>

    <h5>1. Visão Geral das Equipes e Permissões</h5>
    <p>No ZeladorX, as equipes podem ser organizadas por centros administrativos (filiais ou setores) ou por macro serviços (limpeza, manutenção, jardinagem, etc.). Cada equipe tem uma visão centralizada, onde os gestores podem monitorar quem está em cada turno, as tarefas atribuídas, em andamento e concluídas.</p>
    <p>Cada colaborador possui permissões conforme seu cargo:</p>
    <ul>
        <li><strong>Gestores:</strong> Acesso completo a dados e relatórios, controle dos turnos e gestão da produtividade da equipe.</li>
        <li><strong>Supervisores:</strong> Controle sobre suas equipes, distribuição de tarefas e verificação da produtividade.</li>
        <li><strong>Colaboradores:</strong> Acesso às suas tarefas e possibilidade de registrar o andamento e a conclusão das atividades.</li>
    </ul>
    <p>Essa estrutura de permissões garante que cada colaborador acesse apenas o necessário, mantendo a organização e segurança das informações.</p>

    <h5>2. Cálculo da Produtividade Individual e da Equipe</h5>
    <p>Para avaliar o desempenho, o ZeladorX mede a produtividade com indicadores como:</p>
    <ul>
        <li><strong>Tarefas Concluídas:</strong> Quantidade de tarefas finalizadas no turno.</li>
        <li><strong>Tempo por Tarefa:</strong> Comparação entre o tempo esperado e o tempo real.</li>
        <li><strong>Qualidade:</strong> Avaliação por supervisores ou clientes, dependendo da operação.</li>
    </ul>
    <p>Esses dados ajudam a identificar colaboradores com bom desempenho, áreas que precisam de treinamento e a melhorar a alocação das tarefas. Gestores conseguem ter uma visão do desempenho individual e da equipe, ajudando na tomada de decisões para ajustes.</p>

    <h5>3. Organização e Gestão de Escalas</h5>
    <p>As escalas podem ser ajustadas conforme o tipo de trabalho:</p>
    <ul>
        <li><strong>Escalas Fixas:</strong> Horários consistentes, úteis para tarefas recorrentes.</li>
        <li><strong>Escalas Rotativas:</strong> Turnos alternados para evitar sobrecarga, como no turno da noite.</li>
        <li><strong>Escalas por Demanda:</strong> Flexíveis, adaptam-se às necessidades sazonais ou imprevistos.</li>
    </ul>
    <p>Gestores podem ajustar as escalas pelo sistema, visualizando a disponibilidade de cada colaborador para ajustes rápidos quando necessário.</p>

    <h5>4. Estrutura de Escalas por Centro Administrativo e Macro Serviço</h5>
    <p>Em grandes operações, o ZeladorX permite organizar as escalas por:</p>
    <ul>
        <li><strong>Centro Administrativo:</strong> Cada unidade ou filial gerencia suas escalas conforme as necessidades locais.</li>
        <li><strong>Macro Serviço:</strong> Equipes são organizadas por especialidade, como limpeza ou jardinagem, cada uma com seu horário específico.</li>
        <li><strong>Estrutura Combinada:</strong> Agrupa por unidades e especialidades, atendendo as demandas de cada localidade e tipo de serviço.</li>
    </ul>

    <h5>5. Funcionamento Prático no Dia a Dia</h5>
    <p>No uso diário, um gestor consegue:</p>
    <ul>
        <li>Visualizar equipes, escalas, tarefas concluídas e pendentes.</li>
        <li>Atribuir tarefas ou ajustar prioridades com base nos relatórios de produtividade.</li>
        <li>Alterar escalas para cobrir ausências, reorganizando turnos sem afetar as operações.</li>
        <li>Emitir relatórios e revisar a produtividade para planejar treinamentos e otimizar a alocação de tarefas.</li>
    </ul>
    <p>Supervisores utilizam os mesmos recursos para manter suas equipes alinhadas e eficientes, enquanto colaboradores visualizam suas tarefas e registram suas atividades diretamente no sistema.</p>
</div>

"""


dashboards = """
<div>
    <h4>Dashboards e Monitoramento de Performance</h4>
    <p>O ZeladorX oferece uma série de dashboards interativos e intuitivos, proporcionando uma visão detalhada das operações. Essas telas foram projetadas para ajudar os gestores a monitorar atividades em tempo real, avaliar indicadores de desempenho, e realizar ajustes necessários com precisão.</p>

    <h5>Visão Geral da Operação</h5>
    <p>O dashboard principal oferece uma visão ampla das atividades diárias, mostrando o status atual de cada serviço, como limpeza, jardinagem e manutenção. Aqui, gestores podem acompanhar o progresso de cada tarefa, visualizando indicadores-chave de performance (KPIs) para avaliar a eficiência e identificar áreas que necessitam de atenção imediata.</p>

    <h5>Escalas e Disponibilidade de Equipe</h5>
    <p>Este painel detalha as escalas de cada funcionário, permitindo uma visão clara sobre a disponibilidade de cada membro da equipe. Com a funcionalidade de filtros por unidade e macro serviço, é possível identificar facilmente quaisquer lacunas na equipe e reequilibrar as escalas de forma ágil e eficiente.</p>

    <h5>Controle de Estoque e Utilização de Materiais</h5>
    <p>Com o dashboard de controle de estoque, o ZeladorX permite monitorar o uso de materiais e insumos em tempo real. Este painel exibe os níveis de estoque por unidade, permitindo o planejamento antecipado de reabastecimento e evitando faltas de materiais essenciais para a continuidade das operações.</p>

    <h5>Indicadores de Produtividade e Desempenho</h5>
    <p>O painel de produtividade oferece relatórios detalhados sobre o desempenho das equipes e do tempo médio de execução de tarefas. Com dados históricos e gráficos, é possível identificar tendências de produtividade, comparar períodos, e tomar decisões informadas para aumentar a eficiência operacional.</p>

    <h5>Alertas e Notificações</h5>
    <p>Para garantir que os gestores estejam sempre informados, o dashboard de alertas exibe notificações em tempo real sobre tarefas atrasadas, baixa disponibilidade de estoque e necessidades de manutenção emergente. Estes alertas proativos ajudam a antecipar problemas e garantir a continuidade dos serviços.</p>

    <p>Esses dashboards do <strong>ZeladorX</strong> oferecem uma visão robusta e integrada, permitindo uma gestão estratégica de alto nível, que alinha a operação diária com os objetivos organizacionais.</p>
    
    <div>
        <img src='static/index/dash gerencial jardinagem.png' alt='outra foto' class='img-fluid'>
    </div>
</div>
"""