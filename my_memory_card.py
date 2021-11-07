from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox,QButtonGroup

class Question():#функция
    def __init__(
    self,question,right_answer,
    wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer 
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []#список

q1 = Question('Какое первое издание Сары Маарс','Трон','Корона','Убийство по королевски','Кровь которую никто не видел' )#вопрос
question_list.append(q1)#добавление

q2 = Question('Сколько в мире океанов','4','5','3','2' )#вопрос
question_list.append(q2)#добавление

q3 = Question('Сколько  млииардов людей на земле ','7','3','4','1' )#вопрос
question_list.append(q3)#добавление

q4 = Question('Как исследуют Антарктиду','просто','никак','никак','никак' )#вопрос
question_list.append(q4)#добавление

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400,400)

'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Какой национальности не существует?') # текст вопроса

#---------
AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('правильно/неправильно')
correct = QLabel('правильный ответ')

layout = QVBoxLayout()
layout.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))#добавление виджета
layout.addWidget(correct, alignment = Qt.AlignCenter)#добавление виджета

AnsGroupBox.setLayout(layout)
#--------

RadioGroupBox = QGroupBox('Варианты ответов:')
btn1 = QRadioButton('Энцы')#конпка
btn2 = QRadioButton('Чулымцы')#конпка
btn3 = QRadioButton('Смурфы')#конпка
btn4 = QRadioButton('Алеуты')#конпка

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)


layout_ans3 = QHBoxLayout()# adding Layout к линии
layout_ans3 = QHBoxLayout()## adding Layout к линии
layout_ans1 = QVBoxLayout()## adding Layout к линии
layout_ans2 = QVBoxLayout()## adding Layout к линии

layout_ans1.addWidget(btn1)#добавление конпки
layout_ans1.addWidget(btn3)#добавление конпки

layout_ans2.addWidget(btn2)#добавление конпки
layout_ans2.addWidget(btn4)#добавление конпки

layout_ans3.addLayout(layout_ans1)# adding Layout к линии
layout_ans3.addLayout(layout_ans2)# adding Layout к линии

RadioGroupBox.setLayout(layout_ans3)#добавление радиокнопки

line1 = QHBoxLayout()#создание линии
line2 = QHBoxLayout()#создание линии
line3 =QHBoxLayout()#создание линии

line1.addWidget(lb_Question, alignment= Qt.AlignCenter)#
line2.addWidget(RadioGroupBox)
line2.addWidget(AnsGroupBox)
line3.addWidget(btn_OK, stretch=2)
AnsGroupBox.hide()
main = QVBoxLayout()#главное Лейаут
main.addLayout(line1)#главное Лейаут к линии
main.addLayout(line2)#главное Лейаут к линии 
main.addLayout(line3)#главное Лейаут к линии

window.setLayout(main)

def show_result(): #функция
    RadioGroupBox.hide()#Скрытие радиокнопок
    AnsGroupBox.show()#Скрытие ответов которые не выбраны как главные
    btn_OK.setText('Следующий вопрос')#Перемена надписи на кнопке


def show_question():# Создание функции
    AnsGroupBox.hide()#Скрытие ответов которые не выбраны как главные
    RadioGroupBox.show()#Показ радиокнопок 
    btn_OK.setText('Ответить')# Изменение надписи на кнопке
    RadioGroup.setExclusive(False)# Опровержение параметра радиогруппы
    btn1.setChecked(False)# Опровержение параметра радиогруппы
    btn2.setChecked(False)#  Опровержение параметра радиогруппы
    btn3.setChecked(False)# Опровержение параметра радиогруппы
    btn4.setChecked(False)# Опровержение параметра радиогруппы
    RadioGroup.setExclusive(True)

'''def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

btn_OK.clicked.connect(test)'''


answers = [btn1,btn2,btn3,btn4] # список 

def ask(q: Question):#функция
    shuffle(answers)# перемешивание ответов
    answers[0].setText(q.right_answer) # привязка к элементам списка
    answers[1].setText(q.wrong1)# привязка к элементам списка
    answers[2].setText(q.wrong2)# привязка к элементам списка
    answers[3].setText(q.wrong3)# привязка к элементам списка
    lb_Question.setText(q.question)# изменение текста
    correct.setText(q.right_answer)# изменение текста
    show_question()# показать вопрос

def show_correct(res):#функция
    result.setText(res)
    show_result()

def check_answer():#функция
    if answers[0].isChecked():#цикл
        show_correct('Right!')
    else:
        if answers[1].isChecked():
            show_correct('False!')
        if answers[2].isChecked():
            show_correct('False!')
        if answers[3].isChecked():
            show_correct('False!')

def next_question():
    window.total +=1
    print('Статистика\n, всего вопросов', window.total)
    window.cur_question += 1 
    if window.cur_question >= len(question_list):
        window.cur_question = 0

    q = question_list[window.cur_question]
    ask(q)



def click_Ok():
    
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()
window.cur_question = -1
btn_OK.clicked.connect(click_Ok)

window.score = 0
window.total  = 0
#кнопка Ок присоединяется к функции
window.show()
app.exec()