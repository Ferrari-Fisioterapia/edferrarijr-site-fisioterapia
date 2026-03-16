import re
html_file = r"C:\Users\edwil\.openclaw\workspace\meu_novo_site\index.html"
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Header link
html = html.replace('href="https://api.whatsapp.com/send?phone=5519971002263"', 'href="https://api.whatsapp.com/send?phone=5519971002263&text=Olá!%20Gostaria%20de%20saber%20mais%20sobre%20os%20atendimentos%20no%20Swiss%20Park."')

# Revert specific existing links that might have been duplicated if they already had &text
html = html.replace('&text=Olá!%20Gostaria%20de%20saber%20mais%20sobre%20os%20atendimentos%20no%20Swiss%20Park."&text=', '&text=')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
