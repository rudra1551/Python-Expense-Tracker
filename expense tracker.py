# Expense Tracker CLI Application
# Stores expenses in a CSV-like text file and
# allows category-wise and total expense analysis
from datetime import date

# Gets a valid file path from the user
# Creates the file if it does not exist
# Returns the file path for reuse across functions
def get_file_path():
    while True:
        path=input("\nEnter The File Path In Which You Want To Store The Data: ")
        try:
            f=open(path,"a")
            f.close()
            break
        except FileNotFoundError:
            print("\nInvalid File Path, Please Enter VALID File Path:")
    return path

print("Welcome To Expense Tracker")

file_path=get_file_path()

Category_MAP={
    1:"Food",
    2:"Travel",
    3:"Rent",
    4:"Utilities",
    5:"Entertainment",
    6:"Education",
    7:"Medical",
    8:"Miscellaneous",
    9:"Custom"
}

menu={
    1:"add expense",
    2:"show expenses (Category-Wise)",
    3:"Show Total Expense",
    4:"Exit"
}

# Adds a single expense entry to the file
# Format: amount,category,note,date
def add_expense(file_path):
    f=open(file_path,"a")
    while True:
        amount=input("\nEnter The Amount: ")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("\nPlease Enter Positive Number")
        else:
            print("\nPlease Enter amount in digits only")
    
    print("\nSelect Category: ")
    for num,name in Category_MAP.items():
       print(f"{num}.{name}")

# Handle predefined categories and custom category input
    while True:
        choice=input("\nEnter The Category Number: ").strip()
        if choice.isdigit():
            choice=int(choice)
            if choice in Category_MAP:
                if Category_MAP[choice]=="Custom":
                    Category=input("\nEnter The custom Category: ").strip()
                    break
                else:
                    Category=Category_MAP[choice]
                    break
            else:
                print("\nPlease Select from The Category List")
        else:
            print("\nPlease Enter Number Only")

    Optional_Note=input("\nEnter any Note if You Want: ").strip()
    Today_Date=date.today().isoformat()
    record=f"{amount},{Category},{Optional_Note},{Today_Date}\n"
    f.write(record)
    f.close()

# Reads expense records from file
# Groups expenses by category
# Displays category-wise entries and totals
def show_Expense(file_path):

# Dictionary structure:
# {
#   "Food": [[amount, note, date], ...],
#   "Travel": [...]
# }
    records={
        
    }
    f=open(file_path,"r")
    data=f.read()   
    max_length_amount=0
    max_length_optional=0
    space_gap=5     
    if data=="":
        print("\nThe File Is Empty And There Is Nothing To Show")
    else:
        lines=data.split("\n") 
        for line in lines:
            if line=="":
                continue
            else:
                parts=line.split(",")
                Amount=parts[0]
                Category=parts[1]
                Optional_note=parts[2]
                Date=parts[3]
                if len(Amount)>max_length_amount:
                    max_length_amount=len(Amount)
                if len(Optional_note)>max_length_optional:
                    max_length_optional=len(Optional_note)    
                if Category not in records:
                    records.update({Category:[[Amount, Optional_note, Date]]})
                else:
                    records[Category].append([Amount, Optional_note, Date])
        
        print("\n--------------------------------------")
        for cat,rec in  records.items():
            print(f"\n{cat}\n")
            category_sum=0
            print("Amount"," "*(max_length_amount+space_gap-len("Amount")),"Optional Note"," "*(max_length_optional+space_gap-len("Optional Note")),"Date")
            for i in range(len(rec)):
                amount=rec[i][0]
                optional_note=rec[i][1]
                date=rec[i][2]
                category_sum+=int(amount)
                print(f"{amount} Rs"," "*(max_length_amount+space_gap-len(amount)-3),f"{optional_note}"," "*(max_length_optional+space_gap-len(optional_note)),f"{date}")
            print(f"\nTotal Expense In {cat} = {category_sum}")
        print("\n--------------------------------------")
        f.close()

# Calculates and displays total expense across all categories
def total_expense(file_path):
    total_sum=0
    f=open(file_path,"r")
    data=f.read()
    lines=data.split("\n")
    for line in lines:
        if line=="":
            continue
        else:
            parts=line.split(",")
            amount=int(parts[0])
            total_sum+=amount
    print("\n--------------------------------------")
    print(f"The Total Expense Is: {total_sum}")
    print("\n--------------------------------------")
            

    f.close()

# Main menu loop for user interaction
while True:
    print("\nSelect From Menu\n")
    for num,action in menu.items():
        print(f"{num}.{action}")
    choice=input("\nEnter The Action Number: ").strip()
    if choice.isdigit():
        choice=int(choice)
        if choice in menu:
            if choice==1:
                add_expense(file_path)
            elif choice==2:
                show_Expense(file_path)
            elif choice==3:
                total_expense(file_path)
            else:
                print("\nThanks For Using Expense Tracker.\n")
                break
        else:
            print("\nPlease Select Number From The List Only:")
    else:
        print("\nPlease Enter Number Only:")