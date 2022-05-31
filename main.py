
class Account:
   Number_Of_Account = 0
   def __init__(self , name  ,id=0 , type='none' , balance =0):
      self.name = name
      self.id = id
      self.type = type
      self.balace = balance

   def get_name(self):
      return self.name
   def set_name(self , name):
      self.name = name

   def get_type(self):
      return  self.type
   def set_type(self,type):
     self.type= type

   def get_id(self):
      return  self.id
   def set_id(self,id):
     self.id= id


   def get_balace (self) :
      return self.balace
   def set_balace(self):
      return self.balace

   def checkbalance(self):
      if self.balace ==0:
         return False
      else:
         return True

   def deposit(self):
      n = int(input("Enter The  Money You Want Deposit : "))
      self.balace += n
      print( f"You'r Balance After Deposit if {self.balace}" )


   def display(self):
      return f"The Name : {self.get_name()} \nThe ID Account : {self.get_id()} \nThe Type of Account: {self.type}\nThe balace Off Account {self.get_balace()}"



class CurrentAccount(Account):
   def __init__(self , name  ,id=0 , type='none' , balance =0,  minimum_balance=0 ):
      super().__init__(name,id,type,balance)
      self.minimum_balance =minimum_balance
      Account.Number_Of_Account +=1


   def get_minimum_balance(self):
      return self.minimum_balance
   def set_minimum_balance(self ,minimum_balance):
      self.minimum_balance = minimum_balance


   def chequbook(self ):
    cash = float(input("Enter The Money you want to Chequbook"))
    if float(self.get_balace()) >= cash:
        aff = input("Is this check official and confirmed by the account holder? ")

        if aff =="yes" or aff == "YES" or aff == "Yes":
          y = float(self.balace)-float(cash)
          self.balace =y
          print(f"Cheqbook Done and You'r Balance Now : {self.get_balace()}")
        else :
         print("Sorry, the process could not be completed. Please see the administration section")
    else :
     print("You Don't Have Money , You Should Make deposit,  Than You You can make chequbbok")


   def withdrawal(self):
      number= float(input("Entry Money That you want to withdrwal"))
      if self.balace < number:
         print("You Can't Make Withdrwal")
      else:
         self.balace = self.balace - number

   def minimum_balance_check(self):
      if self.balace < self.get_minimum_balance() :
         panel = 20
         self.balace -=panel
         print(" Opening balance should not be less than " + str(self.get_minimum_balance()))
         print("You'r Balance after penality = "+str(self.balace))

      else :
         print("No penality imposed")


class SavingAccount(Account) :
   def __init__(self, name, id=0, type='none', balance=0, interest=0):
       super().__init__(name,id,type,balance)
       self.interest = interest
       Account.Number_Of_Account +=1


   def withdrawal (self):
    number = eval(input("Enter The Number Of Money"))
    if self.balace <number :
     print("You Can't Make Withdrwal")
    else :
      self.balace = self.balace - number
    print("You'r Balance After is : " + str(self.balace))

   def intrest_Check(self):
       time = eval(input("Enter Time "))
       rate = 10
       intrest1 = self.balace * pow(1 + rate / 100.0, time) - self.balace;
       self.balace +=intrest1
       print("Your' intrest is " +str(intrest1))
       print("You'r Balace After Updating = "+ str(self.balace))
p = int(input("Enter Number Of Account You want Add On Our Bank "))
while  p!=0:

    print(
        "Welcome dear in Gaza International Bank\n",
        "At first You must register with the type of account you need in order to be able to get our services \n",
        "To create a savings account, press 1 \n",
        "To create a current account press 2\n")

    p-=1
    n = int(input(''))
    if n == 1:
        name = input("Enter You'r Name  : ")
        id = input("Enter You'r Id : ")
        type = "SavingAccount Account"
        balance = int(input("Enter You'r Balance : "))
        global nameAccount
        nameAccount = str(Account.Number_Of_Account) + "Account"
        nameAccount = SavingAccount(name, id, type, balance)




    elif n == 2:
        name = input("Enter You're Name  :  ")
        id = input("Enter You're Id : ")
        type = "Current Account"
        minimum_balance = int(input("Enter You're minimum balance : "))
        balance = int(input("Enter you're balance : "))
        nameAccount = str(Account.Number_Of_Account) + "Account"
        nameAccount = CurrentAccount(name, id, type, balance, minimum_balance)
    while True:
        print(
            " 0. For Stop Menu\n",
            "1.	Accept deposit from a customer and update the balance \n",
            "2.	Display the balance .\n",
            "3.	Compute and deposit interest. \n",
            "4.	Permit withdrawal and update the balance.\n",
            "5.	Check for the minimum balance, impose a penalty\n")
        t = int(input(''))
        if t == 0:
            if isinstance(nameAccount, CurrentAccount):
                print("Thanks For Uesing Bank ,  All You'r Information Saved On File")
                cu =["\nYou'r Name is : ",nameAccount.get_name() ,"\n" , "Your Balacne :"  ,str(nameAccount.get_balace()), "\nYour Id :" ,str(nameAccount.get_id()),"\n" ,"You'r minimum_balance" ,str(nameAccount.get_minimum_balance())]


            else :
                print("Thanks For Uesing Bank ,  All You'r Information Saved On File")
                cu1 = ["\nYou'r Name is : ", nameAccount.get_name(), "\n", "Your Balacne : ", str(nameAccount.get_balace()), "\nYour Id :" ,str(nameAccount.get_id())]



            break


        elif t == 1:
            nameAccount.deposit()
        elif t == 2:
            print(nameAccount.display())

        elif t == 3:
            if isinstance(nameAccount, SavingAccount):
                nameAccount.intrest_Check()
            else:
                print("For Make interest You're Account Should Be Saving Account ")

        elif t == 4:
            if isinstance(nameAccount, SavingAccount):
                nameAccount.withdrawal()
            else: #For Current Account
                nameAccount.chequbook()

        elif t == 5:
            if isinstance(nameAccount, CurrentAccount):
                nameAccount.minimum_balance_check()
            else:
                print("For Check minimum_balance_check You're Account Should Be Current Account ")