#!/usr/bin/env python3
"""Gera as páginas de serviço, o blog, o sitemap e o robots.txt.

Uso (na raiz do repositório):  python3 tools/gerar_paginas.py
Para mudar um texto, edite SERVICOS ou ARTIGOS abaixo e rode de novo.
A home e a página do perito também são geradas aqui (pagina_home, pagina_perito).
"""
import json
import os
from urllib.parse import quote

BASE = "https://www.edferrarijr.com"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONE = "5519971002263"
DATA = "2026-10-18"
ENDERECO = "Av. Antônio Artioli, 276 - Swiss Park, Campinas - SP, 13049-253"
CREFITO = "CREFITO-3/306266-F"

WA_SVG = ""


def wa(texto):
    return f"https://api.whatsapp.com/send?phone={FONE}&text={quote(texto)}"


# ---------------------------------------------------------------- conteúdo
SERVICOS = [
    {
        "slug": "fisioterapia-ombro-campinas",
        "menu": "Ombro, cotovelo e punho",
        "resumo": "Manguito rotador, epicondilite, túnel do carpo e tendinites.",
        "title": "Fisioterapia para Ombro, Cotovelo e Punho em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapia para dor no ombro, manguito rotador, epicondilite, túnel do carpo e tendinites em Campinas. Avaliação individual no Swiss Park ou em casa.",
        "h1": "Fisioterapia para ombro, cotovelo e punho em Campinas",
        "lead": "Dor ao levantar o braço, ao pegar peso ou ao digitar costuma ter causas diferentes. Eu faço a avaliação para entender qual estrutura está sobrecarregada e montar o plano de reabilitação para o seu caso.",
        "wa": "Olá! Gostaria de agendar uma avaliação para dor no ombro, cotovelo ou punho.",
        "secoes": [
            ("Quais problemas eu avalio e trato", """<ul>
<li><strong>Ombro:</strong> tendinopatia e lesões do manguito rotador, bursite, dor no ombro após luxação ou cirurgia.</li>
<li><strong>Cotovelo:</strong> epicondilite lateral ("cotovelo de tenista") e medial ("cotovelo de golfista").</li>
<li><strong>Punho e mão:</strong> síndrome do túnel do carpo, tenossinovite de De Quervain e outras tendinites.</li>
<li><strong>Pós-operatório:</strong> reabilitação depois de cirurgia no ombro, cotovelo ou punho, conforme a orientação do cirurgião.</li>
</ul>"""),
            ("Como funciona a avaliação", """<p>A primeira sessão é dedicada à avaliação. Converso sobre sua rotina, seu trabalho ou esporte e o histórico da dor. Depois avalio amplitude de movimento, força, estabilidade da articulação e o padrão do movimento. Com isso, defino os exercícios e as técnicas manuais da fase em que você está e quais sinais indicam que é preciso falar com o seu médico.</p>
<p>O tratamento combina exercícios terapêuticos, terapia manual e orientações para a rotina ou o treino. A frequência e a duração dependem do diagnóstico e da sua resposta, e eu ajusto o plano ao longo das sessões.</p>"""),
            ("Atletas e praticantes de musculação, CrossFit e Hyrox", """<p>O ombro é uma das regiões mais exigidas em movimentos acima da cabeça, como o overhead, o snatch, as barras e as argolas, e em exercícios de empurrar, como supino e flexões. Quando a dor aparece nesses movimentos, a reabilitação inclui ajustar a técnica, a carga e o volume do treino. O objetivo é reduzir a dor e preparar o seu retorno ao treino de forma gradual, com critérios definidos.</p>
<p>Veja também: <a href="/blog/dor-no-ombro-crossfit/">dor no ombro no CrossFit: sinais de que vale uma avaliação</a>.</p>"""),
        ],
        "faq": [
            ("Preciso de pedido médico para fazer fisioterapia?", "Para iniciar a avaliação fisioterapêutica não é obrigatório. Se você já tem exames ou laudo, traga para a primeira sessão, pois eles ajudam no planejamento. Alguns convênios exigem o pedido médico para reembolso."),
            ("Quantas sessões vou precisar?", "Depende do problema, do tempo de sintomas e da sua rotina. Eu defino uma estimativa depois da avaliação e reviso o plano conforme sua evolução."),
            ("Posso continuar treinando durante o tratamento?", "Na maioria dos casos é possível manter parte do treino, adaptando movimentos, cargas e volume. Eu oriento o que manter e o que modificar em cada fase."),
        ],
        "rel": ["fisioterapia-esportiva-campinas", "fisioterapia-lesoes-musculares-campinas", "fisioterapia-reembolso-convenio-campinas"],
    },
    {
        "slug": "fisioterapia-joelho-tornozelo-campinas",
        "menu": "Joelho e tornozelo",
        "resumo": "Menisco, LCA, condromalácia, fascite plantar e entorses.",
        "title": "Fisioterapia para Joelho e Tornozelo em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapia para dor no joelho e tornozelo em Campinas: menisco, LCA, condromalácia, fascite plantar e entorses, com retorno gradual ao esporte.",
        "h1": "Fisioterapia para joelho e tornozelo em Campinas",
        "lead": "Joelho e tornozelo suportam o peso do corpo em tudo o que fazemos, de subir escadas a correr uma prova. Eu avalio o que está gerando a dor e conduzo a reabilitação tanto de casos conservadores quanto de pós-operatório.",
        "wa": "Olá! Gostaria de agendar uma avaliação para dor no joelho ou tornozelo.",
        "secoes": [
            ("Quais problemas eu avalio e trato", """<ul>
<li><strong>Joelho:</strong> lesões de menisco, ligamento cruzado anterior (LCA), condromalácia, síndrome da dor patelofemoral, tendinopatia patelar e dor na parte lateral do joelho.</li>
<li><strong>Tornozelo e pé:</strong> entorses, instabilidade do tornozelo, tendinopatia de Aquiles e fascite plantar.</li>
<li><strong>Pós-operatório:</strong> reconstrução de LCA, meniscectomia e outras cirurgias, seguindo o protocolo e as orientações do cirurgião.</li>
</ul>"""),
            ("Como conduzo a reabilitação", """<p>A avaliação inclui histórico, testes de força, estabilidade e mobilidade e a análise de como você agacha, aterrissa, caminha e corre. A partir disso, o plano passa por fases: controle da dor e do inchaço, recuperação do movimento e da força, trabalho de controle neuromuscular e, para quem pratica esporte, retorno gradual ao treino.</p>
<p>No retorno ao esporte, uso testes funcionais, como força, saltos e agilidade, para decidir junto com você quando aumentar a carga. A ideia é voltar com critérios e não só quando a dor diminuir.</p>"""),
            ("Corredores, CrossFit e Hyrox", """<p>Corrida, agachamentos, afundos, sled push e wall balls exigem muito do joelho e do tornozelo. Em muitos casos a dor vem de um aumento rápido de volume ou de intensidade, e não de uma lesão estrutural. A avaliação ajuda a separar uma coisa da outra.</p>
<p>Veja também: <a href="/blog/dor-no-joelho-corrida/">dor no joelho na corrida: por que acontece e quando investigar</a>.</p>"""),
        ],
        "faq": [
            ("Dor no joelho sempre exige cirurgia?", "Não. Muitos casos de dor no joelho são tratados com reabilitação. A necessidade de cirurgia é uma decisão médica, tomada com base em exames e na avaliação clínica."),
            ("Tive entorse e já não dói mais. Preciso de fisioterapia?", "Mesmo sem dor, pode ficar perda de estabilidade e de equilíbrio, o que aumenta o risco de novas entorses. Uma avaliação mostra se há déficits a corrigir."),
            ("Atende pós-operatório?", "Sim. Trabalho junto ao protocolo e às orientações do cirurgião, adaptando a evolução à sua resposta."),
        ],
        "rel": ["fisioterapia-esportiva-campinas", "fisioterapia-lesoes-musculares-campinas", "fisioterapia-home-care-campinas"],
    },
    {
        "slug": "fisioterapia-lesoes-musculares-campinas",
        "menu": "Lesões musculares e ligamentares",
        "resumo": "Estiramentos, rupturas, contraturas e distensões.",
        "title": "Fisioterapia para Lesões Musculares e Ligamentares em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapia para estiramentos, distensões, rupturas, contraturas e lesões ligamentares em Campinas, com avaliação individual e retorno gradual ao treino.",
        "h1": "Fisioterapia para lesões musculares e ligamentares em Campinas",
        "lead": "Estiramento na coxa, dor na panturrilha ou uma entorse forte pedem condutas diferentes. A avaliação define a gravidade, o que pode ser trabalhado agora e em que momento sua carga de treino volta a subir.",
        "wa": "Olá! Gostaria de agendar uma avaliação para uma lesão muscular ou ligamentar.",
        "secoes": [
            ("Situações que eu atendo", """<ul>
<li>Estiramentos e distensões de posterior de coxa, quadríceps, adutores e panturrilha.</li>
<li>Rupturas musculares parciais, com encaminhamento ao médico quando necessário.</li>
<li>Contraturas e dores musculares persistentes.</li>
<li>Lesões ligamentares leves e moderadas, como entorses de tornozelo, joelho e punho.</li>
</ul>"""),
            ("Como é o processo", """<p>Primeiro avalio o mecanismo da lesão, o local da dor, a força e a mobilidade. Se houver sinais que pedem exame de imagem ou avaliação médica, eu oriento. O tratamento usa exercícios progressivos, terapia manual e recursos de eletrotermofototerapia quando indicados. A sequência é sempre baseada na fase do tecido e nos seus objetivos.</p>
<p>Para atletas, o retorno é planejado em etapas: corrida leve, mudanças de direção, saltos e esforço máximo, sempre com critérios de força e de controle do movimento.</p>"""),
            ("Prevenção de novas lesões", """<p>Depois que você está sem dor, ainda há trabalho a fazer. Revisamos o volume de treino, a distribuição de cargas na semana, o aquecimento e os déficits de força que podem ter contribuído para a lesão. Isso reduz a chance de repetir o problema, embora nenhuma estratégia elimine o risco por completo.</p>"""),
        ],
        "faq": [
            ("Quanto tempo leva para voltar a treinar depois de um estiramento?", "Varia conforme a gravidade e o músculo envolvido. Depois da avaliação, passo uma estimativa e os critérios que usamos para liberar cada etapa."),
            ("Gelo ou calor?", "Depende da fase e do tipo de lesão. Na avaliação eu explico o que faz sentido no seu caso."),
            ("Preciso fazer ressonância antes?", "Nem sempre. Eu avalio e, se houver indicação, oriento a procurar o médico para o exame de imagem."),
        ],
        "rel": ["fisioterapia-esportiva-campinas", "fisioterapia-joelho-tornozelo-campinas", "ferrari-recovery-campinas"],
    },
    {
        "slug": "fisioterapia-coluna-campinas",
        "menu": "Coluna vertebral",
        "resumo": "Hérnia de disco, dor lombar, ciatalgia e postura.",
        "title": "Fisioterapia para Coluna, Dor Lombar e Hérnia de Disco em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapia para dor lombar, hérnia de disco, ciatalgia e dor cervical em Campinas. Avaliação individual, exercícios e orientações para a rotina.",
        "h1": "Fisioterapia para coluna, dor lombar e hérnia de disco em Campinas",
        "lead": "Dor nas costas é uma das queixas mais comuns, e nem sempre tem relação com hérnia de disco. A avaliação ajuda a identificar o que piora e o que alivia os sintomas, e a montar um plano que cabe na sua rotina.",
        "wa": "Olá! Gostaria de agendar uma avaliação para dor na coluna.",
        "secoes": [
            ("Quadros que eu avalio e trato", """<ul>
<li>Dor lombar aguda e crônica.</li>
<li>Hérnia de disco e protrusões, com ou sem dor irradiada.</li>
<li>Ciatalgia (dor que desce pela perna).</li>
<li>Dor cervical e na região entre as escápulas, comum em quem passa muitas horas sentado.</li>
<li>Dor na coluna ligada ao treino, como agachamento, levantamento terra e remada.</li>
</ul>"""),
            ("O que a avaliação inclui", """<p>Avalio a coluna e também quadril, ombros e padrões de movimento, porque a dor muitas vezes está relacionada com a forma como o corpo distribui o esforço. Pesquiso sinais de alerta que exigem encaminhamento médico, como perda de força progressiva, alteração de sensibilidade importante, dor noturna intensa ou perda de controle de esfíncteres.</p>
<p>O tratamento costuma combinar exercícios de estabilização e fortalecimento, mobilidade, terapia manual e orientação sobre postura, ergonomia e retorno às atividades. Educação sobre dor é parte importante: entender o que está acontecendo reduz o medo de se mexer.</p>"""),
            ("Treino e coluna", """<p>Quem treina força, CrossFit ou corrida pode precisar adaptar a técnica, os movimentos e a carga por um período. Eu indico alternativas que mantêm você ativo sem agravar os sintomas, e trabalho o retorno aos exercícios principais de forma progressiva.</p>"""),
        ],
        "faq": [
            ("Hérnia de disco tem que operar?", "A maior parte dos casos é tratada sem cirurgia. A indicação cirúrgica é uma decisão médica e depende dos sintomas, da evolução e dos exames."),
            ("Quando devo procurar um médico com urgência?", "Em caso de fraqueza que piora rápido, formigamento importante na região íntima, perda de controle de urina ou fezes, febre com dor nas costas ou dor após trauma forte."),
            ("Posso fazer academia com dor lombar?", "Muitas vezes sim, com adaptações. Eu oriento o que manter e o que ajustar para o seu caso."),
        ],
        "rel": ["fisioterapia-esportiva-campinas", "fisioterapia-home-care-campinas", "fisioterapia-reembolso-convenio-campinas"],
    },
    {
        "slug": "fisioterapia-esportiva-campinas",
        "menu": "Fisioterapia esportiva",
        "resumo": "Retorno ao esporte e performance: CrossFit, Hyrox, ATHX e corrida.",
        "title": "Fisioterapia Esportiva em Campinas: CrossFit, Hyrox e Corrida | Ed Ferrari Jr",
        "desc": "Fisioterapeuta esportivo em Campinas para praticantes de CrossFit, Hyrox, ATHX e corrida. Avaliação biomecânica, retorno ao esporte e prevenção de lesões.",
        "h1": "Fisioterapia esportiva em Campinas para CrossFit, Hyrox e corrida",
        "lead": "Se você treina forte e tem uma dor que não passa, ou quer evitar a próxima lesão, a fisioterapia esportiva trabalha com as demandas do seu esporte. Eu avalio o seu movimento, a sua carga de treino e o seu histórico de lesões.",
        "wa": "Olá! Gostaria de agendar uma avaliação de fisioterapia esportiva.",
        "secoes": [
            ("Para quem é", """<ul>
<li>Praticantes de <strong>CrossFit</strong>, funcional e musculação com dor ou limitação em algum movimento.</li>
<li>Atletas e amadores de <strong>Hyrox</strong> e <strong>ATHX</strong> que combinam corrida e estações de força e querem chegar à prova bem preparados.</li>
<li><strong>Corredores</strong> de rua com dores recorrentes no joelho, na canela, no tornozelo ou no quadril.</li>
<li>Quem está <strong>voltando de lesão ou cirurgia</strong> e quer um retorno com critérios claros.</li>
</ul>"""),
            ("O que a avaliação esportiva inclui", """<p>Além do exame clínico, avalio os movimentos do seu esporte: agachar, correr, saltar, puxar, empurrar e levantar carga acima da cabeça. Medimos força, assimetrias entre os lados, mobilidade e controle do movimento. Também olhamos a sua programação de treino: volume, intensidade, descanso e o que mudou nas semanas antes de a dor começar.</p>
<p>Com isso, monto um plano que combina tratamento da queixa, exercícios específicos e ajustes no treino. O objetivo é que você continue treinando da melhor forma possível durante o processo, quando o seu caso permitir.</p>"""),
            ("Retorno ao esporte e prevenção", """<p>O retorno ao treino é planejado em etapas, com testes funcionais de força, saltos e agilidade e com progressão de carga. A prevenção de lesões não é uma garantia, mas treinar com boa preparação física, carga bem distribuída e recuperação adequada diminui os riscos. Conheça também a <a href="/ferrari-recovery-campinas/">Ferrari Recovery</a>, com bota de compressão e banheira de gelo para a recuperação pós-treino.</p>"""),
            ("Preparação para provas", """<p>Se você tem uma prova de Hyrox, ATHX ou corrida no calendário, uma avaliação preventiva antes do período mais intenso de treino pode apontar pontos fracos e déficits que merecem atenção. Leia também: <a href="/blog/hyrox-prevencao-de-lesoes/">Hyrox: como treinar sem se lesionar</a>.</p>"""),
        ],
        "faq": [
            ("Preciso estar lesionado para marcar?", "Não. Muitos atletas fazem uma avaliação preventiva, para identificar déficits de força, mobilidade ou assimetrias antes que virem dor."),
            ("Você entende de CrossFit e Hyrox?", "Sim. Eu acompanho o esporte, conheço os movimentos e as demandas das provas e converso com o seu treinador, se você quiser, para alinhar a volta ao treino."),
            ("Atende fora da clínica?", "Sim. Há atendimento no Instituto Adara e a domicílio, no Swiss Park e na região metropolitana de Campinas."),
        ],
        "rel": ["fisioterapia-ombro-campinas", "fisioterapia-joelho-tornozelo-campinas", "ferrari-recovery-campinas"],
    },
    {
        "slug": "fisioterapia-home-care-campinas",
        "menu": "Fisioterapia home care",
        "resumo": "Atendimento domiciliar no Swiss Park e região de Campinas.",
        "title": "Fisioterapia Home Care em Campinas e Swiss Park | Ed Ferrari Jr",
        "desc": "Fisioterapia domiciliar em Campinas e no Swiss Park: avaliação e reabilitação ortopédica e esportiva na sua casa, com privacidade e conforto.",
        "h1": "Fisioterapia home care em Campinas e Swiss Park",
        "lead": "Reabilitação ortopédica e esportiva na sua casa, com o mesmo método de avaliação que uso no consultório. Indicada para quem tem pouco tempo, está em pós-operatório ou prefere mais privacidade.",
        "wa": "Olá! Gostaria de saber mais sobre o atendimento de fisioterapia home care.",
        "secoes": [
            ("Quando o home care faz sentido", """<ul>
<li>Pós-operatório recente, quando se deslocar é difícil.</li>
<li>Rotina corrida: o atendimento acontece no seu horário, sem deslocamento.</li>
<li>Preferência por mais privacidade e conforto.</li>
<li>Pessoas que querem fazer a reabilitação junto com o espaço de treino em casa.</li>
</ul>"""),
            ("Como funciona", """<p>Levo os equipamentos portáteis necessários para a avaliação e para os exercícios. A primeira sessão inclui a avaliação completa, a definição do plano e a orientação sobre o que fazer entre as sessões. Podemos usar o espaço da sua casa ou condomínio, como sala, academia e quintal.</p>
<p>Atendo no <strong>Swiss Park</strong> e na região metropolitana de Campinas. Fale pelo WhatsApp para confirmar se o seu endereço está na área de atendimento.</p>"""),
            ("O que posso tratar em casa", """<p>Dores e lesões do ombro, joelho, tornozelo e coluna, lesões musculares, reabilitação pós-cirúrgica e preparação física terapêutica. Quando um caso exige estrutura que só existe na clínica, indico o <strong>Instituto Adara</strong>, onde também atendo.</p>"""),
        ],
        "faq": [
            ("Qual a área de atendimento?", "Swiss Park e a região metropolitana de Campinas. Envie o seu bairro pelo WhatsApp para confirmar."),
            ("O atendimento domiciliar tem a mesma qualidade do da clínica?", "A avaliação e o método são os mesmos. Em casos que exigem equipamentos específicos da clínica, combinamos sessões no Instituto Adara."),
            ("Tem reembolso pelo convênio?", "Eu forneço recibo e relatório para você solicitar o reembolso. A cobertura depende do seu plano."),
        ],
        "rel": ["fisioterapia-reembolso-convenio-campinas", "fisioterapia-coluna-campinas", "fisioterapia-esportiva-campinas"],
    },
    {
        "slug": "fisioterapia-reembolso-convenio-campinas",
        "menu": "Reembolso do convênio",
        "resumo": "Como funciona o reembolso de fisioterapia pelo plano de saúde.",
        "title": "Fisioterapia Particular com Reembolso do Convênio em Campinas | Ed Ferrari Jr",
        "desc": "Entenda como funciona o reembolso de fisioterapia pelo plano de saúde: recibo, relatório e documentos para solicitar em Campinas.",
        "h1": "Fisioterapia com reembolso do convênio em Campinas",
        "lead": "Muitos planos de saúde reembolsam parte das sessões de fisioterapia feitas fora da rede credenciada. Eu forneço a documentação necessária para você fazer a solicitação.",
        "wa": "Olá! Gostaria de entender como funciona o reembolso do convênio na fisioterapia.",
        "secoes": [
            ("Como funciona na prática", """<ol>
<li>Você faz a avaliação e as sessões de forma particular.</li>
<li>Eu emito o <strong>recibo</strong> de cada sessão e, quando o plano pede, um <strong>relatório</strong> com a avaliação e a evolução.</li>
<li>Você envia os documentos ao seu plano pelo aplicativo ou site, seguindo as regras dele.</li>
<li>O plano analisa e, se houver cobertura, reembolsa o valor conforme o seu contrato.</li>
</ol>"""),
            ("O que varia de plano para plano", """<p>Cada plano tem as suas regras: percentual ou tabela de reembolso, limite de sessões, necessidade de pedido médico e prazo para solicitar. Por isso, vale conferir com o seu plano antes de começar. Eu ajudo a organizar o relatório com as informações que o plano costuma pedir, mas não posso garantir o reembolso, pois a decisão é do plano.</p>"""),
            ("Documentos que costumam ser pedidos", """<ul>
<li>Pedido ou indicação médica, quando exigido pelo plano.</li>
<li>Recibo com dados do profissional e do registro no CREFITO.</li>
<li>Relatório fisioterapêutico com diagnóstico funcional e plano de tratamento.</li>
<li>Formulário de reembolso do próprio plano.</li>
</ul>"""),
        ],
        "faq": [
            ("Você é credenciado a convênios?", "O atendimento é particular. Eu forneço a documentação para você solicitar o reembolso diretamente ao seu plano."),
            ("O reembolso é garantido?", "Não. Quem define a cobertura e o valor é o seu plano, de acordo com o contrato."),
            ("Posso pedir o relatório depois das sessões?", "Sim. Peça pelo WhatsApp e eu preparo o relatório com a evolução do seu tratamento."),
        ],
        "rel": ["fisioterapia-home-care-campinas", "fisioterapia-ombro-campinas", "fisioterapia-coluna-campinas"],
    },
    {
        "slug": "ferrari-recovery-campinas",
        "menu": "Ferrari Recovery",
        "resumo": "Bota de compressão e banheira de gelo para recuperação pós-treino.",
        "title": "Ferrari Recovery: Aluguel de Bota de Compressão e Banheira de Gelo em Campinas",
        "desc": "Aluguel de bota de compressão pneumática e banheira de gelo (ice bath) para recuperação pós-treino em Campinas e Swiss Park. Fale pelo WhatsApp.",
        "h1": "Ferrari Recovery: bota de compressão e banheira de gelo em Campinas",
        "lead": "Equipamentos de recuperação usados por atletas, disponíveis para locação por diária no Swiss Park e região. Para quem treina forte e quer incluir um protocolo de recuperação na rotina.",
        "wa": "Olá! Gostaria de informações sobre a Ferrari Recovery (bota de compressão e banheira de gelo).",
        "secoes": [
            ("O que oferecemos", """<div class="s-grid">
<div class="s-card"><img src="/assets/img/image_11.webp" alt="Bota de compressão pneumática" width="500" height="500" loading="lazy" style="width:100%;height:220px;object-fit:cover;margin-bottom:14px"><h3>Bota de compressão pneumática</h3><p>Equipamento de compressão sequencial nas pernas, usado após treinos e provas como parte da rotina de recuperação. A sensação costuma ser de alívio e leveza, mas a resposta varia de pessoa para pessoa.</p></div>
<div class="s-card"><img src="/assets/img/image_12.webp" alt="Banheira de gelo para imersão" width="1024" height="1024" loading="lazy" style="width:100%;height:220px;object-fit:cover;margin-bottom:14px"><h3>Banheira de gelo (ice bath)</h3><p>Imersão em água fria, usada por muitos atletas após esforços intensos. O protocolo de temperatura e de tempo é orientado por mim, e há contraindicações que avalio com você antes.</p></div>
<div class="s-card"><h3>Combo fim de semana</h3><p>Bota e banheira por dois dias, para quem tem prova ou treino pesado no fim de semana.</p></div>
</div>"""),
            ("Como funciona", """<p>Você entra em contato pelo WhatsApp, conta o seu treino ou evento e eu envio os valores e a disponibilidade. Combinamos a entrega, a retirada e a orientação de uso. Como o uso depende da sua condição de saúde, faço algumas perguntas antes, como condições cardiovasculares, circulatórias ou de sensibilidade ao frio.</p>"""),
            ("Tem um evento esportivo?", """<p>Organiza uma corrida, uma competição de CrossFit, Hyrox ou ATHX? A Ferrari Recovery também monta uma estação de recuperação no seu evento, com bota, banheira de gelo e fisioterapeuta no local. <a href="/recovery-para-eventos-esportivos/">Veja como funciona e peça uma proposta</a>.</p>"""),
            ("Importante", """<p>Bota e banheira de gelo são recursos de recuperação e conforto. Não substituem a avaliação de uma dor persistente ou de uma lesão. Se você sente dor que não melhora, marque uma <a href="/fisioterapia-esportiva-campinas/">avaliação de fisioterapia esportiva</a>.</p>"""),
        ],
        "faq": [
            ("Quanto custa?", "Os valores variam conforme o equipamento e o período. Fale pelo WhatsApp e eu envio na hora."),
            ("Quem não deve usar a banheira de gelo?", "Pessoas com certas condições cardiovasculares, circulatórias ou sensibilidade ao frio devem conversar comigo e com o médico antes. Faço essa triagem antes da locação."),
            ("A bota de compressão serve para quê?", "É usada como recurso de recuperação após treinos e provas. Ela não trata lesões."),
        ],
        "rel": ["recovery-para-eventos-esportivos", "fisioterapia-esportiva-campinas", "fisioterapia-lesoes-musculares-campinas"],
    },
    {
        "slug": "recovery-para-eventos-esportivos",
        "menu": "Recovery em eventos",
        "resumo": "Estação de recuperação com bota, banheira de gelo e fisioterapeuta para o seu evento.",
        "title": "Recovery para Evento Esportivo em Campinas: Bota, Banheira de Gelo e Fisioterapeuta",
        "desc": "Leve a Ferrari Recovery ao seu evento de corrida, CrossFit, Hyrox ou ATHX: bota de compressão, banheira de gelo e fisioterapeuta no local. Peça uma proposta pelo WhatsApp.",
        "h1": "Leve a Ferrari Recovery para o seu evento esportivo",
        "lead": "Uma estação de recuperação montada no seu evento, com bota de compressão, banheira de gelo e fisioterapeuta no local. Um diferencial para quem compete e uma experiência a mais para quem organiza.",
        "wa": "Olá! Organizo um evento esportivo e gostaria de uma proposta para levar a Ferrari Recovery até ele.",
        "btn": "Pedir proposta para o meu evento",
        "cta": ("Peça uma proposta para o seu evento", "Conte o nome do evento, a data, o local, o esporte e quantos atletas participam. Eu respondo com a proposta."),
        "secoes": [
            ("Para quem é", """<p>Para organizadores de corridas, competições de CrossFit, Hyrox, ATHX e outros eventos de performance que querem oferecer recuperação a quem participa. A Ferrari Recovery pode ser o recovery oficial do seu evento.</p>
<div class="s-grid">
<div class="s-card"><span class="s-num">CORRIDA</span><h3>Provas de rua e de trilha</h3><p>Recuperação na chegada, quando o atleta mais procura um lugar para parar e se recuperar.</p></div>
<div class="s-card"><span class="s-num">CROSSFIT</span><h3>Competições e campeonatos</h3><p>Para quem faz várias baterias no mesmo dia ou no fim de semana e precisa voltar à próxima prova.</p></div>
<div class="s-card"><span class="s-num">HYROX</span><h3>Provas de Hyrox</h3><p>Pernas, ombros e costas muito exigidos em uma prova longa e intensa.</p></div>
<div class="s-card"><span class="s-num">ATHX</span><h3>Eventos de ATHX</h3><p>Estrutura de recuperação para atletas que competem em formatos híbridos de alta demanda.</p></div>
</div>"""),
            ("O que a estação do evento inclui", """<div class="s-grid">
<div class="s-card"><h3>Bota de compressão pneumática</h3><p>Compressão sequencial nas pernas, usada após o esforço como parte da rotina de recuperação.</p></div>
<div class="s-card"><h3>Banheira de gelo (ice bath)</h3><p>Imersão em água fria para quem gosta desse recurso depois da prova, com tempo e temperatura orientados no local.</p></div>
<div class="s-card"><h3>Fisioterapeuta no local</h3><p>Eu faço a triagem de quem pode usar cada recurso, oriento o tempo de uso e converso com o atleta sobre a recuperação. Conforme o evento, também é possível combinar terapia manual, alongamento e avaliação rápida com o fisioterapeuta. Quem relata dor que pede avaliação é orientado a procurar atendimento.</p></div>
</div>"""),
            ("Por que ter um fisioterapeuta na estação", """<p>Bota e banheira de gelo são ótimos recursos, mas nem todo mundo deve usá-los do mesmo jeito. Condições cardiovasculares, circulatórias ou de sensibilidade ao frio, por exemplo, pedem cuidado. Com um fisioterapeuta na estação, a triagem é feita antes do uso e a orientação é individual, o que torna a experiência mais segura e mais profissional para o atleta e para a imagem do seu evento.</p>"""),
            ("Como funciona", """<ol>
<li>Você entra em contato pelo WhatsApp com o nome do evento, a data, o local, o esporte e uma estimativa do número de participantes.</li>
<li>Eu respondo com a proposta, a estrutura necessária no local (ambiente coberto e apto, com energia e acesso à água) e os valores.</li>
<li>Combinamos montagem, horários de funcionamento e como os atletas vão acessar a estação.</li>
<li>No dia, a estação funciona com a minha presença e você acompanha tudo com a nossa equipe.</li>
</ol>"""),
            ("Importante", """<p>A estação é de recuperação e conforto. Ela não substitui a avaliação de uma dor persistente ou de uma lesão. Os valores e o formato dependem do evento, e a proposta é feita caso a caso.</p>"""),
        ],
        "faq": [
            ("Quanto custa levar a Ferrari Recovery ao meu evento?", "Depende do formato, da duração e do número de participantes. Mande os dados do evento pelo WhatsApp e eu envio uma proposta."),
            ("O que preciso oferecer no local?", "Um ambiente coberto e apto para a Ferrari Recovery operar, com energia para as botas e acesso à água para a banheira. Confirmo os detalhes de cada evento na proposta."),
            ("Quantos equipamentos levam para o evento?", "A quantidade de botas e banheiras é negociada de acordo com o tamanho do evento e o fluxo de atletas, e a proposta é feita caso a caso."),
            ("Os atletas pagam para usar ou o organizador contrata?", "Os dois formatos são possíveis. Podemos montar a estação contratada pelo organizador ou com acesso pago pelo atleta. Combinamos o que fizer mais sentido para o seu evento."),
            ("Funciona para evento pequeno?", "Sim. Conte o tamanho do evento pelo WhatsApp e eu indico o que cabe."),
            ("Quem não deve usar a banheira de gelo?", "Pessoas com certas condições cardiovasculares, circulatórias ou sensibilidade ao frio devem passar pela triagem do fisioterapeuta antes e, em alguns casos, conversar com o médico."),
        ],
        "rel": ["ferrari-recovery-campinas", "fisioterapia-esportiva-campinas", "fisioterapia-lesoes-musculares-campinas"],
    },
]

ARTIGOS = [
    {
        "slug": "dor-no-ombro-crossfit",
        "title": "Dor no ombro no CrossFit: sinais de que vale uma avaliação",
        "desc": "Dor no ombro em movimentos acima da cabeça é comum no CrossFit. Veja causas frequentes, o que pode ajudar e quando procurar um fisioterapeuta.",
        "h1": "Dor no ombro no CrossFit: sinais de que vale uma avaliação",
        "lead": "O ombro é uma das regiões mais exigidas no CrossFit. Nem toda dor significa lesão, mas alguns sinais merecem atenção.",
        "servico": "fisioterapia-ombro-campinas",
        "corpo": """<h2>Por que o ombro sofre tanto</h2>
<p>O ombro é a articulação mais móvel do corpo e depende muito dos músculos para ficar estável. No CrossFit ele é exigido em movimentos acima da cabeça (overhead, snatch, thruster), em barras e argolas e em empurrar e puxar com carga. Quando o volume sobe rápido, a técnica falha por cansaço ou o ombro tem pouca mobilidade, a região pode ficar sobrecarregada.</p>
<h2>Causas comuns de dor</h2>
<ul>
<li>Sobrecarga dos tendões do manguito rotador.</li>
<li>Pouca mobilidade do ombro ou da coluna torácica, que leva a compensações.</li>
<li>Aumento rápido de volume de ginásticos, como kipping, toes to bar e muscle up.</li>
<li>Fraqueza dos músculos que estabilizam a escápula.</li>
<li>Lesões antigas que nunca foram reabilitadas.</li>
</ul>
<h2>Sinais de que vale uma avaliação</h2>
<ul>
<li>A dor dura mais de uma ou duas semanas.</li>
<li>Dói à noite ou ao deitar sobre o ombro.</li>
<li>Você perdeu força ou amplitude de movimento.</li>
<li>A dor aparece sempre no mesmo movimento.</li>
<li>Há formigamento no braço ou na mão.</li>
</ul>
<h2>O que você pode fazer enquanto isso</h2>
<p>Reduza o volume dos movimentos que doem, procure variações que não pioram os sintomas e mantenha o resto do treino. Evite insistir na carga com dor que piora a cada repetição. Se a dor não melhorar em poucos dias, uma avaliação identifica o que está acontecendo e orienta o que manter e o que ajustar.</p>
<p>Se houver trauma, deformidade, perda súbita de força ou dor muito intensa, procure atendimento médico.</p>""",
    },
    {
        "slug": "dor-no-joelho-corrida",
        "title": "Dor no joelho na corrida: por que acontece e quando investigar",
        "desc": "Dor no joelho é uma das queixas mais comuns entre corredores. Entenda causas frequentes, o papel da carga de treino e quando buscar fisioterapia.",
        "h1": "Dor no joelho na corrida: por que acontece e quando investigar",
        "lead": "Dor no joelho é uma queixa comum em quem corre. Na maioria das vezes ela tem relação com a carga de treino, e não com uma lesão grave.",
        "servico": "fisioterapia-joelho-tornozelo-campinas",
        "corpo": """<h2>A carga de treino conta muito</h2>
<p>O joelho absorve força a cada passada. Quando o volume ou a intensidade sobem rápido, como em semanas com muitos quilômetros, aumento de tiros ou de subidas, os tecidos podem não ter tempo de se adaptar. Mudar de tênis, de piso ou voltar de uma pausa longa também pode contribuir.</p>
<h2>Causas frequentes</h2>
<ul>
<li><strong>Dor patelofemoral:</strong> dor na frente do joelho, que piora ao descer escadas, agachar ou ficar sentado por muito tempo.</li>
<li><strong>Síndrome da banda iliotibial:</strong> dor na parte lateral do joelho, que costuma aparecer após certa distância.</li>
<li><strong>Tendinopatia patelar:</strong> dor logo abaixo da patela, mais comum em quem salta ou faz muito agachamento.</li>
<li><strong>Lesões de menisco ou ligamento:</strong> costumam vir de torção ou trauma e podem causar inchaço, travamento ou sensação de falseio.</li>
</ul>
<h2>Quando procurar avaliação</h2>
<ul>
<li>A dor persiste por mais de uma ou duas semanas ou piora a cada treino.</li>
<li>Há inchaço, travamento ou a sensação de que o joelho cede.</li>
<li>Você sentiu um estalo seguido de dor após uma torção.</li>
<li>A dor muda a sua forma de correr ou de caminhar.</li>
</ul>
<h2>O que pode ajudar</h2>
<p>Reduza temporariamente o volume e evite aumentar quilometragem e intensidade ao mesmo tempo. Fortalecimento de quadril, coxa e panturrilha faz parte da reabilitação de muitos corredores. A avaliação mostra quais são os seus pontos fracos e como adaptar o treino sem parar de correr, quando for possível.</p>
<p>Em caso de trauma importante, incapacidade de apoiar o pé ou inchaço grande, procure atendimento médico.</p>""",
    },
    {
        "slug": "hyrox-prevencao-de-lesoes",
        "title": "Hyrox: como treinar sem se lesionar",
        "desc": "O Hyrox combina corrida e estações de força. Veja onde costumam surgir as dores, como organizar a carga de treino e quando fazer uma avaliação preventiva.",
        "h1": "Hyrox: como treinar sem se lesionar",
        "lead": "O Hyrox junta 8 km de corrida com 8 estações de força e resistência. A mistura é divertida, e também exige atenção à carga e à recuperação.",
        "servico": "fisioterapia-esportiva-campinas",
        "corpo": """<h2>O que a prova exige do corpo</h2>
<p>A prova alterna corrida com estações como SkiErg, sled push, sled pull, burpee broad jump, remo, farmer's carry, sandbag lunges e wall balls. Isso significa muito volume de corrida combinado com esforço de pernas, ombros, costas e pegada. Sem uma preparação adequada, essa combinação pode sobrecarregar as articulações e os tendões.</p>
<h2>Regiões que costumam reclamar</h2>
<ul>
<li><strong>Joelhos e tornozelos:</strong> pelo volume de corrida e por afundos com carga.</li>
<li><strong>Costas:</strong> por cargas carregadas, remo e burpees repetidos.</li>
<li><strong>Ombros:</strong> em wall balls e SkiErg com muitas repetições.</li>
<li><strong>Panturrilhas e posteriores:</strong> pelo trabalho de propulsão no sled e na corrida.</li>
</ul>
<h2>Como organizar o treino</h2>
<ul>
<li>Aumente o volume de corrida e de estações de forma gradual, e não ambos de uma vez.</li>
<li>Inclua treino de força para pernas, costas e ombros ao longo da semana.</li>
<li>Reserve dias de descanso e semanas de carga reduzida.</li>
<li>Treine as estações com a técnica correta antes de aumentar a carga.</li>
<li>Durma bem e cuide da alimentação, pois a recuperação faz parte do treino.</li>
</ul>
<h2>Avaliação preventiva</h2>
<p>Se você tem uma prova marcada, uma avaliação antes do período mais pesado de treino pode apontar assimetrias de força, limitações de mobilidade e dores antigas que merecem atenção. Nenhuma estratégia garante que lesões não aconteçam, mas conhecer seus pontos fracos permite ajustar o treino com mais segurança.</p>""",
    },
    {
        "slug": "hyrox-tampa-2026-o-que-muda-para-quem-viaja",
        "data": "2026-10-21",
        "title": "Hyrox Tampa 2026: próxima etapa e cuidados para quem viaja para competir",
        "desc": "O Hyrox segue de São Paulo para Tampa, nos EUA, de 22 a 25 de outubro de 2026. Veja a data, o local e como viajar para competir sem chegar com o corpo cansado.",
        "h1": "Hyrox Tampa 2026: próxima etapa e cuidados para quem viaja para competir",
        "lead": "Depois de São Paulo, o circuito do Hyrox segue para Tampa, na Flórida, de 22 a 25 de outubro de 2026.",
        "servico": "fisioterapia-esportiva-campinas",
        "corpo": """<h2>O que está no calendário oficial</h2>
<p>A página oficial do evento, no <a href="https://hyrox.com/event/hyrox-tampa/" rel="noopener" target="_blank">site do Hyrox</a>, marca a etapa de Tampa, nos Estados Unidos, de 22 a 25 de outubro de 2026. Segundo as informações públicas do evento, a prova acontece no Tampa Convention Center, no centro da cidade.</p>
<p>No Brasil, a temporada 2026/2027 foi aberta em São Paulo, em 17 de outubro, no Distrito Anhembi, com provas individuais, em duplas e em revezamento, <a href="https://distritoanhembi.com.br/?p=16834" rel="noopener" target="_blank">segundo o próprio Distrito Anhembi</a>.</p>
<h2>Viajar para competir também cobra do corpo</h2>
<p>Voos longos e muitas horas sentado costumam sobrecarregar a lombar e o quadril, justamente as regiões que o Hyrox exige depois, com sled, carregadas e corrida. Quem chega à prova direto do aeroporto começa em desvantagem.</p>
<ul>
<li><strong>Chegue com dias de antecedência</strong> sempre que possível, para o corpo se ajustar ao fuso, ao clima e à rotina.</li>
<li><strong>Levante e caminhe</strong> durante o voo ou a viagem de carro, de tempos em tempos.</li>
<li><strong>Hidrate-se</strong> antes, durante e depois da viagem; o ambiente da prova pode ser quente e úmido.</li>
<li><strong>Não estreie nada</strong> na semana da prova: tênis, estratégia de ritmo, alimentação e suplementos devem ser os que você já usa nos treinos.</li>
<li><strong>Reduza o volume de treino</strong> na semana da competição, mantendo o movimento leve, em vez de tentar compensar a viagem.</li>
</ul>
<h2>E depois da prova</h2>
<p>O corpo ainda precisa de recuperação: sono, alimentação, hidratação e uma retomada gradual dos treinos. Dor que persiste por mais de uma ou duas semanas, ou que muda a forma como você se move, merece avaliação. Leia também <a href="/blog/hyrox-prevencao-de-lesoes/">Hyrox: como treinar sem se lesionar</a>.</p>
<p>Este texto é um resumo independente do calendário oficial e não tem vínculo com a organização do Hyrox. Confira sempre datas e regras no site oficial do evento.</p>""",
    },
]

# ---------------------------------------------------------------- templates
NAV = [
    ("/fisioterapia-esportiva-campinas/", "Esportiva", True),
    ("/fisioterapia-home-care-campinas/", "Home care", True),
    ("/ferrari-recovery-campinas/", "Recovery", True),
    ("/perito-assistente-tecnico-em-fisioterapia/", "Perícia", True),
    ("/blog/", "Blog", False),
]


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def head(title, desc, caminho, extra_ld, tipo="website", imagem="/assets/img/foto-sled.webp", robots="index, follow, max-image-preview:large"):
    url = f"{BASE}{caminho}"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{tipo}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Ed Ferrari Jr | Fisioterapia">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{BASE}{imagem}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/assets/fonts/BarlowCondensed-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/Barlow-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css">
<script>document.documentElement.classList.add('js')</script>
<script src="/assets/js/site.js" defer></script>
<script type="application/ld+json">{json.dumps(extra_ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
"""


def header():
    links = "".join(
        '<a href="%s"%s>%s</a>' % (h, ' class="hide-m"' if ocultar else "", t) for h, t, ocultar in NAV
    )
    return f"""<header class="s-header"><div class="s-wide">
<a class="s-brand" href="/"><b>Ed Ferrari Jr</b><small>FISIOTERAPIA · ESPORTIVA</small></a>
<input type="checkbox" id="mn" class="mn-chk" aria-label="Abrir menu"><label for="mn" class="mn-btn" aria-hidden="true"><i></i></label>
<nav class="s-nav" aria-label="Principal">{links}<a class="s-btn small" href="{wa('Olá! Gostaria de agendar uma avaliação.')}">Agendar</a></nav>
</div></header>
"""


def footer():
    servicos = "".join('<a href="/%s/">%s</a>' % (x["slug"], x["menu"]) for x in SERVICOS[:5])
    return f"""<footer class="s-footer"><div class="s-wide"><div class="cols">
<div><div class="assin">Ed Ferrari Jr<small>FISIOTERAPIA · ESPORTIVA</small></div>{CREFITO}<br><br>{ENDERECO}<br>WhatsApp: (19) 97100-2263</div>
<div><strong>Serviços</strong>{servicos}</div>
<div><strong>Mais</strong><a href="/fisioterapia-home-care-campinas/">Home care</a><a href="/fisioterapia-reembolso-convenio-campinas/">Reembolso do convênio</a><a href="/ferrari-recovery-campinas/">Ferrari Recovery</a><a href="/recovery-para-eventos-esportivos/">Recovery em eventos</a><a href="/perito-assistente-tecnico-em-fisioterapia/">Perícia e assistência técnica</a><a href="/blog/">Blog</a><a href="https://www.instagram.com/edferrarijr">Instagram</a><a href="https://www.youtube.com/@EdFerrariJr">YouTube</a></div>
</div>
<p class="s-note" style="margin-top:30px">As informações deste site são educativas e não substituem a avaliação de um profissional de saúde. Os resultados variam de pessoa para pessoa. © 2026 Ed Ferrari Jr.</p>
</div></footer>
<a class="barra-cta" href="{wa('Olá! Gostaria de agendar uma avaliação.')}">Agendar pelo WhatsApp</a>
</body>
</html>
"""


def cta(texto_wa, titulo="Agende sua avaliação", sub="Instituto Adara (Swiss Park) e em domicílio, em Campinas e região."):
    return f"""<section class="s-cta"><span class="rotulo">Atendimento em Campinas</span><h2>{titulo}</h2><p>{sub}</p>
<a class="s-btn" href="{wa(texto_wa)}">Falar pelo WhatsApp</a></section>
"""


def faq_html(faq):
    itens = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    return f'<h2>Perguntas frequentes</h2><div class="s-faq">{itens}</div>'


def faq_ld(faq):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq
        ],
    }


def crumbs_ld(itens):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{BASE}{c}"} for i, (n, c) in enumerate(itens)
        ],
    }


def crumbs_html(itens):
    partes = [f'<a href="{c}">{n}</a>' for n, c in itens[:-1]] + [itens[-1][0]]
    return '<div class="s-crumb">' + " › ".join(partes) + "</div>"


FOTOS = {
    "fisioterapia-ombro-campinas": ("foto-overhead", "Atleta com barra acima da cabeça", "50% 22%"),
    "fisioterapia-joelho-tornozelo-campinas": ("foto-afundo", "Praticante fazendo afundo ao ar livre", "50% 35%"),
    "fisioterapia-lesoes-musculares-campinas": ("foto-costas", "Atleta de costas durante treino de sled", "50% 45%"),
    "fisioterapia-coluna-campinas": ("foto-alongamento", "Praticante se alongando à beira de um píer", "50% 40%"),
    "recovery-para-eventos-esportivos": ("foto-sled", "Atleta durante prova de sled push", "50% 40%"),
    "fisioterapia-esportiva-campinas": ("foto-corrida", "Corredor em movimento", "50% 40%"),
}


def foto_html(s):
    f = FOTOS.get(s["slug"])
    if not f:
        return ""
    return f'<div class="s-foto"><img src="/assets/img/{f[0]}.webp" alt="{f[1]}" style="object-position:{f[2]}" width="1100" height="470" loading="eager"></div>'


def pagina_servico(s):
    caminho = f"/{s['slug']}/"
    migalhas = [("Início", "/"), (s["menu"], caminho)]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "MedicalWebPage",
                "@id": f"{BASE}{caminho}#pagina",
                "url": f"{BASE}{caminho}",
                "name": s["title"],
                "description": s["desc"],
                "inLanguage": "pt-BR",
                "dateModified": DATA,
                "about": {"@type": "MedicalSpecialty", "name": "Physiotherapy"},
                "author": {"@id": f"{BASE}/#pessoa"},
                "publisher": {"@id": f"{BASE}/#clinica"},
            },
            crumbs_ld(migalhas),
            faq_ld(s["faq"]),
        ],
    }
    corpo = "".join(f"<h2>{t}</h2>{h}" for t, h in s["secoes"])
    rel = "".join(
        f'<a class="s-card" href="/{r["slug"]}/"><span class="s-num">SERVIÇO</span><h3>{r["menu"]}</h3><p>{r["resumo"]}</p></a>'
        for r in SERVICOS
        if r["slug"] in s["rel"]
    )
    artigos_rel = "".join(
        f'<a class="s-card" href="/blog/{a["slug"]}/"><h3>{a["h1"]}</h3><p>{a["lead"]}</p></a>'
        for a in ARTIGOS
        if a["servico"] == s["slug"]
    )
    html = head(s["title"], s["desc"], caminho, ld) + header()
    html += f"""<main id="conteudo" class="s-main"><div class="s-wrap">
{crumbs_html(migalhas)}
<section class="s-hero"><span class="rotulo">{CREFITO} · Campinas</span><div class="regua"></div><h1>{s['h1']}</h1><p class="lead">{s['lead']}</p>
<a class="s-btn" href="{wa(s['wa'])}">{s.get('btn', 'Agendar avaliação')}</a></section>
{foto_html(s)}
{corpo}
{faq_html(s['faq'])}
{cta(s['wa'], *s.get('cta', ()))}
<h2>Veja também</h2><div class="s-grid">{rel}{artigos_rel}</div>
</div></main>
"""
    return caminho, html + footer()


def pagina_artigo(a):
    caminho = f"/blog/{a['slug']}/"
    serv = next(s for s in SERVICOS if s["slug"] == a["servico"])
    migalhas = [("Início", "/"), ("Blog", "/blog/"), (a["h1"], caminho)]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "@id": f"{BASE}{caminho}#artigo",
                "headline": a["h1"],
                "description": a["desc"],
                "inLanguage": "pt-BR",
                "datePublished": a.get("data", DATA),
                "dateModified": a.get("data", DATA),
                "mainEntityOfPage": f"{BASE}{caminho}",
                "image": f"{BASE}/assets/img/foto-sled.webp",
                "author": {"@id": f"{BASE}/#pessoa"},
                "publisher": {"@id": f"{BASE}/#clinica"},
            },
            crumbs_ld(migalhas),
        ],
    }
    texto_wa = f"Olá! Li o artigo \"{a['h1']}\" e gostaria de agendar uma avaliação."
    html = head(a["title"], a["desc"], caminho, ld, "article") + header()
    html += f"""<main id="conteudo" class="s-main"><div class="s-wrap">
{crumbs_html(migalhas)}
<section class="s-hero"><span class="rotulo">Blog</span><div class="regua"></div><h1>{a['h1']}</h1><p class="lead">{a['lead']}</p>
<p class="s-meta">Por Ed Ferrari Jr, fisioterapeuta ({CREFITO}) · Atualizado em {a.get('data', DATA)[8:10]}/{a.get('data', DATA)[5:7]}/{a.get('data', DATA)[:4]}</p></section>
{a['corpo']}
{cta(texto_wa, "Quer uma avaliação individual?")}
<p>Saiba mais sobre <a href="/{serv['slug']}/">{serv['menu'].lower()}</a> e sobre a <a href="/fisioterapia-esportiva-campinas/">fisioterapia esportiva em Campinas</a>.</p>
<p class="s-note">Este conteúdo é informativo e não substitui a consulta com um profissional de saúde. Cada caso exige avaliação individual.</p>
</div></main>
"""
    return caminho, html + footer()


def pagina_blog():
    caminho = "/blog/"
    titulo = "Blog de Fisioterapia Esportiva e Ortopédica | Ed Ferrari Jr, Campinas"
    desc = "Artigos sobre dor no ombro, joelho, coluna, corrida, CrossFit e Hyrox, escritos pelo fisioterapeuta Ed Ferrari Jr."
    migalhas = [("Início", "/"), ("Blog", caminho)]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": f"{BASE}{caminho}#pagina", "url": f"{BASE}{caminho}", "name": titulo, "description": desc, "inLanguage": "pt-BR"},
        crumbs_ld(migalhas)]}
    cards = "".join(
        f'<a class="s-card" href="/blog/{a["slug"]}/"><h3>{a["h1"]}</h3><p>{a["lead"]}</p></a>' for a in ARTIGOS
    )
    html = head(titulo, desc, caminho, ld) + header()
    html += f"""<main id="conteudo" class="s-main"><div class="s-wrap">
{crumbs_html(migalhas)}
<section class="s-hero"><span class="rotulo">Blog</span><div class="regua"></div><h1>Fisioterapia esportiva e ortopédica na prática</h1><p class="lead">Conteúdo para quem treina e quer entender melhor a dor, a recuperação e o retorno ao esporte.</p></section>
<div class="s-grid">{cards}</div>
{cta("Olá! Gostaria de agendar uma avaliação.")}
</div></main>
"""
    return caminho, html + footer()


HOME_FAQ = [
    ("Onde você atende em Campinas?", "No Instituto Adara, no Swiss Park (Av. Antônio Artioli, 276), e em domicílio no Swiss Park e na região metropolitana de Campinas."),
    ("Preciso de pedido médico para marcar uma avaliação?", "Para a avaliação fisioterapêutica não é obrigatório. Se você tem exames ou laudos, traga para a primeira sessão. Alguns convênios pedem o pedido médico para reembolso."),
    ("Você atende atletas de CrossFit, Hyrox e corrida?", "Sim. Faço avaliação do movimento e da carga de treino, tratamento das lesões e plano de retorno ao esporte."),
    ("Como funciona o reembolso do convênio?", "O atendimento é particular. Eu forneço recibo e relatório para você solicitar o reembolso ao seu plano. A cobertura depende do contrato."),
]


TICKER = "".join("<span>%s</span>" % x for x in ["Ombro", "Joelho", "Tornozelo", "Coluna", "Lesões musculares", "Hyrox", "CrossFit", "ATHX", "Corrida", "Home care", "Recovery"]) * 2


def pagina_home():
    titulo = "Fisioterapeuta Esportivo e Ortopédico em Campinas | Ed Ferrari Jr"
    desc = "Fisioterapia ortopédica e esportiva em Campinas: ombro, joelho, coluna e lesões musculares. Atendimento no Instituto Adara (Swiss Park) e home care. Agende sua avaliação."
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Physiotherapy", "@id": f"{BASE}/#clinica", "name": "Ed Ferrari Jr. Fisioterapia Ortopédica e Esportiva", "url": f"{BASE}/",
         "image": f"{BASE}/assets/img/foto-sled.webp", "telephone": "+5519971002263",
         "address": {"@type": "PostalAddress", "streetAddress": "Av. Antônio Artioli, 276", "addressLocality": "Campinas", "addressRegion": "SP", "postalCode": "13049-253", "addressCountry": "BR"},
         "areaServed": [{"@type": "City", "name": "Campinas"}, {"@type": "Place", "name": "Swiss Park"}],
         "medicalSpecialty": "Physiotherapy", "sameAs": ["https://www.instagram.com/edferrarijr", "https://www.youtube.com/@EdFerrariJr"], "founder": {"@id": f"{BASE}/#pessoa"}},
        {"@type": "Person", "@id": f"{BASE}/#pessoa", "name": "Ed Ferrari Jr", "jobTitle": "Fisioterapeuta ortopédico e esportivo", "identifier": CREFITO, "url": f"{BASE}/", "worksFor": {"@id": f"{BASE}/#clinica"}},
        {"@type": "WebSite", "@id": f"{BASE}/#site", "url": f"{BASE}/", "name": "Ed Ferrari Jr | Fisioterapia", "inLanguage": "pt-BR"},
        faq_ld(HOME_FAQ)]}
    cards = "".join(
        f'<a class="s-card" href="/{x["slug"]}/"><span class="s-num">{i:02d}</span><h3>{x["menu"]}</h3><p>{x["resumo"]}</p></a>'
        for i, x in enumerate(SERVICOS, 1))
    blog = "".join(f'<a class="s-card" href="/blog/{a["slug"]}/"><span class="s-num">BLOG</span><h3>{a["h1"]}</h3><p>{a["lead"]}</p></a>' for a in ARTIGOS[:3])
    h = head(titulo, desc, "/", ld) + header()
    h += f"""<main id="conteudo">
<section class="h-hero"><video class="fundo" autoplay muted loop playsinline preload="metadata" poster="/assets/img/foto-sled.webp" aria-hidden="true"><source src="/assets/video/hero.mp4" type="video/mp4"></video><div class="s-wide">
<span class="rotulo">Campinas · Instituto Adara e home care</span><div class="regua"></div>
<h1><span class="destaque">Fisioterapia</span> ortopédica e esportiva em Campinas</h1>
<p class="lead">Avaliação individual e reabilitação baseada em evidências, no Instituto Adara (Swiss Park) ou na sua casa.</p>
<div class="acoes"><a class="s-btn" href="{wa('Olá! Vim pelo site e gostaria de agendar uma avaliação.')}">Agendar minha avaliação</a><a class="s-btn vazado" href="#servicos">Ver serviços</a></div>
</div></section>
<div class="h-faixa"><div class="s-wide"><span>Tratamento baseado em evidências</span><span>Avaliação individual</span><span>Minimizando lesões</span><span>{CREFITO}</span></div></div>
<div class="ticker" aria-hidden="true"><div>{TICKER}</div></div>

<section class="h-sec"><div class="s-wide h-sobre">
<img src="/assets/img/image_1.webp" alt="Ed Ferrari Jr, fisioterapeuta" width="600" height="800" loading="lazy">
<div><span class="rotulo">Quem cuida de você</span><h2>Chega de tratamentos genéricos.</h2>
<p>Muitas vezes o tratamento se limita a aliviar o sintoma. Como especialista em ortopedia e fisioterapia esportiva, eu investigo a <strong>raiz biomecânica</strong> da sua dor articular, muscular ou ligamentar.</p>
<p>Meu compromisso é com a sua independência: um plano de eficiência máxima, com o menor número de visitas possível, para você voltar a treinar e viver sem medo.</p></div>
</div></section>

<section class="h-sec" id="servicos" style="padding-top:0"><div class="s-wide"><span class="rotulo">Serviços</span><h2>Cuidado individualizado para cada região do corpo.</h2>
<div class="s-grid">{cards}</div></div></section>

<section class="h-sec escura"><div class="s-wide"><span class="rotulo">Para quem treina</span><h2>CrossFit, Hyrox, ATHX e corrida.</h2>
<p style="max-width:640px">Conheço as demandas do seu esporte. Avalio o movimento e a carga de treino, trato a lesão e planejo o retorno com critérios claros.</p>
<div class="h-esportes"><a href="/fisioterapia-esportiva-campinas/" style="color:#F4F4F1;border-color:#F4F4F1">Hyrox</a><a href="/fisioterapia-esportiva-campinas/" style="color:#F4F4F1;border-color:#F4F4F1">CrossFit</a><a href="/fisioterapia-esportiva-campinas/" style="color:#F4F4F1;border-color:#F4F4F1">ATHX</a><a href="/fisioterapia-esportiva-campinas/" style="color:#F4F4F1;border-color:#F4F4F1">Corrida</a></div>
<a class="s-btn" href="/fisioterapia-esportiva-campinas/">Fisioterapia esportiva</a></div></section>

<section class="h-sec"><div class="s-wide"><span class="rotulo">Ferrari Recovery</span><h2>Recuperação pós-treino. Na sua casa.</h2>
<p class="suave" style="max-width:640px">Aluguel de equipamentos de recuperação pós-treino no Swiss Park e região. Valores sob consulta, pelo WhatsApp.</p>
<div class="h-duo">
<div class="s-card"><span class="s-num">01</span><h3>Bota pneumática</h3><p>Compressão pneumática sequencial nas pernas, usada na rotina de recuperação depois de treinos e provas.</p><a class="s-btn small" href="{wa('Olá! Gostaria de informações sobre a bota de compressão.')}">Pedir informações</a></div>
<div class="s-card"><span class="s-num">02</span><h3>Banheira de gelo</h3><p>Imersão em água fria, usada por atletas após esforços intensos. Orientação de uso e triagem antes da locação.</p><a class="s-btn small" href="{wa('Olá! Gostaria de informações sobre a banheira de gelo.')}">Pedir informações</a></div>
<div class="s-card"><span class="s-num">03</span><h3>Combo fim de semana</h3><p>Bota de compressão e banheira de gelo por 2 dias completos.</p><a class="s-btn small" href="{wa('Olá! Gostaria de informações sobre o combo de fim de semana (bota + banheira).')}">Pedir informações</a></div>
</div><p style="margin-top:20px"><a href="/ferrari-recovery-campinas/">Saiba mais sobre a Ferrari Recovery →</a></p></div></section>

<section class="h-sec escura" id="atendimento"><div class="s-wide"><span class="rotulo">Onde atendo</span><h2>Duas formas de cuidar de você.</h2>
<div class="h-duo">
<div class="s-card escuro"><span class="s-num" style="color:#EE6660">01</span><h3>Instituto Adara</h3><p>Atendimento presencial em uma estrutura moderna e equipada para a sua reabilitação esportiva.</p><div class="h-end">{ENDERECO}</div><a class="s-btn small" href="{wa('Olá! Gostaria de agendar um atendimento no Instituto Adara.')}">Agendar na clínica</a></div>
<div class="s-card escuro"><span class="s-num" style="color:#EE6660">02</span><h3>Home care</h3><p>Reabilitação na sua casa, com privacidade e conforto, no Swiss Park e na região metropolitana de Campinas.</p><a class="s-btn small" href="{wa('Olá! Gostaria de agendar um atendimento Home Care.')}">Agendar home care</a> &nbsp; <a href="/fisioterapia-home-care-campinas/" style="color:#EE6660">Saiba mais →</a></div>
</div></div></section>

<section class="h-sec"><div class="s-wide"><span class="rotulo">Blog</span><h2>Para entender melhor a sua dor.</h2><div class="s-grid">{blog}</div><p><a href="/blog/">Ver todos os artigos →</a></p></div></section>

<section class="h-sec" style="padding-top:0"><div class="s-wrap s-main"><span class="rotulo">Dúvidas</span>{faq_html(HOME_FAQ).replace('<h2>Perguntas frequentes</h2>', '<h2 style="margin-top:10px">Perguntas frequentes</h2>')}
<p style="margin-top:22px"><a href="/fisioterapia-reembolso-convenio-campinas/">Como funciona o reembolso do convênio →</a></p></div></section>
<div class="s-wide">{cta('Olá! Vim pelo site e gostaria de agendar uma avaliação.')}</div>
</main>
"""
    return "/", h + footer()



def pagina_link_bio():
    """Página de links da bio do @edferrarijr. Fora do Google (noindex) e fora do sitemap."""
    caminho = "/instagram/"
    titulo = "Links do Ed Ferrari | Fisioterapia Esportiva em Campinas"
    desc = "Agende sua avaliação, veja o home care, o reembolso do convênio e os artigos do blog."
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": titulo, "url": f"{BASE}{caminho}"}
    botoes = [
        ("Agendar avaliação", "Pelo WhatsApp, no Instituto Adara ou em casa", wa("Oi Ed, vim do Instagram e quero agendar uma avaliação.")),
        ("Fisioterapia para Hyrox, CrossFit e corrida", "Retorno ao esporte e prevenção", "/fisioterapia-esportiva-campinas/?utm_source=instagram&utm_medium=bio"),
        ("Atendimento em casa", "Home care no Swiss Park e região", "/fisioterapia-home-care-campinas/?utm_source=instagram&utm_medium=bio"),
        ("Reembolso do convênio", "Como pedir ao seu plano", "/fisioterapia-reembolso-convenio-campinas/?utm_source=instagram&utm_medium=bio"),
        ("Ferrari Recovery", "Bota de compressão e banheira de gelo", "/ferrari-recovery-campinas/?utm_source=instagram&utm_medium=bio"),
        ("Blog", "Artigos sobre dor, treino e recuperação", "/blog/?utm_source=instagram&utm_medium=bio"),
    ]
    cards = "".join(f'<a class="s-card" href="{h}"><span class="s-num">{i:02d}</span><h3>{t}</h3><p>{d}</p></a>' for i, (t, d, h) in enumerate(botoes, 1))
    h = head(titulo, desc, caminho, ld, robots="noindex, follow") + header()
    h += f"""<main id="conteudo" class="s-main"><div class="s-wrap">
<section class="s-hero"><span class="rotulo">{CREFITO} · Campinas</span><div class="regua"></div><h1>Ed Ferrari<br><span class="destaque">Fisio esportivo</span></h1>
<p class="lead">Para quem treina Hyrox, CrossFit e corrida. Escolha o que você procura.</p></section>
<div class="s-grid" style="grid-template-columns:1fr">{cards}</div>
</div></main>
"""
    return caminho, h + footer()




PERITO_FAQ = [
    ("Qual a diferença entre perito judicial e assistente técnico?",
     "O perito judicial é nomeado pelo juiz e atua de forma imparcial. O assistente técnico é indicado por uma das partes (o advogado ou o trabalhador) para acompanhar a perícia, formular quesitos e, se for o caso, apresentar um parecer técnico próprio. Na mesma ação, o profissional atua em um papel só."),
    ("Como contestar um laudo que negou meu benefício no INSS?",
     "A contestação passa pela via jurídica, com o seu advogado. A parte técnica pode ser apoiada por um parecer fisioterapêutico que descreve a sua limitação funcional com base em avaliação e exames. A decisão cabe à Justiça, e o resultado depende de cada caso."),
    ("O que é LER/DORT e como se avalia a relação com o trabalho?",
     "LER e DORT são termos para distúrbios ligados a esforços repetitivos e condições de trabalho. A relação com a função é avaliada pela análise da atividade, da biomecânica e dos exames clínicos. Quem decide sobre o nexo é o juiz, com base nas provas do processo."),
    ("Por que um advogado trabalhista pode precisar de um fisioterapeuta assistente?",
     "Questões de capacidade funcional, concausa e ergonomia têm natureza técnica. O assistente técnico ajuda o advogado a compreender o laudo, formular quesitos adequados e, se houver divergência técnica, fundamentá-la na literatura."),
    ("Como são definidos os honorários?",
     "Os honorários são pagos pela parte que contrata e variam com a complexidade do caso (por exemplo, se há acompanhamento presencial da perícia e a emissão de parecer). Faço uma análise inicial para alinhar o escopo e o valor antes de começar."),
]


def pagina_perito():
    caminho = "/perito-assistente-tecnico-em-fisioterapia/"
    titulo = "Perito e Assistente Técnico em Fisioterapia em Campinas | Ed Ferrari Jr"
    desc = "Assistência técnica fisioterapêutica em Campinas e região: parecer de viabilidade, quesitos, acompanhamento da perícia e análise de laudos para advogados e trabalhadores (TRT-15, Justiça Federal e TJSP)."
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "ProfessionalService", "@id": f"{BASE}{caminho}#servico", "name": "Assistência técnica e perícia em fisioterapia", "url": f"{BASE}{caminho}",
         "description": desc, "provider": {"@id": f"{BASE}/#pessoa"}, "areaServed": [{"@type": "City", "name": "Campinas"}, {"@type": "AdministrativeArea", "name": "Região Metropolitana de Campinas"}],
         "telephone": "+5519971002263", "inLanguage": "pt-BR"},
        {"@type": "Person", "@id": f"{BASE}/#pessoa", "name": "Ed Ferrari Jr", "jobTitle": "Fisioterapeuta", "identifier": CREFITO, "url": f"{BASE}/"},
        crumbs_ld([("Início", "/"), ("Perícia e assistência técnica", caminho)]), faq_ld(PERITO_FAQ)]}
    adv = [
        ("Parecer de viabilidade", "Análise de prontuários e exames antes do ajuizamento, apontando os aspectos técnicos que merecem atenção no caso."),
        ("Quesitos", "Elaboração de quesitos preliminares, suplementares e de esclarecimento, direcionados aos pontos técnicos da controvérsia."),
        ("Acompanhamento da perícia", "Presença no ato pericial, em Campinas e região, acompanhando o exame físico e as metodologias aplicadas."),
        ("Análise de laudos", "Parecer técnico divergente, quando houver, fundamentado na literatura de cinesiologia e biomecânica."),
        ("Análise do posto de trabalho", "Levantamento ergonômico no local de trabalho (NR-17) para descrever os fatores de risco da atividade."),
        ("Capacidade funcional", "Descrição da limitação funcional com base em instrumentos reconhecidos, como a CIF, para subsidiar a análise de danos."),
    ]
    adv_html = "".join(f'<div class="s-card"><span class="s-num">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(adv, 1))
    trab = [
        ("LER/DORT e esforço repetitivo", "Descrição técnica da atividade e da limitação funcional, relacionando função, movimentos exigidos e exames."),
        ("Doenças da coluna", "Análise da carga física da função, da postura e dos exames para apoiar a discussão sobre a relação com o trabalho."),
        ("Benefício negado ou cessado", "Avaliação funcional detalhada, que o seu advogado pode usar para fundamentar o pedido de revisão."),
    ]
    trab_html = "".join(f'<div class="s-card"><span class="s-num">{i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(trab, 1))
    passos = [
        ("Contato e triagem", "Você conta o caso, o tipo de processo e os prazos. Eu indico se e como a assistência técnica pode ajudar."),
        ("Análise dos documentos", "Leitura de exames, laudos, prontuários e documentos do processo."),
        ("Avaliação e atuação", "Avaliação funcional, análise do posto de trabalho e acompanhamento da perícia, conforme o caso."),
        ("Parecer técnico", "Entrega do parecer ou dos quesitos, nos prazos combinados com o advogado."),
    ]
    passos_html = "".join(f'<div class="pt-passo"><span class="s-num">PASSO {i:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(passos, 1))
    msg_adv = "Olá, Dr. Ed! Sou advogado(a) e gostaria de conversar sobre assistência técnica em fisioterapia em um caso."
    msg_trab = "Olá, Dr. Ed! Gostaria de saber como funciona a avaliação técnica da minha lesão para o meu processo."
    h = head(titulo, desc, caminho, ld, imagem="/assets/img/foto-sled.webp") + header()
    h += f"""<main id="conteudo">
<section class="pt-hero"><div class="s-wide"><div>
<span class="rotulo">Perícia e assistência técnica · Campinas e região</span><div class="regua"></div>
<h1>Assistência técnica em <span class="destaque">fisioterapia</span> para o seu processo</h1>
<p class="lead">Parecer técnico fisioterapêutico para advogados e para trabalhadores em processos que discutem capacidade funcional, relação com o trabalho e danos.</p>
<div class="acoes" style="display:flex;gap:14px;flex-wrap:wrap"><a class="s-btn" href="{wa(msg_adv)}">Sou advogado(a)</a><a class="s-btn vazado" href="{wa(msg_trab)}">Sou trabalhador(a)</a></div>
<div class="pt-chips"><span>TRT-15</span><span>Justiça Federal e INSS</span><span>TJSP</span><span>{CREFITO}</span></div>
</div>
<div class="pt-doc" aria-hidden="true"><b>Parecer técnico</b><small>FISIOTERAPIA · ASSISTÊNCIA TÉCNICA</small><i></i><i></i><i></i><i></i><i></i><i></i><span class="sel">Análise individual</span></div>
</div></section>

<section class="h-sec"><div class="s-wide"><span class="rotulo">Os dois papéis</span><h2>Perito do juízo ou assistente técnico?</h2>
<p class="suave" style="max-width:680px">São funções diferentes e o profissional atua em apenas uma delas na mesma ação.</p>
<div class="pt-papeis">
<div class="pt-papel"><span class="s-num">PERITO DO JUÍZO</span><h3>Nomeado pelo juiz</h3><p>Atua de forma imparcial, realiza o exame e entrega o laudo ao juízo.</p></div>
<div class="pt-papel destaque-p"><span class="s-num">ASSISTENTE TÉCNICO</span><h3>Indicado por uma das partes</h3><p>Acompanha a perícia, ajuda a formular quesitos e pode apresentar um parecer técnico próprio sobre o laudo.</p></div>
</div></div></section>

<section class="h-sec escura"><div class="s-wide"><span class="rotulo">Para advogados</span><h2>Apoio técnico do pedido ao laudo.</h2>
<p style="max-width:680px">O embate sobre capacidade física, concausa e ergonomia é técnico. Estes são os pontos em que a assistência fisioterapêutica costuma ajudar.</p>
<div class="s-grid" style="margin-top:28px">{adv_html}</div>
<p style="margin-top:26px"><a class="s-btn" href="{wa(msg_adv)}">Conversar sobre um caso</a></p></div></section>

<section class="h-sec"><div class="s-wide"><span class="rotulo">Para trabalhadores e pacientes</span><h2>Sua limitação, descrita tecnicamente.</h2>
<p class="suave" style="max-width:680px">A Justiça trabalha com documentos técnicos. Um parecer fisioterapêutico organiza e descreve o que o seu corpo consegue e não consegue fazer.</p>
<div class="s-grid" style="margin-top:28px">{trab_html}</div>
<div class="pt-aviso">O parecer é um documento técnico. Não há garantia de resultado em processos judiciais: a decisão cabe ao juiz.</div>
<h3 style="margin-top:30px">O que levar na primeira conversa</h3>
<div class="s-main"><ul>
<li>Exames de imagem e laudos médicos</li><li>Prontuários e relatórios de tratamento</li><li>CAT (comunicação de acidente de trabalho), se houver</li><li>Descrição das suas funções e da rotina de trabalho</li><li>Documentos do INSS e do processo, se já existirem</li></ul></div></div></section>

<section class="h-sec escura"><div class="s-wide"><span class="rotulo">Como funciona</span><h2>Quatro passos, com prazos combinados.</h2>
<div class="pt-passos">{passos_html}</div></div></section>

<section class="h-sec"><div class="s-wrap s-main"><span class="rotulo">Onde atuo</span><h2 style="margin-top:10px">Campinas e região.</h2>
<p>Atuo em processos da Justiça do Trabalho (TRT-15), da Justiça Federal (INSS) e da Justiça Estadual (TJSP), com acompanhamento presencial de perícias em Campinas e na Região Metropolitana.</p>
{faq_html(PERITO_FAQ)}</div></section>
<div class="s-wide">{cta(msg_adv, "Converse sobre o seu caso", "Conte o tipo de processo e os prazos. Respondo pelo WhatsApp e indico como a assistência técnica pode ajudar.")}</div>
</main>
"""
    return caminho, h + footer()


def escrever(caminho, html):
    pasta = os.path.join(RAIZ, caminho.strip("/"))
    os.makedirs(pasta, exist_ok=True)
    with open(os.path.join(pasta, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def main():
    c, h = pagina_home()
    escrever(c, h)
    c, h = pagina_link_bio()
    escrever(c, h)
    c, h = pagina_perito()
    escrever(c, h)
    urls = [("/", "1.0"), ("/perito-assistente-tecnico-em-fisioterapia/", "0.7")]
    for s in SERVICOS:
        c, h = pagina_servico(s)
        escrever(c, h)
        urls.append((c, "0.9"))
    ultimo = {}
    c, h = pagina_blog()
    escrever(c, h)
    urls.append((c, "0.6"))
    for a in ARTIGOS:
        c, h = pagina_artigo(a)
        escrever(c, h)
        urls.append((c, "0.6"))
        ultimo[c] = a.get("data", DATA)
    itens = "".join(
        f"  <url><loc>{BASE}{c}</loc><lastmod>{ultimo.get(c, DATA)}</lastmod><priority>{p}</priority></url>\n" for c, p in urls
    )
    with open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{itens}</urlset>\n')
    with open(os.path.join(RAIZ, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print(f"{len(urls)} URLs geradas")


if __name__ == "__main__":
    main()
