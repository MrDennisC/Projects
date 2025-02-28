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
import time as t
import random as r

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

    print("Palavra-Passe:\n".center(LT+4), end='', flush=True)
    return SPP()

# Chamar a tela de login 
LS()

# Iniciar a variável de escolha de opções do Menu
O = -1

# Iniciar a variável de escolha de outras opções
OO = -1

# Menu Principal
def MP():
    print(("=" * 10 + "Menu" + "=" * 10).center(LT))
    print(("1- Área dos Tickets").center(LT))
    print(("2- Adesões/Vendas").center(LT-8))
    print(("3- Pagamentos").center(LT))
    print(("4- Consultar Dados").center(LT-5))
    print(("0- Encerrar Computador").center(LT))
    print(("=" * 24).center(LT))

# Menu 1
def MN1():
    print("=" * 10 + "Área dos Tickets" + "=" * 10)
    print("1- Registar Tickets")
    print("2- Atender Tickets")
    print("3- Visualizar Tickets")
    print("4- Remover Tickets")
    print("0- Voltar ao Menu Principal")
    print("=" * 20)

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

# Menu 2AA
def MN2AA():
    print("=" * 20)
    print("Qual o tipo de cliente que está a atender?")
    print("=" * 20)
    print("1- Cliente Existente")
    print("2- Cliente Não Registado")
    print("0- Voltar ao Menu Principal")
    print("=" * 24)

# Menu 2AAA
def MN2AAA():
    print("=" * 20)
    print(f"Qual o tipo de serviço que a área de residência do cliente suporta?")
    print("=" * 20)
    print("1- Satélite")
    print("2- Fibra")
    print("0- Voltar ao Menu Principal")
    print("=" * 24)

# Menu 2AAAA
def MN2AAAA():
    print("=" * 20)
    print("Qual dos seguintes serviços se adapta mais ao cliente?")
    print("=" * 20)
    print("1-", SP["Satélite"]["M1"][0][0])
    print("2-", SP["Satélite"]["M2"][0][0])
    print("3-", SP["Satélite"]["M3"][0][0])
    print("4-", SP["Satélite"]["M4"][0][0])
    print("0- Voltar ao Menu Principal")
    print("=" * 24)

# Menu 2AAAAA
def MN2AAAAA():
    print("=" * 20)
    print("Dentro do serviço selecionado:", SP["Satélite"]["M1"][0][0])
    print("Selecione o serviço que o cliente pretende:\n")
    print("1-", SP["Satélite"]["M1"][0][0], SP["Satélite"]["M1"][0][8],"com", SP["Satélite"]["M1"][0][9],"\nPor:",P, SP["Satélite"]["M1"][0][2],f"\n{SP["Satélite"]["M1"][0][3]}", f"{PD:.2f}", SP["Satélite"]["M1"][0][5], QM, SP["Satélite"]["M1"][0][7], "\n")
    print("2-", SP["Satélite"]["M1"][1][0], SP["Satélite"]["M1"][1][8], "com", SP["Satélite"]["M1"][1][9], "\nPor:",P2, SP["Satélite"]["M1"][1][2], f"\n{SP["Satélite"]["M1"][1][3]}", f"{PD:.2f}", SP["Satélite"]["M1"][1][5], QM, SP["Satélite"]["M1"][1][7], "\n")
    print("0- Voltar ao Menu Principal\n")
     
# Menu 3
def MN3():
    print("1- Validar Pagamentos de Particulares")
    print("2- Validar Pagamentos de Empresas")
    print("3- Consultar Pagamentos Validados")
    print("0- Voltar ao Menu Principal")

# Menu 4
def MN4():
    print("1- Consultar Dados de Particulares")
    print("2- Consultar Dados de Empresas")
    print("0- Voltar ao Menu Principal")

# Lista com as letras dos tickets
LST = ["A","B","C","D"]

# Lista dos tickets
TS = ["A01"]

# Dicionário para os serviços dos particulares
SP = {"Satélite": {"M1": [("M1 TV", [15.99], "€/mês", "Desconto de", [5.50], "€/mês x", [24], "meses", "Pack Light", "25 Canais"),
                                       ("M1 TV", [21.99], "€/mês", "Desconto de", [5.50], "€/mês x", [24], "meses", "Pack Standard", " 79 Canais")],

                            "M2": [("M2 TV e Voz", [27.99], "€/mês", "Pack Standard", " 79 Canais", "Chamadas para redes fixas nacionais + 50 destinos internacionais")],

                            "M3": [("M3 TV, Net e Voz", "Pack Standard", "MEOBox", " 79 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M3 TV, Net e Voz", "Pack Standard", "MEOBox", " 79 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M3 TV, Net e Voz", "Pack Standard", "MEOBox", "3 meses Sport TV HD", "90 Canais", "40/4 Mbps", "Chamadas para redes fixas nacionais + 50 destinos internacionais")],

                            "M4": [("M4 TV, Net, Voz e Móvel", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps",  [5], "GB (Padrão)", "3.500 minutos + 3.500 SMS", [1],"Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", "Dados Ilimitados", "Minutos & SMS Ilimitados", [1],"Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                        ("M4 TV, Net, Voz e Móvel", "Pack Standard + Extra + MEOBox", "90 Canais", "40/4 Mbps", [10], "GB (Padrão)", "3.500 minutos + 3.500 SMS", [1],"Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais")]},

         "Fibra":{"M1":[("M1 TV", "Canais RF Digital Sem MEOBox", "99 canais"),
                                  ("M1 Net", ["Router Wifi"], "Tráfego Ilimitado"),
                                  ("M1 Net 1Giga","1000/400 Mbps", "Router FiberGateway WiFi 6")],

                       "M2":[("M2 Net e Voz", "100/100 Mbps", ["Router WiFi"], "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                  ("M2 TV e Voz", "Pack Standard",  "MEOBox", "140 Canais", "Chamadas para redes fixas nacionais + 50 destinos internacionais")],

                        "M3":[("M3 200 Net Fibra"," Pack Standard", [98], "Canais", "200/100 Mbps", "Router FiberGateway WiFi 6", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                   ("M3 TV Net e Voz", "Pack Standard", [98], "Canais", ["500/100 Mbps (Padrão)"],"Router FiberGateway WiFi 6", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                   ("M3 500 Net Fibra","Pack Standard", [98], "Canais", "Inlui SkyShowtime", "500/100 Mbps", "Router FiberGateway WiFi 6", "Chamadas para redes fixas nacionais + 50 destinos internacionais")],

                        "M4":[("M4 200 Net Fibra" ,"Pack Standard + Extra de Canais", [139], "Canais" , "200/100 Mbps", "Router FiberGateway WiFi 6", "3500 minutos + 3500 SMS", [1], "Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                   ("M4 2 Cartões-10GB", "Pack Standard + Extra de Canais", [139], "Canais", "200/100 Mbps", "Router FiberGateway WiFi 6", "10GB", "3500 minutos + 3500 SMS", [1], "Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                   ("M4 2 Cartões-20GB", "Pack Standard + Extra de Canais", [139], "Canais", "Router FiberGateway WiFi 6", "3500 minutos + 3500 SMS", [1], "Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais")],
                                   
                        "Speed Edition 10Gbps":[("M3 10Gbps Net Fibra", "Pack Standard" , [99] , "Canais" , "Inclui SkyShowtime", "10/10Gbps" , "Router FiberX", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                                              ("M4 10Gbps Net Fibra", "Pack Standard + Extra de Canais", [140] , "Canais", "Inclui SkyShowtime", "10/10Gbps", "Router FiberX", "Dados Ilimitados", "Minutos & SMS Ilimitados", [1], "Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais")],
                                                               
                        "Destaques":[("M3 200 Net Fibra", "Pack Standard", [98], "Canais", "200/100 Mbps", "Router FiberGateway WiFi 6", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                             ("M4", "Pack Standard + Extra de Canais", [140], "Canais", "500/100 Mbps", "Router FiberGateway WiFi 6", "3500 Minutos + 3500 SMS", [1], "Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais"),
                                             ("M4 2 Cartões-20GB", "Pack Standard + Extra de Canais", [139], "Canais", "Router FiberGateway WiFi 6", "3500 minutos + 3500 SMS", [1], "Cartão 5G", "Chamadas para redes fixas nacionais + 50 destinos internacionais")]}}

# Preço em Serviços M1 de Satélite 
for P in SP["Satélite"]["M1"][0][1]:
    print()

# Preço Desconto em Serviços M1 de Satélite 
for PD in SP["Satélite"]["M1"][0][4]:
    print()

# Quantidade de Meses em Serviços M1 de Satélite
for QM in SP["Satélite"]["M1"][0][6]:
    print()

# Preço 2 em Serviços M1 de Satélite 
for P2 in SP["Satélite"]["M1"][1][1]:
    print()

# Dicionário com Preço e Modificadores dos Serviços
MS = {"Satélite":{"M3":{"Preço":[42.49,35.49],
                                      "1 Mensalidade Paga":[42.49,35.49],
                                      "Desconto de,":[13.00, "€/mês x", 4, "meses", 8.00, "€/mês x", 6, "meses"],
                                      "Oferta de,":["Honor 90 Smart 5G", 249.99,"por", 89.99, "Coluna Bang & Olufsen Beosound", 199.99,"por", 69.99],
                                      "Extras":["3 meses de Sport TV HD", 1.00, "€/mês"]},
                            
                            "M4":{"Preço":[63,99, 80.99, 69.99],
                                      "1 Mensalidade Paga":[63.99, 80.99, 69.99],
                                      "Desconto de,":{3.00,"€/mês x",24,"meses", 4.00,"€/mês x",24,"meses"},
                                      "Oferta de,":["Honor 90 Smart 5G", 249.99, "Coluna Bang & Olufsen Beosound", 199.99],
                                      "Dados Móveis":{"10GB","Custo:", 2.00,"20GB","Custo:", 2.00, 4.00, 6.00, "Velocidade:","10Mbps","Velocidade Máx.", 7.00},
                                      "Extras":["3 meses de Sport TV HD", 1.00, "€/mês"],
                                      "Cartões":["1-20 Cartões/Un x",11.00, "1-20 Cartões Ilimitados/Un x", 30.00]}},

            "Fibra":{"M1":{"Preço":[25.99, 40.99],
                                  "1 Mensalidade":[25.99, 40.99],
                                  "Voucher":[50.00], 
                                  "Extras":["Router FiberGateway WiFi 6", 2.99, "€/mês"]},

                          "M2":{"Preço":[31.99, 32.99],
                                    "1 Mensalidade":[31.99, 32.99]},

                          "M3":{"Preço":[42.49, 45.49, 46.49],
                                    "1 Mensalidade Paga":[42.49, 45.49, 46.49],
                                    "Desconto de,":[13.00,"€/mês x",4,"meses", 5.00,"€/mês x",24,"meses"],
                                    "Oferta de,":["Honor 90 Smart 5G", 249.99,"por", 89.99],
                                    "TV Box ou TV":["MEOBox Android TV 4K","Smart TV Xiaomi 4K 43''",3.69,"Smart TV Sony 4K 43''",6.81,10.50],
                                    "Velocidade WiFi":["1000/400 Mbps", 4.00],
                                    "Extras":["12 meses de SkyShowtime",1.00]},
                                    
                           "M4":{"Preço":[63.99,69.99,71.99],
                                      "1 Mensalidade Paga":[63.99,69.99,71.99],
                                      "Desconto de,":[14.00,"€/mês x",5,"meses", 5.00,"€/mês x",24,"meses"],
                                      "Oferta de,":["Honor 90 Smart 5G", 249.99],
                                      "TV Box ou TV":["MEOBox Android TV 4K","Smart TV Xiaomi 4K 43''",3.69,"Smart TV Sony 4K 43''",6.81,10.50],
                                      "Dados Móveis":["10GB","Custo:", 2.00,"20GB","Custo:", 2.00, 4.00, 6.00, "40GB", 4.00],
                                      "Cartões":["1-20 Cartões/Un x",11.00, "1-20 Cartões Ilimitados/Un x", 30.00],
                                      "Extras":["12 meses de SkyShowtime",1.00]}}}

# Dicionário com os dados dos clientes
DC = {"Nome": ["Carlos Malta","Pinto da Costa","Vitor Baia"],
         "Data de Nascimento": ["05/11/1973","28/12/1937","15/10/1969"],
         "Endereço de Email":{"p946@esenviseu.net","pcosta@sapo.pt","vtbaia@hotmail.com"},
         "Morada":["Rua Belo Horizonte 6, 3500-612, Viseu","Avenida do Pinto da Costa 4660, 4100-141, Porto","Rua da Discordância 76, 9270-150, Porto"],
         "Nº de Cliente":{1,2,3},
         "IBAN":["PT5123443211234567890172","PT502384756123489017561693","PT50345678901234567890162"]}
                           
# Fazer 10 Sorteios de Tickets com a variável Sorteador de Tickets
for ST in range(1,11):
    # Declarar a variável que vai escolher o Nº Aleatório
    NA = r.randint(1,99)
    # Declarar a variável que vai escolher a letra do ticket
    LTS = r.choice(LST)
    # Se o número aleatório escolhido for menor ou igual a 9
    if(NA <= 9):    
        # Transformar a Variável do Nº Aleatório para string
        NA = str(NA)
        # Atribuição de um zero atrás do Nº aleatório
        NA = "0" + str(NA)
    # Adicionar à lista o ticket
    TS.append(LTS + str(NA))
    # Organizar a lista com os tickets
    TS.sort

# Verificação da Password & Entrada no Menu
if(PP == "MEOadmin96"):
    ws.PlaySound("SystemExclamation", ws.SND_NOSTOP)
    # Atribuir sentido às opções
    while O != 0:
        MP()
        O = int(input("Opção:"))
        # Encerrar o computador com "0"
        if(O == 0):
            print("A Encerrar")
            t.sleep(3)
            break
        
        # Menu dos Tickets
        elif(O == 1):
                    # Menu 1
                    MN1()
                    OO = int(input("Opção:"))
                    # Se a opção 0 for selecionada
                    if(OO == 0):
                        # Imprimir nada para voltar ao início do while
                        print()
                    # Se a opção 1 for selecionada
                    elif(OO == 1):
                            # Declarar a variável de registo de tickets
                            RT = "-1"
                            # Registar os tickets
                            while RT != "0":
                                # Em caso de erro uso do try e do except
                                try:
                                    # Input dos tickets
                                    RT = input("Tickets a registar (1 por vez/0 para sair):")
                                    # Adicionar os tickets manualmente
                                    TS.append(RT)
                                    # Se 0 for pressionada
                                    if(RT == "0"):
                                        # Remover o 0 da lista dos tickets
                                        TS.remove("0")
                                        #Sair do ciclo while
                                        break
                                except:
                                    ("Tente novamente!")
                
                    # Se a opção selecionada for 2
                    elif(OO == 2):
                            # Imprimir o ticket que deve ser chamado
                            print("Ticket:", TS[0])
                            # Apagar o ticket da lista
                            TS.pop(0)
                            # Input para esperar o enter do utilizador
                            input("Clique Enter para Continuar...")

                    # Se a opção selecionada for 3     
                    elif(OO == 3):
                        # Organizar a lista com os tickets
                        TS.sort
                        # Imprimir a lista de tickets que estão em espera
                        print("=== Lista de Tickets em Espera: ===")
                        # Ticket em Tickets
                        for T in TS:
                            # Imprimir os tickets que estão em esperar um a um 
                            print(T, end=" ")
                        print()
                        t.sleep(5)

                    # Se a opção selecionada for 4
                    elif(OO == 4):
                        # Ticket em Tickets
                        for T in TS:
                            # Imprimir os tickets que estão na lista um a um
                            print(T, end=" ")
                        TR = input("Ticket a remover:")
                        TS.remove(TR)

                    # Se nenhuma das opções acima foi selecionada
                    else:
                        print("Verifique se não escolheu a opção errada e tente novamente!")

        # Menu das Adesões/Vendas
        elif(O == 2):
            # Imprimir o Menu 2
            MN2()
            # Mostrar a variável das outras opções
            OO = int(input("Opção:"))

            # Se outra opção selecionada for 0
            if(OO == 0):
                print()
            # Se outra opção selecionada for 1
            elif(OO == 1):
                # Imprimir o Menu 2A
                MN2A()

                # Se outra opção selecionada for 0
                if(OO == 0):
                    print()

                # Se outra opção selecionada for 1
                elif(OO == 1):
                    while True:
                        # Imprimir o Menu 2AA
                        MN2AA()
                        # Mostrar a variável das outras opções
                        OO = int(input("Opção:"))

                        # Se outra opção selecionada for 0
                        if(OO == 0):
                            #Imprimir nada para ir para o menu principal
                            print()
                            break

                        # Se outra opção selecionada for 1
                        elif(OO == 1):

                            # Perguntar o nº de cliente
                            NC = int(input("Nº de cliente (0 para voltar):"))

                            # Utilização do 0 para voltar ao Menu 2AA
                            if(NC == 0):
                                continue

                            # Se o Nº de Cliente não constar na lista dos Nºs de Cliente
                            elif(NC not in DC["Nº de Cliente"]):
                                print("Esse número de cliente não existe no sistema!")
                                continue

                            # Se o Nº de Cliente constar na lista dos Nºs de Cliente
                            elif(NC in DC["Nº de Cliente"]):
                                # Imprimir o Menu 2AAA
                                MN2AAA()
                                # Mostrar a variável das outras opções
                                OO = int(input("Opção:"))
                            
                                # Se a outra opção selecionada for 0
                                if(OO == 0):
                                    print()
                                    
                                # Se a outra opção selecionada for 1
                                elif(OO == 1):
                                    #Imprimir o Menu 2AAAA
                                    MN2AAAA()
                                    # Mostrar a variável das outras opções
                                    OO = int(input("Opção:"))

                                    # Se a outra opção selecionada for 0
                                    if(OO == 0):
                                            print()
                                    # Se a outra opção selecionada for 1
                                    elif(OO == 1):
                                        while True:
                                            # Imprimir o Menu 2AAAAA
                                            MN2AAAAA()

                                            # Mostrar a variável das outras opções
                                            OO = int(input("Opção:"))
                                            
                                            # Se outra opção for 0
                                            if(OO == 0):
                                                # Utilização do continue para voltar ao Menu 2 AAAAA
                                                continue
    
                                            # Se a outra opção for 1
                                            elif(OO == 1):
                                                print("=" * 20)
                                                # Retificação da escolha do Cliente
                                                print("Para retificar, a escolha do cliente:\n")
                                                print(SP["Satélite"]["M1"][0][0], SP["Satélite"]["M1"][0][8],"com", SP["Satélite"]["M1"][0][9],"\nPor:",P, SP["Satélite"]["M1"][0][2],"com", SP["Satélite"]["M1"][0][3], f"{PD:.2f}", SP["Satélite"]["M1"][0][5], QM, SP["Satélite"]["M1"][0][7], "\nDurante",QM, SP["Satélite"]["M1"][0][7], "o cliente pagará um valor de", P - PD, SP["Satélite"]["M1"][0][2], "e depois pagará o valor habitual de", P, SP["Satélite"]["M1"][0][2])
                                                # Confirmação da escolha do cliente
                                                C = (input("Pretende confirmar a escolha (S/N):")).upper()
                                                # Se a confirmação for S(Sim)
                                                if(C == "S"):
                                                    # Introdução e Verificação dos Dados
                                                    while True:
                                                            # IBAN do Cliente (Débito Direto)
                                                            IBAN = input("Qual o IBAN do cliente (p/ Débito Direto)?\n").upper()
                                                            # Verificar o tamanho do IBAN e os primeiros 4 caracteres
                                                            if(len(IBAN)!= 25 or not IBAN[0:2] == "PT" and not IBAN[2:4] == "50"):
                                                                # Mensagem de erro
                                                                print("IBAN inválido")
                                                                continue

                                                            # Caso contrário, se o IBAN não estiver em IBAN do Cliente
                                                            elif(IBAN not in DC["IBAN"]):
                                                                OO = -1
                                                                break
                                                            
                                                            # Caso contrário, se o IBAN já estiver em IBAN do Cliente
                                                            elif(IBAN in DC["IBAN"]):
                                                                # Mensagem de erro
                                                                print("IBAN já existe no sistema!")
                                                                continue

                                                    # Sortear o nº de cliente
                                                    NMC = r.randint(1,4)

                                                    while True: 
                                                        # Se Nº de Cliente não estiver em Número de Cliente
                                                        if(NMC not in DC["Nº de Cliente"]):
                                                            # Congratular o Cliente
                                                            # print(f"\nParabéns ! Bem-Vindo à MEO, Cliente Nº {NMC:.0f}!")
                                                            input("\nPressione enter para continuar...")
                                                            break
                                                        # Caso contrário, se Nº de Cliente já estiver em Número de Cliente
                                                        elif(NMC in DC["Nº de Cliente"]):
                                                            # Voltar a sortear o nº de cliente
                                                            NMC = r.randint(1,4)
                                                            # Se o Nº de Cliente não estiver em Número de Cliente
                                                            if(NMC not in DC["Nº de Cliente"]):
                                                                # Adicionar o Nº de Cliente ao set Número de Cliente
                                                                break

                                                # Se a confirmação for N(Não)
                                                elif(C == "N"):
                                                    # Imprimir nada para ir para o Menu Principal
                                                    print()
                                                # Se nenhum deles for escolhido
                                                else:
                                                    # Mensagem de erro
                                                    print("Verifique se não escreveu nada errado e tente novamente!")

            else:
                while OO != 0:
                    if(OO == 0):
                        break
                    elif(OO == 1):
                        break
                    

# Password Errada
else:
    print("Essa não é a password correta!")
