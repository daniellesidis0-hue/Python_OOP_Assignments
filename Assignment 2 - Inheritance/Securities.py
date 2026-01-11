#Parent class
class Security:
    def __init__(self,symbol,market_price,quantity):
    #Common attributes
        self.symbol=symbol
        self.market_price=market_price
        self.quantity=quantity

    #Method 1 - Calculate total holding value
    def calculate_value(self):
        return self.market_price*self.quantity

    #Method 2 - Display basic informationד
    def display_info(self):
        val=self.calculate_value()
        print(f"--- Security: {self.symbol} ---")
        print(f"Price: {self.market_price}, Quantity:{self.quantity}")
        print(f"Total Holding Value: {val:.2f}")

#Childs classes
class Stock(Security):
    def __init__(self,symbol,market_price,quantity,dividend_yield):
        #Super->send attributes to the Parent
        super().__init__(symbol,market_price,quantity)
        #Specific attribute
        self.dividend_yield=dividend_yield
    
    #Specific method
    def estimate_annual_dividend(self):
        total_val=self.calculate_value()
        annual_income=total_val*self.dividend_yield
        print(f"Estimated Annual Dividend Income: {annual_income:.2f}")
    
class Bond(Security):
    def __init__(self,symbol,market_price,quantity,coupon_rate):
        super().__init__(symbol,market_price,quantity)
        #Specific attribute
        self.coupon_rate=coupon_rate
    #Specific method
    def calculate_annual_coupon(self):
        total_val=self.calculate_value()
        coupon_payment=total_val*self.coupon_rate
        print(f"Annual Coupon Payment: {coupon_payment:.2f}")

class Option(Security):
    def __init__(self,symbol,market_price,quantity,strike_price):
        super().__init__(symbol,market_price,quantity)
        #Specific attribute
        self.strike_price=strike_price
    #Specific method
    def display_strike_details(self):
        print(f'Option Strike Price: {self.strike_price}')
        #Check the gap between current price and strike price
        gap=self.strike_price-self.market_price
        print(f"Gap From Market Price: {gap:.2f}")
    
#Main Program
if __name__=="__main__":
    print("\n--- Securities Management System ---")
    #Input For Stock
    print("--- Enter Stock Details ---")
    s_symbol=input("Enter Symbol: ")
    s_price=float(input("Enter Market Price: "))
    s_qty=int(input("Enter Quantity: "))
    s_div=float(input("Enter Dividend Yield (e.g., 0.05): "))

    #Create Stock Instance
    my_stock=Stock(s_symbol,s_price,s_qty,s_div)

    #Call Methods
    my_stock.display_info()
    my_stock.estimate_annual_dividend()

    #Input For Bond
    print("\n--- Enter Bond Details ---")
    b_symbol=input("Enter Symbol: ")
    b_price=float(input("Enter Market Price: "))
    b_qty=int(input("Enter Quantity: "))
    b_coupon=float(input("Enter Coupon Rate (e.g., 0.04): "))

    #Create Bond Instance
    my_bond=Bond(b_symbol,b_price,b_qty,b_coupon)

    #Call Methods
    my_bond.display_info()
    my_bond.calculate_annual_coupon()

    #Input For Option
    print("\n--- Enter Option Details ---")
    o_symbol=input("Enter Symbol: ")
    o_price=float(input("Enter Market Price: "))
    o_qty=int(input("Enter Quantity: "))
    o_strike=float(input("Enter Strike Price: "))

    #Create Option Instance
    my_option=Option(o_symbol,o_price,o_qty,o_strike)

    #Call Methods
    my_option.display_info()
    my_option.display_strike_details()
