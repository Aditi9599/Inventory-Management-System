import inventory_management_system as ms
op='True'
while(op=='True'):
     choice=int(input("1. Manage Stock \n 2. Sale \n 3. Manage Product \n 4. View Profit Details \n 5. Exit"))
     if(choice==1):
        ms.Manage_Stock()
     if(choice==2):
        ms.Sale()
     if(choice==3):
        ms.Manage_Product()
     if(choice==4):
        ms.profite_details()
     if(choice==5):
        op='False'


