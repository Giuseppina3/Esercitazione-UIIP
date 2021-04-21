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
lista_test = [ Auto(), Auto()]
lista_test[0].tipo='u'
lista_test[0].cavalli=5
lista_test[0].modello = 'x'
lista_test[0].produttore ='x'
lista_test[0].cilindrata = 20

lista_test[1].tipo= 'b'
lista_test[1].cavalli= 50
lista_test[1].modello = 'y'
lista_test[1].produttore = 'x'
lista_test[1].cilindrata = 30


while comando != -1:
    if comando==1 :               #lettura
        for p in lista_test:
            print('Modello'+ p.modello)
            print('Cilindrata'+ str(p.cilindrata))
            print('Cavalli'+ str(p.cavalli))
            print('Produttori' + p.produttore)
            print ('Tipo' + p.tipo)
            print(p.modello, str(p.cilindrata)+ '', str(p.cavalli) + '', p.produttore, p.tipo)


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

