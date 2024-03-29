print("-------------------------")
print("WELCOME TO BUDGET TRACKER")
print("-------------------------")


def home():
    print()
    print("'1' To add expenses and its amount")
    print("'2' To change monthly income")
    print("'3' Open the expenses file")
    print("'4' To see trend of my expenses")
    print("'0' EXIT")
    option=input("select your option: ")
    print()
    return option

def inc():
    income=input("Your monthly income: ")
    return income
    
def change_inc():
    income=input("Your monthly income: ")
    return income


def budget_cal(income,exp_amount):
    saving=float(income)*(20/100)
    temp_income=float(income)-saving
    print("After saving '20%' of your income, the remaining budget is",temp_income)
    cur_income=(float(income)-saving)-exp_amount
    if cur_income==0.0:
        print("You saved nothing:",cur_income)
    elif cur_income>0:
        print("You saved",saving,"and saved",temp_income-exp_amount)
    else:
        if (temp_income+abs(cur_income))<float(income) and (temp_income+abs(cur_income))>temp_income:
            print("You spent more then your budget:",abs(cur_income))
        elif (temp_income+abs(cur_income))>float(income):
            print("You spent more then your income:",(temp_income+abs(cur_income))-float(income))
        else:
            print("You spent equal to your income!")
        
    print("Your current budget(if negative it means you spent more then your budget/income) is",cur_income)

cat=[]
def expense(income):
    done=False
    d={}
    dates=[]
    while not done:
        expense=input("The item description you purchase or if done type('yes'): ")
        if expense.lower()=="yes":
            print("ok, its done\n")
            done=True
        elif expense=="":
            print("write the description!!\n")

        else:
            category=input("Type catogory:('HOME','FOOD','CLOTHING','NEEDS','OTHER'): ").lower()
            date,month,year=map(str,input("date(DD MM YYYY): ").split())
            if date=="" or month=="" or year=="" or category=="":
                print("please give dates to your expense or give category..")
            else:
                amount=float(input("The amount of that purchase: "))
                d[expense]=amount
                dates.append(f"{date}/{month}/{year}")
                cat.append(category)

    keys=list(d.keys())
    values=list(d.values())
    user=input("Do you want to save this expense('1' for YES or '2' for NO): ")
    if user=="1":
        file=open("spent.txt","a")
        for i in range(len(keys)):
            print(f"Item: {keys[i]}, amount= {values[i]}, date: {dates[i]}, category: {cat[i]}")
            file.write(f"\nItem: {keys[i]}, amount= {values[i]}, date: {dates[i]}, category: {cat[i]}")
        
        print("Saved successfully!!")

    elif user=="2":
        print("Nothing saved!")
        for i in range(len(keys)):
            print(f"Item: {keys[i]}, amount= {values[i]}, date: {dates[i]}, category: {cat[i]}")

    else:
        print("Nothing saved because wrong option selected!!")
    file.write("\n")
    file.close()
    print()
    print("The total amount of expenses is",sum(list(d.values())))
    budget_cal(income,sum(list(d.values())))


def file_handle():
    file=open("spent.txt","r")
    print(file.read())


def spending_analysis(income,categories):
    file=open("spent.txt","r")
    read=file.readlines()
    category_opt={1:"HOME",2:"FOOD",3:"CLOTHING",4:"NEEDS",5:"OTHER"}
    amount_home=[]
    amount_food=[]
    amount_clothing=[]
    amount_needs=[]
    amount_other=[]

    for i in read:
        if i!="\n":
            category=i[i.index("category")+10:]
            amount=float(i[i.index("amount")+8:i.index(".")+2])
            if category=="home\n":
                amount_home.append(amount)
            elif category=="food\n":
                amount_food.append(amount)
            elif category=="clothing\n":
                amount_clothing.append(amount)
            elif category=="needs\n":
                amount_needs.append(amount)
            elif category=="other\n":
                amount_other.append(amount)
            else:
                print("Wrong catrgory!!")
        else:
            pass

    total_home=sum(amount_home)
    total_food=sum(amount_food)
    total_clothing=sum(amount_clothing)
    total_needs=sum(amount_needs)
    total_other=sum(amount_other)

    print(f"{category_opt[1]} has got total amount of {total_home} or {(total_home*100)/float(income)}% from your monthly income.")
    print(f"{category_opt[2]} has got total amount of {total_food} or {(total_food*100)/float(income)}% from your monthly income.")
    print(f"{category_opt[3]} has got total amount of {total_clothing} or {(total_clothing*100)/float(income)}% from your monthly income.")
    print(f"{category_opt[4]} has got total amount of {total_needs} or {(total_needs*100)/float(income)}% from your monthly income.")
    print(f"{category_opt[5]} has got total amount of {total_other} or {(total_other*100)/float(income)}% from your monthly income.\n")

    
    arr={"HOME":total_home,"FOOD":total_food,"CLOTHING":total_clothing,"NEEDS":total_needs,"OTHER":total_other}
    d_values=list(arr.values())
    d_keys=list(arr.keys())
    delete_values=[]
    delete_keys=[]
    i=0
    print("Trend:-")
    print("~~~~~\n")
    while i<5:
        print(f"{d_keys[d_values.index(max(d_values))]}",end=" : ")
        delete_keys=d_keys.pop(d_values.index(max(d_values)))
        delete_values=d_values.pop(d_values.index(max(d_values)))
        print(delete_values)
        i+=1


income=input("Your monthly income: ")

run=True
while run:
    option=home()
    if option=="0":
        run=False
    
    elif option=="1":
        if income=="" or income=="0":
            print("please add income...")
            income=inc()
        else:
            if income.isnumeric():
                expense(income)
            elif income.isalnum() or income.isalpha():
                print("please write the income in the correct form!")
 
    
    elif option=="2":
        income=change_inc()

    elif option=="3":
        file_handle()

    elif option=="4":
        categories=cat
        spending_analysis(income,categories)
    

    else:
        print("Wrong option selected!!")