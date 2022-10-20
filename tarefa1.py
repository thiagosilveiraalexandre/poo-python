#
# Tarefa 1
# Competências avaliadas:
# - Saber interpretar o que foi solicitado
# - Desenvolver uma solução viável para o problema
# - Saber utilizar classes e objetos

'''
Faça um algoritmo que controle o acesso de pessoas a
um estabelecimento comercial.

Para isso você deverá utilizar as seguintes classes:

Crie uma classe Profissional com os atributos:
        - nome
        - especialidade
        - sala
    Todos atributos devem ser privados e string.

crie uma classe Visitante com os atributos:
        - nome
        - documento
    Todos atributos devem ser privados e string.

crie a classe Visita com os atributos:
        - visitante
        - profissional
        - data_visita
    O atributo visitante deverá ser um objeto da
        classe Visitante escolhido de lista_visitantes.
    O atributo profissional deverá ser um objeto da
        classe Profissional escolhido de lista_profissionais.

Crie os métodos que forem necessários para acessar os
atributos das classes.


Desenvolva seu código a partir do menu abaixo:

======================
MENU
======================
1- Cadastrar Profissional
2- Localizar Profissional
3- Cadastrar Visitante
4- Registrar Visita
5- Relatório de Conferência
Escolha:


Na opção 1 do menu cadastre o nome, especialidade e sala
    onde o profissional atende. Armazene esses dados em
    lista_Profissionais (como objetos).

Na opção 2 do menu é possível localizar um profissional
    pelo nome ou pela profissão. Isso serve para o caso
    do visitante não saber a sala do profissional.
    (Apenas mostrar na tela o nome e a sala do profissional)

Na opção 3 do menu será cadastrado o visitante com nome,
    documento. Armazene esses dados em lista_visitantes
    (como objetos).

Na opção 4 do menu será registrado a visita.
    Escolha o visitante (da lista de visitantes) e o
    profissional (da lista_profissionais), entre com a
    data e armazene a visita em lista_visitas
    (como objeto).

Na opção 5 do menu apenas crie um relatório de conferência.
    Selecione o Profissional e mostre todos os visitantes
    e a data da visita.

Obs. Em todas as listas serão armazenados as instâncias
de suas classes.

'''
lista_Profissionais = []
lista_visitantes = []
lista_Visita = []

class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala
    
    def getNome(self):
        return self.__nome

    def __str__(self):
        return f"Nome:{self.__nome} Especialidade:{self.__especialidade} Sala:{self.__sala}"


def pro(Profissional):
    objprofissional = Profissional("Paulo Michalim", "Médico Geral", "01")
    lista_Profissionais.append(objprofissional)
    objprofissional = Profissional("John Paul", "Médico Cardiologista", "02")
    lista_Profissionais.append(objprofissional)
    objprofissional = Profissional("Martin Ricky", "Médico Radiologista", "03")
    lista_Profissionais.append(objprofissional)
    print(lista_Profissionais[0])
    print(lista_Profissionais[1])
    print(lista_Profissionais[2])


def Busca_Pro():
    for prof in lista_Profissionais:
        print(prof)

    nome = input("Digite o nome do profissional: ")
    
    for prof in lista_Profissionais:
        if nome == prof.getNome():
            print(f"O nome é {nome}")
        return "Não achei"
#    procurar = input('Digite o nome a ser procurado: ')
#    for Profissional in procurar:
#        if procurar == "Paulo Malanga":
#            print(lista_Profissionais[0])
#            break
#        elif procurar == "John Paul":
#            print(lista_Profissionais[1])
#            break
#        elif procurar == "Martin Ricky":
#            print(lista_Profissionais[2])
#            break
#        else:
#            print("Profissional não encontrado")
#            break




class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def __str__(self):
        return f"Nome: {self.__nome} Documento: {self.__documento}"


def objVisi(Visitante):
    objvisitante = Visitante("Thomas Salim", "7894")
    lista_visitantes.append(objvisitante)
    objvisitante = Visitante("Henry Klhaus", "9867")
    lista_visitantes.append(objvisitante)
    objvisitante = Visitante("Adam West", "1235")
    lista_visitantes.append(objvisitante)
    print(lista_visitantes[0])
    print(lista_visitantes[1])
    print(lista_visitantes[2])

def Busca_Visi(Visitante):
    procurar = input('Digite o nome a ser procurado: ')
    for Visitante in procurar:
        if procurar == "Thomas Salim":
            print(lista_visitantes[0])
            break
        elif procurar == "Henry Klhaus":
            print(lista_visitantes[1])
            break
        elif procurar == "Adam West":
            print(lista_visitantes[2])
            break
        else:
            print("Profissional não encontrado")
            break

class Visita:
    def __init__(self, visitante, profissional, data_visita):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_visita = data_visita

    def __str__(self):
        return f"Visitante: {self.__visitante} Profissional: {self.__profissional} Data da Visita: {self.__data_visita}"


def registra_dia():
    print("Escolha os visitantes: ")
    for y in range(len(lista_visitantes)):
        print(f"{y+1}- {lista_visitantes[y]}")
    visi =lista_visitantes[int(input("Escolha o visitante pelo indice: "))]
    print("Escolha os profissionais:\n")
    for y in range(len(lista_Profissionais)):
        print(f"{y+1}- {lista_Profissionais[y]}\n")
    pro = lista_Profissionais[int(input("Escolha o profissional pelo indice: "))]
    data = input("Insira data de visita: ")
    lista_Visita.append(Visita(visi,pro,data))

def relatorio():
    print("Escolha os profissionais:\n")
    for w in range(len(lista_Profissionais)):
        print(f"{w+1}- {lista_Profissionais[w]}\n")
    ind = int(input("coloque o índice de profissionais aqui: "))
    print("Visitas: ")
    for z in range(len(lista_Visita)):
         print(f"""{lista_Visita[z]}""")

def menu():
    while True:
        escolha = input("""
        ======================
        MENU
        ======================
        1- Cadastrar Profissional
        2- Localizar Profissional
        3- Cadastrar Visitante
        4- Registrar Visita
        5- Relatório de Conferência
        Escolha: """)
        if escolha == "1":
            pro(Profissional)
        elif escolha == "2":
            Busca_Pro()
        elif escolha == "3":
            objVisi(Visitante)
        elif escolha == "4":
            registra_dia()
        elif escolha == "5":
            relatorio()
        


menu()
