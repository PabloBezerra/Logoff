from PyQt6 import uic,QtWidgets
import os
from time import sleep

# FUNÇÕES DE SISTEMA

def sair(h,m):  # Comando de encerramento do windows
    num = (h * 60) + m
    sec = num * 60
    os.system(f'shutdown /{variaveis[0]} /t {sec}')


def cancelar():  # Comando de cancelamento de encerramento do windows
    os.system('shutdown -a')


def bloquear():  # Comando de bloquear o usuário do windows
    os.system('rundll32.exe user32.dll,LockWorkStation')

# FUNÇÕES DE OPERAÇÃO

def atualizar_pri(n): # Função interna de funcionamento da primeira dezena
    if janela1.quadro_pri.text() == '99' and janela1.quadro_sec.text() == '00' and n == 1:
        janela1.quadro_pri.setText('01')
    elif janela1.quadro_pri.text() == '01' and janela1.quadro_sec.text() == '00' and n == 0:
        janela1.quadro_pri.setText('99')
    elif janela1.quadro_pri.text() == '99' and n == 1:
        janela1.quadro_pri.setText('00')
    elif janela1.quadro_pri.text() == '00' and n == 0:
        janela1.quadro_pri.setText('99')
    else:
        num = int(janela1.quadro_pri.text())
        num = num + 1 if n == 1 else num - 1
        if num < 10:
            janela1.quadro_pri.setText(f'0{num}')
        else:
            janela1.quadro_pri.setText(f'{num}')

def atualizar_sec(n): # Função interna de funcionamento da segunda dezena
    if janela1.quadro_sec.text() == '01' and janela1.quadro_pri.text() == '00' and n == 0:
        janela1.quadro_sec.setText('59')
    elif janela1.quadro_sec.text() == '59' and janela1.quadro_pri.text() == '00' and n == 1:
        janela1.quadro_sec.setText('01')
    elif janela1.quadro_sec.text() == '59' and n == 1:
        janela1.quadro_sec.setText('00')
    elif janela1.quadro_sec.text() == '00' and n == 0:
        janela1.quadro_sec.setText('59')
    else:
        num = (int(janela1.quadro_sec.text()))
        num = num + 1 if n == 1 else num - 1
        if num < 10:
            janela1.quadro_sec.setText(f'0{num}')
        else:
            janela1.quadro_sec.setText(f'{num}')

def inicializador():
    if janela1.modo.currentText() == 'Desligar':
        variaveis[0] = 's'
        variaveis[1] = 'Desligado'
    else:
        variaveis[0] = 'r'
        variaveis[1] = 'Reiniciado'

    h = int(janela1.quadro_pri.text())
    m = int(janela1.quadro_sec.text())

    variaveis[2] = 'Hora' if h == 1 or h == 0 else 'Horas'
    variaveis[3] = 'Minuto' if m == 1 or m == 0 else 'Minutos'

    #sair(h,m)
    sucesso(h, m)
    contador(h, m)

def sucesso(h, m):
    janela1.close()
    janela2.show()
    janela2.informacao1.setText(f'Seu Pc será {variaveis[1]}')

def contador(h,m):
    

def cancelamento():
    janela2.close()
    janela3.show()
    cancelar()
    
def ok():
    janela3.close()
    janela1.show()

def finalizador():
    if janela2.check.isChecked():
        bloquear()

    janela2.close()
    exit()

# VARIAVEIS

variaveis = ['s', 'Desligado']

# INICIANDO O SITEMA

app = QtWidgets.QApplication([])
janela1 = uic.loadUi('Principal.ui')
janela2 = uic.loadUi('Sucesso.ui')
janela3 = uic.loadUi('Cancelado.ui')

janela1.show()
janela2.close()
janela3.close()

janela1.up_pri.clicked.connect(lambda: atualizar_pri(1))
janela1.down_pri.clicked.connect(lambda: atualizar_pri(0))
janela1.up_sec.clicked.connect(lambda: atualizar_sec(1))
janela1.down_sec.clicked.connect(lambda: atualizar_sec(0))

janela1.btn_iniciar.clicked.connect(inicializador)

janela2.btn_cancelar.clicked.connect(cancelamento)
janela2.btn_finalizar.clicked.connect(finalizador)

janela3.btn_ok.clicked.connect(ok)

app.exec()
