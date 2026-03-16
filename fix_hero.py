import os
import re
import urllib.request
import subprocess

html_file = r"C:\Users\edwil\.openclaw\workspace\meu_novo_site\index.html"
img_dir = r"C:\Users\edwil\.openclaw\workspace\meu_novo_site\assets\img"

new_bg_url = "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?ixlib=rb-4.0.3&auto=format&fit=crop&w=1470&q=80"
local_name = "hero_bg.jpg"
local_path = os.path.join(img_dir, local_name)

# Baixar imagem
try:
    req = urllib.request.Request(new_bg_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
        out_file.write(response.read())
    print("Imagem de fundo baixada com sucesso!")
except Exception as e:
    print(f"Erro ao baixar: {e}")

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Trocar o CSS da imagem de fundo para usar o arquivo local com overlay escuro
old_css = r"""        \.hero-bg \{
            background: linear-gradient\(to right, rgba\(255,255,255,0\.9\) 40%, rgba\(255,255,255,0\.3\)\), url\('https://images\.unsplash\.com/[^']+'\);
            background-size: cover; 
            background-position: center right;
        \}"""

new_css = """        .hero-bg {
            background: linear-gradient(to right, rgba(18,18,18,0.95) 30%, rgba(18,18,18,0.5)), url('assets/img/hero_bg.jpg');
            background-size: cover; 
            background-position: center;
        }"""
html = re.sub(old_css, new_css, html, flags=re.DOTALL)

# Se n mudou com regex (caso a string n de match exato), vamos tentar outro replace
if new_css not in html:
    # Achar bloco .hero-bg { ... }
    html = re.sub(r'\.hero-bg\s*\{[^}]+\}', new_css, html)

# Trocar textos para branco
html = html.replace('text-gray-900 text-4xl md:text-6xl', 'text-white text-4xl md:text-6xl')
html = html.replace('text-gray-600 font-semibold', 'text-gray-300 font-semibold')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

# Recompilar CSS
os.chdir(r"C:\Users\edwil\.openclaw\workspace\meu_novo_site")
subprocess.run(['npx', 'tailwindcss', '-i', r'css\input.css', '-o', r'css\style.css', '--minify'])
print("HTML atualizado e CSS recompilado.")