import pyautogui
from time import sleep
from colorama import init, Fore
import sys
##
init()
##
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
##
class Spammer(object):
	##
	def reverse_counter():
		for i in range(5, -1, -1):
			sleep(1)
			print(Fore.RED + str(i))
	##
	def spam():
		with open(r'C:\Users\Jesewe\Downloads\RFT\RFT.txt', encoding = 'latin-1') as file:
			for j in file:
				pyautogui.typewrite(j)
				pyautogui.press('enter')
	##
	pyautogui.alert(text='Вас приветствует \"f0rk1l spam script\"', button='Начать работу')
	confirm = pyautogui.confirm(text='Какую функцию вы хотите использовать?', buttons=['Spammer', 'Справка', 'Отмена'], title='Выбор фунции')
	##
	if confirm == 'Справка':
		text_ = '''
это спам-скроипт который спамит текстом bee movie script.
Но если вы хотите использовать другой текст то измените файл \"RFT.txt\"(текст обязательно должен быть на английском для корректного вывода).
Для дострочного завершения работы программы наведите курсор в левый верхний угол экрана.
'''
		label = pyautogui.alert(text=text_, button = 'OK', title='Справка')
		if label == 'OK':
			dub_confirm = pyautogui.confirm('какую функцию вы хотите использовать?', buttons = ['Spammer', 'Cancel'], title='Выбор фунции')
			if dub_confirm == 'Spammer':
				reverse_counter()
				spam()
			else:
				sys.exit()
	##
	elif confirm == 'Spammer':
		reverse_counter()
		spam()
	##
	else:
		sys.ex