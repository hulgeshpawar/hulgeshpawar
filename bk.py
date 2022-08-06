from ast import While
from distutils.util import execute
import pymysql
try:
    conn=pymysql.connect(host='localhost',user='root',password='',db='bank')
except Exception as e:
    print(e)
else:
    print('connection succesfully created')

class OpenNewAcc():
    def gets(self):
        while True:
            try:
                self.__accountno=int(input("Enter Account No:"))
            except Exception as no:
                print(no)
            else:
                self.__accountname=input("Enter Account Holder Name:")
            while True:
                try:
                    self.__age=int(input("Enter Your Age:"))
                except Exception as age:
                    print(age)
                else:
                    while True:
                        try:
                            self._balance=float(input("Enter Amount To Deposit:"))
                        except Exception as bal:
                            print(bal)
                        else:
                            data=(self.__accountno,self.__accountname,self.__age,self._balance)
                            query="insert into account(account_no,name,age,balance)values(%s,%s,%s,%s)"
                            cur=conn.cursor()
                            try:
                                cur.execute(query,data)
                            except Exception as e1:
                                print("Query Error")
                            else:
                                conn.commit()
                                print('Data Entered Successfully')
o=OpenNewAcc()

class BalanceEnquiry():
    def gets(self):
        self.__accountno=int(input("Enter Account No:"))
        d=(self.__accountno)
        query='select balance from account where account_no=%s'
        cur=conn.cursor()
        try:
            cur.execute(query,d)
        except Exception as bal:
            print(bal)
        else:
            f=cur.fetchall()
            print("Balance:")
            print(f)
be=BalanceEnquiry()  

    
class Deposite():
    def gets(self):
        self.__accountno=int(input("Enter account no:"))
        self.__amt=int(input("Enter Amount:"))
        #d=(self.__accountno) 
        query='select balance from account where account_no=%s'
        cur=conn.cursor()
        try:
            cur.execute(query,self.__accountno)

        except Exception as dep:
            print(dep)
        else:
            
            f=cur.fetchall()
            if f:
                for row in f:
                    t=row[0]+self.__amt
                    print("New Balance:",t)
            else:
                pass
        
        d=(t,self.__accountno)
        query='update account set balance=%s where account_no=%s'
        try:
            cur.execute(query,d)
            conn.commit()
        except Exception as e:
            print(e)
        print("data update")
    
de=Deposite()

       
class withDrawal():
    def gets(self):
        self.__accountno=int(input("Enter Account No:"))
        self.__amt=float(input("Withdrawl Amount:"))
        query='select balance from account where account_no=%s'
        cur=conn.cursor()
        try:
            cur.execute(query,self.__accountno)
        except Exception as dep:
            print(dep)
        else:  
            f=cur.fetchall()
            if f:
                for row in f:
                    t=row[0]-self.__amt
                    print("New Balance:",t)
            else:
                pass
    
        d=(t,self.__accountno)
        query='update account set balance=%s where account_no=%s'
        try:
            cur.execute(query,d)
            conn.commit()
        except Exception as e:
            print(e)
        print("data update")
        
wd=withDrawal() 

class ShowDetails():
    def gets(self):
        self.__accountno=int(input("Enter Account No:"))
        d=(self.__accountno)
        query='select * from account where account_no=%s'
        cur=conn.cursor()
        try:
            cur.execute(query,d)
        except Exception as show:
            print(show)
        else:
            f=cur.fetchall()
            print("Acc_no,name,__age_,balance")
            print(f)
sd=ShowDetails()

'''
class Loan():
    def Apply(self):
        self.__accountno=int(input("Enter Your Account No:"))
        self.__job=input("Are you a Goverment Employee OR Private Employee:")
        self.__salary=float(input("Enter Your Age:"))
        self.__age=int(input("Enten Your Age:"))
        self.__amt=float(input("Enter Loan Amonut:"))
    if self.__job=="goverment job" and self.__salary<=50000:
        print()
'''
# MAIN PROGRAM
while True:
    print("********************************")
    print("***Bank Management System*******")
    print("********************************")

    print('''
    Enter 1:To Open New Account
    Enter 2:To Deposit Money
    Enter 3:To Withdraw Money
    Enter 4:To Balance Enquiry
    Enter 5:To Show Account Details
    Enter 6:To Apply Loan 
    Enter 7:To Exit
    ''')

    ch=int(input("Select Your Option(1-7):"))

    if ch==1: 
        o.gets()
    elif ch==2:
        de.gets()  
    elif ch==3:
        wd.gets()
    elif ch==4:
         be.gets()
    elif ch==5:
        sd.gets()
    elif ch==6:
        pass
    else :
        break





