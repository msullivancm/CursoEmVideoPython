'''
pip install pandas
pip install requests
pip install bs4
'''
import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

page = requests.get("https://arte.engpro.totvs.com.br/protheus/padrao/published/repositorio/lobo_guara/", auth=HTTPBasicAuth('marcus.motta', 'senha'))

if page.status_code >= 200 and page.status_code <= 400:
    soup = BeautifulSoup(page.content, 'html.parser')
    selecao = [a['href'] for a in soup.select('a[href]')]
    for sel in selecao:
        print(repr(sel).replace("""<p class="hui-highlight-title hui-highlight-title--primario">""", "").replace("""</p>""",""))

