import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('C:\\Users\\LENOVO\\Documents\\salesdata.csv')

Mno=df['MONTH']
QR=df['QUARTER']
perfume=df['perfume']
Fmask=df['face mask']
Haccess=df['hair accessories']
Fcream=df['face cream']
cloth=df['clothing']
Bsoap=df['bathing soap']
TU=df['total_units']
TP=df['total profit']
sal=df['sales']

#submenu 2 for data visualisation
def submenu2():
    ch2=0
    while ch2!=6:
        print('\n-----------------------------------------')
        print('           DATA VISUALISATION MENU         ')
        print('1.Line graph : month wise - unit sold for each product')
        print('2. Scatter plot - month vs total unit sold')
        print('3. multibar plot for product wise units sold')
        print('4. histogram - company profit per month')
        print('5. pie chart- total sum of units sold ,product wise')
        print('6. go back to main menu')
        ch2=int(input('\n choose a option for data visualisation : '))
        if ch2==1:
            plt.plot( Mno,perfume,label='perfume',color='r',linestyle='-')
            plt.plot( Mno,Fmask,label='face mask',color='b',linestyle='-.' )
            plt.plot( Mno,Haccess,label='hair accessories',color='g',linestyle='-')
            plt.plot( Mno,Fcream,label='face cream',color='k',linestyle='-')
            plt.plot( Mno,cloth,label='clothing',color='y',linestyle='-')
            plt.plot( Mno,Bsoap,label='bathing soap',color='m',linestyle='-')
            #plt.xticks(np.arange(0,13,1),fontsize=12,rotation=30)
           # plt.yticks(np.arange(1000,15000,1000),fontsize=8,rotation=30)
            plt.xlabel('month number',fontsize=16)
            plt.ylabel('sales units',fontsize=16)
            plt.legend(loc='upper left')
            plt.title('SALES-PRODUCT wise unit sold',fontsize=18)
            plt.grid(True)
            plt.savefig('C:\\Users\\LENOVO\\Documents\\fig\\multiline.png')
            plt.show()
        elif ch2==2:
            plt.scatter(Mno,TU,s=100,c='g',label='total_units')
            plt.scatter(Mno,perfume,s=100,c='r',label='perfume')
           # plt.xticks(np.arange(0,13,1),fontsize=12,rotation=30)
           # plt.yticks(np.arange(1000,31000,1000),fontsize=8,rotation=30)
            plt.xlabel('month number',fontsize=16)
            plt.ylabel('sales unit',fontsize=16)
            plt.title('SALES DATA - Total unit sold',fontsize=18)
            plt.grid(True)
            plt.savefig('C:\\Users\\LENOVO\\Documents\\fig\\scatter.png')
            plt.show()
        elif ch2==3:
            x1=np.arange(1,13,1)
            x2= x1 + 0.15
            x3= x2 + 0.15
            x4= x3 + 0.15
            x5= x4 + 0.15
            x6= x5 + 0.15
            plt.bar(x1,perfume,tick_label=Mno,width=0.15,label='perfume')
            plt.bar(x2,Fmask,tick_label=Mno,width=0.15,label='face mask')
            plt.bar(x3,Haccess,tick_label=Mno,width=0.15,label='hair accessories')
            plt.bar(x4,Fcream,tick_label=Mno,width=0.15,label='face cream')
            plt.bar(x5,cloth,tick_label=Mno,width=0.15,label='clothing')
            plt.bar(x6,Bsoap,tick_label=Mno,width=0.15,label='bathing soap')
           # plt.xticks(x4,labels=Mno,fontsize=10,rotation=0)
            #plt.yticks(np.arange(1000,12000,1000),fontsize=8,rotation=30)
            plt.xlabel('Names',fontsize=16)
           # plt.ylabel("marks".fontsize=16)
            plt.legend()
            plt.grid(True)
            plt.title('multiple bar plot - term wise comaprison',fontsize=18)
            plt.savefig('C:\\Users\\LENOVO\\Documents\\fig\\multibar.png')
            plt.show()
        elif ch2==4:
            plt.hist(TP,bins=4,range=(100000,350000),edgecolor='k')
           # plt.xticks(np.arange(150000,400000,50000),fontsize=12,rotation=30)
            #plt.yticks(np.arange(0,9,1),fontsize=12,rotation=30)
            plt.xlabel('total profit',fontsize=16)
            plt.ylabel('months',fontsize=16)
            plt.legend()
            plt.grid(True)
            plt.title('Histogram-company profit months',fontsize=16)
            plt.savefig('C:\\Users\\LENOVO\\Documents\\fig\\histogram.png')
            plt.show()
        elif ch2==5:
            S_perfume=df['perfume'].sum()
            S_Fmask=df['face mask'].sum()
            S_Haccess=df['hair accessories'].sum()
            S_Fcream=df['face cream'].sum()
            S_cloth=df['clothing'].sum()
            S_Bsoap=df['bathing soap'].sum()
            sums = [S_perfume,S_Fmask,S_Haccess,S_Fcream,S_cloth,S_Bsoap]
            Slabels = ['perfume','faec mask','hair accessories','face cream','clothing','bathing soap']
            plt.pie(sums,labels=Slabels)
            plt.axis='equal'
            plt.title('pie plot',fontsize=16)
            plt.legend(loc = 'lower left')
            plt.savefig('C:\\Users\\LENOVO\\Documents\\fig\\piechart.png')
            plt.show()
        elif ch2==6:
            mainmenu()
        else:
            print('wrong input')
#submenu3 for data analysis
def submenu3():
    ch1=0
    while ch1!=4:
        print('\n--------------------------------')
        print('       DATA ANALYSIS MENU          ' )
        print('----------------------------------')
        print('1.find the maximum,minimum,mean,sumof - total units and total unit profit earned')
        print('2. display the details of sales of those 3 months which have highest sales')
        print('3. first quartile,second quartile and third quartile of total profit')
        print('4. go back to main menu')
        ch1=int(input('\nChoose a option for data analysis :'))
        if ch1==1:
            print('the maximum,minimum,mean,sumof - total units and total unit profit earned')
            print(df.aggregate({'total_units':['max','min','mean','sum'],'total profit':['max','min','mean','sum']}))
        elif ch1==2:
            print('details of sales of those 3 months which have highest sales')
            print(df.sort_values('total profit',ascending=False).head(3) )
        elif ch1 == 3:
            print('first quartile,second quartile and third quartile of total profit')
            print(df['total profit'].quantile([0.25,0.50,0.75]))
        elif ch1 == 4:
            mainmenu()
        else :
            print('wrong input')

#main  menu containg all the required options
def mainmenu():
    choice=0
    while choice!=4:
        print('\n--------------------------------')
        print('           MAIN MENU              ')
        print('----------------------------------')
        print('1.DISPLAY DATA')
        print('2. DATA VISUALISATION')
        print('3. DATA ANALYSIS')
        print('4. EXIT')
        choice=int(input('\n Choose a option from the main menu'))
        if choice == 1:
            print('  display  data')
            print(df)
            print(df.columns)
        elif choice == 2:
            submenu2()
        elif choice == 3:
            submenu3()
        elif choice == 4 :
            exit(0)
        else :
            print('wrong input')

mainmenu()
                   
            

            
