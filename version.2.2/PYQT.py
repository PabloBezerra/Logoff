# IMPORTAÇÕES

from PyQt6 import uic, QtWidgets, QtGui
import os
from time import sleep

# FUNÇÕES DE SISTEMA

def sair(h,m):  # Comando de encerramento do windows
    num = (h * 60) + m
    sec = num * 60
    os.system(f'shutdown /{sigla} /t {sec}')


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
        janela1.quadro_pri.setText(f'{num:02d}')


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
        num = int(janela1.quadro_sec.text())
        num = num + 1 if n == 1 else num - 1
        janela1.quadro_sec.setText(f'{num:02d}')


def inicializador():  # função interna de tratamento e distribuição de dados
    global sigla, condicao
    if janela1.modo.currentText() == 'Desligar':
        sigla = 's'
        condicao = 'Desligado'
    else:
        sigla = 'r'
        condicao = 'Reiniciado'

    h = int(janela1.quadro_pri.text())
    m = int(janela1.quadro_sec.text())

    sair(h,m)
    sucesso(h, m)


def sucesso(h, m):  # função interna da tela de sucesso e do timer de contagem regressiva
    global rodando
    rodando = True
    janela1.close()
    janela2.show()
    janela2.informacao_1.setText(f'Seu Pc será {condicao} em:')
    janela2.verificado.setPixmap(QtGui.QPixmap('verificado.png'))
    s = 00
    hs = h
    mn = m
    while rodando:
        if s <= 0:
            mn -= 1
            s = 59
        else:
            s -= 1
        if mn < 0:
            hs -= 1
            mn = 59
        janela2.informacao_h.setText(f'{hs:02d} : {mn:02d} : {s:02d}')
        QtWidgets.QApplication.processEvents()
        sleep(1)  


def cancelamento():  # função interna de cancelamento da operação
    global rodando 
    rodando = False
    janela2.close()
    janela3.show()
    janela3.cancelar_4.setPixmap(QtGui.QPixmap('cancelado.png'))
    cancelar()
    

def ok():  # função interna de retorno a tela principal
    janela3.close()
    janela1.show()
    

def finalizador():  # função interna de encerramento do programa e bloqueio do usuário caso requerido
    global rodando
    rodando = False
    if janela2.check.isChecked():
        bloquear()
    janela2.close()
    exit()


# VARIAVEIS

sigla = 's'
condicao = 'Desligado'
rodando = True

# INICIANDO O SITEMA

# Inicializando o programa
app = QtWidgets.QApplication([])

janela1 = uic.loadUi('Principal.ui')
janela2 = uic.loadUi('Sucesso.ui')
janela3 = uic.loadUi('Cancelado.ui')

# Configurando janelas
janela1.show()
janela1.setFixedSize(400,500)
janela2.close()
janela2.setFixedSize(400,500)
janela3.close()
janela3.setFixedSize(400,500)

# Configurando botões da primeira principal
janela1.up_pri.clicked.connect(lambda: atualizar_pri(1))
janela1.down_pri.clicked.connect(lambda: atualizar_pri(0))
janela1.up_sec.clicked.connect(lambda: atualizar_sec(1))
janela1.down_sec.clicked.connect(lambda: atualizar_sec(0))

janela1.btn_iniciar.clicked.connect(inicializador)

# Configurando botões da primeira de sucesso
janela2.btn_cancelar.clicked.connect(cancelamento)
janela2.btn_finalizar.clicked.connect(finalizador)

# Configurando botões da primeira de cancelamento
janela3.btn_ok.clicked.connect(ok)

app.exec()
