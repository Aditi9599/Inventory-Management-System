from tkinter import *
import pymysql as py
from datetime import date
con=py.connect("localhost","root","","ims")
cur=con.cursor()
def Manage_Stock():
    value=input("a. Update Product Quantity In Stock \n b. View Stock")
    pname=input("Enter The Product Name-")
    if(value=='a'):
         Qty=int(input("enter the quantity-"))
         Q="update Product set productQty= %d where productName='%s'"%(Qty,pname)
         cur.execute(Q)
         rec=cur.fetchone()
         con.commit()
         print(rec)
    if(value=='b'):
         q="select productId,productName,purshasePrice,salePrice, productQty from Product where productName='%s'"%(pname)
         cur.execute(q)
         rec=cur.fetchone()
         con.commit()
         print(rec)
def Sale():
    value=input("a. insert product sale detail \n b. update product sale detail \n c. view product sale detail")
    if(value=='a'):
            pname=input("enter product name-")
            cur.execute("select productid from product where productName='%s'"%(pname))
            if cur.rowcount>0:
                id1=cur.fetchone()
                productid=id1[0]
                q="select max(sn) from Sale"
                cur.execute(q)
                rec=cur.fetchone()
                if(rec[0]==None):
                    sn=1
                else:
                    sn=int(rec[0])+1
                date1=str(date.today())
                saleid=str(sn)+'_'+productid+'_'+str(date1)
                price=int(input("enter the price"))
                saleQty=int(input("enter the quantity"))
                qry="select productQty from product where productName='%s'"%(pname)
                cur.execute(qry)
                con.commit()
                f=cur.fetchone()
                newqty=int(f[0])
                newqtyy=newqty-saleQty
                qq="update product set productQty=%d where productName='%s'"%(newqtyy,pname)
                cur.execute(qq)
                con.commit()
                total=price*saleQty
                print(total)
                q="insert into Sale(sn,saleid,productid,price,date,saleQty) values(%d,'%s','%s',%f,'%s',%d)"%(sn,saleid, productid,price,date1,saleQty)
                cur.execute(q)
                con.commit()
            else:
                print("Invalid Product Name")
    elif(value=='b'):
        id=input("enter sale id")
        qty=int(input("enter quantity"))
        price=float(input("enter price"))
        q="update Sale set price=%f,saleQty=%d where saleid='%s'"%(price,qty,id)#error
        print(q)
        cur.execute(q)
        con.commit()
    elif(value=='c'):
          pname=input("enter product name-")
          q="select saleid,productid, price,date,saleQty from sale where productid='%s'"%(pname)
          cur.execute(q)
          rec=cur.fetchone()
          con.commit()
          print(rec)
def Manage_Product():
          ch=input("a. Add New Product \n b. View All Products \n c. Remove Product")
          if(ch=='a'):
                nm=input("enter product name")
                ps=int(input("enter purchase price"))
                sp=int(input("enter sale price"))
                pq=int(input("enter product quantity"))
                q="select max(sn) from product"
                cur.execute(q)
                rec=cur.fetchone()
                print(rec[0])
                if(rec[0]==None):
                    sn=1
                else:
                    sn=int(rec[0]+1)
                pid=nm+'_'+str(sn)
                q="insert into product values(%d,'%s','%s',%d,%f,%d)"%(sn,pid,nm,ps,sp,pq)
                print(q)
                cur.execute(q)
                con.commit()
          elif(ch=='b'):
                      q="select * from product"
                      cur.execute(q)
                      con.commit
                      r=cur.fetchall()
                      print(r)
          elif(ch=='c'):
                         d=input("enter the product id to be deleted")
                         q="delete from product where productid='%s'"%(d)
                         cur.execute(q)
                         rec=cur.fetchone()
                         con.commit()
                         print(rec)
def profite_details():
    qry="select productid,saleQty,totalSale,purchaseSale,(totalSale-purchaseSale) as profit from (select productid,saleQty,totalSale,(saleQty*price) as purchaseSale from (select productid,sum(price) as totalSale,sum(saleQty) as saleQty,(select purshasePrice from product where productid=sale.productid) as price from sale group by productid) as p) as p1"
    cur.execute(qry)
    for i in cur.fetchall():
        for j in i:
            print("%13s"%(str(j)),end="\t")
        print()
                      
                      
