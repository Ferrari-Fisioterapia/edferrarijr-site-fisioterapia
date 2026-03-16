import os
import re
import urllib.request

html_file = r"C:\Users\edwil\.openclaw\workspace\meu_novo_site\index.html"
img_dir = r"C:\Users\edwil\.openclaw\workspace\meu_novo_site\assets\img"

os.makedirs(img_dir, exist_ok=True)

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Download images
urls = [
    "https://images.unsplash.com/photo-1631815588090-d4bfec5b1b98?q=80&w=1470&auto=format&fit=crop",
    "https://i.postimg.cc/cLZgKDHV/PERITO-JUDICIAL-E-ASSISTENTE-TECNICO-EM-FISIOTERAPIA-CAMPINAS-SAO-PAULO-Fisioterapeuta-Dr-Ferrar.png",
    "https://i.postimg.cc/hG0xzjwQ/coluna_vector.png",
    "https://i.postimg.cc/9fBTRMSf/ombro_vector.png",
    "https://i.postimg.cc/CK4DB1t5/joelho_vector.png",
    "https://i.postimg.cc/9fBTRMSr/cotovelo_vector.png",
    "https://i.postimg.cc/nL17jz5X/tornozelo_vector.png",
    "https://i.postimg.cc/k5y864ZP/quadril_vector.png",
    "https://i.postimg.cc/t70w12ZD/lupa_vector.png",
    "https://i.postimg.cc/7bvdCmGG/simbulo_quimico_vector.png",
    "https://i.postimg.cc/pyN49qhq/halter_vector.png",
    "https://http2.mlstatic.com/D_NQ_NP_675370-MLB71772756364_092023-O-bota-de-compresso-pneumatica-para-massagem-avanutri.webp",
    "https://acdn-us.mitiendanube.com/stores/003/156/867/products/imagens-site-banheira2_01-120f704fb63a92009b17270501245731-1024-1024.webp"
]

for i, url in enumerate(urls):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        ext = "webp"
        if "png" in url.lower(): ext = "png"
        elif "jpg" in url.lower() or "jpeg" in url.lower(): ext = "jpg"
        
        local_name = f"image_{i}.{ext}"
        local_path = os.path.join(img_dir, local_name)
        
        with urllib.request.urlopen(req) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
            
        html = html.replace(url, f"assets/img/{local_name}")
    except Exception as e:
        print(f"Erro: {url} - {e}")

# 2. Tailwind & Config
html = html.replace('<script src="https://cdn.tailwindcss.com"></script>', '<link rel="stylesheet" href="css/style.css">')
html = re.sub(r'<script>\s*tailwind\.config = \{.*?</script>', '', html, flags=re.DOTALL)

# 3. Preconnect
fonts_preconnect = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Open+Sans:wght@300;400;600&display=swap" rel="stylesheet">
"""
html = re.sub(r'<link href="https://fonts\.googleapis\.com/[^>]+>', fonts_preconnect, html)

# 4. Lazy loading
html = re.sub(r'<img(?!.*loading="lazy")', r'<img loading="lazy"', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
