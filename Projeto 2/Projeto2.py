# Bernardo Goncalves de Faria, 87636


# -------------------------------------------Tipos Abstratos de Dados - Tipo posicao--------------------------------------------------------


def faz_pos(l, c):
    if isinstance(l, int) and isinstance(c, int) and l >= 0 and c >= 0:
        return (l, c)
    else:
        raise ValueError('faz_pos: argumentos errados')
    
'''
Construtor - A funcao vai receber dois numeros (o primeiro correspondente a uma 
linha e o segundo correspondente a uma coluna) e verificar se sao inteiros 
maiores que 0. De seguida, vai coloca-los num tuplo, formando um elemento do 
tipo posicao.
''' 

    
    
def linha_pos(p):
    return p[0]

'''
Seletor - A funcao recebe um elemento do tipo posicao (um tuplo) e vai devolver 
o valor da linha (o primeiro elemento do tuplo).
'''



def coluna_pos(p):
    return p[1]

'''
Seletor - A funcao recebe um elemento do tipo posicao (um tuplo) e vai devolver
o valor da coluna (o segundo elemento do tuplo).
'''           


    
def e_pos(arg):
    if isinstance(arg, tuple) and len(arg) == 2 and \
            isinstance(linha_pos(arg), int) and isinstance(coluna_pos(arg), int)\
            and linha_pos(arg) >= 0 and coluna_pos(arg) >= 0:
        return True
    else:
        return False
    
'''
Reconhecedor - A funcao recebe um argumento e vai avalia-lo em True ou False 
dependendo se for do tipo posicao ou nao, atraves das suas carateristicas.
'''



def pos_iguais(p1, p2):
    if linha_pos(p1) == linha_pos(p2) and coluna_pos(p1) == coluna_pos(p2):
        return True
    else:
        return False

'''
Teste - A funcao recebe dois argumentos do tipo posicao, e devolve True se os 
argumentos correspondem a mesma posicao da chave, isto e, se tiverem as mesmas 
coordenadas. Caso contrario, devolve False.
'''
 
 
 
 
    
#------------------------------------------Tipos Abstratos de Dados - Tipo Chave-----------------------------------------------


def gera_chave_linhas(l, mgc):
    mgc_aux = []
    chave1 = []
    cont1 = 0
    cont2 = 5
    nao_repetidos = ''
    if len(l) != 25:
        raise ValueError('gera_chave_linhas: argumentos errados')
    for a in l:
        if a not in nao_repetidos:
            nao_repetidos += a
        else:
            raise ValueError('gera_chave_linhas: argumentos errados')
    for b in mgc:
        if b not in str(l):
            raise ValueError('gera_chave_linhas: argumentos errados')
    else:
        for c in list(mgc):
            if c not in mgc_aux and c != ' ':
                mgc_aux += c
        for d in l:
            if d not in mgc_aux:
                mgc_aux += d
        for e in range(5):
            chave1 += [mgc_aux[cont1:cont2]]
            cont1 += 5
            cont2 += 5
        return chave1

'''
Construtor - A funcao vai receber dois argumentos, l um tuplo de 25 letras e mgc
uma string (cadeia de carateres). Vai verificar as validade destes dois 
argumentos (ver se o tuplo tem 25 carateres, se nao ha letras repetidas dentro
do tuplo, e se todas as letras de mgc estao no tuplo l. De seguida cria
uma chave usando a disposicao por linhas.
''' 

        

def ref_chave(c, p):
    return c[p[0]][p[1]]

'''
Seletor - A funcao recebe como argumentos uma chave c e um elemento do tipo
posicao p. A funcao utiliza as coordenadas da posicao p para ir buscar
o elemento correspondente a chave.
'''



def muda_chave(c, p, l):
    c[p[0]][p[1]] = l
    return c

'''
Modificador - A funcao recebe como argumentos uma chave c, um elemento do tipo
posicao p e uma letra l. Depois vai colocar a letra l na posicao p da
chave, e devolve a chave modificada.
''' 



def e_chave(arg):
    lst_aux = []
    if len(arg) != 5:
        return False
    for a in range(len(arg)):
        if len(arg[a]) != 5:
            return False
        for b in range(len(arg)):
            if 65 <= ord(arg[a][b]) <= 90 and arg[a][b] not in lst_aux:
                lst_aux += arg[a][b]
            else:
                return False
    return True

'''
Reconhecedor - A funcao recebe um argumento e vai avalia-lo em True ou False 
dependendo se for do tipo posicao ou nao, atraves das suas carateristicas.
A funcao ord() vai devolver um numero que representa o codigo Unicode da
letra dada.
'''



def string_chave(c):
    string = ' '.join(str(b) for a in c for b in a)
    string += ' '
    string_final = ''
    conta1 = 0
    conta2 = 10
    for i in range(5):
        string_final += string[conta1:conta2] + '\n'
        conta1 +=10
        conta2 += 10
    return string_final

'''
Transformador - A funcao recebe uma chave c, e vai devolver uma string com as
letras da chave. Ao ser impressa, vai apresentar essas letras dispostas numa
tabela 5 x 5.
'''





#---------------------------------------Funcoes a desenvolver------------------------------------------------------------------

        
def digramas(mens):
    mens_aux = ''
    mens_final = ''
    for a in mens:
        if a != ' ':
            mens_aux += a
    for b in range(len(mens_aux) - 1):
        if mens_aux[b] == mens_aux[b+1]:
            mens_final += mens_aux[b] + 'X'
        else:
            mens_final += mens_aux[b]
    mens_final += mens_aux[-1]
    if len(mens_final) % 2 != 0:
        mens_final += 'X'
    return mens_final

'''
A funcao vai receber uma string (mens). De seguida, vai juntar todos os seus
caracteres e tranforma-os em digramas sem espacos, noutra string.
'''



def figura(digrm, chave):
    for a in range(len(chave)):
        for b in range(len(chave[a])):
            if chave[a][b] == digrm[0]:
                pos1 = (a, b)
    for c in range(len(chave)):
        for d in range(len(chave[c])):
            if chave[c][d] == digrm[1]:
                pos2 = (c, d)
    if pos1[0] == pos2[0]:
        return ('l', pos1, pos2)
    elif pos1[1] == pos2[1]:
        return ('c', pos1, pos2)
    else:
        return ('r', pos1, pos2)

'''
A funcao vai receber um digrama e uma chave. A funcao vai ver onde se situa cada
letra do digrama na chave, vai devolver a figura das letras do digrama (se estao
na mesma linha, mesma coluna, ou em cantos de um retangulo) e as suas 
coordenadas, tudo dentro de um tuplo.
''' 



def codifica_l(pos1, pos2, inc):
    if inc == 1:
        if pos1[1] == 4:
            pos1_cod = (pos1[0], 0)
        else:
            pos1_cod = (pos1[0], pos1[1] + 1)
        if pos2[1] == 4:
            pos2_cod = (pos2[0], 0)
        else:
            pos2_cod = (pos2[0], pos2[1] + 1)
    if inc == -1:
        if pos1[1] == 0:
            pos1_cod = (pos1[0], 4)
        else:
            pos1_cod = (pos1[0], pos1[1] - 1)
        if pos2[1] == 0:
            pos2_cod = (pos2[0], 4)
        else:
            pos2_cod = (pos2[0], pos2[1] - 1)
    return (pos1_cod, pos2_cod)

'''
A funcao vai receber dois argumentos do tipo posicao (representam dois digramas) 
que estejam na mesma linha da chave, e um inteiro (inc) que so assume 
os valores 1 ou -1. Vai devolver as posicoes dos digramas encriptados se inc = 1
ou desencriptados se inc = -1.
'''



def codifica_c(pos1, pos2, inc):
    if inc == 1:
        if pos1[0] == 4:
            pos1_cod = (0, pos1[1])
        else:
            pos1_cod = (pos1[0] + 1, pos1[1])
        if pos2[0] == 4:
            pos2_cod = (0, pos2[1])
        else:
            pos2_cod = (pos2[0] + 1, pos2[1])
    if inc == -1:
        if pos1[0] == 0:
            pos1_cod = (4, pos1[1])
        else:
            pos1_cod = (pos1[0] - 1, pos1[1])
        if pos2[0] == 0:
            pos2_cod = (4, pos2[1])
        else:
            pos2_cod = (pos2[0] - 1, pos2[1])
    return (pos1_cod, pos2_cod)

'''
A funcao vai receber dois argumentos do tipo posicao (representam dois digramas) 
que estejam na mesma coluna da chave, e um inteiro (inc) que so assume 
os valores 1 ou -1. Vai devolver as posicoes dos digramas encriptados se inc = 1
ou desencriptados se inc = -1.
'''



def codifica_r(pos1, pos2):
    return ((pos1[0], pos2[1]), (pos2[0], pos1[1]))

'''
A funcao vai receber dois argumentos do tipo posicao (representam dois digramas) 
que estao em linhas e colunas diferentes da chave, e um inteiro (inc) que so 
assume os valores 1 ou -1. Vai devolver as posicoes dos digramas encriptados 
se inc = 1 ou desencriptados se inc = -1.
'''



def codifica_digrama(digrm, chave, inc):
    digrm_cod = figura(digrm, chave)
    if digrm_cod[0] == 'l':
        d = codifica_l(digrm_cod[1], digrm_cod[2], inc)
    elif digrm_cod[0] == 'c':
        d = codifica_c(digrm_cod[1], digrm_cod[2], inc)
    elif digrm_cod[0] == 'r':
        d = codifica_r(digrm_cod[1], digrm_cod[2])
    digrm_final = ref_chave(chave, faz_pos(linha_pos(d[0]), coluna_pos(d[0]))) \
        + ref_chave(chave, faz_pos(linha_pos(d[1]), coluna_pos(d[1])))
    return digrm_final

'''
A funcao vai receber um digrama, uma chave, e um numero inteiro (inc). Se inc = 1
vai haver encriptacao; se inc = -1 vai haver desencriptacao. A funcao vai 
codificar o digrama dado chamando a funcao figura. De seguida, dependendo
da figura, vai chamando a funcao correspondente a sua figura. Por fim, vai 
chamar varias funcoes anteriormente desenvolvidas para retornar o digrama final.
'''



def codifica(mens, chave, inc):
    encri = ''
    mens = digramas(mens)
    for a in range(0, len(mens), 2):
        encri += codifica_digrama(mens[a:a+2], chave, inc)
    return encri

'''
A funcao vai receber uma string, uma chave, e um numero inteiro (inc). Se 
inc = 1 vai encriptar; se inc = -1 vai desencriptar. A funcao vai pegar na string
dada e codifica-la atraves da funcao digramas. De seguida, vai correr a string
de dois em dois e vai codificando-a chamando a funcao codifica_digramas.
'''