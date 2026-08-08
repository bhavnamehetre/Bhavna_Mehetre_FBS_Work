from EmpMan import EmpManage
class login:
    e = EmpManage()
    uid = input("enter the user is:")
    passw = input("enter the password:")
    if(uid == "admin" and passw == "2005"):
        while True:
            print("please select one choice:")
            print("1.Add Employee")
            print("2.Display Employee")
            print("3.Update Employee")
            print("4.Search Employee")
            print("5.Delete Employee")
            print("6.Exit")
            choice = int(input("enter the choice:"))
            if choice == 1:
                e.Add()
            elif choice == 2:
                e.Display()
                
            elif choice == 3:
                e.Update()
            elif choice == 4:
                e.Search()
            elif choice == 5:
                e.Delete()
                
            elif choice == 6:
                print("Thank you and visit again....")
                break
            else:
                print("Invalid choice")
    else:
        print("Invalid id or password")
login()