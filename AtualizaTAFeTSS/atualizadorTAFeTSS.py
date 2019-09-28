'''
O que este programa se propõe:
 Baixar pacotes de atualização via Scraping;
	Lembrando que os patchs devem ser baixados com data superior a do rpo;
	Os dicionários devem ser baixados com data superior ao dicionário completo/diferencial da release;
 Descompactar arquivos baixados;
 Parar os serviços do TAF WS, TAF, DBAccess, TSS e DBAccess do TSS;
 Sobrepor o conteúdo dos arquivos baixados e descompactados para seus respectivos diretórios no TAF e TSS;
 Limpar arquivos temporários e inúteis;
 Iniciar os serviços do DBAccess, TAF;
 Abrir o cliente do TAF para executar o UPDDistr e UPDTAF;
 Abrir o cliente do TAF para acessar o TAF e atualizar as tabelas autocontidas;
 Iniciar os serviços do DBAccess, TAF, TAF WS, DBAccess do TSS e TSS.
'''

import requests
import os
import shutil
import zipfile
from zipfile import ZipFile
from datetime import date
from requests.auth import HTTPBasicAuth

urls = ["https://arte.engpro.totvs.com.br/protheus/padrao/published/repositorio/lobo_guara/TTTP120.RPO",
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
        ]

def extSemDir(my_dir, my_Zip):
    with zipfile.ZipFile(my_Zip) as Zip_file:
        for member in Zip_file.namelist():
            filename = os.path.basename(member)
            # skip directories
            if not filename:
                continue
            # copy file (taken from zipfile's extract)
            source = Zip_file.open(member)
            target = open(os.path.join(my_dir, filename), "wb")
            with source, target:
                shutil.copyfileobj(source, target)

def estrutura(caminho, arquivo):
    if arquivo[len(arquivo) - 3:].lower() == 'zip':
        with ZipFile(arquivo, 'r') as zipObj:
            if url.lower().__contains__("menu") or \
                    url.lower().__contains__("arquivos_de_configuracao") or \
                    url.lower().__contains__("stored_procedures"):
                zipObj.extractall(caminho + "\\protheus_data\\system")
            elif url.lower().__contains__("dicionario_de_dados") or url.lower().__contains__(
                    "help_de_campo") or url.lower().__contains__("web-files"):
                if url.upper().__contains__("BRA_DICIONARIO"):
                    _lista = url.split('/')
                    _arquivo = lista[len(lista) - 1]
                    zipObj.extractall(caminho + "\\protheus_data\\systemload\\" + _arquivo)
                elif url.upper().__contains__("HELPS_DIF"):
                    extSemDir(caminho + "\\protheus_data\\systemload", arquivo)
                elif url.lower().__contains__("web-files"):
                    extSemDir(caminho + "\\protheus_data\\systemload", arquivo)
                else:
                    zipObj.extractall(caminho + "\\protheus_data\\systemload")
            elif url.lower().__contains__("includes"):
                zipObj.extractall(caminho + "\\include")
            elif url.lower().__contains__("appserver") or url.lower().__contains__("webapp"):
                zipObj.extractall(caminho + "\\bin\\appserver")
            elif url.lower().__contains__("dbaccess"):
                zipObj.extractall(caminho + "\\bin\\dbaccess")
            elif url.lower().__contains__("smartclient"):
                zipObj.extractall(caminho + "\\bin\\smartclient")
    else:
        if url.lower().__contains__("repositorio"):
            if not os.path.exists(caminho + "\\apo\\tttp120.rpo"):
                if not os.path.exists(caminho + "\\apo"):
                    os.makedirs(caminho + "\\apo")
                shutil.copy(arquivo, caminho + "\\apo\\tttp120.rpo")
        elif url.lower().__contains__("libs"):
            if not os.path.exists(caminho + "\\apo\\lib.tttp120.ptm"):
                if not os.path.exists(caminho + "\\apo"):
                    os.makedirs(caminho + "\\apo")
                shutil.copy(arquivo, caminho + "\\apo\\lib.tttp120.ptm")

def estrBasica(caminho):
    if not os.path.exists(caminho + "\\protheus_data\\system\\sigaadv.pss"):
        shutil.copy("sigaadv.pss", caminho + "\\protheus_data\\system")
    if not os.path.exists(caminho + "\\protheus_data\\cprova"):
        os.mkdir(caminho + "\\protheus_data\\cprova")
    if not os.path.exists(caminho + "\\protheus_data\\data"):
        os.mkdir(caminho + "\\protheus_data\\data")
        if not os.path.exists(caminho + "\\protheus_data\\pli"):
            os.mkdir(caminho + "\\protheus_data\\pli")
        if not os.path.exists(caminho + "\\protheus_data\\spool"):
            os.mkdir(caminho + "\\protheus_data\\spool")
        if not os.path.exists(caminho + "\\protheus_data\\workflow"):
            os.mkdir(caminho + "\\protheus_data\\workflow")
        if not os.path.exists(caminho + "\\protheus_data\\comex"):
            os.mkdir(caminho + "\\protheus_data\\comex")
        if not os.path.exists(caminho + "\\protheus_data\\crystal"):
            os.mkdir(caminho + "\\protheus_data\\crystal")
        if not os.path.exists(caminho + "\\protheus_data\\esb"):
            os.mkdir(caminho + "\\protheus_data\\esb")
        if not os.path.exists(caminho + "\\protheus_data\\ireport"):
            os.mkdir(caminho + "\\protheus_data\\ireport")
        if not os.path.exists(caminho + "\\protheus_data\\neogrid"):
            os.mkdir(caminho + "\\protheus_data\\neogrid")
        if not os.path.exists(caminho + "\\protheus_data\\sara"):
            os.mkdir(caminho + "\\protheus_data\\sara")
        if not os.path.exists(caminho + "\\protheus_data\\systemload"):
            os.mkdir(caminho + "\\protheus_data\\systemload")
        if not os.path.exists(caminho + "\\protheus_data\\system"):
            os.mkdir(caminho + "\\protheus_data\\system")
        if not os.path.exists(caminho + "\\protheus_data\\semaforo"):
            os.mkdir(caminho + "\\protheus_data\\semaforo")


login = input("Informe seu login: ")
senha = input("Informe sua senha: ")
dirDownload = input('Informe o caminho para download dos arquivos: ')
dirBuild = dirDownload + '\\' + str(date.today())
for url in urls:
    lista = url.split('/')
    arquivo = dirBuild + '\\' + lista[len(lista) - 1]
    if not os.path.exists(dirBuild):
        os.makedirs(dirBuild)
    if not os.path.exists(arquivo):
        page = requests.get(url, auth=HTTPBasicAuth(login, senha))
        if page.status_code == 200:
            open(arquivo, 'wb').write(page.content)
    else:
        print('{} já existe'.format(arquivo))
    estrutura(dirBuild, arquivo)
estrBasica(dirBuild)
