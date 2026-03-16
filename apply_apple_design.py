import os
import subprocess

html_file = r"C:\Users\edwil\.openclaw\workspace\meu_novo_site\index.html"

premium_html = """<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dr. Ed Ferrari Jr | Fisioterapeuta Especialista</title>
    <meta name="description" content="Especialista em Fisioterapia Ortopédica e Esportiva, tratamento de Coluna e Joelho no Swiss Park, Campinas.">
    <meta name="robots" content="index, follow">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/style.css">

    <style>
        body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background-color: #fbfbfd; color: #1d1d1f; }
        
        /* Apple-like Typography */
        .headline-hero { font-size: clamp(3rem, 8vw, 6rem); line-height: 1.05; letter-spacing: -0.04em; font-weight: 800; }
        .subhead-hero { font-size: clamp(1.2rem, 3vw, 1.8rem); line-height: 1.4; letter-spacing: -0.01em; font-weight: 500; color: #86868b; }
        .headline-section { font-size: clamp(2.5rem, 5vw, 4rem); line-height: 1.1; letter-spacing: -0.03em; font-weight: 800; }
        
        /* Bento Box Grid */
        .bento-card { background: #ffffff; border-radius: 28px; padding: 40px; box-shadow: 0 4px 24px rgba(0,0,0,0.04); transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease; border: 1px solid rgba(0,0,0,0.02); }
        .bento-card:hover { transform: scale(1.02); box-shadow: 0 12px 40px rgba(0,0,0,0.08); }
        
        .bento-card-dark { background: #1d1d1f; border-radius: 28px; padding: 40px; border: 1px solid rgba(255,255,255,0.05); transition: transform 0.4s ease; }
        .bento-card-dark:hover { transform: scale(1.02); }

        /* Premium Buttons */
        .btn-primary { background-color: #1d1d1f; color: #ffffff; border-radius: 999px; padding: 14px 28px; font-weight: 600; font-size: 1rem; transition: all 0.3s ease; display: inline-flex; align-items: center; justify-content: center; gap: 8px; }
        .btn-primary:hover { background-color: #333336; transform: scale(1.02); }
        
        .btn-accent { background-color: #c4302b; color: #ffffff; border-radius: 999px; padding: 14px 28px; font-weight: 600; font-size: 1rem; transition: all 0.3s ease; display: inline-flex; align-items: center; justify-content: center; gap: 8px; }
        .btn-accent:hover { background-color: #a12521; transform: scale(1.02); box-shadow: 0 8px 20px rgba(196,48,43,0.3); }

        /* Glassmorphism Header */
        .glass-header { background: rgba(251, 251, 253, 0.8); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid rgba(0,0,0,0.05); }

        /* Subtle Fade In Animation */
        .fade-in-up { animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; transform: translateY(30px); }
        .delay-100 { animation-delay: 100ms; }
        .delay-200 { animation-delay: 200ms; }
        .delay-300 { animation-delay: 300ms; }
        @keyframes fadeInUp { to { opacity: 1; transform: translateY(0); } }

        /* Custom Dark Section Gradient */
        .dark-section { background: radial-gradient(circle at top, #2a2a2d 0%, #000000 70%); color: #f5f5f7; }
    </style>
</head>

<body class="antialiased selection:bg-[#c4302b] selection:text-white">

    <!-- HEADER -->
    <header class="fixed top-0 w-full z-50 glass-header transition-all duration-300">
        <div class="max-w-7xl mx-auto px-6 flex justify-between items-center h-16">
            <div class="font-bold text-xl tracking-tight text-[#1d1d1f]">
                Ed Ferrari Jr<span class="text-[#c4302b]">.</span>
            </div>
            <nav class="hidden md:flex gap-8 items-center">
                <a href="#inicio" class="text-sm font-medium text-[#1d1d1f]/70 hover:text-[#1d1d1f] transition">Início</a>
                <a href="#especialidades" class="text-sm font-medium text-[#1d1d1f]/70 hover:text-[#1d1d1f] transition">Tratamentos</a>
                <a href="#recovery" class="text-sm font-medium text-[#1d1d1f]/70 hover:text-[#1d1d1f] transition">Recovery</a>
            </nav>
            <a href="https://api.whatsapp.com/send?phone=5519971002263&text=Olá!%20Gostaria%20de%20agendar%20uma%20avaliação." target="_blank" class="btn-primary px-5 py-2 text-sm">
                Agendar
            </a>
        </div>
    </header>

    <!-- HERO SECTION -->
    <main id="inicio" class="pt-40 pb-24 md:pt-52 md:pb-32 px-6 overflow-hidden flex flex-col items-center text-center">
        <div class="max-w-4xl mx-auto z-10">
            <span class="text-[#c4302b] font-bold tracking-widest uppercase text-sm md:text-base mb-6 block fade-in-up">Swiss Park, Campinas</span>
            <h1 class="headline-hero mb-8 fade-in-up delay-100">
                O movimento perfeito.<br>A vida sem dor.
            </h1>
            <p class="subhead-hero mb-12 max-w-2xl mx-auto fade-in-up delay-200">
                Fisioterapia Ortopédica e Esportiva de alto nível. Diagnóstico preciso e reabilitação avançada para você voltar a fazer o que ama.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center items-center fade-in-up delay-300">
                <a href="https://api.whatsapp.com/send?phone=5519971002263" target="_blank" class="btn-accent text-lg w-full sm:w-auto">
                    <i class="fa-brands fa-whatsapp"></i> Falar com Especialista
                </a>
            </div>
        </div>
    </main>

    <!-- BIO SECTION -->
    <section id="sobre" class="py-24 px-6 bg-white">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
                <div class="rounded-[2rem] overflow-hidden shadow-2xl relative">
                    <img src="assets/img/image_1.png" alt="Dr Ed Ferrari Jr" class="w-full h-auto object-cover hover:scale-105 transition duration-700" loading="lazy">
                </div>
                <div>
                    <h2 class="headline-section mb-6">A ciência<br>por trás da cura.</h2>
                    <p class="text-[#86868b] text-xl mb-6 leading-relaxed">
                        Como Mestre pela UNICAMP e especialista em Ortopedia, o Dr. Ed Ferrari Jr. não trata apenas sintomas. Ele investiga a <strong>raiz biomecânica</strong> da sua dor.
                    </p>
                    <p class="text-[#86868b] text-xl leading-relaxed">
                        Nossa filosofia é simples: eficiência máxima no tratamento com o menor número de sessões possíveis. O foco é a sua independência.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- ESPECIALIDADES (BENTO GRID) -->
    <section id="especialidades" class="py-32 px-6">
        <div class="max-w-7xl mx-auto text-center mb-20">
            <h2 class="headline-section">Áreas de especialidade.</h2>
            <p class="subhead-hero mt-4">Soluções definitivas para o seu corpo.</p>
        </div>
        
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            
            <div class="bento-card flex flex-col items-start">
                <img src="assets/img/image_2.png" alt="Coluna" class="w-16 h-16 mb-6 rounded-2xl shadow-sm" loading="lazy">
                <h3 class="text-2xl font-bold mb-3 text-[#1d1d1f]">Coluna Vertebral</h3>
                <p class="text-[#86868b] font-medium leading-relaxed">Hérnia de disco, dor lombar aguda, ciatalgia e correções posturais focadas em alívio rápido e estabilidade.</p>
            </div>

            <div class="bento-card flex flex-col items-start">
                <img src="assets/img/image_4.png" alt="Joelho" class="w-16 h-16 mb-6 rounded-2xl shadow-sm" loading="lazy">
                <h3 class="text-2xl font-bold mb-3 text-[#1d1d1f]">Joelho e LCA</h3>
                <p class="text-[#86868b] font-medium leading-relaxed">Reabilitação cirúrgica e conservadora. Menisco, condromalácia, tendinite patelar e retorno ao esporte seguro.</p>
            </div>

            <div class="bento-card flex flex-col items-start">
                <img src="assets/img/image_3.png" alt="Ombro" class="w-16 h-16 mb-6 rounded-2xl shadow-sm" loading="lazy">
                <h3 class="text-2xl font-bold mb-3 text-[#1d1d1f]">Ombro Esportivo</h3>
                <p class="text-[#86868b] font-medium leading-relaxed">Síndrome do impacto, manguito rotador, tendinites e capsulite. Foco em atletas de CrossFit, Tênis e natação.</p>
            </div>

            <div class="bento-card flex flex-col items-start lg:col-span-2 bg-gradient-to-br from-gray-50 to-gray-100">
                <h3 class="text-3xl font-bold mb-4 text-[#1d1d1f]">Alta Performance</h3>
                <p class="text-[#86868b] text-lg font-medium leading-relaxed mb-8 max-w-xl">
                    Seu protocolo não termina quando a dor some; termina quando você bate seu Recorde Pessoal. Avaliação biomecânica e periodização de força para atletas.
                </p>
                <a href="https://api.whatsapp.com/send?phone=5519971002263" class="btn-primary">Saber mais <i class="fa-solid fa-arrow-right text-sm"></i></a>
            </div>

            <div class="bento-card flex flex-col items-start">
                <img src="assets/img/image_6.png" alt="Tornozelo" class="w-16 h-16 mb-6 rounded-2xl shadow-sm" loading="lazy">
                <h3 class="text-2xl font-bold mb-3 text-[#1d1d1f]">Tornozelo e Corrida</h3>
                <p class="text-[#86868b] font-medium leading-relaxed">Fascite plantar, entorses e análise de corrida para transição segura nas pistas.</p>
            </div>

        </div>
    </section>

    <!-- RECOVERY (DARK MODE) -->
    <section id="recovery" class="py-32 px-6 dark-section">
        <div class="max-w-7xl mx-auto text-center mb-20">
            <span class="text-[#c4302b] font-bold tracking-widest uppercase text-sm mb-4 block">Ferrari Recovery</span>
            <h2 class="headline-section text-white">Recuperação de elite.<br>Na sua casa.</h2>
            <p class="text-gray-400 mt-6 text-xl max-w-2xl mx-auto">Aluguel de equipamentos profissionais para acelerar sua recuperação muscular no Swiss Park e região.</p>
        </div>

        <div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
            <!-- Bota -->
            <div class="bento-card-dark flex flex-col text-center items-center">
                <img src="assets/img/image_11.webp" alt="Bota Pneumática" class="w-full h-64 object-cover rounded-xl mb-8" loading="lazy">
                <h3 class="text-3xl font-bold mb-4 text-white">Bota Pneumática</h3>
                <p class="text-gray-400 mb-8 font-medium">Compressão avançada. Drena toxinas, elimina o ácido lático e reduz o inchaço pós-treino imediatamente.</p>
                <div class="mt-auto w-full">
                    <div class="text-4xl font-bold text-white mb-6">R$ 347<span class="text-lg text-gray-500 font-medium">/diária</span></div>
                    <a href="https://api.whatsapp.com/send?phone=5519971002263" target="_blank" class="w-full bg-white text-black rounded-full px-6 py-3 font-bold hover:bg-gray-200 transition inline-block">Reservar Bota</a>
                </div>
            </div>

            <!-- Gelo -->
            <div class="bento-card-dark flex flex-col text-center items-center">
                <img src="assets/img/image_12.webp" alt="Banheira de Gelo" class="w-full h-64 object-cover rounded-xl mb-8" loading="lazy">
                <h3 class="text-3xl font-bold mb-4 text-white">Banheira de Gelo (Ice Bath)</h3>
                <p class="text-gray-400 mb-8 font-medium">Crioterapia padrão ouro. Controle máximo de inflamação e recuperação profunda do sistema nervoso central.</p>
                <div class="mt-auto w-full">
                    <div class="text-4xl font-bold text-white mb-6">R$ 247<span class="text-lg text-gray-500 font-medium">/diária</span></div>
                    <a href="https://api.whatsapp.com/send?phone=5519971002263" target="_blank" class="w-full bg-white text-black rounded-full px-6 py-3 font-bold hover:bg-gray-200 transition inline-block">Reservar Banheira</a>
                </div>
            </div>
        </div>

        <div class="max-w-5xl mx-auto mt-8">
            <div class="bento-card-dark bg-gradient-to-r from-[#1d1d1f] to-[#2a1312] border-[#c4302b]/30 flex flex-col md:flex-row justify-between items-center text-left">
                <div class="mb-8 md:mb-0">
                    <span class="bg-[#c4302b] text-white text-xs font-bold uppercase tracking-wider py-1 px-3 rounded-full mb-4 inline-block">Recomendado</span>
                    <h3 class="text-3xl font-bold text-white mb-2">Combo PRO (Fim de Semana)</h3>
                    <p class="text-gray-400 font-medium">Bota de Compressão + Banheira de Gelo por 2 dias completos.</p>
                </div>
                <div class="text-center md:text-right">
                    <div class="text-4xl font-bold text-white mb-4">R$ 594</div>
                    <a href="https://api.whatsapp.com/send?phone=5519971002263" target="_blank" class="btn-accent whitespace-nowrap">Quero o Combo</a>
                </div>
            </div>
        </div>
    </section>

    <!-- LOCATION -->
    <section class="py-32 px-6 bg-white text-center">
        <div class="max-w-3xl mx-auto">
            <i class="fa-solid fa-house-chimney-medical text-5xl text-[#c4302b] mb-8"></i>
            <h2 class="headline-section mb-6">Sua casa.<br>Sua clínica.</h2>
            <p class="text-[#86868b] text-xl mb-12 leading-relaxed">
                Atendimento exclusivo no formato <strong>Home Care no Swiss Park</strong> e região. O nível de um centro de reabilitação de elite, com a privacidade e o conforto do seu lar.
            </p>
            <a href="https://api.whatsapp.com/send?phone=5519971002263" target="_blank" class="btn-primary text-lg">
                Solicitar Atendimento Domiciliar
            </a>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-[#f5f5f7] py-16 px-6 border-t border-gray-200">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8">
            <div class="text-[#1d1d1f] font-bold text-xl">
                Ed Ferrari Jr.
            </div>
            <div class="flex gap-6">
                <a href="https://www.instagram.com/edferrarijr" target="_blank" class="text-[#86868b] hover:text-[#1d1d1f] text-2xl transition"><i class="fa-brands fa-instagram"></i></a>
                <a href="https://www.youtube.com/@EdFerrariJr" target="_blank" class="text-[#86868b] hover:text-[#1d1d1f] text-2xl transition"><i class="fa-brands fa-youtube"></i></a>
            </div>
            <div class="text-[#86868b] text-sm">
                © 2026 Dr. Ed Ferrari Jr. Todos os direitos reservados.
            </div>
        </div>
    </footer>

</body>
</html>
"""

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(premium_html)

os.chdir(r"C:\Users\edwil\.openclaw\workspace\meu_novo_site")
subprocess.run(['npx', 'tailwindcss', '-i', r'css\input.css', '-o', r'css\style.css', '--minify'])
print("Redesign Apple-style aplicado e CSS recompilado com sucesso.")