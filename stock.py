class box_:
    def __init__(self,name1,name2,name3,number1,number2,number3):
        self.number1=number1
        self.number2=number2
        self.number3=number3
        self.name1=name1
        self.name2=name2
        self.name3=name3
        self.balance1=0
        self.balance2=0
        self.balance3=0
    def add_stock(self,good_name,amount):
        if amount<=0:
            print("must be positive")
        if good_name==self.name1:
            self.balance1+=amount
            print("add amount:",amount)
            print("Current dog amount",self.balance1)
        if good_name==self.name2:
            self.balance2+=amount
            print("add amount:",amount)
            print("Current cat amount",self.balance2)
        if good_name==self.name3:
            self.balance3+=amount
            print("add amount:",amount)
            print("Current duck amount",self.balance3)
    def ship(self,good_name,amount):
        if good_name==self.name1:
            if amount<=self.balance1:
                self.balance1-=amount
                print('ship dog amount',amount)
                print("Current amount",self.balance1)
            else:
                print('out of stock!')
        if good_name==self.name2:
            if amount<=self.balance2:
                self.balance2-=amount
                print('ship cat amount',amount)
                print("Current amount",self.balance2)
            else:
                print('out of stock!')
        if good_name==self.name3:
            if amount<=self.balance3:
                self.balance1-=amount
                print('ship duck amount',amount)
                print("Current amount",self.balance3)
            else:
                print('out of stock!')
    def find(self,good_name):
        if good_name==self.name1:
            print(self.name1+'have'+(str)(self.balance1)+'in stock')
        if good_name==self.name2:
            print(self.name2+'have'+(str)(self.balance2)+'in stock')
        if good_name==self.name3:
            print(self.name3+'have'+(str)(self.balance3)+'in stock')
Use=box_('dog','cat','duck','50','75','25')
run="ture"
while run:
    command=input("Enter the opration: 1:stock,2:ship,3:find,4:end")
    if command=="1":
        name=input("the name:")
        num=(int)(input("The number:"))
        Use.add_stock(name, num)
    if command=="2":
        name=input("the name:")
        num=(int)(input("The number:"))
        Use.ship(name, num)
    if command=="3":
        name=input("the name:")
        Use.find(name)
    if command=="4":
       print("The end")
       run="false"
       break