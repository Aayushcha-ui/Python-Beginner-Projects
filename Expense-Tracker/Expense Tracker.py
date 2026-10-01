Expence = {}

def main ():
    while True :
        print("Expence Tracker App")
        print(" 1.Record Income")
        print(" 2.Record Expense")
        print("3.Categorize Transaction")
        print("4. Monthly Summary")
        print("5.Search Records")
        print("6.Save Records")
        print(" 7.Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
           recored()
        elif choice == 2:
            print("Record Expense")
        elif choice == 3 :
          record_expense()
        elif choice == 4 :
           summery ()
        elif choice == 5 :
           record ()
        elif choice == 6 :
           save ()
        elif choice == 7 :
            print("Thank you")
            break
        
def recored ():
    amount = int(input("Enter your amount :"))
    Expence ["income"] = amount
    print("Income Added")
   
def record_expense():
    amount = int(input("Enter your expense: "))
    Expence["expense"] = amount
    print("Expense Added") 

def  Categorize ():
    amount = int(input("Enter your Transaction :"))  
    Askuser = int(input("Enter your Categore :"))
    Expence[amount] = Askuser
    print("Categor added")

def summery ():
   income = Expence["income"]
   expense = Expence["expense"]
   print("Total Income:", income)
   print("Total Expense:", expense)

def record ():
    Askuser = input("Search")
    if Askuser in Expence :
        print("Record",Askuser)
        print("value",Expence[Askuser])
    
    else :
        print("No record Found")
    
def save ():
    file = open("expense.txt", "w")
    file.write(str(Expence))
    file.close()
    print("Records saved")





    




 
main ()     