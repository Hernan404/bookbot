
def words_number (text):
    cant = 0 
    words = text.split()
    for n in words: 
        cant += 1

    return (cant)

def times_per_each (text):
    words = text.lower()
    
    dic = {}

    for c in words:
        if c in dic: 
            dic[c] += 1  
        else:
            dic[c] = 1
    
    return dic 

def sort_on (items):
    return items["num"]


def report (dic):
    lista = []
     
    for c, n in dic.items():
        if c.isalpha():
            dic2 = {"name": c, "num": n}
            lista.append(dic2)
    
    lista.sort(reverse=True, key=sort_on)
    return lista
