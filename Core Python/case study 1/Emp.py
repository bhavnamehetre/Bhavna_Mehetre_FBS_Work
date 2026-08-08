from abc import ABC,abstractmethod
class emp(ABC):
    def __init__(self,id,name,sal,dept):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = dept
    @abstractmethod
    def calsal(self):
        pass
    def __str__(self):
        return f"ID={self.id} \t NAME={self.name} \t SALARY={self.sal} \t DEPARTMENT={self.dept}"

        
    