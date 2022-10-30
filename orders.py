from datetime import *
import xml.etree.ElementTree as ET

resdict={}
tree = ET.parse('orders.xml')
root = tree.getroot()

n=len(root)
it=datetime.now()
print("Processing started at: ",it)
initialtimestamp=it.timestamp()
for i in range(n):
    p=root[i].attrib['book']
    if p in resdict.keys():
        if len(root[i].attrib)==5:
            l=[]
            l.append(root[i].attrib['operation'])
            l.append(root[i].attrib['price'])
            l.append(root[i].attrib['volume'])
            l.append(root[i].attrib['orderId'])
            
            resdict[p].append(l.copy())
            
        else :
            for j in range(len(resdict[p])-1):
                
                if resdict[p][j][3]==root[i].attrib['orderId']:
                    resdict[p].remove(resdict[p][j])
    else :
        resdict[p]=[]
        if len(root[i].attrib)==5:
            l=[]
            l.append(root[i].attrib['operation'])
            l.append(root[i].attrib['price'])
            l.append(root[i].attrib['volume'])
            l.append(root[i].attrib['orderId'])
            resdict[p].append(l)
        else :
            for j in range(len(resdict[p])-1):
                if resdict[p][j][3]==root[i].attrib['orderId']:
                    resdict[p].remove(resdict[p][j])



for key in resdict.keys():
    
    buy=[]
    sell=[]
    for i in range(len(resdict[key])-1):
        if resdict[key][i][0]=="SELL":
            sell.append(resdict[key][i])
        else:
            buy.append(resdict[key][i])

    print("book: ",key)
    print("                       ","Buy -- Sell")
    print("======================================================================")
    while(len(sell)!=0 and len(buy)!=0):
        
        b=buy[0][2]+"@"+buy[0][1]
        s=sell[0][2]+"@"+sell[0][1]
        print("           ",b,"    --     ",s)







ft=datetime.now()
print("Processing completed at: ",ft)
finaltimestamp=ft.timestamp()
print("Processing Duration: ",finaltimestamp-initialtimestamp," seconds")