
#Regista um País no inicio da Lista
def registar_country_before(data, country_list):
    country_list.insert_at_start(data)

#Regista um País no fim da lista
def registar_country_after(data, country_list):
    country_list.insert_at_end(data)

#Regista um País depois de outro elemento já registado 
def insert_country_after_other(x, data, country_list):
    country_list.insert_after_item(x, data)

#Regista um País antes de outro elemento
def insert_country_before_other(x, data, country_list):
    country_list.insert_before_item(x, data)

#Regista um País num determinado índece    
def insert_country_index(index, data, country_list):
    country_list.insert_at_index(index, data)

#Verifica número de elementos da lista   
def list_country(country_list):
    country_list.get_count()

#Verifica se um País se encontra na lista    
def has_country(x, country_list):
    country_list.search_item(x)

#Elimina o primeiro elemento da lista    
def delete_firt_country(country_list):
    country_list.delete_at_start()

#Elimina o último elemento da lista   
def delete_last_country(country_list):
    country_list.delete_at_end()

#Elimina um determinado País da lista   
def delete_country(country_list, x):
    country_list.delete_element_by_value(x)
    