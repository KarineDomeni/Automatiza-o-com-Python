# Passo a passo do projeto.
# Passo 1: Entrar no site da empresa.
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 1

# Clicando na tecla windows e abrindo o navegador.
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link.
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Uma pausa um pouco maior (3 seg.):
time.sleep (3)

# Passo 2: Fazer login.
# Selecionar o campo de e-mail.
pyautogui.click(x=900, y=408)

# Escrever o seu e-mail.
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste9876543210@")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de produtos pra cadastrar.
import pandas
tabela = pandas.read_csv("produtos.csv")
#print(tabela)

# Passo 4: Cadastrar um produto.
# Para cada linha da tabela 
for linha in tabela.index:
    # Clicar no campo de código do produto.
    pyautogui.click(x=788, y=292)

    # Pegar da tabela o valor do campo que quero preencher.
    #Preenchendo campos:
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #Se não estiver vazia a obs escrever, se não, pular.
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    # Cadastrando o produto (botão enviar).
    pyautogui.press("enter")

    # Dar scroll de tudo pra cima.
    pyautogui.scroll(15000) 

# Passo 5: Repetir o processo de cadastro até o fim