import os
rows = open("Listatdc.txt", "r").read().split("\n")

for row in rows:
    cols = row.split(";")
    os.system("python Eorder.py {} {} {} {}".format(cols[0], cols[1],cols[2],cols[3]))
    dir = r'imagens'
    for file in os.scandir(dir):
        os.remove(file.path)
        
for row in rows:
    cols = row.split(";")
    
    os.system("python GPM.py {} {} {} {}".format(cols[0], cols[1],cols[2],cols[3]))

import openpyxl

# Função para listar os arquivos em uma pasta e criar uma planilha Excel com os nomes
def listar_arquivos_em_excel(pasta):
    # Inicializar um objeto Workbook
    workbook = openpyxl.Workbook()
    # Selecionar a planilha padrão (Sheet)
    sheet = workbook.active
    
    # Listar os arquivos na pasta especificada
    arquivos = os.listdir(pasta)
    
    # Iterar sobre a lista de arquivos e adicioná-los à planilha
    for i, arquivo in enumerate(arquivos, start=1):
        sheet.cell(row=i, column=1, value=arquivo)
    
    # Salvar a planilha em um arquivo Excel
    excel_file = os.path.join(pasta, 'nomes_arquivos.xlsx')
    workbook.save(excel_file)

if __name__ == "__main__":
    pasta_alvo = 'resultado'  # Substitua pelo caminho da pasta desejada
    listar_arquivos_em_excel(pasta_alvo)
    print(f'Nomes dos arquivos salvos em {os.path.join(pasta_alvo, "nomes_arquivos.xlsx")}')
