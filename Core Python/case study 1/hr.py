from Emp import emp 
class Hr(emp):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal,dept="IT")
        self.bonus = bonus
        
    def calsal(self,bonus):
        final = self.sal + self.bonus
        print("final salry is:",final)
        
    def __str__(self):
        return super().__init__()+f" \t bonus={self.bonus}"
    def __repr__(self):
        return super().__str__()
