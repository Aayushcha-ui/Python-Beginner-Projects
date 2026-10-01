
Hospital = {}


def main ():
    while True :
        print(" 1.Register Patient")
        print("2.Search Patient")
        print("3.Update Patient")
        print("4.Delete Patient")
        print("5.Save Records")
        print("6.Exit")
        
        choice = int(input("Enter your Choice :"))
        if choice == 1 :
            details()
        elif choice == 2 :
            Search ()
        elif choice == 3 :
           update_patient()
        elif choice == 4 :
          delete_patient()
        elif choice == 5 :
            delete_patient()
                
        elif choice == 6 :
            print(".Exit")
            break

def details ():
    name  = input("Enter patient name :")
    age = int(input("Enter patient age :"))
    
    Hospital [name] = {
        "name" :name,
        "age" : age 
    }
    print("Patient added...")

def Search ():
    Askuser = input("Enter your name :")
    if Askuser in details :
           print("Record",Askuser)
           print("age",Hospital[Askuser])

def update_patient():
    name = input("Enter patient name: ")

    if name in Hospital:
        age = input("Enter new age: ")
        Hospital[name]["age"] = age
        print("Patient updated")
    else:
        print("Patient not found")
        
def delete_patient():
    name = input("Enter patient name: ")

    if name in Hospital:
        del Hospital[name]
        print("Patient deleted")
    else:
        print("Patient not found") 
        

main()  
    

            
    
        
