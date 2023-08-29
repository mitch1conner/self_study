class Coffee:

    
    def __init__(self,name:str,coffee:float,water:float,milk:float,price:float):
        self.water=water
        self.milk=milk
        self.coffee=coffee
        self.price=price
        self.name=name
        assert price>0, f"Invalid amount of coin"
    def __repr__(self) :
        return f"Coffee('Name:{self.name}','Coffee:{self.coffee} ml','Water:{self.water} ml','Milk:{self.milk} ml','Price{self.price} $')"
    def report_product(self):
        print("Water:",self.water,"ml")
        print("Milk:",self.milk,"ml")
        print("Coffee:",self.coffee,"g")
        print("Price:",self.price,"$")
    def pay_method(self,total_price_class):
        refund=total_price_class-self.price
        loop_var=0
        while loop_var>=0:
            if refund>=0:
                print("Your refund:",'$',refund)
                loop_var=-1
            else:
                while refund<0:
                    print("Not enough coins add more")
                    print("Your credit:",total_price_class)
                    adding_coing=input("Add quarters,dimes,nickels,pennies: ")
                    additions = [float(addition.strip()) if addition.strip() else 0 for addition in adding_coing.split(',')]    
    
                    while len(additions) < 4:
                        additions.append(0)
                    added_amount= additions[0]*0.25 +additions[1]*0.10 + additions[2]*0.05 + additions[3]*0.01
                    refund=refund+added_amount

                  
                    

    