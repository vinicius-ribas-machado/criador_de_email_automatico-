import pyautogui
import time
import random

#lembrar de deixar o email em uma segunda guia pra o prejeto iniciar com "alt + tab"
time.sleep(0.4)
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.hotkey('F5')
time.sleep(3)

#evolução do projeto poderia ser colocado um "inpput" para vc escolher os nomes
no =['vinicius','sabrina','jose','maria','marcos']
sobrenome = ['silva','machado','pereira','lovato']
numeros = ['0','1','2','3','4','5','6','7','8','9']
carc = ['!','@','#','%']

#gerar o nome
nome=random.choice(no)
sobre = random.choice(sobrenome)

#coloar nome e sobrenome
pyautogui.write(nome)
time.sleep(0.5)
pyautogui.hotkey('tab')
pyautogui.write(sobre)
time.sleep(1)
pyautogui.hotkey('tab')

#gerador de email forte

email1 = random.choice(numeros)
email2 = random.choice(numeros)
email3 = random.choice(numeros)
email4 = random.choice(numeros)


time.sleep(2)
pyautogui.write(sobre)
pyautogui.write(nome)
pyautogui.write(sobre)

n1 =pyautogui.write(email2),pyautogui.write(email3),pyautogui.write(email4)

#gerar uma senha forte
caract =random.choice(carc)
caract1 =random.choice(carc)
caract2 =random.choice(carc)

time.sleep(1)
pyautogui.hotkey('tab')
#pyautogui.hotkey('tab')
time.sleep(2)
pyautogui.write(sobre)
pyautogui.write(email2)
pyautogui.write(email2)
pyautogui.write(caract)
pyautogui.write(caract2)
pyautogui.write(caract1)

pyautogui.click(655,706)
time.sleep(1)
pyautogui.doubleClick(768,629)
pyautogui.click(768,629)
time.sleep(1)
pyautogui.hotkey('ctrl','c')
time.sleep(0.5)
pyautogui.hotkey('tab')
time.sleep(1)
pyautogui.hotkey('ctrl','v')

#clicr em continuar
