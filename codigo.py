import pyautogui


pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)

pyautogui.press("enter")

pyautogui.click(x=797, y=366)
pyautogui.press("enter")

pyautogui.write("joaovitordev1@hotmail.com")
pyautogui.press("tab")

pyautogui.write("minhasenha123")
pyautogui.press("tab")

pyautogui.press("enter")

# cadastrar os produtos da tabela uma 1 unica vez
import pandas
import time


tabela = pandas.read_csv("produtos.csv")

time.sleep(2)

for linha in tabela.index:
    pyautogui.click(x=725, y=253)



    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo =  marca = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = marca = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = marca = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = marca = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    
    pyautogui.press("enter")

    pyautogui.scroll(10000)

