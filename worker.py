class Worker():
    
    def __init__(self, nome, cognome, email, nome_datore, datore, specifica, paga_oraria):
        
        self.nome = nome
        self.nome_datore = nome_datore
        self.cognome = cognome
        self.email = email
        self.datore = datore
        self.specifica = specifica
        self.paga_oraria = paga_oraria
        
        self.lista = [self.nome, self.cognome, self.email, self.nome_datore, self.datore, self.specifica, self.paga_oraria]