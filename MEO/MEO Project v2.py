'''
Módulos 5 e 6
Projeto Loja da MEO
Dono: Dinis Marques 
Nº 4 - 10ºH
Curso Profissional de Técnico de Gestão e Programação de Sistemas Informáticos 
'''
'''
Variáveis:
LT- Largura do Terminal
LS- Login Screen (Ecrã de Login)
MP- Menu Principal 
SPP- Sistema de Palavra-Passe
PP- Palavra-Passe (Password)
CE- Caracter Escolhido
'''

# Importar as libraria
import shutil as s
import msvcrt as ms
import winsound as ws

# Obter a largura do terminal através das colunas do mesmo (Vertical)
LT = s.get_terminal_size().columns

# Login Screen
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

    print("Palavra-Passe:\n".center(LT+5), end='', flush=True)
    return SPP()

# Chamar a tela de login 
LS()

# Menu Principal
def MP():
    print(("=" * 10 + "Menu" + "=" * 10).center(LT))
    print(("1- Atendimento Tickets").center(LT))
    print(("2- Adesões/Vendas").center(LT-12))
    print(("3- Pagamentos").center(LT))
    print(("4- Consultar Dados").center(LT-5))
    print(("0- Encerrar Computador").center(LT))
    print(("=" * 24).center(LT))

# Menu 1
def MN1():
    print("=" * 10 + "Atendimento de Tickets" + "=" * 10)
    print("1- Registar Tickets")
    print("2- Atender Tickets")
    print("0- Voltar ao Menu Principal")
    print("=" * 20)

# Menu 1A
def MN1A():
    print("1- Registo c/ Marcação")
    print("2- Registo s/ Marcação")

# Menu 1B
def MN1B():
    print("1- Atendimento c/ Marcação")
    print("2- Atendimento s/ Marcação")


# Menu 2
def MN2():
    print("=" * 10 + "Adesões/Vendas" + "=" * 10)
    print("1- Serviços")
    print("2- Equipamentos")
    print("3- MEO Care")
    print("0- Voltar ao Menu Principal")

# Menu 2A
def MN2A():
    print("1- Serviços para Particulares")
    print("2- Serviços para Empresas")
    print("0- Voltar ao Menu Principal")

# Menu 3
def MN3():
    print("1- Validar Pagamentos de Particulares")
    print("2- Validar Pagamentos de Empresas")
    print("3- Consultar Pagamentos Validados")

# Menu 4
def MN4():
    print("1- Consultar Dados de Particulares")
    print("2- Consultar Dados de Empresas")
    print("0- Voltar para o Menu Principal")

# Set com a lista dos tickets
T = {"A01","A02","A03","B01","B02","B03"}

# Dicionário para os serviços dos particulares
SP = {"Satélite": {"M1": [("M1 TV", [9.49], "€/mês", "Desconto de", [5.50], "€/mês x", [24], "meses", [15.99], "€/mês", "Pack Light", "25 Canais"),
                                  ("M1 TV", [16.49], "€/mês", "Desconto de", [5.50], "€/mês x", [24], "meses", [21.99], "€/mês", "Pack Standard", " 79 Canais")],

                            "M2": [("M2 TV e Voz", [27.99], "€/mês", "Pack Standard", " 79 Canais", "Chamadas para redes fixas nacionais + 50 destinos internacionais")],

                            "M3": [("M3 TV, Net e Voz", [42.49], "€/mês", "1 Mensalidade Paga", "Pack Standard + MEOBox", " 79 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M3 TV, Net e Voz", [43.49], "€/mês", "1 Mensalidade Paga", "Pack Standard + Extra + MEOBox", "3 meses Sport TV HD", " 90 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M3 TV, Net e Voz", [29.49], "€/mês", "Desconto de", [13.00], "€/mês x", [4], "meses", [42.49], "€/mês", "Pack Standard + MEOBox", " 79 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M3 TV, Net e Voz", [35.49], "€/mês", "Desconto de", [8.00], "€/mês x", [6], "meses", [43.49], "€/mês", "Pack Standard + Extra + MEOBox", "3 meses Sport TV HD", " 90 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M3 TV, Net e Voz", [42.49], "€/mês", "Oferta de Honor 90 Smart 5G no valor de", [249.99], "€ por", [89.99], "€", "Pack Standard + MEOBox", " 79 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M3 TV, Net e Voz", [43.49], "€/mês", "Oferta de Coluna Bang & Olufsen no valor de", [199.99], "€ por", [69.99], "€", "Pack Standard + Extra + MEOBox", "3 meses Sport TV HD", " 90 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais")],

                            "M4": [("M4 TV, Net, Voz e Móvel", [63.99], "€/mês", "1 Mensalidade Paga", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "5GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [65.99], "€/mês", "1 Mensalidade Paga", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [69.99], "€/mês", "1 Mensalidade Paga", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "20GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [60.99], "€/mês", "Desconto de", [3.00], "€/mês x", [24], "meses", [63.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "5GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [62.99], "€/mês", "Desconto de", [3.00], "€/mês x", [24], "meses", [65.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [66.99], "€/mês", "Desconto de", [3.00], "€/mês x", [24], "meses", [69.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "20GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [63.99], "€/mês", "Oferta de Honor 90 Smart 5G no valor de", [249.99], "€", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "5GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [65.99], "€/mês", "Oferta de Honor 90 Smart 5G no valor de", [249.99], "€", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [69.99], "€/mês", "Oferta de Honor 90 Smart 5G no valor de", [249.99], "€", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "20GB", "3.500 minutos + 3.500 SMS", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [73.99], "€/mês", "1 Mensalidade Paga", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "Dados Ilimitados", "Minutos & SMS Ilimitados", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [69.99], "€/mês", "Desconto de", [4.00], "€/mês x", [24], "meses", [73.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "Dados Ilimitados", "Minutos & SMS Ilimitados", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [73.99], "€/mês", "Oferta de Coluna Bang & Olufsen no valor de", [199.99], "€", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "Dados Ilimitados", "Minutos & SMS Ilimitados", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [69.99], "€/mês", "1 Mensalidade Paga", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "2 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [80.99], "€/mês", "1 Mensalidade Paga", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "3 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [91.99], "€/mês", "1 Mensalidade Paga", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "4 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [66.99], "€/mês", "Desconto de", [3.00], "€/mês x", [24], "meses", [69.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "2 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [77.99], "€/mês", "Desconto de", [3.00], "€/mês x", [24], "meses", [80.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "3 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [88.99], "€/mês", "Desconto de", [3.00], "€/mês x", [24], "meses", [91.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "4 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [69.99], "€/mês", "Oferta de Honor 90 Smart 5G no valor de", [249.99], "€", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "2 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [80.99], "€/mês", "Oferta de Honor 90 Smart 5G no valor de", [249.99], "€", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "3 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [91.99], "€/mês", "Oferta de Honor 90 Smart 5G no valor de", [249.99], "€", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "10GB", "3.500 minutos + 3.500 SMS", "4 Cartões 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [77.99], "€/mês", "Desconto de", [4.00], "€/mês x", [24], "meses", [81.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "Dados Ilimitados", "Minutos & SMS Ilimitados", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [88.99], "€/mês", "Desconto de", [4.00], "€/mês x", [24], "meses", [92.99], "€/mês", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "Dados Ilimitados", "Minutos & SMS Ilimitados", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", [92.99], "€/mês", "Oferta de Coluna Bang & Olufsen no valor de", [199.99], "€", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "Dados Ilimitados", "Minutos & SMS Ilimitados", "1 Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais")]},

         "Fibra":{}}


# Verificação da Password
if (PP == "MEOadmin96"):
    ws.PlaySound("SystemExclamation", ws.SND_NOSTOP)
    MP()
else:
    print("Essa não é a password correta!")
