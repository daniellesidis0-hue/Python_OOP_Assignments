class Invoice:
    def __init__(self,inv_id,customer_name,date,items_count,total_amount):
        #Public attributes
        self.inv_id=inv_id
        self.customer_name=customer_name
        self.date=date
        self.items_count=items_count
        #Private attribute
        self.__total_amount=total_amount

    #Read access to the Private attribute (getter)
    @property
    def total_amount(self):
        return self.__total_amount

    #Write access with validation logic (setter)
    @total_amount.setter
    def total_amount(self,new_amount):
        if new_amount>=0:
            self.__total_amount=new_amount
            print(f"Amount updated successfully to: {new_amount}")
        else:
            print("Error!: Invoice amount cannot be negative")
        
    #Method 1 - Print invoice details
    def display_invoice(self):
        print(f"--- Invoice No. {self.inv_id} ---")
        print(f"Customer: {self.customer_name}")
        print(f"Date: {self.date}")
        print(f"Total Amount: {self.total_amount}")
        
    #Methods 2 - Add VAT to total amount (17%)
    def add_vat(self):
        vat=self.__total_amount*0.17
        self.__total_amount+=vat
        print(f"Added VAT of {vat:.2f} NIS. New total is {self.__total_amount:.2f}")
        
#Main Program
if __name__=="__main__":
    print("--- Creating New Invoice ---")
    #Input values from the user
    in_id=int(input("Enter Invoice ID: "))
    in_name=(input("Enter Customer Name: "))
    in_date=(input("Enter Date: "))
    in_items=int(input("Enter Items Count: "))
    in_amount=float(input("Enter Total Amount: "))
            
    #Create an Invoice instance (object)
    my_invoice=Invoice(in_id,in_name,in_date,in_items,in_amount)

    #Call methods
    print("\n--- Invoice Details ---")
    my_invoice.display_invoice()

    print("\n--- Adding VAT ---")
    my_invoice.add_vat()

    #Test Encapsulation (setter)
    print("\n--- Testing Update ---")
    new_val=float(input("Enter new amount to update: "))
    my_invoice.total_amount=new_val

    #Add VAT to the new total amount
    if my_invoice.total_amount == new_val:
        print("\n--- Update Success! Adding VAT ---")
        my_invoice.add_vat()
    else:
        print("\n--- Update Failed. Skipping VAT calculation ---")







