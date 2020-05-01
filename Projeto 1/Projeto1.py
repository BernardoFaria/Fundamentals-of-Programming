# Bernardo Goncalves de Faria, 87636


#------------------------------Versao Simplificada------------------------------

def gera_chave1(letras):
    chave = ( letras [0:5], letras [5:10], letras [10:15], letras [15:20], \
                  letras [20:25] )
    return chave

"""
 Separa o tuplo dado pelo utilizador em cinco tuplos, dentro de um novo tuplo.
"""


def obtem_codigo1(car, chave):
    for e in range(len(chave)):
        for i in range(len(chave[e])):
            if chave[e][i] == car:
                return str(e) + str(i)

"""            
A funcao atribui duas coordenadas a cada caractere, sendo a primeira
coordenada o numero da linha e a segunda coordenada o numero da coluna.
"""



def codifica1(cad, chave):
    encri = ''
    for e in cad:
        encri = encri + obtem_codigo1(e, chave)
    return encri

"""    
A funcao vai ler cada caracter de cad e devolver a sua encriptacao (encri) 
com dois caracteres, correspondentes a chave
"""    
    

def obtem_car1(cod, chave):
    caractere = str(chave[int(cod[0])][int(cod[1])])
    return caractere

"""
A funcao vai transformar os digitos de cod num inteiro, por forma a ler as
linhas e as colunas da chave, e assim retornar o caracter correspondente
"""



def descodifica1(cad_codificada, chave):
    desencri = ''
    for e in range(0, len(cad_codificada), 2):
        caracteres = cad_codificada[e] + cad_codificada[e + 1]
        desencri = desencri + obtem_car1(caracteres, chave)
    return desencri

"""
A funcao le a cadeia de caracteres dois a dois, atribuindo para cada par, uma
letra definida na chave utilizada
"""


#-------------------------------Versao final------------------------------------

from math import sqrt


def gera_chave2(letras):
    tuplo = ()
    raiz = sqrt(len(letras))
    contador = 0
    a = 1
    if (raiz % 10 != 0 and (raiz * 10 % 10) != 0):
        raiz = (int(raiz) + 1)
    else:
        raiz = int(raiz)
    b = len(letras)/raiz
    if (b % 10 != 0 and b * 10 % 10 != 0):
        b = (int(b)+1)
    else:
        b = int(b)
    while raiz >= a:
        tuplo = tuplo + (letras[contador:(contador+b)],)
        contador += b
        a += 1
    return tuplo
    
"""    
A funcao vai gerar uma chave, cujo ultimo tuplo pode conter menos caracteres
que os outros tuplos. O numero total de tuplos vai ser igual a raiz quadrada
do menor quadrado perfeito nao inferior ao comprimento da sequencia.
"""



def obtem_codigo2(car, chave):
    for e in range(len(chave)):
        for i in range(len(chave[e])):
            if chave[e][i] == car:
                return str(e) + str(i)
    return 'XX'     

"""
A funcao corre a chave, de maneira a encontrar a linha e a coluna que 
correspondem ao caracter dado. Se esse caracter nao existir na chave, a funcao
devolve 'XX'
"""            

        
def codifica2(cad, chave):
    encri = ''
    for e in cad:
        encri = encri + obtem_codigo2(e, chave)
    return encri

"""
A funcao vai percorrer a cadeia de caracteres, dois a dois, e utilizando a
funcao obtem_codigo2, vai associar cada caracter ao numero da linha e coluna
correspondente a ele
"""    


    
def obtem_car2(cod, chave):
    if cod == 'XX':
        return '?'
    else:
        return obtem_car1(cod, chave)
 
"""   
A funcao vai ler os dois digitos dados. Se esses dois digitos corresponderem
a um caracter da chave, vai retornar esse caracter. Se nao existir, a funcao
vai retornar 'XX'
"""   
   
 
   
def descodifica2(cad_codificada, chave):
    desencri = ''
    for e in range(0, len(cad_codificada), 2):
        caracteres = cad_codificada[e] + cad_codificada[e + 1]
        desencri = desencri + obtem_car2(caracteres, chave)
    return desencri    

"""
A funcao vai ler a cadeira de caracteres dados, dois a dois, e atraves da
funcao obtem_car2, vai associar a cada par de caracter, o caracter da chave
que lhe corresponde
"""