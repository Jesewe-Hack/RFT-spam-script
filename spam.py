# импортирование необходимых модулей
import pyautogui
from time import sleep
from colorama import init, Fore
import sys
##
init() # вызов функции для корректного цветного вывода модуля "colorama" 
##
pyautogui.PAUSE = 0.1 # задержка в 0.1 секунд
pyautogui.FAILSAFE = True # экстренное завершение работы при наведении курсора в левый-верхний угол экрана
##
def reverse_counter(): # отвечает за обратный отсчёт
	for i in range(5, -1, -1):
		sleep(1)
		print(Fore.RED + str(i))
##
def spam(): # отвечает за спам
	with open(r'C:\Users\User\Downloads\RFT\RFT.txt', 'r',encoding = 'latin-1') as file: # считывание файла RFT.txt
		for j in file:
			pyautogui.typewrite(j) # автоматический ввод текста(поставить в графу ввода текста)
			pyautogui.press('enter') # отправка сообщения(или спуск на новую строку если вы его запустили в редакторе текста)
##
pyautogui.alert(text='Вас приветствует \"f0rk1l spam script\"', button='Начать работу')
confirm = pyautogui.confirm(text='Какую функцию вы хотите использовать?', \
			    buttons=['Spammer', 'Справка', 'Отмена'], \
			    title='Выбор фунции') # выбор функци
##
if confirm == 'Справка':
	text_ = '''
это спам-скрипт который спамит текстом \"bee movie script\".
Но если вы хотите использовать другой текст то измените файл \"RFT.txt\"(текст обязательно должен быть на английском для корректного вывода).
Для дострочного завершения работы программы наведите курсор в левый верхний угол экрана.

'''
# вывод справки и дальнейший выбор действий
	label = pyautogui.alert(text=text_, \
				button = 'OK', \
				title='Справка') # вывод справки(для дальнейшего выбора действий нажминте на "OK")
	if label == 'OK':
		dub_confirm = pyautogui.confirm('какую функцию вы хотите использовать?',  \
						buttons = ['Spammer', 'Отмена'], title='Выбор фунции') # выбор дальнейших действий после получения справки
		if dub_confirm == 'Spammer':
			reverse_counter() # запуск обратного отчёта(обратный отчёт выводится в консоль)
			spam() # запуск спам-скрипта
		else:
			sys.exit() # завершение работы программы
##
elif confirm == 'Spammer':
	reverse_counter() # запуск обратного отчёта(обратный отчёт выводится в консоль)
	spam() # запуск спам-скрипта
##
else:
	sys.exit # завершение работы программы
