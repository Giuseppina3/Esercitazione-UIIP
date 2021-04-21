class Auto:
    def __int__(self, modello_p, cilindrata_p, cavalli_p, produttore_p, tipo_p):
        self.modello = modello_p
        self.cilindrata = cilindrata_p
        self.cavalli = cavalli_p
        self.produttore = produttore_p
        self.tipo = tipo_p

comando = input('Inserisci comando')
comando = int(comando)

lista = []
lista_test = [ Auto ('x', 10, 5, 'y', 'u'), Auto('a', 5, 50, 'b', 'c')]

while comando != -1:
    if comando==1 :#lettura
        print()

    if comando==2 :#ricerca
        print()

    if comando==3 : #occorrenze produttore
        print()

    if comando== 4 :#modello con più cavalli
        print()

    if comando==5 : #media delle cilindrate
        print()

    comando = input('Inserisci comando')
    comando = int(comando)

