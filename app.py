# REconhecimento de imagem simples com pyautogui
import pyautogui

captcha = pyautogui.locateCenterOnScreen('captcha.png')
pyautogui.click(captcha[0],captcha[1],duration=2)