arrayPalabras = []


def definirArrayPalabras():
    global arrayPalabras
    file = open('source.txt', 'r')
    texto = file.read()
    file.close()

    texto = texto.replace('.', '').replace(',', '').replace(';', '').replace('(', '').replace(')', '').replace('\n',
                                                                                                               ' ')
    texto = texto.lower()

    arrayPalabras = texto.split(' ')

