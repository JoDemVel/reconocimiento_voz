import json
import Levenshtein as lev

class Processor:

    def __init__(self):
        self.palabras = set()
        self.lugares = set()
        with open('words.json', encoding='utf-8') as file:
            data = json.load(file)
            self.palabras = set(data['palabras'])
            self.lugares = set(data['lugares'])

    def process(self, text):
        text = text.replace(',','').replace('.','')
        arr = text.split(' ')
        palabras = self.palabras
        lugares = self.lugares
        
        comandos = []
        i = 1
        while i<len(arr):
            temp = arr[i]
            if temp == 'gracias':
                break
            if temp == 'kevin':
                i += 1
                continue
            if(temp == 'calle' or temp == 'avenida'):
                k = i + 1
                if k < len(arr):
                    c = 0
                    aux = temp + ' ' + arr[k]
                    while(aux not in lugares and c<5 and k+1<len(arr)):
                        k += 1
                        c += 1
                        aux = aux + ' ' + arr[k]

                    if(aux in lugares):
                        comandos.append(aux)
                    else:
                        min = 100000
                        minCad = ''
                        for cad in lugares:
                            minAct = lev.distance(cad, aux)
                            if(minAct < min):
                                min = minAct
                                minCad = cad
                            if(minAct < 1):
                                break
                        comandos.append(minCad)
                i = k
            else:
                if (temp in palabras):
                    comandos.append(temp)
                elif (len(temp) >=5):
                    min = 100000
                    minCad = ''
                    for cad in palabras:
                        minAct = lev.distance(cad, temp)
                        if(minAct < min):
                            min = minAct
                            minCad = cad
                        if(minAct < 1):
                            break
                    comandos.append(minCad)
            i += 1

        return comandos