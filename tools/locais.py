"""Páginas de atendimento local (busca "fisioterapeuta perto de mim", bairro e cidade).

Cada página tem texto próprio: nada de copiar e trocar só o nome do bairro (o Google trata como spam).
"tipo": "hub" (página-mãe), "regiao" (bairro ou cidade) ou "necessidade" (o que a pessoa procura).
"rel": slugs de LOCAIS ou SERVICOS para o bloco "Veja também".
"area": nome do lugar para o schema (areaServed).
"""

LOCAIS = [
    # ------------------------------------------------------------ página-mãe
    {
        "slug": "fisioterapeuta-campinas",
        "tipo": "hub",
        "menu": "Onde eu atendo",
        "resumo": "Fisioterapeuta em Campinas: consultório no Swiss Park e atendimento em casa.",
        "title": "Fisioterapeuta em Campinas perto de você | Ed Ferrari Jr",
        "desc": "Procurando fisioterapeuta perto de você em Campinas? Atendo no Instituto Adara (Swiss Park) e em domicílio em Campinas e região. Agende pelo WhatsApp.",
        "h1": "Fisioterapeuta em Campinas, no consultório ou na sua casa",
        "lead": "Quando alguém procura \"fisioterapeuta perto de mim\", quase sempre quer duas coisas: começar logo e não perder meia hora no trânsito. Eu atendo no Instituto Adara, no Swiss Park, e vou até a sua casa em Campinas e cidades vizinhas. Aqui você vê como funciona cada formato e em que regiões eu atendo.",
        "wa": "Olá! Encontrei seu site procurando fisioterapeuta em Campinas e gostaria de agendar uma avaliação.",
        "area": "Campinas",
        "foto": ("foto-alongamento", "Praticante se alongando ao ar livre", "50% 40%"),
        "secoes": [
            ("Dois jeitos de fazer a fisioterapia", """<ul>
<li><strong>No consultório</strong>: Instituto Adara, Av. Antônio Artioli, 276, Swiss Park. Bom para quem quer usar a estrutura da clínica e já passa pela região.</li>
<li><strong>Em domicílio</strong>: eu levo o material portátil até você, em casa, no condomínio ou na academia do prédio. Bom para pós-operatório, rotina apertada ou quem prefere privacidade. Veja como funciona em <a href="/fisioterapia-home-care-campinas/">fisioterapia home care</a>.</li>
</ul>"""),
            ("Regiões em que eu atendo", """<p>Escolha a sua região para ver como funciona o atendimento aí. Se o seu bairro não está na lista, mande o endereço pelo WhatsApp que eu confirmo.</p>
{{LISTA_REGIOES}}"""),
            ("O que você está procurando", """<p>Se você já sabe o que precisa tratar, vá direto para a página do assunto:</p>
{{LISTA_NECESSIDADES}}"""),
            ("Como escolher um fisioterapeuta perto de você", """<p>Distância conta, mas não é o único critério. Antes de marcar, vale conferir três coisas:</p>
<ol>
<li><strong>Registro no CREFITO</strong>: todo fisioterapeuta precisa ter. O meu é o {crefito}.</li>
<li><strong>Experiência com o seu caso</strong>: dor de quem corre, pós-operatório de joelho e lesão de CrossFit pedem avaliações diferentes. Eu trabalho com ortopedia e esporte.</li>
<li><strong>Atendimento individual</strong>: a sessão é só sua, do começo ao fim, sem dividir o horário com outros pacientes.</li>
</ol>"""),
        ],
        "faq": [
            ("Você atende pelo convênio?", "O atendimento é particular. Eu forneço recibo e relatório para você pedir o reembolso ao seu plano, conforme as regras dele."),
            ("Preciso de pedido médico?", "Para a avaliação, não. Alguns planos pedem a indicação médica para reembolsar; vale conferir com o seu."),
            ("Quanto tempo dura a sessão?", "A sessão é individual. O tempo e a frequência são definidos na avaliação, de acordo com o seu caso."),
            ("Como agendo?", "Pelo WhatsApp (19) 97100-2263. Diga o seu bairro e o que está sentindo que eu respondo com os horários."),
        ],
        "rel": ["fisioterapia-home-care-campinas", "fisioterapia-esportiva-campinas", "fisioterapia-reembolso-convenio-campinas"],
    },
    # ------------------------------------------------------------ regiões
    {
        "slug": "fisioterapeuta-swiss-park-campinas",
        "tipo": "regiao",
        "menu": "Swiss Park",
        "resumo": "Consultório no Instituto Adara e atendimento nos condomínios do bairro.",
        "title": "Fisioterapeuta no Swiss Park, Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapeuta no Swiss Park: consultório no Instituto Adara (Av. Antônio Artioli, 276) e atendimento em casa nos condomínios. Agende pelo WhatsApp.",
        "h1": "Fisioterapeuta no Swiss Park, em Campinas",
        "lead": "O Swiss Park é a minha base. O consultório fica no Instituto Adara, na Av. Antônio Artioli, 276, e boa parte dos meus pacientes de domicílio mora nos condomínios do próprio bairro. Para quem está aqui, a fisioterapia cabe na rotina sem sair do bairro.",
        "wa": "Olá! Moro no Swiss Park e gostaria de agendar uma avaliação de fisioterapia.",
        "area": "Swiss Park, Campinas",
        "foto": ("foto-afundo", "Praticante fazendo afundo ao ar livre", "50% 35%"),
        "secoes": [
            ("Consultório ou em casa: o que faz mais sentido", """<p>Morando no Swiss Park, você tem as duas opções perto:</p>
<ul>
<li><strong>Instituto Adara</strong>: indicado quando o tratamento pede equipamentos da clínica ou quando você prefere separar o momento da fisioterapia da sua casa.</li>
<li><strong>No seu condomínio</strong>: indicado no pós-operatório, quando sair de casa é difícil, ou quando a agenda está apertada. Muitos condomínios do bairro têm academia ou área comum que funcionam bem para os exercícios.</li>
</ul>
<p>Dá também para combinar: algumas sessões no consultório e outras em casa, conforme a fase do tratamento.</p>"""),
            ("Atendimento no condomínio: como funciona a portaria", """<p>Para o atendimento em casa, você deixa meu nome autorizado na portaria e eu chego no horário combinado com o material portátil. Se quiser usar a academia ou outra área comum, vale confirmar antes as regras do seu condomínio para uso com profissional externo.</p>"""),
            ("O que eu mais atendo no bairro", """<ul>
<li>Dor no ombro, no joelho e na coluna de quem treina musculação, CrossFit, Hyrox ou corre pelas ruas do bairro.</li>
<li><a href="/fisioterapia-pos-operatorio-joelho-campinas/">Pós-operatório de joelho</a> e de ombro, com as primeiras semanas em casa.</li>
<li>Lesões musculares e dores que voltam toda vez que o treino aperta.</li>
</ul>"""),
        ],
        "faq": [
            ("Onde fica o consultório?", "No Instituto Adara, Av. Antônio Artioli, 276, Swiss Park, Campinas."),
            ("Você atende em qualquer condomínio do Swiss Park?", "Sim, desde que a portaria libere a minha entrada. Mande o nome do condomínio pelo WhatsApp quando for agendar."),
            ("Posso começar em casa e depois ir ao consultório?", "Pode. É comum no pós-operatório: as primeiras semanas em casa e, quando você já se desloca bem, as sessões no Instituto Adara."),
        ],
        "rel": ["fisioterapeuta-campinas", "fisioterapia-home-care-campinas", "fisioterapia-pos-operatorio-joelho-campinas"],
    },
    {
        "slug": "fisioterapeuta-cambui-campinas",
        "tipo": "regiao",
        "menu": "Cambuí",
        "resumo": "Fisioterapia em casa ou no prédio, para quem mora ou trabalha no Cambuí.",
        "title": "Fisioterapeuta no Cambuí, Campinas, em casa | Ed Ferrari Jr",
        "desc": "Fisioterapeuta para quem mora ou trabalha no Cambuí, em Campinas: atendimento domiciliar no apartamento ou na academia do prédio. Agende pelo WhatsApp.",
        "h1": "Fisioterapeuta no Cambuí: a sessão vai até o seu prédio",
        "lead": "No Cambuí, achar vaga e enfrentar o trânsito do horário de pico às vezes toma mais tempo que a própria sessão. Por isso, para quem mora no bairro, o formato que mais uso é o domiciliar: eu vou até o seu apartamento, ou até a academia do prédio, no horário combinado.",
        "wa": "Olá! Moro no Cambuí e gostaria de saber sobre o atendimento de fisioterapia em casa.",
        "area": "Cambuí, Campinas",
        "foto": ("foto-barra", "Mulher treinando na barra", "50% 30%"),
        "secoes": [
            ("Fisioterapia em apartamento funciona?", """<p>Funciona bem para a maior parte dos casos ortopédicos e esportivos. Para avaliar e tratar, eu preciso de pouco espaço: o suficiente para você deitar, ficar em pé e dar alguns passos. Levo maca portátil quando é necessário, elásticos, pesos leves e os instrumentos de medida que uso na avaliação.</p>
<p>Se o seu prédio tem academia, ela costuma ser ótima para a fase de fortalecimento, com halteres e polias à mão.</p>"""),
            ("Quem mais me procura no Cambuí", """<ul>
<li>Quem passa o dia no computador e convive com dor no pescoço, nas costas ou no punho. Veja <a href="/fisioterapia-coluna-campinas/">fisioterapia para coluna</a> e <a href="/fisioterapia-ombro-campinas/">ombro, cotovelo e punho</a>.</li>
<li>Quem treina na academia do prédio ou nos estúdios do bairro e começou a sentir dor em algum movimento.</li>
<li>Quem prefere encaixar a sessão antes ou depois do expediente, sem deslocamento.</li>
</ul>"""),
            ("Horários", """<p>A agenda do domicílio é combinada caso a caso. Diga pelo WhatsApp os dias e períodos que funcionam para você, e eu respondo com as opções disponíveis.</p>"""),
        ],
        "faq": [
            ("Preciso ter algum equipamento em casa?", "Não. Eu levo o material necessário. Se você tiver halteres ou elásticos, aproveitamos."),
            ("Você atende no escritório?", "Depende do espaço e das regras do local. Me conte como é o ambiente pelo WhatsApp que eu digo se dá para fazer a sessão lá."),
            ("O atendimento em casa tem reembolso do convênio?", "Eu forneço recibo e relatório. A cobertura e o valor dependem do seu plano."),
        ],
        "rel": ["fisioterapeuta-campinas", "fisioterapia-home-care-campinas", "fisioterapia-coluna-campinas"],
    },
    {
        "slug": "fisioterapeuta-taquaral-campinas",
        "tipo": "regiao",
        "menu": "Taquaral",
        "resumo": "Para quem corre na Lagoa do Taquaral e mora na região.",
        "title": "Fisioterapeuta no Taquaral, Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapeuta no Taquaral, em Campinas: dor de quem corre na Lagoa, joelho, canela e tornozelo. Atendimento em casa na região. Agende pelo WhatsApp.",
        "h1": "Fisioterapeuta no Taquaral, para quem corre na Lagoa e mora na região",
        "lead": "A volta da Lagoa do Taquaral é onde muita gente de Campinas começa a correr, e também onde aparecem as primeiras dores: canela, joelho, tornozelo e quadril. Atendo moradores do Taquaral e dos bairros vizinhos em casa, com foco em quem corre e treina.",
        "wa": "Olá! Moro no Taquaral e gostaria de agendar uma avaliação de fisioterapia.",
        "area": "Taquaral, Campinas",
        "foto": ("foto-corrida-laranja", "Corredora em treino ao ar livre", "50% 40%"),
        "secoes": [
            ("As dores mais comuns de quem corre na Lagoa", """<ul>
<li><strong>Dor na canela</strong> no começo ou na volta aos treinos, quando o volume sobe rápido.</li>
<li><strong>Dor na frente ou do lado de fora do joelho</strong>, que aparece depois de alguns quilômetros.</li>
<li><strong>Dor no calcanhar e no tendão de Aquiles</strong>, principalmente de manhã.</li>
<li><strong>Entorses de tornozelo</strong> que deixam o tornozelo \"falseando\".</li>
</ul>
<p>Cada uma tem causas diferentes. Na avaliação eu olho a sua corrida, a força, a mobilidade e, principalmente, o que mudou no seu treino nas últimas semanas. Leia também: <a href="/blog/dor-no-joelho-corrida/">dor no joelho na corrida</a>.</p>"""),
            ("Continuar correndo durante o tratamento", """<p>Sempre que o caso permite, a ideia é ajustar a carga em vez de parar tudo: reduzir volume ou ritmo, trocar alguns treinos e fortalecer o que precisa. Quando é preciso dar uma pausa, eu explico o porquê e quais são os critérios para voltar.</p>"""),
            ("Atendimento em casa ou no consultório", """<p>Para quem mora no Taquaral, o mais prático costuma ser o atendimento domiciliar. Se você preferir a estrutura da clínica, também atendo no Instituto Adara, no Swiss Park. Veja a página de <a href="/fisioterapia-para-corredores-campinas/">fisioterapia para corredores</a>.</p>"""),
        ],
        "faq": [
            ("Preciso parar de correr?", "Nem sempre. Em muitos casos dá para ajustar o treino e seguir correndo. A avaliação define isso para o seu caso."),
            ("Você analisa a corrida?", "Sim. Observo como você corre e relaciono com a dor, a força e a mobilidade, além do seu histórico de treino."),
            ("Atende só quem corre?", "Não. Atendo dores e lesões ortopédicas em geral, de quem treina ou não."),
        ],
        "rel": ["fisioterapia-para-corredores-campinas", "fisioterapia-joelho-tornozelo-campinas", "fisioterapeuta-campinas"],
    },
    {
        "slug": "fisioterapeuta-barao-geraldo-campinas",
        "tipo": "regiao",
        "menu": "Barão Geraldo",
        "resumo": "Atendimento em casa para moradores de Barão Geraldo e região da Unicamp.",
        "title": "Fisioterapeuta em Barão Geraldo, Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapeuta em Barão Geraldo, Campinas: atendimento em casa para moradores do distrito e da região da Unicamp. Ortopedia e esporte. Agende pelo WhatsApp.",
        "h1": "Fisioterapeuta em Barão Geraldo",
        "lead": "Barão Geraldo tem ritmo próprio: muita gente corre, pedala e treina por ali, e muita gente também passa horas sentada estudando ou trabalhando na região da Unicamp. Atendo moradores do distrito em casa, com avaliação ortopédica e esportiva completa.",
        "wa": "Olá! Moro em Barão Geraldo e gostaria de saber sobre o atendimento de fisioterapia em casa.",
        "area": "Barão Geraldo, Campinas",
        "foto": ("foto-corrida-poca", "Corredor passando por uma poça", "50% 40%"),
        "secoes": [
            ("Para quem é", """<ul>
<li>Quem corre ou pedala pelas ruas e estradas do distrito e está com dor que não passa.</li>
<li>Quem passa muitas horas sentado e sente dor no pescoço, nas costas ou no punho.</li>
<li>Quem fez cirurgia ortopédica e precisa começar a reabilitação sem se deslocar.</li>
</ul>"""),
            ("Como é a primeira sessão", """<p>A primeira sessão é a avaliação: conversamos sobre a dor, a sua rotina e o seu treino; depois faço os testes de movimento, força e mobilidade. Saio da avaliação com um plano claro, e você sai com os primeiros exercícios e orientações para os dias entre as sessões.</p>"""),
            ("Atendimento em casa", """<p>Em Barão Geraldo o atendimento é domiciliar. Envie o seu endereço pelo WhatsApp e eu confirmo os dias disponíveis para a região. Quem preferir pode fazer as sessões no Instituto Adara, no Swiss Park. Saiba mais sobre a <a href="/fisioterapia-home-care-campinas/">fisioterapia home care</a>.</p>"""),
        ],
        "faq": [
            ("Você atende em república ou kitnet?", "Sim, se houver espaço para você deitar e se movimentar. Me conte como é o local pelo WhatsApp."),
            ("Quantas sessões vou precisar?", "Só dá para dizer depois da avaliação, porque depende da lesão, do tempo de dor e dos seus objetivos."),
            ("Você fornece recibo para reembolso?", "Sim, recibo e relatório para você solicitar o reembolso ao seu plano."),
        ],
        "rel": ["fisioterapeuta-campinas", "fisioterapia-home-care-campinas", "fisioterapia-coluna-campinas"],
    },
    {
        "slug": "fisioterapeuta-sousas-joaquim-egidio",
        "tipo": "regiao",
        "menu": "Sousas e Joaquim Egídio",
        "resumo": "Para quem corre e pedala nas estradas de Sousas e Joaquim Egídio.",
        "title": "Fisioterapeuta em Sousas e Joaquim Egídio | Ed Ferrari Jr",
        "desc": "Fisioterapeuta em Sousas e Joaquim Egídio, Campinas: atendimento em casa para quem corre, pedala e faz trilha na região. Agende pelo WhatsApp.",
        "h1": "Fisioterapeuta em Sousas e Joaquim Egídio",
        "lead": "Subida, descida, estrada de terra e trilha: quem treina em Sousas e Joaquim Egídio exige mais de tornozelos, joelhos e quadris do que quem corre no plano. Atendo moradores dos dois distritos em casa, olhando também para o terreno em que você treina.",
        "wa": "Olá! Moro em Sousas/Joaquim Egídio e gostaria de agendar uma avaliação de fisioterapia.",
        "area": "Sousas e Joaquim Egídio, Campinas",
        "foto": ("foto-corrida", "Corredor em movimento", "50% 40%"),
        "secoes": [
            ("O terreno muda a lesão", """<p>Descidas longas pedem muito do quadríceps e da frente do joelho. Chão irregular e trilha aumentam o risco de entorse de tornozelo. Subidas exigem mais da panturrilha e do tendão de Aquiles. Por isso, na avaliação, além dos testes de força e mobilidade, eu pergunto onde e como você treina.</p>"""),
            ("Ciclistas também", """<p>Quem pedala muito costuma chegar com dor no joelho, na lombar ou no pescoço. Muitas vezes a dor vem da soma de força, mobilidade e volume de treino. Eu avalio e trato a parte física; para ajustes finos da bike, indico um profissional de bike fit.</p>"""),
            ("Atendimento em casa", """<p>Para Sousas e Joaquim Egídio o formato é o domiciliar. Envie o endereço pelo WhatsApp para confirmar os dias da região. Se preferir, também atendo no Instituto Adara, no Swiss Park. Veja <a href="/fisioterapia-joelho-tornozelo-campinas/">joelho e tornozelo</a>.</p>"""),
        ],
        "faq": [
            ("Torci o tornozelo na trilha. Quando procuro avaliação?", "Se não consegue apoiar o pé, se o inchaço é grande ou se a dor é forte em cima do osso, procure um médico primeiro. Nos outros casos, a avaliação de fisioterapia ajuda a voltar com segurança."),
            ("Você atende em chácara ou condomínio afastado?", "Envie a localização pelo WhatsApp que eu confirmo se está na minha área de atendimento."),
            ("Atende quem não treina?", "Sim. Atendo dores e lesões ortopédicas de qualquer pessoa."),
        ],
        "rel": ["fisioterapia-para-corredores-campinas", "fisioterapia-joelho-tornozelo-campinas", "fisioterapeuta-campinas"],
    },
    {
        "slug": "fisioterapeuta-valinhos",
        "tipo": "regiao",
        "menu": "Valinhos",
        "resumo": "Atendimento domiciliar em Valinhos, em casa ou no condomínio.",
        "title": "Fisioterapeuta em Valinhos: atendimento em casa | Ed Ferrari Jr",
        "desc": "Fisioterapeuta em Valinhos com atendimento domiciliar: ortopedia, esporte e pós-operatório na sua casa ou condomínio. Agende pelo WhatsApp.",
        "h1": "Fisioterapeuta em Valinhos, com atendimento em casa",
        "lead": "Para quem mora em Valinhos, ir até Campinas para cada sessão pode virar o motivo de largar o tratamento no meio. Por isso eu levo a fisioterapia até você: avaliação e sessões na sua casa ou no seu condomínio, com o mesmo método do consultório.",
        "wa": "Olá! Moro em Valinhos e gostaria de saber sobre o atendimento de fisioterapia em casa.",
        "area": "Valinhos",
        "foto": ("foto-remo", "Atleta no remo ergômetro", "50% 40%"),
        "secoes": [
            ("Por que o domicílio ajuda a terminar o tratamento", """<p>Boa parte do resultado da fisioterapia vem da regularidade: fazer as sessões e os exercícios em casa durante semanas. Quando cada sessão exige deslocamento entre cidades, a chance de faltar aumenta. Com o atendimento em casa, a sessão começa na hora marcada e você não perde tempo no caminho.</p>"""),
            ("O que eu atendo em Valinhos", """<ul>
<li>Dores e lesões de ombro, joelho, tornozelo e coluna.</li>
<li>Reabilitação depois de cirurgia ortopédica.</li>
<li>Quem treina musculação, CrossFit, Hyrox ou corrida e quer voltar sem dor. Veja <a href="/fisioterapia-esportiva-campinas/">fisioterapia esportiva</a>.</li>
</ul>"""),
            ("Agenda", """<p>Os horários em Valinhos são combinados por região, para eu chegar no horário. Mande o seu bairro pelo WhatsApp e eu respondo com os dias disponíveis.</p>"""),
        ],
        "faq": [
            ("Você atende em todos os bairros de Valinhos?", "Envie o seu bairro pelo WhatsApp para eu confirmar. A agenda é organizada por região."),
            ("O valor é o mesmo de Campinas?", "Os valores são informados pelo WhatsApp, de acordo com o local e o tipo de atendimento."),
            ("Posso fazer algumas sessões no consultório?", "Pode. O consultório fica no Instituto Adara, no Swiss Park, em Campinas."),
        ],
        "rel": ["fisioterapia-home-care-campinas", "fisioterapeuta-vinhedo", "fisioterapeuta-campinas"],
    },
    {
        "slug": "fisioterapeuta-vinhedo",
        "tipo": "regiao",
        "menu": "Vinhedo",
        "resumo": "Fisioterapia em casa para quem mora em Vinhedo.",
        "title": "Fisioterapeuta em Vinhedo: fisioterapia em casa | Ed Ferrari Jr",
        "desc": "Fisioterapeuta em Vinhedo com atendimento em casa: dor, lesão esportiva e pós-operatório tratados no seu condomínio. Agende pelo WhatsApp.",
        "h1": "Fisioterapeuta em Vinhedo: fisioterapia na sua casa",
        "lead": "Vinhedo tem muitos condomínios com espaço, academia e área verde, o que facilita a fisioterapia em casa. Eu atendo moradores da cidade no próprio condomínio, com avaliação ortopédica e esportiva e um plano feito para a sua rotina.",
        "wa": "Olá! Moro em Vinhedo e gostaria de agendar uma avaliação de fisioterapia em casa.",
        "area": "Vinhedo",
        "foto": ("foto-overhead", "Atleta com barra acima da cabeça", "50% 22%"),
        "secoes": [
            ("Aproveitando o espaço do condomínio", """<p>Quando o condomínio tem academia, quadra ou área gramada, dá para fazer partes do tratamento que normalmente seriam feitas na clínica: fortalecimento com carga, exercícios de salto, corrida leve e testes de retorno ao esporte. Basta confirmar as regras de uso com profissional externo.</p>"""),
            ("Para quem é", """<ul>
<li>Quem tem dor no ombro, no joelho ou na coluna e quer tratar sem sair de casa.</li>
<li>Quem está em <a href="/fisioterapia-pos-operatorio-joelho-campinas/">pós-operatório</a> e ainda não dirige.</li>
<li>Quem treina e quer uma avaliação para prevenir lesão antes de uma prova.</li>
</ul>"""),
            ("Como agendar", """<p>Mande pelo WhatsApp o seu condomínio ou bairro e o que está sentindo. Eu confirmo a disponibilidade para Vinhedo e combinamos a primeira sessão, que é a avaliação.</p>"""),
        ],
        "faq": [
            ("Preciso reservar a academia do condomínio?", "Se quiser usar, sim, conforme as regras do seu condomínio. Também dá para fazer tudo dentro de casa."),
            ("Você atende em Louveira ou Itatiba?", "Envie o endereço pelo WhatsApp que eu confirmo se consigo atender."),
            ("Fornece relatório para o convênio?", "Sim, recibo e relatório para solicitar o reembolso. A cobertura depende do plano."),
        ],
        "rel": ["fisioterapia-home-care-campinas", "fisioterapeuta-valinhos", "fisioterapeuta-campinas"],
    },
    # ------------------------------------------------------------ necessidades
    {
        "slug": "fisioterapia-pos-operatorio-joelho-campinas",
        "tipo": "necessidade",
        "menu": "Pós-operatório de joelho",
        "resumo": "LCA, menisco e prótese: reabilitação em casa e no consultório.",
        "title": "Fisioterapia Pós-operatório de Joelho em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapia no pós-operatório de joelho em Campinas: LCA, menisco e prótese. Começo em casa nas primeiras semanas e retorno ao esporte com critérios.",
        "h1": "Fisioterapia no pós-operatório de joelho em Campinas",
        "lead": "Depois de uma cirurgia de joelho, as primeiras semanas são as mais difíceis para sair de casa, e também as que mais pedem acompanhamento. Eu começo a reabilitação na sua casa e sigo com você até a volta às atividades, sempre alinhado com a orientação do seu cirurgião.",
        "wa": "Olá! Fiz (ou vou fazer) cirurgia no joelho e gostaria de agendar a fisioterapia.",
        "area": "Campinas",
        "foto": ("foto-afundo", "Praticante fazendo afundo ao ar livre", "50% 35%"),
        "secoes": [
            ("Cirurgias que eu acompanho", """<ul>
<li>Reconstrução do <strong>ligamento cruzado anterior (LCA)</strong>.</li>
<li>Cirurgias de <strong>menisco</strong> (sutura ou retirada parcial).</li>
<li><strong>Prótese de joelho</strong>.</li>
<li>Outras cirurgias ortopédicas do joelho, conforme o protocolo do seu médico.</li>
</ul>"""),
            ("As fases da reabilitação", """<ol>
<li><strong>Primeiras semanas</strong>: controle de dor e inchaço, ganho de movimento e ativação do quadríceps. Aqui o atendimento em casa faz diferença.</li>
<li><strong>Fortalecimento</strong>: força, equilíbrio e marcha normal, com carga progressiva.</li>
<li><strong>Retorno às atividades</strong>: corrida, saltos e mudanças de direção, liberados por testes de força e função, não só pelo calendário.</li>
</ol>
<p>O tempo de cada fase varia com a cirurgia, o protocolo do cirurgião e a sua resposta ao tratamento.</p>"""),
            ("Quando começar", """<p>Em geral a fisioterapia começa logo nos primeiros dias depois da cirurgia, conforme a liberação médica. Se você já tem a cirurgia marcada, vale fazer uma avaliação antes: chegar com mais força e movimento ajuda na recuperação. Veja também <a href="/fisioterapia-joelho-tornozelo-campinas/">fisioterapia para joelho e tornozelo</a>.</p>"""),
        ],
        "faq": [
            ("Você segue o protocolo do meu cirurgião?", "Sim. O plano respeita as restrições e os prazos definidos pelo seu médico, e eu mantenho contato com ele quando necessário."),
            ("Vou voltar a correr ou treinar?", "Esse é o objetivo de muitos pacientes. A volta é feita em etapas e liberada por testes; o tempo e o resultado variam de pessoa para pessoa."),
            ("Tem reembolso do convênio?", "Eu forneço recibo e relatório para o pedido de reembolso. A cobertura depende do seu plano."),
        ],
        "rel": ["fisioterapia-joelho-tornozelo-campinas", "fisioterapia-home-care-campinas", "fisioterapia-reembolso-convenio-campinas"],
    },
    {
        "slug": "fisioterapia-pos-operatorio-ombro-campinas",
        "tipo": "necessidade",
        "menu": "Pós-operatório de ombro",
        "resumo": "Manguito rotador, luxação e instabilidade: reabilitação passo a passo.",
        "title": "Fisioterapia Pós-operatório de Ombro em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapia no pós-operatório de ombro em Campinas: manguito rotador, luxação e instabilidade. Atendimento em casa e no Swiss Park.",
        "h1": "Fisioterapia no pós-operatório de ombro em Campinas",
        "lead": "Com o braço na tipoia, tarefas simples como se vestir, dormir e tomar banho ficam complicadas, e dirigir até a clínica costuma estar fora de questão. Eu atendo em casa nessa fase e acompanho a reabilitação até você voltar a usar o braço no dia a dia e no treino.",
        "wa": "Olá! Fiz (ou vou fazer) cirurgia no ombro e gostaria de agendar a fisioterapia.",
        "area": "Campinas",
        "foto": ("foto-overhead", "Atleta com barra acima da cabeça", "50% 22%"),
        "secoes": [
            ("Cirurgias que eu acompanho", """<ul>
<li>Reparo do <strong>manguito rotador</strong>.</li>
<li>Estabilização do ombro depois de <strong>luxação</strong> ou instabilidade.</li>
<li>Outras cirurgias do ombro, seguindo o protocolo do seu médico.</li>
</ul>"""),
            ("Como a reabilitação avança", """<ol>
<li><strong>Proteção</strong>: respeitar o tempo de cicatrização, controlar a dor e manter o resto do corpo em movimento.</li>
<li><strong>Movimento</strong>: recuperar a amplitude do ombro aos poucos, conforme liberado.</li>
<li><strong>Força</strong>: fortalecer o manguito, a escápula e o braço todo.</li>
<li><strong>Retorno</strong>: trabalho, esporte e movimentos acima da cabeça, com progressão de carga.</li>
</ol>"""),
            ("Orientações para o dia a dia", """<p>Desde a primeira sessão eu oriento como dormir, se vestir e usar a tipoia, o que pode e o que ainda não pode fazer. Para quem treina, conversamos sobre o que dá para manter no treino de pernas e tronco durante a recuperação. Veja <a href="/fisioterapia-ombro-campinas/">fisioterapia para ombro, cotovelo e punho</a>.</p>"""),
        ],
        "faq": [
            ("Quando posso voltar ao CrossFit ou à musculação?", "Depende da cirurgia e da sua evolução. A volta é feita em etapas, com liberação do médico e testes de força."),
            ("A fisioterapia dói?", "Pode haver desconforto em alguns exercícios, mas ele é controlado. Eu ajusto a sessão conforme a sua resposta."),
            ("Atende em casa no começo?", "Sim. É o formato mais usado nas primeiras semanas, quando você ainda não dirige."),
        ],
        "rel": ["fisioterapia-ombro-campinas", "fisioterapia-home-care-campinas", "fisioterapia-crossfit-campinas"],
    },
    {
        "slug": "fisioterapia-para-corredores-campinas",
        "tipo": "necessidade",
        "menu": "Fisioterapia para corredores",
        "resumo": "Canelite, joelho, Aquiles e fascite em quem corre em Campinas.",
        "title": "Fisioterapia para Corredores em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapeuta para corredores em Campinas: dor no joelho, canelite, tendão de Aquiles e fascite plantar. Avaliação da corrida e ajuste de treino.",
        "h1": "Fisioterapia para corredores em Campinas",
        "lead": "A maior parte das dores de corrida tem a ver com carga: muito, rápido demais, sem o corpo estar preparado. Eu avalio a dor, a sua corrida e o seu treino para que você trate sem precisar abandonar a rotina, sempre que possível.",
        "wa": "Olá! Sou corredor(a) e gostaria de agendar uma avaliação de fisioterapia.",
        "area": "Campinas",
        "foto": ("foto-corrida-laranja", "Corredora em treino ao ar livre", "50% 40%"),
        "secoes": [
            ("Dores que eu mais atendo em corredores", """<ul>
<li>Dor na frente do joelho e banda iliotibial (lado de fora do joelho).</li>
<li>Canelite (dor na canela).</li>
<li>Tendinopatia do tendão de Aquiles e dor no calcanhar.</li>
<li>Fascite plantar.</li>
<li>Dor no quadril e na lombar em treinos longos.</li>
</ul>"""),
            ("O que a avaliação inclui", """<p>Conversa sobre o histórico de treino (volume, ritmo, provas, tênis), testes de força e mobilidade, análise da corrida e testes específicos para a região da dor. O resultado é um plano com tratamento, fortalecimento e ajuste de treino, que você pode compartilhar com o seu treinador. Leia: <a href="/blog/dor-no-joelho-corrida/">dor no joelho na corrida</a>.</p>"""),
            ("Prova marcada?", """<p>Se você tem uma prova no calendário, procure avaliação com antecedência. Assim dá tempo de tratar a dor e ajustar o treino sem pressa. Para provas que misturam corrida e força, veja a página de <a href="/fisioterapia-hyrox-campinas/">fisioterapia para Hyrox</a>.</p>"""),
        ],
        "faq": [
            ("Preciso trocar de tênis?", "Talvez, mas raramente o tênis é a única causa. A avaliação mostra se vale a pena trocar."),
            ("Atende corredor iniciante?", "Sim. Quem está começando é justamente quem mais sente o aumento rápido de volume."),
            ("Você conversa com o meu treinador?", "Se você quiser, sim, para alinhar a carga de treino com o tratamento."),
        ],
        "rel": ["fisioterapeuta-taquaral-campinas", "fisioterapia-joelho-tornozelo-campinas", "fisioterapia-esportiva-campinas"],
    },
    {
        "slug": "fisioterapia-crossfit-campinas",
        "tipo": "necessidade",
        "menu": "Fisioterapia para CrossFit",
        "resumo": "Ombro, lombar, punho e joelho de quem treina CrossFit.",
        "title": "Fisioterapia para CrossFit em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapeuta para praticantes de CrossFit em Campinas: dor no ombro, lombar, punho e joelho. Tratamento sem largar o box, quando possível.",
        "h1": "Fisioterapia para quem treina CrossFit em Campinas",
        "lead": "Eu conheço o box por dentro: snatch, kipping, wall ball, double under e WOD longo. Quando aparece dor em algum movimento, a avaliação mostra o que está sobrecarregado e o que dá para manter no treino enquanto você trata.",
        "wa": "Olá! Treino CrossFit e gostaria de agendar uma avaliação de fisioterapia.",
        "area": "Campinas",
        "foto": ("foto-barra", "Mulher treinando na barra", "50% 30%"),
        "secoes": [
            ("As queixas mais comuns no box", """<ul>
<li><strong>Ombro</strong>: dor em movimentos acima da cabeça, ginástica e kipping. Leia <a href="/blog/dor-no-ombro-crossfit/">dor no ombro no CrossFit</a>.</li>
<li><strong>Lombar</strong>: levantamento terra, kettlebell swing e volumes altos de levantamento.</li>
<li><strong>Punho</strong>: front rack, handstand e apoios.</li>
<li><strong>Joelho</strong>: agachamentos, saltos e corrida dentro do WOD.</li>
</ul>"""),
            ("Tratar sem parar de treinar", """<p>Na maioria dos casos dá para adaptar: trocar um movimento, mudar a carga ou a amplitude e manter o restante do treino. Eu passo as adaptações por escrito e, se você quiser, alinho com o seu coach. Parar tudo é exceção, e quando for necessário eu explico os critérios para voltar.</p>"""),
            ("Avaliação de movimento", """<p>Além dos testes clínicos, avalio os movimentos que doem: agachamento, overhead, puxadas e o que mais for preciso. Medimos força e mobilidade dos dois lados para encontrar diferenças. Veja também <a href="/fisioterapia-esportiva-campinas/">fisioterapia esportiva</a>.</p>"""),
        ],
        "faq": [
            ("Posso continuar indo ao box?", "Na maioria dos casos, sim, com adaptações. A avaliação define o que manter e o que ajustar."),
            ("Você atende no box?", "Depende da estrutura e da autorização do box. Também atendo em casa e no Instituto Adara."),
            ("Atende atleta de competição?", "Sim, e também quem treina por saúde. O plano muda conforme o objetivo."),
        ],
        "rel": ["fisioterapia-ombro-campinas", "fisioterapia-coluna-campinas", "fisioterapia-hyrox-campinas"],
    },
    {
        "slug": "fisioterapia-hyrox-campinas",
        "tipo": "necessidade",
        "menu": "Fisioterapia para Hyrox",
        "resumo": "Preparação e tratamento para quem vai competir no Hyrox.",
        "title": "Fisioterapia para Hyrox em Campinas | Ed Ferrari Jr",
        "desc": "Fisioterapeuta para atletas de Hyrox em Campinas: dor no joelho, lombar e panturrilha, avaliação preventiva antes da prova e plano de recuperação.",
        "h1": "Fisioterapia para quem treina Hyrox em Campinas",
        "lead": "O Hyrox junta 8 km de corrida com estações como sled push, sled pull, burpee broad jump, lunges e wall balls. É muito volume para joelhos, lombar e panturrilhas. Eu ajudo quem treina para a prova a tratar a dor e a chegar ao dia da competição bem preparado.",
        "wa": "Olá! Estou treinando para o Hyrox e gostaria de agendar uma avaliação de fisioterapia.",
        "area": "Campinas",
        "foto": ("foto-sled", "Atleta durante prova de sled push", "50% 40%"),
        "secoes": [
            ("Onde o Hyrox mais cobra", """<ul>
<li><strong>Joelhos</strong>: lunges com saco, wall balls e corrida com as pernas já cansadas.</li>
<li><strong>Lombar</strong>: sled push e sled pull, farmers carry e remo.</li>
<li><strong>Panturrilha e tendão de Aquiles</strong>: corrida somada aos empurrões do sled.</li>
<li><strong>Ombros</strong>: wall balls em volume alto.</li>
</ul>
<p>Leia o artigo <a href="/blog/hyrox-prevencao-de-lesoes/">Hyrox: as 4 regiões que mais reclamam</a>.</p>"""),
            ("Avaliação antes da prova", """<p>Uma avaliação algumas semanas antes do bloco mais pesado de treino ajuda a encontrar déficits de força, mobilidade e diferenças entre os lados. Com isso, ajustamos o que dá tempo de ajustar antes da prova, sem mexer no que já está funcionando.</p>"""),
            ("Depois da prova", """<p>A recuperação também faz parte do plano. Além da fisioterapia, a <a href="/ferrari-recovery-campinas/">Ferrari Recovery</a> tem bota de compressão e banheira de gelo para quem quer cuidar da recuperação depois de treinos e provas.</p>"""),
        ],
        "faq": [
            ("A prova está perto e estou com dor. Ainda dá tempo?", "Depende da dor e de quanto tempo falta. Na avaliação eu digo o que é possível ajustar e o que é melhor deixar para depois da prova."),
            ("Você atende quem faz Hyrox em dupla ou revezamento?", "Sim. O plano considera as estações que você vai fazer."),
            ("Preciso estar com dor para marcar?", "Não. A avaliação preventiva é para quem quer chegar mais preparado."),
        ],
        "rel": ["fisioterapia-esportiva-campinas", "fisioterapia-crossfit-campinas", "fisioterapia-para-corredores-campinas"],
    },
    {
        "slug": "voltar-a-treinar-com-fisioterapeuta-campinas",
        "tipo": "necessidade",
        "menu": "Voltar a treinar com fisioterapeuta",
        "resumo": "Exercício orientado por fisioterapeuta para voltar a treinar depois da dor.",
        "title": "Voltar a Treinar Depois de Lesão em Campinas | Ed Ferrari Jr",
        "desc": "Parou de treinar por causa de dor ou lesão? Fisioterapeuta em Campinas para guiar a volta ao treino com exercício terapêutico e progressão de carga.",
        "h1": "Voltar a treinar depois de dor ou lesão, com fisioterapeuta",
        "lead": "Muita gente que procura \"personal perto de mim\" está, na verdade, tentando voltar a treinar depois de uma dor ou de uma cirurgia, e tem medo de piorar. Nessa fase, o profissional indicado é o fisioterapeuta: eu avalio, trato e conduzo os exercícios até você estar pronto para voltar ao treino normal.",
        "wa": "Olá! Quero voltar a treinar depois de uma dor/lesão e gostaria de agendar uma avaliação.",
        "area": "Campinas",
        "foto": ("foto-remo", "Atleta no remo ergômetro", "50% 40%"),
        "secoes": [
            ("Para quem é", """<ul>
<li>Quem parou de treinar por causa de dor no ombro, joelho, coluna ou outra região.</li>
<li>Quem terminou o pós-operatório e ainda não se sente seguro para voltar à academia ou ao box.</li>
<li>Quem tenta voltar e a dor reaparece toda vez que a carga sobe.</li>
</ul>"""),
            ("Como funciona", """<ol>
<li><strong>Avaliação</strong>: dor, força, mobilidade e os movimentos do seu treino.</li>
<li><strong>Exercício terapêutico</strong>: exercícios escolhidos para a sua lesão, com carga que sobe aos poucos.</li>
<li><strong>Testes de retorno</strong>: quando os números de força e função mostram que você está pronto, você volta ao treino normal.</li>
</ol>"""),
            ("E depois?", """<p>A fisioterapia cuida da fase de reabilitação. Quando você estiver liberado, segue com o seu treinador ou personal de confiança, e eu passo para ele o que foi feito e o que merece atenção. Veja também <a href="/fisioterapia-esportiva-campinas/">fisioterapia esportiva</a> e <a href="/fisioterapia-lesoes-musculares-campinas/">lesões musculares</a>.</p>"""),
        ],
        "faq": [
            ("Você é personal trainer?", "Não. Sou fisioterapeuta ({crefito}). Eu conduzo a reabilitação e a volta ao treino; depois, o treino de rotina fica com um profissional de educação física."),
            ("Posso fazer as sessões na academia do meu prédio?", "Sim, desde que o condomínio permita. Também atendo em casa e no Instituto Adara."),
            ("Quanto tempo leva para voltar?", "Depende da lesão e de como você responde. Na avaliação eu explico as etapas e os critérios de cada uma."),
        ],
        "rel": ["fisioterapia-esportiva-campinas", "fisioterapia-lesoes-musculares-campinas", "fisioterapeuta-campinas"],
    },
]
