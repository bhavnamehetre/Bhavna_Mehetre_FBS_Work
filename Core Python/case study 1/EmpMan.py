from hr import Hr
from dev import dev
class EmpManage:
    empDict = {}
    def Add(self):
        print(".......Add Employee.........")
        id = int(input("enter the EmpId:"))
        if id in self.empDict:
            print("Employee already Exist....")
            return
        name = input("enter the name:")
        sal = float(input("enter the salary:"))
        print("1.HR")
        print("2.Developer")
        ch = int(input("enter your choice:"))
        if(ch ==1):
            com = float(input("enter the commission for HR:"))
            emp = Hr(id,name,sal,com)
        elif(ch == 2):
            bonus = float(input("enter the bonus:"))
            emp = dev(id,name,sal,bonus)
        else:
            print("Invalid choice....")
            return 
        self.empDict[id]=emp
        print("Emp added successfully....")

    def Display(self):
        print(EmpManage.empDict)
    

    def Update(self):
        print(".......Update Employee.........")

        id = int(input("Enter the EmpId: "))

        if id not in self.empDict:
            print("Employee does not Exist....")
        else:
            e = self.empDict[id]

            print("1. Name")
            print("2. Salary")
            print("3. Department")
            print("4. Bonus")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                e.name = input("Enter new name: ")

            elif ch == 2:
                e.sal = float(input("Enter new salary: "))

            elif ch == 3:
                e.dept = input("Enter new department: ")

            elif ch == 4:
                e.bonus = float(input("Enter new bonus: "))

            else:
                print("Invalid choice")

            print("Employee Updated Successfully....")
    def Search(self):
            name = input("Enter the Employee Name: ")

            found = False

            for e in self.empDict.values():
                if e.name == name:
                    print(e)
                    found = True

            if not found:
                print("Employee does not Exist....")
        
    def Delete(self):
        print(".......Delete Employee.........")

        id = int(input("Enter the EmpId: "))

        if id in self.empDict:
            del self.empDict[id]
            print("Employee Deleted Successfully....")
        else:
         print("Employee does not Exist....")
    