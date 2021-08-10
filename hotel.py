class hotel:
    '''this program is developed by shubham salunkhe'''
    hotel_name='Golden Leaf'
    def __init__(self,name):
        self.name=name
        

    def veg(self,veg_bill=0):
        self.veg_bill=veg_bill        
        self.veg_dish=['','Veg Kolhapuri','Mix Veg      ','Paneer Kadai ']
        self.veg_price=['',180,200,220]
        self.veg_order=[]
        self.veg_p=[]
        while True:
            print('''press 1 - Veg Kolhapuri   -Rs.180\npress 2 - Mix Veg         -Rs.200\npress 3 - Paneer Kadai    -Rs.220
              ''')
            self.veg_option=int(input('Please select your Veg option: '))
            print('You have ordered',self.veg_dish[self.veg_option])
            self.veg_quantity=int(input('Please enter quantity? '))

            self.veg_order.append(self.veg_dish[self.veg_option])

            self.veg_p.append(self.veg_price[self.veg_option]*self.veg_quantity)

            self.veg_bill=self.veg_bill+(self.veg_price[self.veg_option]*self.veg_quantity)
            
            want=input('Want more Veg dishes[yes/no]? ').lower()
            if want=='no':
                break

        q=0                
        for q in range(len(self.veg_order)):
            print(self.veg_order[q],'----',self.veg_p[q])
            q+=1
        print('Your Veg bill is:',self.veg_bill)
                

    def non_veg(self,non_veg_bill=0):
        self.non_veg_bill=non_veg_bill
        self.non_veg_dish=['','Chicken Angara ','Butter Chicken ','Chicken Biryani']
        self.non_veg_price=['',220,240,260]
        self.non_veg_order=[]
        self.non_veg_p=[]
        while True:
            print('''press 1 - Chicken Angara     -Rs.220\npress 2 - Butter Chicken     -Rs.240\npress 3 - Chicken Biryani    -Rs.260
              ''')
            self.non_veg_option=int(input('Please select your Non-Veg option: '))
            print('You have ordered',self.non_veg_dish[self.non_veg_option])
            self.non_veg_quantity=int(input('Please enter quantity? '))

            self.non_veg_order.append(self.non_veg_dish[self.non_veg_option])

            self.non_veg_p.append(self.non_veg_price[self.non_veg_option]*self.non_veg_quantity)
            
            self.non_veg_bill=self.non_veg_bill+(self.non_veg_price[self.non_veg_option]*self.non_veg_quantity)
            
            
            want=input('Want more Non-Veg dishes[yes/no]? ').lower()
            if want=='no':
                break
        k=0                
        for k in range(len(self.non_veg_order)):
            print(self.non_veg_order[k],'----',self.non_veg_p[k])
            k+=1
        print('Your Non-Veg bill is:',self.non_veg_bill)
            


print('Welcome to Hotel',hotel.hotel_name)
name=input('Enter your name: ').upper()
print()
print('Hello',name,'...What would you like to order?')
print()
h=hotel(name)

while True:
    print('''Press - 1 for Veg\nPress - 2 for Non-Veg''' )
    print()
    order=input('Please,select your option: ')
    print()
    if order=='1':
        h.veg()
        want=input('Do you want to order more[yes/no]? ').lower()
        if want=='no':
            break
    
    elif order=='2':
        h.non_veg()
        want=input('Do you want to order more[yes/no]? ').lower()
        if want=='no':
            break
    
    else:
        print('Enter vaild option')

print('Your total bill is:',h.veg_bill+h.non_veg_bill)
print('Thanks for comimg......\nHope you enjoyed the food......')
