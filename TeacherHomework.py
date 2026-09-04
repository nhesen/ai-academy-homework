from datetime import datetime
class Transaction:
    def __init__(self,amount,transaction_type,description,date):
        self.amount=amount
        self.transaction_type=transaction_type
        self.description=description
        self.date=date
class BudgetManager:
    def __init__(self):
        self.__balance=0
        self.__transactions=[]
        self.load_transactions()      #kohne melumati getirir
    def add_income(self,amount,description,date):
        transaction=Transaction(amount,"income",description,date)  #incomeni ozu basa dusur 
        self.__transactions.append(transaction)       #yuxarida yaradilan transactionu listin icine elave edir
        self.__balance+=amount    #balans artirir
        self.save_transactions()
    def add_expense(self,amount,description,date):
        transaction=Transaction(amount,"expense",description,date)
        self.__transactions.append(transaction)
        self.__balance-=amount                  #xercler balansdan cixilir
        self.save_transactions()
    def get_balance(self):
        return self.__balance
    def show_transactions(self):    #gelir ve xerci gorursen
        for transaction in self.__transactions:
            print(transaction.amount,transaction.transaction_type,transaction.description,transaction.date)
    def filter_transactions(self, start_date, end_date):
        for transaction in self.__transactions:
            if transaction.date >=start_date and transaction.date<=end_date:
                print(transaction.amount,transaction.transaction_type,transaction.description,transaction.date)
    def save_transactions(self):
        with open("transactions.txt", "w") as file:
            for transaction in self.__transactions:
                file.write(str(transaction.amount) + "," + transaction.transaction_type + "," + transaction.description + "," + str(transaction.date)+ "\n") #amount eded ola biler ona gore str 
    def load_transactions(self):
        try:
            with open("transactions.txt","r") as file:
                
                for transaction in file:
                    transaction=transaction.strip().split(",")
                    amount=float(transaction[0])
                    transaction_type=transaction[1]
                    description=transaction[2]
                    date = datetime.fromisoformat(transaction[3])

                    new_transaction = Transaction(amount, transaction_type, description, date)  #geri qaytar
                    self.__transactions.append(new_transaction) 

                    if transaction_type=="income":
                        self.__balance+=amount
                    elif transaction_type=="expense":
                        self.__balance-=amount
        except FileNotFoundError:
            pass
manager=BudgetManager()
while True:
    print("1.Add Income")
    print("2.Add Expense")
    print("3.Show Balance")
    print("4.Show Transactions")
    print("5.Filter Transactions")
    print("6.Exit")

    choice = input("Choose: ")
    if choice == "1" or choice == "2":
        try:
            amount=float(input("Enter amount:"))
            if amount<0:
                raise ValueError
            description=input("Enter description:")
            date=datetime.fromisoformat(input("Date:"))
            if choice=="1":
                manager.add_income(amount,description,date)
            else:
                manager.add_expense(amount,description,date)
        except ValueError:
            print("Wrong amount or date .")
    elif choice=="3":
        print(manager.get_balance())
    elif choice=="4":
        manager.show_transactions()
    elif choice=="5":
        try:
            start_date=datetime.fromisoformat(input("Start date: "))
            end_date=datetime.fromisoformat(input("End date: "))
            manager.filter_transactions(start_date,end_date)
        except ValueError:
            print("Wrong date")
    elif choice=="6":
        break


   