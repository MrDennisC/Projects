'''
Módulos 7
Projeto Gestão Escolar (Inovar)
Elaborado por: Dinis Marques Nº4/10ºH
Curso Profissional de Técnico de Gestão e Programação de Sistemas Informáticos (GPSI)
'''

# Antiga Secção das Variáveis:
    # >>> Hey, algumas coisas mudaram desde a última vez. 
    # >>> Agora as descrições das variáveis encontram-se exclusivamente in-line.

# Importar as librarias
import shutil as s                              # Libraria shutil para tamanho do terminal
import msvcrt as ms                            # Libraria msvcrt para codificação da password
import pickle                                         # Libraria pickle para os ficheiros 
import os                                                 # Libraria os para limpeza do ecrã do terminal
import time as t                                         # Libraria time para temporizadores
from datetime import datetime as dt           # Libraria datetime para datas
import calendar as c                                      # Libraria calendar para promenores de datas

# Obter a largura do terminal através das colunas do mesmo (Vertical)
LT = s.get_terminal_size().columns  # LT é a variável da Largura do Terminal e tem valor Inteiro

# Criação da Ficha dos Integrantes da Escola
def CIE():   # CIE é uma variável de função que correponde à "Criação dos Integrantes da Escola"

    # Declarar a variável dos Integrantes da Escola como Global
    global IE   # Tornar a variável IE global
    # A variável IE é uma variável de uma estrutura de dados e representa "Integrantes da Escola"
    IE = {"a24629":{"Nome":"Josefino Pinto","Turma":"10ºH","Notas":{"português":[10],
                                                                                                          "língua estrangeira (inglês)": [20],
                                                                                                          "área de integração": [15],
                                                                                                          "tic": [16],
                                                                                                          "educação física": [14],
                                                                                                          "matemática": [15],
                                                                                                          "física e química":[14],
                                                                                                          "sistemas operativos (so)":[17],
                                                                                                          "programação e sistemas de informação (psi)":[16]}, "Data de Nascimento":()}}
# Criação da Ficha das Notas dos Cursos Regulares  
def CNCR(): # CNRC é uma variável de função que corresponde à "Criação das Notas dos Cursos Regulares"

    # Declarar a variável das Notas dos Cursos Regulares como Global
    global NCR # Tornar a variável NCR Global

    # A variável NCR é uma variável de uma estrutura de dados e representa "Notas dos Cursos Regulares"                         
    NCR = {"Notas Curso Regular Científico-Humanísticos":{"Cientifícos":{"Ciências e Tecnologias":{"10ºA":{"português":[],
                                                                                                                                                                "língua estrangeira":{"inglês":[],
                                                                                                                                                                                                    "espanhol":[]},
                                                                                                                                                                "filosofia":[],
                                                                                                                                                                "educação física":[],
                                                                                                                                                                "educação moral religiosa":[],
                                                                                                                                                                "matemática a":[],
                                                                                                                                                                "física e química a":[],
                                                                                                                                                                "biologia e geologia":[],
                                                                                                                                                                "geometria descritiva a":[]},

                                                                                                                                                    "11ºA":{"português":[],
                                                                                                                                                                "língua estrangeira":{"inglês":[],
                                                                                                                                                                                                    "espanhol":[]},
                                                                                                                                                                "filosofia":[],
                                                                                                                                                                "educação física":[],
                                                                                                                                                                "educação moral religiosa":[],
                                                                                                                                                                "matemática a":[],
                                                                                                                                                                "física e química a":[],
                                                                                                                                                                "biologia e geologia":[],
                                                                                                                                                                "geometria descritiva a":[]},
                                                                                                                                                                        
                                                                                                                                                    "12ºA":{"português":[],
                                                                                                                                                                "educação física":[],
                                                                                                                                                                "educação moral religiosa":[],
                                                                                                                                                                "biologia":[],
                                                                                                                                                                "química":[],
                                                                                                                                                                "física":[],
                                                                                                                                                                "psicologia b":[],
                                                                                                                                                                "aplicações informáticas b":[]}},


                                                                                                                "Ciências Sócio-Económicas":{"10ºB":{"português":[],
                                                                                                                                                                        "língua estrangeira":{"inglês":[],
                                                                                                                                                                                                        "espanhol":[]},
                                                                                                                                                                        "filosofia":[],
                                                                                                                                                                        "educação física":[],
                                                                                                                                                                        "educação moral religiosa":[],
                                                                                                                                                                        "matemática a":[],
                                                                                                                                                                        "economia a":[],
                                                                                                                                                                        "geografia a":[],
                                                                                                                                                                        "história b":[]},

                                                                                                                                                            "11ºB":{"português":[],
                                                                                                                                                                        "língua estrangeira":{"inglês":[],
                                                                                                                                                                                                            "espanhol":[]},
                                                                                                                                                                        "filosofia":[],
                                                                                                                                                                        "educação física":[],
                                                                                                                                                                        "educação moral religiosa":[],
                                                                                                                                                                        "matemática a":[],
                                                                                                                                                                        "economia a":[],
                                                                                                                                                                        "geografia a":[],
                                                                                                                                                                        "história b":[]},
                                                                                                                                                        
                                                                                                                                                            "12ºB":{"português":[],
                                                                                                                                                                        "educação física":[],
                                                                                                                                                                        "educação moral religiosa":[],
                                                                                                                                                                        "economia c":[],
                                                                                                                                                                        "geografia c":[],
                                                                                                                                                                        "sociologia":[],
                                                                                                                                                                        "aplicações informáticas b":[],
                                                                                                                                                                        "língua estrangeira":{"espanhol":[]}}}},


                                                                                       "Humanidades":{"Línguas e Humanidades":{"10ºC":{"português":[],
                                                                                                                                                                        "língua estrangeira":{"inglês":[],
                                                                                                                                                                                                            "espanhol":[]},
                                                                                                                                                                        "filosofia":[],
                                                                                                                                                                        "educação física":[],
                                                                                                                                                                        "educação moral religiosa":[],
                                                                                                                                                                        "geografia a":[],
                                                                                                                                                                        "latim a":[],
                                                                                                                                                                        "língua estrangeira i, ii ou iii (francês/alemão)":[],
                                                                                                                                                                        "literatura portuguesa":[],
                                                                                                                                                                        "macs (matemática aplicada às ciências sociais)":[]},
                                                                                                                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                            "11ºC":{"português":[],
                                                                                                                                                                        "língua estrangeira":{"inglês":[],
                                                                                                                                                                                                            "espanhol":[]},
                                                                                                                                                                        "filosofia":[],
                                                                                                                                                                        "educação física":[],
                                                                                                                                                                        "educação moral religiosa":[],
                                                                                                                                                                        "geografia a":[],
                                                                                                                                                                        "latim a":[],
                                                                                                                                                                        "língua estrangeira i, ii ou iii (francês/alemão)":[],
                                                                                                                                                                        "literatura portuguesa":[],
                                                                                                                                                                        "macs (matemática aplicada às ciências sociais)":[]},


                                                                                                                                                                "12ºC":{"português":[],
                                                                                                                                                                            "educação física":[],
                                                                                                                                                                            "educação moral religiosa":[],
                                                                                                                                                                            "psicologia b":[],
                                                                                                                                                                            "geografia c":[],
                                                                                                                                                                            "sociologia":[],
                                                                                                                                                                            "direito":[],
                                                                                                                                                                            "inglês":[],
                                                                                                                                                                            "aplicações informáticas b":[],
                                                                                                                                                                            "língua estrangeira: espanhol":[]}}}}}

# Criação da Ficha das Notas dos Cursos Profissionais   
def CNCP(): # CNRC é uma variável de função que corresponde à "Criação das Notas dos Cursos Profissionais"

    # Declarar a variável das Notas dos Cursos Profissionais como Global
    global NCP # Tornar a variável NCP Global

    NCP = {"Notas Curso Profissional":{"Técnico Administrativo":{"10ºD":{"português":[],
                                                                                                                        "língua estrangeira":[],
                                                                                                                        "área de integração":[],
                                                                                                                        "tic":[],
                                                                                                                        "educação física":[],
                                                                                                                        "educação moral religiosa":[],
                                                                                                                        "psicologia e sociologia":[],
                                                                                                                        "economia":[],
                                                                                                                        "matemática":[],
                                                                                                                        "técnicas de administração":[],
                                                                                                                        "comunicação administrativa":[],
                                                                                                                        "legislação comercial, fiscal e laboral":[],
                                                                                                                        "técnicas de cálculo e contabilidade":[]},

                                                                                                            "11ºD":{"português":[],
                                                                                                                        "língua estrangeira":[],
                                                                                                                        "área de integração":[],
                                                                                                                        "educação física":[],
                                                                                                                        "psicologia e sociologia":[],
                                                                                                                        "economia":[],
                                                                                                                        "técnicas de administração":[],
                                                                                                                        "comunicação administrativa":[],
                                                                                                                        "legislação comercial, fiscal e laboral":[],
                                                                                                                        "técnicas de cálculo e contabilidade":[],
                                                                                                                        "formação em contexto de trabalho (estágio)":[]},

                                                                                                            "12ºD":{"português":[],
                                                                                                                        "língua estrangeira":[],
                                                                                                                        "área de integração":[],
                                                                                                                        "educação física":[],
                                                                                                                        "ed. moral e religiosa":[],
                                                                                                                        "técnicas de administração":[],
                                                                                                                        "comunicação administrativa":[],
                                                                                                                        "técnicas de cálculo e contabilidade":[],
                                                                                                                            "formação em contexto de trabalho (estágio)":[]}},
                                                                

                                                                    "Técnico de Ação Educativa": {"10ºE": {"português": [],
                                                                                                                            "língua estrangeira(inglês)": [],
                                                                                                                            "área de integração": [],
                                                                                                                            "tic": [],
                                                                                                                            "educação física": [],
                                                                                                                            "psicologia": [],
                                                                                                                            "sociologia": [],
                                                                                                                            "matemática": [],
                                                                                                                            "saúde": [],
                                                                                                                            "expressão plástica": [],
                                                                                                                            "expressão e comunicação": []},

                                                                                                                    "11ºE": {"português": [],
                                                                                                                                "língua estrangeira(inglês)": [],
                                                                                                                                "área de integração": [],
                                                                                                                                "educação física": [],
                                                                                                                                "psicologia": [],
                                                                                                                                "sociologia": [],
                                                                                                                                "saúde": [],
                                                                                                                                "expressão plástica": [],
                                                                                                                                "expressão e comunicação": [],
                                                                                                                                "formação em contexto de trabalho (estágio)": []},

                                                                                                                    "12ºE": {"português": [],
                                                                                                                                "língua estrangeira(inglês)": [],
                                                                                                                                "área de integração": [],
                                                                                                                                "educação física": [],
                                                                                                                                "ed. moral e religiosa": [],
                                                                                                                                "saúde": [],
                                                                                                                                "técnicas pedagógicas e intervenção educativa": [],
                                                                                                                                "formação em contexto de trabalho (estágio)": []}},


                                                                    "Técnico de Desporto":{"10ºF": {"português": [],
                                                                                                                    "língua estrangeira (inglês)": [],
                                                                                                                    "área de integração": [],
                                                                                                                    "tic": [],
                                                                                                                    "educação física": [],
                                                                                                                    "estudo do movimento": [],
                                                                                                                    "matemática": [],
                                                                                                                    "psicologia": [],
                                                                                                                    "teoria do desporto": [],
                                                                                                                    "desportos individuais e de exploração da natureza": [],
                                                                                                                    "modalidades coletivas": [],
                                                                                                                    "atividades de ginásio": []},

                                                                                                        "11ºF": {"português": [],
                                                                                                                    "língua estrangeira (inglês)": [],
                                                                                                                    "área de integração": [],
                                                                                                                    "educação física": [],
                                                                                                                    "ed. moral e religiosa": [],
                                                                                                                    "estudo do movimento": [],
                                                                                                                    "teoria do desporto": [],
                                                                                                                    "desportos individuais e de exploração da natureza": [],
                                                                                                                    "modalidades coletivas": [],
                                                                                                                    "atividades de ginásio": [],
                                                                                                                    "formação em contexto de trabalho (estágio)": []},

                                                                                                            "12ºF": {"português": [],
                                                                                                                        "língua estrangeira (inglês)": [],
                                                                                                                        "área de integração": [],
                                                                                                                        "educação física": [],
                                                                                                                        "ed. moral e religiosa": [],
                                                                                                                        "estudo do movimento": [],
                                                                                                                        "modalidades coletivas": [],
                                                                                                                        "atividades de ginásio": [],
                                                                                                                        "formação em contexto de trabalho (estágio)": []}},


                                                                    "Técnico de Eletrónica, Automação e Comando": {"10ºG": {"português": [],
                                                                                                                                                            "língua estrangeira (inglês)": [],
                                                                                                                                                            "área de integração": [],
                                                                                                                                                            "tic": [],
                                                                                                                                                            "educação física": [],
                                                                                                                                                            "matemática": [],
                                                                                                                                                            "física e química": [],
                                                                                                                                                            "eletricidade e eletrónica": [],
                                                                                                                                                            "tecnologias aplicadas": [],
                                                                                                                                                            "sistemas digitais": [],
                                                                                                                                                            "automação e comando": []},

                                                                                                                                                "11ºG": {"português": [],
                                                                                                                                                            "língua estrangeira (inglês)": [],
                                                                                                                                                            "área de integração": [],
                                                                                                                                                            "educação física": [],
                                                                                                                                                            "matemática": [],
                                                                                                                                                            "física e química": [],
                                                                                                                                                            "eletricidade e eletrónica": [],
                                                                                                                                                            "tecnologias aplicadas": [],
                                                                                                                                                            "sistemas digitais": [],
                                                                                                                                                            "automação e comando": [],
                                                                                                                                                            "formação em contexto de trabalho (estágio)": []},
                        
                                                                                                                                                "12ºG": {"português": [],
                                                                                                                                                            "língua estrangeira (inglês)": [],
                                                                                                                                                            "área de integração": [],
                                                                                                                                                            "educação física": [],
                                                                                                                                                            "matemática": [],
                                                                                                                                                            "eletricidade e eletrónica": [],
                                                                                                                                                            "tecnologias aplicadas": [],
                                                                                                                                                            "automação e comando": [],
                                                                                                                                                            "formação em contexto de trabalho (estágio)": []}},

                                                                    "Técnico de Gestão e Programação de Sistemas Informáticos":{"10ºH":{"português":[],
                                                                                                                                                                                    "língua estrangeira (inglês)": [],
                                                                                                                                                                                    "área de integração": [],
                                                                                                                                                                                    "tic": [],
                                                                                                                                                                                    "educação física": [],
                                                                                                                                                                                    "matemática": [],
                                                                                                                                                                                    "física e química":[],
                                                                                                                                                                                    "sistemas operativos (so)":[],
                                                                                                                                                                                    "programação e sistemas de informação (psi)":[]},

                                                                                                                                                                                "11ºH":{"português":[],
                                                                                                                                                                                        "língua estrangeira (inglês)": [],
                                                                                                                                                                                        "área de integração": [],
                                                                                                                                                                                        "educação física": [],
                                                                                                                                                                                        "educação moral e religiosa":[],
                                                                                                                                                                                        "matemática": [],
                                                                                                                                                                                        "física e química":[],
                                                                                                                                                                                        "sistemas operativos (so)":[],
                                                                                                                                                                                        "arquitetura de computadores (ac)":[],
                                                                                                                                                                                        "redes de comunicação (rc)":[],
                                                                                                                                                                                        "programação e sistemas de informação (psi)":[]}, 
                                                                                                                                                                                
                                                                                                                                                                                "12ºH":{"português":[],
                                                                                                                                                                                        "língua estrangeira (inglês)": [],
                                                                                                                                                                                        "área de integração": [],
                                                                                                                                                                                        "educação física": [],
                                                                                                                                                                                        "matemática": [],
                                                                                                                                                                                        "arquitetura de computadores (ac)":[],
                                                                                                                                                                                        "redes de comunicação (rc)":[],
                                                                                                                                                                                        "programação e sistemas de informação (psi)":[]}},


                                                                    "Técnico de Manutenção Industrial - variante Mecatrónica": {"10ºI": {"português": [],
                                                                                                                                                                                "língua estrangeira (inglês)": [],
                                                                                                                                                                                "área de integração": [],
                                                                                                                                                                                "tic": [],
                                                                                                                                                                                "educação física": [],
                                                                                                                                                                                "matemática": [],
                                                                                                                                                                                "física e química": [],
                                                                                                                                                                                "tecnologia e processos": [],
                                                                                                                                                                                "práticas oficinais": [],
                                                                                                                                                                                "organização industrial": [],
                                                                                                                                                                                "desenho técnico": []},
                                                                                                                                                                                    
                                                                                                                                                                    "11ºI": {"português": [],
                                                                                                                                                                                "língua estrangeira (inglês)": [],
                                                                                                                                                                                "área de integração": [],
                                                                                                                                                                                "educação física": [],
                                                                                                                                                                                "ed. moral e religiosa": [],
                                                                                                                                                                                "matemática": [],
                                                                                                                                                                                "física e química": [],
                                                                                                                                                                                "tecnologia e processos": [],
                                                                                                                                                                                "práticas oficinais": [],
                                                                                                                                                                                "organização industrial": [],
                                                                                                                                                                                "desenho técnico": [],
                                                                                                                                                                                "formação em contexto de trabalho (estágio)": []},

                                                                                                                                                                    "12ºI": {"português": [],
                                                                                                                                                                                "língua estrangeira (inglês)": [],
                                                                                                                                                                                "área de integração": [],
                                                                                                                                                                                "educação física": [],
                                                                                                                                                                                "matemática": [],
                                                                                                                                                                                "tecnologia e processos": [],
                                                                                                                                                                                "práticas oficinais": [],
                                                                                                                                                                                "formação em contexto de trabalho (estágio)": []}},


                                                                    "Técnico de Mecatrónica Automóvel": {"10ºJ": {"português": [],
                                                                                                                                            "língua estrangeira (inglês)": [],
                                                                                                                                            "área de integração": [],
                                                                                                                                            "tic": [],
                                                                                                                                            "educação física": [],
                                                                                                                                            "matemática": [],
                                                                                                                                            "física e química": [],
                                                                                                                                            "tecnologias e processos": [],
                                                                                                                                            "práticas oficinais": [],
                                                                                                                                            "sistemas técnicos": []},

                                                                                                                                "11ºJ": {"português": [],
                                                                                                                                            "língua estrangeira (inglês)": [],
                                                                                                                                            "área de integração": [],
                                                                                                                                            "educação física": [],
                                                                                                                                            "ed. moral e religiosa": [],
                                                                                                                                            "matemática": [],
                                                                                                                                            "física e química": [],
                                                                                                                                            "tecnologias e processos": [],
                                                                                                                                            "práticas oficinais": [],
                                                                                                                                            "sistemas técnicos": [],
                                                                                                                                            "formação em contexto de trabalho (estágio)": []},

                                                                                                                                "12ºJ": {"português": [],
                                                                                                                                            "língua estrangeira (inglês)": [],
                                                                                                                                            "área de integração": [],
                                                                                                                                            "educação física": [],
                                                                                                                                            "matemática": [],
                                                                                                                                            "tecnologias e processos": [],
                                                                                                                                            "práticas oficinais": [],
                                                                                                                                            "sistemas técnicos": [],
                                                                                                                                            "formação em contexto de trabalho (estágio)": []}},


                                                                    "Técnico de Multimédia": {"10ºK": {"português": [],
                                                                                                                        "língua estrangeira (inglês)": [],
                                                                                                                        "área de integração": [],
                                                                                                                        "tic": [],
                                                                                                                        "educação física": [],
                                                                                                                        "matemática": [],
                                                                                                                        "física": [],
                                                                                                                        "história da cultura e das artes": [],
                                                                                                                        "programação de sistemas": [],
                                                                                                                        "técnicas e processos": [],
                                                                                                                        "design": [],
                                                                                                                        "desenvolvimento de projetos": []},

                                                                                                            "11ºK": {"português": [],
                                                                                                                        "língua estrangeira (inglês)": [],
                                                                                                                        "área de integração": [],
                                                                                                                        "tic": [],
                                                                                                                        "educação física": [],
                                                                                                                        "ed. moral e religiosa": [],
                                                                                                                        "matemática": [],
                                                                                                                        "história da cultura e das artes": [],
                                                                                                                        "programação de sistemas": [],
                                                                                                                        "técnicas e processos": [],
                                                                                                                        "design": [],
                                                                                                                        "desenvolvimento de projetos": [],
                                                                                                                        "formação em contexto de trabalho (estágio)": []},

                                                                                                            "12ºK": {"português": [],
                                                                                                                        "língua estrangeira (inglês)": [],
                                                                                                                        "área de integração": [],
                                                                                                                        "educação física": [],
                                                                                                                        "programação de sistemas": [],
                                                                                                                        "técnicas e processos": [],
                                                                                                                        "formação em contexto de trabalho (estágio)": []}},


                                                                    "Técnico de Turismo Ambiental e Rural": {"10ºL": {"português": [],
                                                                                                                                                "língua estrangeira (inglês)": [],
                                                                                                                                                "área de integração": [],
                                                                                                                                                "tic": [],
                                                                                                                                                "educação física": [],
                                                                                                                                                "matemática": [],
                                                                                                                                                "geografia": [],
                                                                                                                                                "história da cultura e das artes": [],
                                                                                                                                                "ambiente e desenvolvimento rural": [],
                                                                                                                                                "turismo e técnicas de gestão": [],
                                                                                                                                                "técnicas de acolhimento e animação": [],
                                                                                                                                                "comunicar em...": []},

                                                                                                                                    "11ºL": {"português": [],
                                                                                                                                                "língua estrangeira (inglês)": [],
                                                                                                                                                "área de integração": [],
                                                                                                                                                "educação física": [],
                                                                                                                                                "ed. moral e religiosa": [],
                                                                                                                                                "geografia": [],
                                                                                                                                                "história da cultura e das artes": [],
                                                                                                                                                "ambiente e desenvolvimento rural": [],
                                                                                                                                                "turismo e técnicas de gestão": [],
                                                                                                                                                "técnicas de acolhimento e animação": [],
                                                                                                                                                "formação em contexto de trabalho (estágio)": []},

                                                                                                                                    "12ºL": {"português": [],
                                                                                                                                                "língua estrangeira (inglês)": [],
                                                                                                                                                "área de integração": [],
                                                                                                                                                "educação física": [],
                                                                                                                                                "ambiente e desenvolvimento rural": [],
                                                                                                                                                "turismo e técnicas de gestão": [],
                                                                                                                                                "técnicas de acolhimento e animação": [],
                                                                                                                                                "formação em contexto de trabalho (estágio)": []}}}}

# Verificação da existência de folder para armazenar os ficheiros
if not (os.path.exists(".\\Inovar_Py\\Ficheiros\\Ficheiros Binários\\")):
    # Criação de novo caminho para ficheiros
    os.makedirs(".\\Inovar_Py\\Ficheiros\\Ficheiros Binários\\")

# ----- Integrantes da Escola -----
# Gravar o Ficheiro Binário (Integrantes da Escola)
def GIE():  # GIE é uma variável de função que representa "Gravar Integrantes da Escola" 
    global IE # Declarar a variável dos Integrantes da Escola como global
    # Abrir o ficheiro binário no modo de escrita
    FIE = open(".\\Inovar_Py\\Ficheiros\\Ficheiros Binários\\Integrantes_Da_Escola.bin", "wb")
    # Gravar os dados dos alunos no ficheiro
    pickle.dump(IE,FIE)
    # Fechar o ficheiro
    FIE.close()

# Ler o Ficheiro Binário (Integrantes da Escola)
def LIE(): # LIE é uma variável de função que representa "Ler Integrantes da Escola" 
    global IE
    # Abrir ficheiro binário no modo de leitura
    FIE = open(".\\Inovar_Py\\Ficheiros\\Ficheiros Binários\\Integrantes_Da_Escola.bin", "rb")
    # Carregar os dados do ficheiro para a variável
    IE = pickle.load(FIE)
    # Fechar o ficheiro
    FIE.close()

# ----- Notas dos Cursos Regulares ----- 
# Gravar o Ficheiro Binário (Notas dos Cursos Regulares)
def GNCR():  # GNCR é uma variável de função que representa "Gravar Notas dos Cursos Regulares" 
    global NCR # Declarar a variável das Notas dos Cursos Regulares como global
    # Abrir o ficheiro binário no modo de escrita
    FNCR = open(".\\Inovar_Py\\Ficheiros\\Ficheiros Binários\\Notas_Cursos_Regulares.bin", "wb")
    # Gravar os dados dos alunos no ficheiro
    pickle.dump(NCR,FNCR)
    # Fechar o ficheiro
    FNCR.close()

# Ler o Ficheiro Binário (Notas dos Cursos Regulares)
def LNCR(): # LNCR é uma variável de função que representa "Ler Notas dos Cursos Regulares" 
    global NCR
    # Abrir ficheiro binário no modo de leitura
    FNCR = open(".\\Inovar_Py\\Ficheiros\\Ficheiros Binários\\Notas_Cursos_Regulares.bin", "rb")
    # Carregar os dados do ficheiro para a variável
    NCR = pickle.load(FNCR)
    # Fechar o ficheiro
    FNCR.close()

# ----- Notas dos Cursos Profissionais ----- 
# Gravar o Ficheiro Binário (Notas dos Cursos Profissionais)
def GNCP():  # GNCP é uma variável de função que representa "Gravar Notas dos Cursos Profissionais" 
    global NCP # Declarar a variável das Notas dos Cursos Profissionais como global
    # Abrir o ficheiro binário no modo de escrita
    FNCP = open(".\\Inovar_Py\\Ficheiros\\Ficheiros Binários\\Notas_Cursos_Profissionais.bin", "wb")
    # Gravar os dados dos alunos no ficheiro
    pickle.dump(NCP,FNCP)
    # Fechar o ficheiro
    FNCP.close()

# Ler o Ficheiro Binário (Notas dos Cursos Profissionais)
def LNCP(): # LNCP é uma variável de função que representa "Ler Notas dos Cursos Profissionais" 
    global NCP
    # Abrir ficheiro binário no modo de leitura
    LNCP = open(".\\Inovar_Py\\Ficheiros\\Ficheiros Binários\\Notas_Cursos_Profissionais.bin", "rb")
    # Carregar os dados do ficheiro para a variável
    NCP = pickle.load(LNCP)
    # Fechar o ficheiro
    LNCP.close()

# Login na aplicação
def L(): # L é a variável que representa o "Login". Esta é uma variável de Função

    # Imprimir o nome do programa

    print(("  ██╗███╗░░██╗░█████╗░██╗░░░██╗░█████╗░██████╗░").center(LT))
    print(("  ██║████╗░██║██╔══██╗██║░░░██║██╔══██╗██╔══██╗").center(LT))
    print(("  ██║██╔██╗██║██║░░██║╚██╗░██╔╝███████║██████╔╝").center(LT))
    print(("  ██║██║╚████║██║░░██║░╚████╔╝░██╔══██║██╔══██╗").center(LT))
    print(("  ██║██║░╚███║╚█████╔╝░░╚██╔╝░░██║░░██║██║░░██║").center(LT))
    print(("  ╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝").center(LT))
                                                                                                
    
    # Declarar como global a variável NP
    global NP

    # NP é uma variável com valor String que serve para identificar quem está a logar
    NP = input("Nº Processo:") # NP significa "Nº de Processo"
    
    # Sistema de Password
    def SPW():
        # Declarar a variável da Palavra-Passe como global
        global PW

        # Declarar a variável da Palavra-Passe
        PW = ""

        # Ciclo While para esconder a Password atrás de *
        while True:
            # Ocultar o caracter que o utilizador escolheu
            CE = ms.getch().decode("UTF-8")
            
            # Verificar se o utilizador escolheu a tecla enter
            if(CE == "\r"):
                print()
                return PW
            
            # Verificar se o utilizador escolheu a tecla do backspace
            elif(CE == "\x08"):

                # Se o comprimento da Palavra-Passe for superior a 0
                if len(PW) > 0:
                    # O último caracter da Palavra-Passe armazenada vai ser removido 
                    PW = PW[:-1]
                    # Apagar o último caracter na Login Screen
                    print("\b \b", end="", flush=True)

            # Se nenhuma das condições acima for válida        
            else:
                # Adicionar à Palavra-Passe o Caracter Escolhido
                PW += CE
                # Finalmente mostrar "*" ao invés do atual caracter
                print("*", end = "", flush = True)

    print("Palavra-Passe:", end='', flush=True)
    return SPW()

# Menu do Diretor 
def MND(): # A variável MND é uma variável de função que representa "Menu do Diretor"
    print("=" * 10 + "Menu do Diretor" + "=" * 10)
    print("=" * 10 + "Consultar/Modificar:" + "=" * 10)
    print("1 - Alunos/as")
    print("2 - Notas")
    print("0 - Terminar Sessão")
    print("=" * 30)

# Menu do Diretor (Versão: Alunos)
def MNDA(): # A variável MNDA é uma variável de função que representa "Menu do Diretor (Versão: Alunos)"
    print("=" * 10 + "Alunos/as" + "=" * 10)
    print("1.1 - Inserir novo aluno/a")
    print("1.2 - Eliminar aluno/a")
    print("1.3 - Pesquisar aluno/a por...")
    print("1.4 - Imprimir dados de aluno/a")
    print("0 - Voltar atrás")
    print("=" * 30)

# Menu do Diretor (Versão: Notas)
def MNDN(): # A variável MNDN é uma variável de função que representa "Menu do Diretor (Versão: Notas)"
    print("=" * 10 + "Notas" + "=" * 10)
    print("2.1 - Adicionar Notas")
    print("2.2 - Remover Notas")
    print("2.3 - Consultar Notas")
    print("0 - Voltar atrás")
    print("=" * 30)

# Menu do Aluno
def MNA():  # A variável MNA é uma variável de função que representa "Menu do Aluno"
    print("=" * 10 + "Menu do Aluno" + "=" * 10)
    print("1 - Consultar Notas")
    print("0 - Terminar Sessão")
    print("=" * 30)  

# Iniciar o programa
while True:
    # Tentar
    try:
        # Carregar (Dar Load) dos "Integrantes da Escola"
        LIE()
        # Carregar (Dar Load) dos "Notas dos Cursos Regulares"
        LNCR()
        # Carregar (Dar Load) dos "Notas dos Cursos Profissionais"
        LNCP()
    # Exceção se o ficheiro não existir 
    except FileNotFoundError:
        # Criar o Ficheiro "Integrantes da Escola"
        CIE()
        # Gravar o Ficheiro "Integrantes da Escola"
        GIE()
        # Criar o Ficheiro "Notas dos Cursos Regulares"
        CNCR()
        # Gravar o Ficheiro "Notas dos Cursos Regulares"
        GNCR()
        # Criar o Ficheiro "Notas dos Cursos Profissionais"
        CNCP()
        # Gravar o Ficheiro "Notas dos Cursos Profissionais"
        GNCP()
        continue

    # Limpar o ecrã
    os.system("cls")
    # Chamar o Login na aplicação
    L()

    # Declarar a variável dos Integrantes da Escola como Global
    global IE

    # Se o 1º Caracter do Nº de Proceso for "a"
    if(NP[:1] == "a"):
        # Se o Nº de Proceso não estiver no Nº de Processo dos ALunos ou a Password seja diferente de "@EuMesmoAluno"
        # Ou o Nº de Proceso ser igual a "p925" e a password diferente de "@EuMesmoDiretor"
        if(NP not in IE or PW != "@EuMesmoAluno" or NP == "p225" and PW != "@EuMesmoDiretor"):
            # Imprimir a mensagem de erro
            print("Nº de Processo ou Password Incorretos! Tente novamente em: 5 segundos")
            # Dar 5 segundos de espera ao utilizador
            t.sleep(5)
            # Usar a libraria os para limpar o ecrã
            os.system("cls")
            # Usar o continue para voltar para o início do while
            continue  
    
        # Se o Nº de Proceso constar nos Nºs de Processos dos Alunos e a Password for "@EuMesmoAluno"
        elif(NP in IE and PW == "@EuMesmoAluno"):
            # Imprimir Mensagem de Boas-Vindas
            print("Bem-Vindo!")
            # Limpar o ecrã com o os
            os.system("cls")
            # Ciclo While
            while True:
                # Tentar o input da opção
                try:
                    # Mostrar o Menu do Aluno
                    MNA()
                    # Input da opção
                    O = input("\nOpção:")
                    # Se a opção não for 0, 1 ou 2 
                    if not (O == "0" or O == "1" or O == "2"):
                        # Mensagem de Erro
                        print("Essa opção não é válida. Tente novamente!")
                        # Tempo de Espera de 3 segundos
                        t.sleep(3)
                        # Continue para voltar para o while
                        continue  
                    
                # Se não conseguir
                except:
                    # Mensagem de erro
                    print("Essa opção não é válida. Tente novamente!")
                    # Continue para voltar para o ínicio do ciclo while
                    continue

                # Se a opção for 0
                if(O == "0"):
                    # Mensagem de Saída
                    print("A Terminar Sessão! Até breve!")
                    # Tempo de espera de 3 segundos 
                    t.sleep(3)
                    # Sair do Ciclo While
                    break

                # Se a opção for 1
                elif(O == "1"):
                    # Limpar o ecrã
                    os.system("cls")
                    # Imprimir o cabeçalho
                    print("=" * 10,"Notas", "=" * 10)
                    # Perguntar pelo nº de processo
                    print("Nº de Processo:", NP, "-", IE[NP]["Nome"])
                    # D é a variável correspondente à Disciplina
                    for D, NTS in IE[NP]["Notas"].items(): # NTS é a variável correspondente às Notas
                            # Imprimir notas
                            print(f"{D} - {NTS[0]}")
                    # Input para controlo
                    input("Clique Enter para Continuar...")

    # Se o Nº de Proceso for "p225" e a Password for "@EuMesmoDiretor"            
    elif(NP == "p225" and PW == "@EuMesmoDiretor"):
            # Limpar o ecrã com os
            os.system("cls")
            # Mostrar mensagem de boas-vindas
            print(f"Bem-Vindo, Diretor!")
            # Tempo para a mensagem de cima ser visivel
            t.sleep(1)
            # Limpar o ecrã com os
            os.system("cls")
            # Ciclo While
            while True:
                # Tentar o input da opção
                try:
                    # Mostrar o Menu do Diretor
                    MND()
                    # Input da opção
                    O = input("\nOpção:")
                    # Se a opção for diferente de 0, 1 ou 2 
                    if not (O == "0" or O == "1" or O == "2"):
                        # Mensagem de Erro
                        print("Essa opção não é válida. Tente novamente!")

                        # Tempo de Espera de 3 segundos
                        t.sleep(3)
                        # Limpar o ecrã
                        os.system("cls")
                        # Continue para voltar para o while
                        continue

                # Se não conseguir
                except:
                    # Mensagem de erro
                    print("Essa opção não é válida. Tente novamente!")
                    # Tempo de Espera de 3 segundos
                    t.sleep(3)
                    # Limpar o ecrã
                    os.system("cls")
                    # Continue para voltar para o ínicio do ciclo while
                    continue
    
                # Se a opção for 0
                if(O == "0"):
                    # Sair do Ciclo While
                    break

                # Se a opção for 1
                elif(O == "1"):
                    # Ciclo while
                    while True: 
                        # Tentar o input da opção
                        try:
                            # Limpar o ecrã
                            os.system("cls")
                            # Mostrar o Menu do Diretor
                            MNDA()
                            # Input da opção
                            OO = input("\nOpção:")
                            # Se a opção for diferente de 0, 1 ou 2 
                            if not (OO == "1.1" or OO == "1.2" or OO == "1.3" or OO == "1.4"):
                                # Mensagem de Erro
                                print("Essa opção não é válida. Tente novamente!")
                                # Tempo de Espera de 3 segundos
                                t.sleep(3)
                                # Limpar o ecrã
                                os.system("cls")
                                # Continue para voltar para o while
                                continue
                            # Senão
                            else:
                                # Sair do ciclo while 
                                break

                        # Se não conseguir
                        except:
                            # Mensagem de erro
                            print("Essa opção não é válida. Tente novamente!")
                            # Tempo de Espera de 3 segundos
                            t.sleep(3)
                            # Limpar o ecrã
                            os.system("cls")
                            # Continue para voltar para o ínicio do ciclo while
                            continue

                    # Se outras opções for 1.1
                    if(OO == "1.1"):
                        # Ciclo While
                        while True:
                            # Limpar o ecrã
                            os.system("cls")
                            # Imprimir cabeçalho
                            print("=" * 10 + "Inserir novo aluno/a" + "=" * 10)
                            # Adicionar o Nº de Processo
                            NP = input("Nº de Processo (0 = Sair):")

                            # Se o Nº de Processo for 0
                            if(NP == "0"):
                                # Limpar o ecrã com os
                                os.system("cls")
                                # Break para sair do ciclo while
                                break
                                
                            # Se o primeiro caracter do nº de processo for diferente de "a"
                            if(NP[0:1] != "a"):
                                # Mensagem de erro
                                print(f"Este número de processo não corresponde a um aluno! Tente novamente em 3 segundos!")
                                # Tempo de espera de 3 segundos
                                t.sleep(3)
                                # Limpar o ecrã com os
                                os.system("cls")
                                # Continue para repetir o processo
                                continue

                            # Se o Nº de Processo estiver na estrutura de dados do ficheiro Integrantes da Escola
                            elif(NP in IE):
                                # Mensagem de erro
                                print("Este número de processo já está registrado no sistema! Tente novamente em 3 segundos!")
                                # Tempo de espera de 3 segundos
                                t.sleep(3)
                                # Limpar o ecrã com os
                                os.system("cls")
                                # Continue para repetir o processo
                                continue

                            # Adicionar o Nome
                            N = input("Nome:")

                            # Adicionar a data de nascimento
                            # Tentar
                            try:
                                # D, M e A são variáveis inteiras que representam "Dia", "Mês" e "Ano" respetivamente
                                D, M, A = map(int , input("Data de Nascimento(dd/mm/yyyy):").split("/"))
                            
                                # Verificar se o mês está entre 1 e 12 (se é um mês válido)
                                if(M < 1 or M > 12):
                                    print("O mês deve estar entre 1 e 12.")
                                    # Tempo de espera de 3 segundos
                                    t.sleep(3)
                                    # Continue para repetir o processo
                                    continue

                                # Verifica se o dia está dentro do intervalo válido para o mês e ano fornecidos
                                if(D < 1 or D > c.monthrange(A, M)[1]):
                                    print(f"O dia inserido deve estar compreendido entre 1 e {c.monthrange(A, M)[1]} do mês {M}.")
                                    # Tempo de espera de 3 segundos
                                    t.sleep(3)
                                    # Continue para repetir o processo
                                    continue

                                # Criar as variáveis que irão armazenar a data de nascimento
                                DNS = f"{D:02d}/{M:02d}/{A}" # DNS é uma variável que significa "Data de Nascimento em String"
                                DN = dt.strptime(DNS, "%d/%m/%Y") # DN é uma variável que significa "Data de Nascimento"

                                # Verificar se a data é uma data que ainda não aconteceu
                                if (DN > dt.now()):
                                    print("A data inserida é inválida. Esta data ainda não aconteceu!")
                                    # Tempo de espera de 3 segundos
                                    t.sleep(3)
                                    # Continue para repetir o processo
                                    continue

                                # Calcular a idade do futuro aluno
                                I = dt.now().year - A - ((dt.now().month, dt.now().day) < (M, D))
                                
                                # Verifica se a idade é maior ou igual a 23 anos
                                if(I >= 23):
                                    print(f"{N} tem {I} anos. Logo não se pode matricular!")
                                    # Tempo de espera de 3 segundos
                                    t.sleep(3)
                                    # Voltar ao início do ciclo while
                                    continue

                            except:
                                # Apresentar mensagem de erro
                                print("Certifique-se de que tudo está certo!")
                                # Tempo de espera de 3 segundos
                                t.sleep(3)
                                # Usar o voltar para o ciclo while inicial
                                continue

                            # Adicionar a turma
                            T = input("Turma (AnoºTurma):")    

                            # Se a Turma não estiver em nenhum dos cursos regulares nem nenhum profissional 
                            if (T not in NCR["Notas Curso Regular Científico-Humanísticos"]["Cientifícos"]["Ciências e Tecnologias"]
                             and T not in NCR["Notas Curso Regular Científico-Humanísticos"]["Cientifícos"]["Ciências Sócio-Económicas"]
                             and T not in NCR["Notas Curso Regular Científico-Humanísticos"]["Humanidades"]["Línguas e Humanidades"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico Administrativo"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico de Ação Educativa"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico de Desporto"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico de Eletrónica, Automação e Comando"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico de Gestão e Programação de Sistemas Informáticos"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico de Manutenção Industrial - variante Mecatrónica"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico de Mecatrónica Automóvel"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico de Multimédia"]
                             and T not in NCP["Notas Curso Profissional"]["Técnico de Turismo Ambiental e Rural"]):
                                # Mensagem de erro
                                print("Turma inexistente! Tente novamente em 3 segundos!")
                                # Tempo de espera de 3 segundos
                                t.sleep(3)
                                # Limpar o ecrã
                                os.system("cls")
                                # Continue para repetir o processo
                                continue

                            # Se a turma constatar nas Notas dos Cursos Regulares - Ciências e Tecnologias
                            if T in NCR["Notas Curso Regular Científico-Humanísticos"]["Cientifícos"]["Ciências e Tecnologias"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCR["Notas Curso Regular Científico-Humanísticos"]["Cientifícos"]["Ciências e Tecnologias"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Regulares - Ciências Sócio-Económicas
                            elif T in NCR["Notas Curso Regular Científico-Humanísticos"]["Cientifícos"]["Ciências Sócio-Económicas"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCR["Notas Curso Regular Científico-Humanísticos"]["Cientifícos"]["Ciências Sócio-Económicas"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Regulares - Línguas e Humanidades
                            elif T in NCR["Notas Curso Regular Científico-Humanísticos"]["Humanidades"]["Línguas e Humanidades"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCR["Notas Curso Regular Científico-Humanísticos"]["Humanidades"]["Línguas e Humanidades"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico Administrativo
                            elif T in NCP["Notas Curso Profissional"]["Técnico Administrativo"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico Administrativo"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico de Ação Educativa
                            elif T in NCP["Notas Curso Profissional"]["Técnico de Ação Educativa"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico de Ação Educativa"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico de Desporto
                            elif T in NCP["Notas Curso Profissional"]["Técnico de Desporto"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico de Desporto"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico de Eletrónica, Automação e Comando
                            elif T in NCP["Notas Curso Profissional"]["Técnico de Eletrónica, Automação e Comando"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico de Eletrónica, Automação e Comando"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico de Gestão e Programação de Sistemas Informáticos
                            elif T in NCP["Notas Curso Profissional"]["Técnico de Gestão e Programação de Sistemas Informáticos"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico de Gestão e Programação de Sistemas Informáticos"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico de Manutenção Industrial - variante Mecatrónica
                            elif T in NCP["Notas Curso Profissional"]["Técnico de Manutenção Industrial - variante Mecatrónica"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico de Manutenção Industrial - variante Mecatrónica"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico de Mecatrónica Automóvel
                            elif T in NCP["Notas Curso Profissional"]["Técnico de Mecatrónica Automóvel"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico de Mecatrónica Automóvel"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico de Multimédia
                            elif T in NCP["Notas Curso Profissional"]["Técnico de Multimédia"]:
                                IE.update({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico de Multimédia"][T], "Data de Nascimento": (D, M, A)}})

                            # Se a turma constatar nas Notas dos Cursos Profissionais - Técnico de Turismo Ambiental e Rural
                            elif T in NCP["Notas Curso Profissional"]["Técnico de Turismo Ambiental e Rural"]:
                                IE.update(({NP: {"Nome": N, "Turma": T, "Notas": NCP["Notas Curso Profissional"]["Técnico de Turismo Ambiental e Rural"][T], "Data de Nascimento": (D, M, A)}}))
                            
                            # Chamar a função para adicionar ao ficheiro dos Integrantes da Escola
                            GIE()
                            # Mostrar mensagem de adição bem-sucedida
                            print(f"Parabéns! O aluno {N} foi adicionado à turma {T}!")
                            # Input para dar ao utilizador mais controlo sobre o que está a fazer
                            input("Pressione enter para continuar...")
                            # Limpar o ecrã
                            os.system("cls")
                            # Break para voltar ao menu principal
                            break

                    # Se as outra opção for 1.2
                    elif(OO == "1.2"):
                        # Ciclo While
                        while True:
                            # Limpar o ecrã
                            os.system("cls")
                            # Imprimir o cabeçalho
                            print("=" * 10 + "Eliminar aluno/a" + 10 * "=")
                            # Pedir o nº de processo do aluno ao utilizador
                            NP = input("Insira o nº de processo do aluno (0 = Sair):")

                            # Se o Nº de Processo for 0
                            if(NP == "0"):
                                # Break para sair do ciclo while
                                break

                            # Se o primeiro caracter do nº de processo for "a" 
                            # E o Nº de Processo estiver na estrutura de dados do ficheiro Integrantes da Escola
                            elif(NP in IE):
                                # Apagar aluno
                                IE.pop(NP)
                                # Chamar função para guardar a estrutura de dados
                                GIE()
                                # Mensagem de eliminação bem sucedida 
                                print(f"O aluno {NP} foi eliminado com sucesso!")

                            else:
                                # Mensagem de erro
                                print("Este número de processo não corresponde a um aluno! Tente novamente em 3 segundos!")
                                # Tempo de espera de 3 segundos
                                t.sleep(3)
                                # Limpar o ecrã
                                os.system("cls")
                                # Continue para repetir o processo
                                continue

                    # Se a outra opção for 1.3
                    elif(OO == "1.3"):
                        while True:
                            # try:
                                # Limpar o ecrã
                                os.system("cls")
                                # Procurar ao utilizador qual o método que este pretende para procurar o aluno
                                # MPA é uma variável com valor string que serve para o utilizador escolher o método que quer para procurar um aluno
                                MPA = input("Pretende procurar o aluno por: Nome, Nº de processo ou Turma?\n").upper()

                                # Se o método selecionado for diferente de algum dos 3 válidos
                                if not (MPA == "Nome" or MPA == "Nº de processo" or MPA == "Turma"):
                                    # Mensagem de erro
                                    print("Esse método não é válido! Tente novamente em 3 segundos!")
                                    # Tempo de espera de 3 segundos
                                    t.sleep(3)
                                    # Limpar o ecrã
                                    os.system("cls")
                                    # Continue para repetir o processo
                                    continue


                            # except:





                        
    else:
        # Imprimir a mensagem de erro
        print("Nº de Processo ou Password Incorretos! Tente novamente em: 5 segundos")
        # Dar 5 segundos de espera ao utilizador
        t.sleep(5)
        # Usar a libraria os para limpar o ecrã
        os.system("cls")
        # Usar o continue para voltar para o início do while
        continue
