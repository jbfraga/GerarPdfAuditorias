import sys
def consulta_GPM(num_TdC,numero_ordem,nome_municipio,cod_SOB):
        
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.options import Options
    import os
    import time
    from PIL import Image
    from credenciais import login_GPM,senha_GPM
    import json


    options = webdriver.ChromeOptions()
    
    settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], "selectedDestinationId": "Save as PDF", "version": 2}

    options.add_experimental_option("prefs", {
        "download.default_directory": r'C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\resultado.pdf',
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        'profile.default_content_setting_values.automatic_downloads': 1,
        'printing.print_preview_sticky_settings.appState': json.dumps(settings)
    })

    # options.headless = False
    options.add_argument("--window-position=1200,0")
    options.add_argument('--kiosk-printing')
    """options.add_argument('--disable-print-preview')"""
    # options.add_argument('--print-to-pdf=nome_do_arquivo.pdf')

    driver = webdriver.Chrome(service=Service(), options=options)



    driver.get("https://cosampa.gpm.srv.br/gpm/geral/consulta_servico.php")
    tela_consulta_serv = driver.window_handles[0]
    tela_login = driver.window_handles[1]


    #Login
    driver.switch_to.window(tela_login)
    driver.find_element(By.CSS_SELECTOR,"#idLogin").send_keys(login_GPM)
    driver.find_element(By.CSS_SELECTOR,"#idSenha").send_keys(senha_GPM)
    driver.find_element(By.CLASS_NAME,"blogin").click()
    driver.switch_to.window(tela_consulta_serv)
    driver.maximize_window()
    print("LOGIN OK")


    #Pesquisando a ordem

    driver.find_element(By.CSS_SELECTOR,"#num_se").send_keys(cod_SOB)
    driver.find_element(By.NAME,"submit").click()
    driver.find_elements(By.CSS_SELECTOR,"img[src='https://s3.amazonaws.com/s3-gpm/includes/icons/print.png']")[0].click()
    tela_pdf = driver.window_handles[1]
    driver.switch_to.window(tela_pdf)
    driver.maximize_window()
    time.sleep(3)
    print("ORDEM ACESSADA")

    #Removendo linhas
    driver.execute_script("var l = document.querySelector('body > div:nth-child(11)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(2)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(2)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(2)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(3)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(5)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(6)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(8)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(8)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(8)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(8)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(8)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(9)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > div:nth-child(35)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > div:nth-child(37) > div.div_head').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > div:nth-child(37) > div:nth-child(15)').remove()")
    time.sleep(0.1)
    driver.find_element(By.CSS_SELECTOR,"#btn_mostra_fotos").click()
    time.sleep(5)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(13)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(13)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > table.tbl_head > tbody > tr:nth-child(13)').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > div:nth-child(37) > input.dt-button.btn_pdf').remove()")
    time.sleep(0.1)
    driver.execute_script("var l = document.querySelector('body > div:nth-child(37) > input.dt-button.btn_doc').remove()")
    time.sleep(0.1)
    print("LINHAS REMOVIDAS")


    #Aumentando imgs
    driver.execute_script(
        "let aumentarImagens = document.querySelector('#div_fotos').querySelectorAll('img');aumentarImagens.forEach((el) => {el.style.width = '40%';})")
    print("IMAGENS AUMENTADAS")

    
    driver.execute_script('window.print();')
    time.sleep(5)
    driver.quit()

    
    import shutil

    # Defina o caminho para a pasta "Downloads" em seu sistema
    pasta_downloads = os.path.expanduser("~") + "\\Downloads"

    # Verifique se a pasta "Downloads" existe
    if os.path.exists(pasta_downloads):
        # Nome do arquivo que você deseja renomear
        nome_arquivo_antigo = "cosampa.gpm.srv.br_gpm_geral_relatorio_servico.php.pdf"

        # Caminho completo para o arquivo antigo
        caminho_arquivo_antigo = os.path.join(pasta_downloads, nome_arquivo_antigo)

        # Nome que você deseja dar ao arquivo
        nome_arquivo_novo = "{}_{}_jupiter.pdf".format(numero_ordem,nome_municipio)

        # Caminho completo para o arquivo novo
        caminho_arquivo_novo = os.path.join("C:\\Users\\bruno.fraga\\Desktop\\ADS\\Códigos Cosampa\\Gerar Pdf Auditoria\\GerarPdfAuditorias\\resultado", nome_arquivo_novo)

        # Verifique se o arquivo antigo existe na pasta "Downloads"
        if os.path.exists(caminho_arquivo_antigo):
            # Renomeie o arquivo
            shutil.move(caminho_arquivo_antigo, caminho_arquivo_novo)
            print(f"Arquivo renomeado para {nome_arquivo_novo}")
        else:
            print("O arquivo antigo não foi encontrado na pasta 'Downloads'.")
    else:
        print("A pasta 'Downloads' não foi encontrada no seu sistema.")
    print("GPM FINALIZADO")
if __name__ == "__main__":
    num_de_TdC = sys.argv[1]
    nome_mun = sys.argv[3]
    num_ordem = sys.argv[2]
    codigo_SOB = sys.argv[4]
    consulta_GPM(num_de_TdC,num_ordem,nome_mun,codigo_SOB)
