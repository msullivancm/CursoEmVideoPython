import wget
import requests
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
for url in urls:
    if url.find("MENU"):
        page = requests.get(url, auth=HTTPBasicAuth('marcus.motta', 'senha'))
        lista = url.split('/')
        if page.status_code == 200:
            open(lista[len(lista)-1], 'wb').write(page.content)