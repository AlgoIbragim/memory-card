from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel) 
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'))
questions_list.append(Question('Сколько планет в солнечной системе?', '8', '12', '1', '9'))
questions_list.append(Question('На каком языке разговаривают а Бразилии?', 'Португальский', 'Бразильский', 'Английский', 'Французский'))
questions_list.append(Question('Кто самый богатый человек в мире?', 'Бернар Арно', 'Илон маск', 'Марк Цукерберг', 'Билл Гейтс'))
questions_list.append(Question('Какой город является самым посещаемым в мире?', 'Париж', 'Нью-Йорк', 'Токио', 'Лондон'))
questions_list.append(Question('Какое из этих морей считается самым солёным?', 'Мёртвое море', 'Каспийское море', 'Средиземное море', 'Красное море'))
questions_list.append(Question('В каком году был основан первый компьютерный бренд IBM?', '1935', '1945', '1955', '1965'))
questions_list.append(Question('Как называется феномен, когда луна полностью заслоняет солнце?', 'Солнечное затмение', 'Лунное затмение', 'Солнечный ветер', 'Парадокс Шрёдингера'))
questions_list.append(Question('Какой элемент используется для измерения уровня кислорода в крови?', 'Кислород', 'Железо', 'Магний', 'Углерод'))
questions_list.append(Question('Какой химический элемент является основным компонентом стекла?', 'Кремний', 'Свинец', 'Бор', 'Серебро'))

shuffle(questions_list)

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')

btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Какой национальности не существует?')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1, alignment=Qt.AlignVCenter)
layout_ans2.addWidget(rbtn_2, alignment=Qt.AlignVCenter)
layout_ans3.addWidget(rbtn_3, alignment=Qt.AlignVCenter)
layout_ans3.addWidget(rbtn_4, alignment=Qt.AlignVCenter)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)   

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_main = QVBoxLayout()

layout_main.addLayout(layout_line1, stretch=2)
layout_main.addLayout(layout_line2, stretch=8)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3, stretch=1)
layout_main.addStretch(1)
layout_main.setSpacing(5)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Правильно/Неправильно')
lb_Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

window.setStyleSheet("QWidget {background: rgb(221, 160, 221);}")
btn_OK.setStyleSheet("QPushButton {background: rgb(255,255,0);}")
RadioGroupBox.setStyleSheet("QRadioButton {background: rgb(218, 112, 214);}")
#btn_OK.setStyleSheet('font-weight: bold;')
rbtn_1.setStyleSheet('font-weight: bold;')
rbtn_2.setStyleSheet('font-weight: bold;')
rbtn_3.setStyleSheet('font-weight: bold;')
rbtn_4.setStyleSheet('font-weight: bold;')
lb_Question.setStyleSheet('font-weight: bold;')
#RadioGroupBox.setStyleSheet('font-weight: bold;')
AnsGroupBox.setStyleSheet('font-weight: bold;')
lb_Result.setStyleSheet('font-weight: bold;')
lb_Correct.setStyleSheet('font-weight: bold;')

layout_line2.addWidget(AnsGroupBox)  

window.cur_questio = -1
window.cur_question = -1
window.cur_questions = 0

def show_result():
    Check_Ans()
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
    d = window.cur_questions/window.cur_questio*100
    print('-Всего вопросов:', window.cur_questio)
    print('-Правильных ответов:', window.cur_questions)
    print('Рейтинг:', d, '%')
    print('Статистика')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    print('-Всего вопросов:', window.cur_questio)
    print('-Правильных ответов:', window.cur_questions)
    print('Статистика')

def click_ok():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        next_question()

def Check_Ans():
    if answers[0].isChecked():
        lb_Correct.setText('Правильно')
        window.cur_questions += 1
    else:
        lb_Correct.setText('Неправильно')

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def next_question():
    window.cur_question += 1
    window.cur_questio += 1
    l = len(questions_list)
    if window.cur_question >= len(questions_list):
        window.cur_questio = 1
        window.cur_question = 0
        window.cur_questions = 0
        shuffle(questions_list)
    q = questions_list[window.cur_question]
    ask(q)

window.cur_questio += 1
AnsGroupBox.hide()
next_question()
btn_OK.clicked.connect(click_ok)
window.setLayout(layout_main)
window.show()
app.exec()