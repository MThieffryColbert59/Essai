class Pile:
    
        def __init__(self):
            self.pile = []
            self.top = None
            
        def est_vide(self):
            return len(self.pile) == 0
        
        def sommet(self):
            return self.top
        
        def empiler(self, el):
            self.pile.append(el)
            self.top = el
            
        def depiler(self):
            if not self.est_vide():
                el =self.pile.pop()
                if not self.est_vide():
                    self.top == self.pile[-1]
                else:
                    self.top = None
                return el
            return None
        
        def verifParenthese():
            