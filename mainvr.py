import urllib.request
import json
import datetime
urljson="https://gugudesign.it/its/dati20220704.json"
#comando per caricare variabilecon contenuto pagina web
pagina = urllib.request.urlopen(urljson).read()
datijson = json.loads(pagina)
task=datijson["task"]
name=task["name"]
print("nome: ", name)
subtasks=task ["subtasks"]
tempi=[]
for sub in subtasks:
    print(sub["name"])
    #siamo sulla singola attività 
    listaStep=sub["tools"]
    #scorro singoli stepcon la datache mi interessa
    for azione in listaStep:
        dataStep = azione ["lastChange"]
        #data in formato testo
        #"22 june 2022 13:30:16 GMT"
        #trasformo in data python datetime library
        tempo = datetime.datetime.strptime(dataStep,
        "%d %b %Y %H:%M:%S %Z")
        print(tempo)
        #raggiungo il tempo all'elenco tempi
        tempi.append(tempo)
last=tempi [len(tempi)-1]
first=tempi[0]
delta=last-first
print ("\n-----tempo attivita'- ", name , " --" )
print ("tempo impiegato: ", delta) 
print("------------------------------\n") 
