import controller as cr
from models.LinkedList import LinkedList

def main():
    country_list = LinkedList()
    while True:
        line = input()
        if not line:
            exit(0)
        commands = line.split(" ")
        if commands[0] == "RPI":
            commandRPI(commands, country_list)
        elif commands[0] == "RPF":
            commandRPF(commands, country_list)
        elif commands[0] == "RPDE":
            commandRPDE(commands, country_list)
        elif commands[0] == "RPAE":
            commandRPAE(commands, country_list)
        elif commands[0] == "RPII":
            commandRPII(commands, country_list)
        elif commands[0] == "VNE":
            commandVNE(country_list)
        elif commands[0] == "VP":
            commandVP(commands, country_list)
        elif commands[0] == "EPE":
            commandEPE(country_list)
        elif commands[0] == "EUE":
            commandEUE(country_list)
        elif commands[0] == "EP":
            commandEP(commands)
        else:
            print("Instrução inválida.")

def commandRPI(commands, country_list):
    new_country = commands[1]
    cr.registar_country_before(new_country, country_list)
    country_list.traverse_list()


def commandRPF(commands, country_list):
    new_country = commands[1]
    cr.registar_country_after(new_country, country_list)
    country_list.traverse_list()

def commandRPDE(commands, country_list):
    new_country = commands[1]
    country = commands[2]
    cr.insert_country_after_other(new_country, country, country_list)
    country_list.traverse_list()


def commandRPAE(commands, country_list):
    new_country = commands[1]
    country = commands[2]
    cr.insert_country_before_other(new_country, country, country_list)
    country_list.traverse_list()

def commandRPII(commands, country_list):
    new_country = commands[1]
    index = commands[2]
    cr.insert_country_index(new_country, index, country_list)
    country_list.traverse_list()
    
def commandVNE(country_list):
    n = cr.list_country(country_list)
    print("O número de elementos são {}".format(n))
    

def commandVP(commands):
    country = commands[1]
    if not country == cr.has_country:
        print("O país {} não se encontra na lista.")
    else:
        print("O país {} encontra-se na lista.")

def commandEPE(country_list):
    r = cr.delete_firt_country(country_list)
    print("O país {} foi eliminado da lista.".format(r))

def commandEUE(country_list):
    r = cr.delete_last_country(country_list)
    print("O país {} foi eliminado da lista.".format(r))

def commandEP(commands):
    country = commands[1]
    if not country == cr.has_country:
        print("O país {} não se encontra na lista.")
    else:
        cr.delete_country == country
        print("O país {} foi eliminado da lista.")

