# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import unittest
import os
import time
from PIL import Image


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": rf"C:\Users\bruno.fraga\Desktop\ADS\Códigos Cosampa\Gerar Pdf Auditoria\GerarPdfAuditorias\resultado",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False,
    'profile.default_content_setting_values.automatic_downloads': 1
})
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument("--window-position=-1200,0")
chrome_options.add_argument('--kiosk-printing')
"""chrome_options.add_argument('--disable-print-preview')
chrome_options.add_argument('--print-to-pdf=nome_do_arquivo.pdf')"""
options.add_experimental_option("prefs", chrome_options._experimental_options["prefs"])
driver = webdriver.Chrome(service=Service(), options=options)


# %%
driver.get("https://cosampa.gpm.srv.br/gpm/geral/consulta_servico.php")
tela_consulta_serv = driver.window_handles[0]
tela_login = driver.window_handles[1]

# %%
#Login
driver.switch_to.window(tela_login)
driver.find_element(By.CSS_SELECTOR,"#idLogin").send_keys("JARVIS_NAC")
driver.find_element(By.CSS_SELECTOR,"#idSenha").send_keys("123Mudar!")
driver.find_element(By.CLASS_NAME,"blogin").click()
driver.switch_to.window(tela_consulta_serv)
driver.maximize_window()


# %%
#Pesquisando a ordem

driver.find_element(By.CSS_SELECTOR,"#num_se").send_keys(184521358)
driver.find_element(By.NAME,"submit").click()
driver.find_elements(By.CSS_SELECTOR,"img[src='https://s3.amazonaws.com/s3-gpm/includes/icons/print.png']")[0].click()
tela_pdf = driver.window_handles[1]
driver.switch_to.window(tela_pdf)
driver.maximize_window()
time.sleep(3)

# %%
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

# %%
driver.execute_script("""
    let aumentarImagens = document.querySelector('#div_fotos').querySelectorAll('img');
    aumentarImagens.forEach((el) => {
        el.style.width = '40%';
    });
""")