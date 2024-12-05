def report(x,a):
    print(f"Degree : {a} \n ")
    print("Sr.No. Roll No.   Student Name               ITC  PF DLD Total %age Grade ")
    print("============================================ === === === ===== ==== ===== ")
    ict=0
    pf=0
    dld=0
    count=0
    j=0
    i=[]
    p=[]
    dl=[]
    t=[]
    for line in x:
        name=line[3:41]
        s=line[42:45]
        b=line[49:51]
        c=line[52:55]
        d=line[55:57]
        
            
        if s == "ITC":
        
            ict = int(b)+int(c)+int(d)
        elif s == "DLD":
                
            dld=int(b)+int(c)+int(d)
        else:
            
            pf=int(b)+int(c)+int(d)
        
    
        if ict!=0 and pf!=0 and dld!=0:
            i.append(ict)
            p.append(pf)
            dl.append(dld)
            total=ict+pf+dld
            t.append(total)
            perc=(total*100)//300
            if perc > 85:
                grade = "A"
            elif perc >80 and perc <85:
                grade = "A-"
            elif perc >75 and perc <80:
                grade = "B+"
            elif perc >70 and perc <75:
                grade = "B"
            elif perc >65 and perc <70:
                grade = "B-"
            elif perc >60 and perc <65:
                grade = "C+"
            elif perc >55 and perc <60:
                grade = "C"
            elif perc >50 and perc <55:
                grade = "C-"
            elif perc <50:
                grade = "F"
            print(f"{a}{name}    {ict}  {pf}  {dld}  {total}   {format((total*100)/300,'.1f')} {grade}")
            ict=0
            pf=0
            dld=0
            j=j+1
    ave_ict=format((sum(i)*100)/(j*100),'.0f')
    ave_pf=format((sum(p)*100)/(j*100),'.0f')
    ave_dld=format((sum(dl)*100)/(j*100),'.0f')
    ave_total=format((sum(t)*100)/(j*100),'.0f')
    
    print(f"                       {a} Degree Average :  {ave_ict}  {ave_pf}  {ave_dld}  {ave_total}")
            
    
    
def main():
    f1=open("grades.txt",'r')
    n=f1.readline()
    m=f1.readline()
    x=f1.readlines()
    print(len(x))
    y=[];z=[];a='';b=''
    for i in x:
        if i[0:3]=="BSE":
            y.append(i)
            a=i[0:3]
        else:
            z.append(i)
            b=i[0:3]
    report(y,a)
    print('\n\n')
    report(z,b)
        
    f1.close()
main()
