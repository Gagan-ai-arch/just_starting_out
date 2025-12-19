import csv
#playing with functions

def entercredentials():
    name = input("enter your name: ")
    email = input("enter your email ")
    password = input("enter your password: ")
    return name, email, password


def duplicate(email):
    with open("database.csv", "r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for lines in csv_reader:
            if lines[1] == email:
                return True
        return False
    
    
def save(name, email, password):    
    user_Str = [name, email, password]
    with open("database.csv", "a", newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(user_Str)
            print("data saved")

        

def showalluser():
    new_line = []
    with open("database.csv", "r") as f:
        content = csv.reader(f)
        next(content)
        for line in content:
            new_line.append(line)
    return new_line


def deluser():
     query = input("give the email to delete your data:  ")
     h = ["name", "email", "password"]
     filtered_lines = []
     with open("database.csv", "r") as f:
          csv_reader = csv.reader(f)
          next(csv_reader)
          for rows in csv_reader:
               if  rows[1] != query:
                filtered_lines.append(rows)
     with open("database.csv", "w") as r:
         csv_writer = csv.writer(r)
         csv_writer.writerow(h)
         csv_writer.writerows(filtered_lines)
         print("dataupdated")


while True:
    query = input("what you wanna do?(signup/deletion/showingall the user/) :    ")
    if query == "signup":
        name, email, password = entercredentials()
        if not duplicate(email):
            save(name,email,password)
        else:
            print("account already exists")
    elif query == "del":
            deluser()
    elif query == "show":
        content = showalluser()
        print(content)
    elif query == "exit":
        break

            
 


