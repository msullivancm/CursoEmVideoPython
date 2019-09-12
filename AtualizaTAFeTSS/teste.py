'''
O que este programa se propõe:
 Baixar pacotes de atualização via Scraping;
 Descompactar arquivos baixados;
 Parar os serviços do TAF WS, TAF, DBAccess, TSS e DBAccess do TSS;
 Sobrepor o conteúdo dos arquivos baixados e descompactados para seus respectivos diretórios no TAF e TSS;
 Limpar arquivos temporários e inúteis;
 Iniciar os serviços do DBAccess, TAF;
 Abrir o cliente do TAF para executar o UPDDistr e UPDTAF;
 Abrir o cliente do TAF para acessar o TAF e atualizar as tabelas autocontidas;
 Iniciar os serviços do DBAccess, TAF, TAF WS, DBAccess do TSS e TSS.
'''

'''
"https://arte.engpro.totvs.com.br/protheus/padrao/published/repositorio/lobo_guara/TTTP120.RPO",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/arquivos_de_configuracao/ARQUIVOS_CONFIGURACAO_FISCAL.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/dicionario_de_dados/atualizacoes_manutencoes/19-07-15-BRA_DICIONARIO_FISCAL_MANUTENCAO.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/dicionario_de_dados/atualizacoes_manutencoes/19-07-18-BRA_DICIONARIO_DIF_MANUTENCAO_SIGAMNT.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/dicionario_de_dados/atualizacoes_manutencoes/19-08-27-BRA_DICIONARIO_DIF_SIGATMS_MANUTENCAO.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/dicionario_de_dados/atualizacoes_manutencoes/19-08-28-BRA_DICIONARIO_FISCAL_MANUTENCAO.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/dicionario_de_dados/atualizacoes_manutencoes/19-08-29_BRA_DICIONARIO_DIF_FINANCEIRO_CNAB_J52.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/dicionario_de_dados/atualizacoes_manutencoes/19-09-02-BRA_DICIONARIO_DIF_MANUTENCAO_SIGAMDT.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/dicionario_de_dados/completo/BRA-DICIONARIOS_COMPL.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/dicionario_de_dados/diferencial/BRA-DICIONARIOS_DIF.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/help_de_campo/completo/BRA-HELPS_COMPL.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/help_de_campo/diferencial/BRA-HELPS_DIF.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/menus/BRA-MENUS.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/menus/BRA-MENU_COMPLEMENTAR_SIGAPCP.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/menus/BRA-MENUS_COMPLEMENTAR_RH.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/stored_procedures/STORED_PROCEDURES.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/web-files/WEB-FILES.ZIP",
        "https://arte.engpro.totvs.com.br/framework/includes/lobo_guara/published/includes.zip",
        "https://arte.engpro.totvs.com.br/framework/libs/lib/published/lobo_guara/TTTP120.PTM",
        "https://arte.engpro.totvs.com.br/tec/appserver/lobo_guara/windows/64/published/appserver.zip",
        "https://arte.engpro.totvs.com.br/tec/dbaccess/windows/64/published/dbaccess.zip",
        "https://arte.engpro.totvs.com.br/tec/smartclient/lobo_guara/windows/64/published/smartclient.zip",
        "https://arte.engpro.totvs.com.br/tec/smartclientwebapp/lobo_guara/windows/64/published/webapp.zip",
        "https://arte.engpro.totvs.com.br/tss/published/instaladores/windows/P12_TSS3.0_RELEASE_12.1.25_WINDOWS.ZIP",
        "https://arte.engpro.totvs.com.br/tss/published/schemas/TSS_SCHEMAS_RELEASE_12.1.25.ZIP",
        "https://arte.engpro.totvs.com.br/tss/published/arquivos_de_url/TSS_URLS_RELEASE_12.1.17.ZIP"
'''

import requests
import os
from zipfile import ZipFile
from datetime import date
from requests.auth import HTTPBasicAuth

urls = ["https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/menus/BRA-MENU_COMPLEMENTAR_SIGAPCP.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/menus/BRA-MENUS_COMPLEMENTAR_RH.ZIP",
        "https://arte.engpro.totvs.com.br/protheus/padrao/published/dicionario/stored_procedures/STORED_PROCEDURES.ZIP"
]

def criaDir(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        return True

def estrutura(caminho, arquivo):
    caminho = caminho+"\\build"+date.today()
    with ZipFile(arquivo, 'r') as zipObj:
        if url.lower().__contains__("menu") or url.lower().__contains__("arquivos_de_configuracao") or url.lower().__contains__("stored_procedures"):
            if criaDir(caminho + "\\protheus_data\\system"):
                zipObj.extractall(caminho+"\\protheus_data\\system")
        elif url.lower().__contains__("repositorio"):
            if criaDir(caminho + "\\apo"):
                os.renames(arquivo, caminho + "\\apo\\tttp120.rpo")
        elif url.lower().__contains__("dicionario_de_dados") or url.lower().__contains__("help_de_campo") or url.lower().__contains__("web-files") or url.lower().__contains__("libs"):
            criaDir(caminho + "\\protheus_data\\systemload")
            zipObj.extractall(caminho+"\\protheus_data\\systemload")
        elif url.lower().__contains__("includes"):
            criaDir(caminho + "\\include")
            zipObj.extractall(caminho+"\\include")
        elif url.lower().__contains__("appserver") and url.lower().__contains__("webapp"):
            criaDir(caminho+"\\bin\\appserver")
            zipObj.extractall(caminho+"\\bin\\appserver")
        elif url.lower().__contains__("dbaccess"):
            criaDir(caminho+"\\bin\\dbaccess")
            zipObj.extractall(caminho+"\\bin\\dbaccess")
        elif url.lower().__contains__("smartclient"):
            criaDir(caminho+"\\bin\\smartclient")
            zipObj.extractall(caminho+"\\bin\\smartclient")

nome = input("Informe seu login: ")
senha = input("Informe sua senha: ")
caminho = input('Informe o caminho para download dos arquivos: ')

for url in urls:
    page = requests.get(url, auth=HTTPBasicAuth(nome, senha))
    lista = url.split('/')
    arquivo = caminho + '\\' + lista[len(lista) - 1]
    if page.status_code == 200:
        if criaDir(caminho):
            if not os.path.exists(arquivo):
                open(arquivo, 'wb').write(page.content)
                print(arquivo)
                estrutura(arquivo)

