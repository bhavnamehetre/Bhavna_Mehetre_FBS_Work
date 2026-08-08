from Emp import emp 
class dev(emp):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal,dept="IT")
        self.com = com
        
    def calsal(self,bonus):
        final = self.sal + self.com
        print("final salry is:",final)
        
    def __str__(self):
        return super().__init__()+ f" \t com={self.com}"
    def __repr__(self):
            return super().__str__()