'''
Módulos 5 e 6
Projeto Loja da MEO
Dono: Dinis Marques 
Nº 4 - 10ºH
Curso Profissional de Técnico de Gestão e Programação de Sistemas Informáticos 
'''
'''
LT- Largura do Terminal
AT- Altura do Terminal
LS- Login Screen (Ecrã de Login)
SPP- Sistema de Palavra-Passe
PP- Palavra-Passe (Password)
CE- Caracter Escolhido
DT- Desktop (Ambiente de Trabalho)
'''

# Importar as libraria
import shutil as s
from datetime import datetime as dt
import time as t
import calendar as c
import locale as l
import msvcrt as ms
import winsound as ws


# Obter a largura do terminal através das colunas do mesmo (Vertical)
LT = s.get_terminal_size().columns

# Obter a altura do terminal através das linhas do mesmo (Horizontal)
AT = s.get_terminal_size().lines

# Colocar a localização em Portugal (Isto fará com que o dia da semana seja mostrado em Português)
l.setlocale(l.LC_TIME , "pt_PT.UTF-8")

# 1ª Login Screen
def LS():
    # Imprimir o cabeçalho da Login Screen e o ícone
    print("|" + "=" * (LT-2) + "|" , "👤".center(LT))
    # Imprimir o nome de utilizador
    print("MEO Loja".center(LT+2))

    # Sistema de Password
    def SPP():
        # Declarar a variável da Palavra-Passe como global
        global PP

        # Declarar a variável da Palavra-Passe
        PP = ""

        # Ciclo While para esconder a Password atrás de *
        while True:
            # Ocultar o caracter que o utilizador escolheu
            CE = ms.getch().decode("UTF-8")

            # Verificar se o utilizador escolheu a tecla enter
            if(CE == "\r"):
                print()
                return PP
            
            # Verificar se o utilizador escolheu a tecla do backspace
            elif(CE == "\x08"):

                # Se o comprimento da Palavra-Passe for superior a 0
                if len(PP) > 0:
                    # O último caracter da Palavra-Passe armazenada vai ser removido 
                    PP = PP[:-1]
                    # Apagar o último caracter na Login Screen
                    print("\b \b", end="", flush=True)

            # Se nenhuma das condições acima for válida        
            else:
                # Adicionar à Palavra-Passe o Caracter Escolhido
                PP += CE
                # Finalmente mostrar "*" ao invés do atual caracter
                print("*", end = "", flush = True)

    print("Palavra-Passe:\n".center(LT+4), end='', flush=True)
    return SPP()

# Chamar a tela de login 
LS()
