class BankAccount:
    def __init__(self,name, acNo, bal):
        self.name = name
        self.acNo = acNo
        self.bal = bal

    def name(self):
        return self.name
    
    def setname(self,cname):
        self.name = cname

    def getAcNo(self):
        return self.acNo
    
    def setAcNo(self,cno):
        self.acNo = cno
    
    def getBal(self):
        return self.bal
    
    def setBal(self,nB):
        self.bal = nB

    def calAmount(self):
        print(f'Account balance = {self.bal}')     

    def __str__(self):
        return f'Name = {self.name}\tAccount_no = {self.acNo}\tBalance = {self.bal}'
    
# Bank Account Ends Here..........

class currentAccount(BankAccount):
    def __init__(self, name, acNo, bal, overdraftLmt):
        super().__init__(name, acNo, bal) 
        self.overdraftLmt = overdraftLmt

    def getOverdraftLmt(self):
        return self.overdraftLmt
    
    def setOverdraftLmt(self,Lmt):
        self.overdraftLmt = Lmt

    def calAmount(self):
        finalAmount = self.bal + self.overdraftLmt
        print (f'Account Balance = {finalAmount}')

    def __str__(self):
        return super().__str__()+'\tOverdraft Limit = '+str(self.overdraftLmt)
    
#### Current Account Ends Here.........

class SavingAccount(BankAccount):
    def __init__(self, name, acNo, bal, iRate):
        super().__init__(name, acNo, bal)
        self.iRate = iRate

    def getiRate(self):
        return self.iRate
    
    def setRate(self,rate):
        self.irate = rate

    def calAmount(self):
        si = self.bal * (self.iRate/100)
        finalAmount = self.bal + si
        print (f'Account Balance = {finalAmount}')

    def __str__(self):
        return super().__str__()+'\tRate of interest = '+ str(self.iRate)


a1 = currentAccount('Vishal', 1234567890, 15000, 100)
print(a1)
a1.calAmount()

a2 = SavingAccount('Ganesh', 9529001808, 100000, 5)
print(a2)
a2.calAmount()