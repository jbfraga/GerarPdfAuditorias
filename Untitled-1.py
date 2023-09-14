
import sys
def consulta_Eorder(num_TdC,nome_municipio):

    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.options import Options


    import pandas
    import pyautogui
    import time
    from PIL import Image

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": rf"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\imagens",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        'profile.default_content_setting_values.automatic_downloads': 1
    })
    options = webdriver.ChromeOptions()
    options.headless = False
    options.add_argument("--window-position=1200,0")
    options.add_experimental_option("prefs", chrome_options._experimental_options["prefs"])
    driver = webdriver.Chrome(service=Service(), options=options)

    # %%
    """#Login Eorder"""

    driver.get("https://eordercoe.enel.com/geocallcoe/w/LoginServlet")
    driver.find_elements(By.ID, "USER")[0].send_keys("ENELINT\BR0012049443")
    driver.find_elements(By.ID, "INPUTPASS")[0].send_keys("Saca40f31f1!")
    driver.find_elements(By.ID, "COMPANY")[0].send_keys("")
    driver.find_elements(By.ID, "submbtn")[0].click()
    driver.maximize_window()


    # %%
    """Acessar Lista TDC"""
    driver.find_elements(By.CSS_SELECTOR,"#TBB_tbm2 > div.tbi")[4].click()
    driver.find_elements(By.CSS_SELECTOR,"#TBB_tbm2 > div.tbi")[0].click()

    # %%
    """Enviar o TDC e acessar os locais de print"""

    driver.find_element(By.XPATH, '//td[label/text() = "Código TdC"]/following-sibling::td[1]//table[1]//tr[1]//td[1]//input').send_keys(num_TdC)
    driver.find_element(By.XPATH, '//td[label/text() = "Código TdC"]/following-sibling::td[1]//table[1]//tr[1]//td[1]//input').send_keys(Keys.ENTER)

    time.sleep(3)

    driver.find_elements(By.CSS_SELECTOR,"img[src='r/std/icons/cerca64.png'")[3].click()
    time.sleep(2)



    # %%
    """Acessar a página multimida"""

    driver.find_elements(By.CSS_SELECTOR,"img[src='r/std/icons/PC64.png'")[0].click()

    # %%
    """Baixar as Fotos do Eorder"""

    """clicar em cada linha da foto"""
    foto_Even = driver.find_elements(By.CSS_SELECTOR, "#TV-rvRfmu > div > div > div > table > tbody > tr.tvRow.tvRoll")

    # Itere sobre a lista de elementos e aplique um clique duplo em cada um
    for i in range(len(foto_Even)):
        try:
            # Refaça a pesquisa do elemento a cada iteração
            elemento = driver.find_elements(By.CSS_SELECTOR, "#TV-rvRfmu > div > div > div > table > tbody > tr.tvRow.tvRoll")[i]
            driver.execute_script("var evt = new MouseEvent('dblclick', { bubbles: true, cancelable: true, view: window }); arguments[0].dispatchEvent(evt);", elemento)
            time.sleep(10)
        except Exception as e:
            print(f"Erro: {str(e)}")
    time.sleep(1)
    driver.find_elements(By.CSS_SELECTOR, "img[src='r/std/icons/chiudi64.png']")[2].click()


    # %%
    """Clicar em Visualizar planejamento TdC"""

    time.sleep(3)
    driver.find_elements(By.CSS_SELECTOR,"img[src='r/std/icons/cerca64.png'")[0].click()

    elements = driver.find_elements(By.CSS_SELECTOR, "img[src='r/std/icons/cerca64.png']")
    if elements:
        last_element = elements[-1]  # Acessa o último elemento da lista
        last_element.click()

    # %%
    """Print do retorno de campo e OBS"""

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--window-position=1420,0")

    driver.find_element(By.CSS_SELECTOR, "#flowscrew").click()

    time.sleep(1)

    screen = driver.find_elements(By.CSS_SELECTOR,"#MTA-sfEsitoAgenda-HLCasdfa")[0]

    screen.screenshot(rf"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\imagens\img1.png")

    time.sleep(1)

    text_inputss = driver.find_elements(By.TAG_NAME,'textarea')
    for text_input in text_inputss:
        if "NOTESERVIZIO" in text_input.get_attribute("name"):
            text_input.screenshot(rf"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\imagens\img3.png")
            break

    driver.find_element(By.CSS_SELECTOR, "#flowscrew").click()


    # %%
    """Print dos materiais"""
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,"icon_pullright").click()

    time.sleep(3)

    driver.find_elements(By.CSS_SELECTOR, "img[src='r/std/icons/articoli64.png'")[1].click()

    time.sleep(1)

    driver.find_elements(By.CSS_SELECTOR, "#MTT-mtListaMateriali-ncMaterialiGiorno > div:nth-child(1) > img")[0].click()

    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, "#flowscrew").click()

    time.sleep(1)

    driver.execute_script('document.querySelectorAll("#TVSCR-tv_materialigiorno")[0].style.height="100%";')
    time.sleep(1)

    element = driver.find_elements(By.CSS_SELECTOR,"#TVSCR-tv_materialigiorno > div > table")[0]
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'start', inline: 'start' });", element)

    time.sleep(1)

    screen = driver.find_elements(By.CSS_SELECTOR,"#TVSCR-tv_materialigiorno > div > table")[0]
    screen.screenshot(rf"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\imagens\img2.png")

    driver.quit()


    # %%
    """Juntando as imagens em um pdf"""
    """falta só ele dinamicamente renomear o PDF final"""

    from PIL import Image
    import os

    # Diretório onde as imagens estão localizadas
    image_dir = rf"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\imagens"

    # Lista de arquivos de imagem no diretório
    image_files = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    images = []

    for path in image_files:
        image = Image.open(path)
        
        

        if image.mode == 'RGBA':
            image = image.convert("RGB")  # Converter para RGB se estiver no modo RGBA
        
        if path.endswith(".jpg"):
                # Redimensionar a imagem JPG para um tamanho específico (por exemplo, 800x600)
                width, height = 384, 512
                image = image.resize((width, height), Image.ANTIALIAS)
        
        images.append(image)

    pdf_path = r"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\resultado\{}_{}.pdf".format(num_TdC, nome_municipio)

    # Salvar as imagens no arquivo PDF
    images[0].save(
        pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )


    # %%
    """Arrumando o PDF"""
    """Falta estudar um Resize das fotos para não ficarem muito grandes,
    mas já está considerando aqui a junção das fotos em uma só pagina, uma após a outra"""
    import os
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas


    # Diretório onde as imagens estão localizadas
    image_dir = rf"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\imagens"

    # Lista de arquivos de imagem no diretório
    image_files = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir)]

    pdf_path = r"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\resultado\{}_{}.pdf".format(num_TdC, nome_municipio)

    # Tamanho de página A4 em pontos (595.276 x 841.890)
    page_width, page_height = A4
    max_width = page_width - 40  # Margens de 20 pontos em ambos os lados
    max_height = page_height - 40

    c = canvas.Canvas(pdf_path, pagesize=A4)

    # Configurações de layout para as imagens
    x_offset = 20
    y_offset = page_height - 20  # Começar do topo da página
    new_page = True

    for image_path in image_files:
        image = Image.open(image_path)
        
        # Redimensionar a imagem para 70% do tamanho original
        width_percent = 50
        width = int(image.width * (width_percent / 100))
        height = int(image.height * (width_percent / 100))
        image = image.resize((width, height), Image.ANTIALIAS)
            
        # Redimensionar a imagem para caber na página (mantendo a proporção)
        image.thumbnail((max_width, max_height))
        
        # Verificar se a imagem cabe na página atual
        if y_offset - image.height < 20:
            # Iniciar uma nova página
            c.showPage()
            y_offset = page_height - 20  # Começar do topo da nova página
            new_page = True
        
        if new_page:
            new_page = False
        else:
            # Adicionar um espaço vertical entre as imagens
            y_offset -= 10
        
        # Desenhar a imagem na página
        c.drawImage(image_path, x_offset, y_offset - image.height, width=image.width, height=image.height)
        
        # Atualizar a posição para a próxima imagem
        y_offset -= image.height
    
    c.save()

    # %%
    """Excluindo as fotos da pasta"""

    dir = rf'C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\imagens'
    for file in os.scandir(dir):
        os.remove(file.path)


if __name__ == "__main__":
    num_de_TdC = sys.argv[1]
    nome_mun = sys.argv[2]
    consulta_Eorder(num_de_TdC,nome_mun)