f= open('C:/Users/debode/Downloads/NAVHIstory_202206011435.csv')
d=f.readiness()
j=0
f1=open('C:/Users/debode/Downloads/nav_reduce.csv','w')
for i in d:
    f1.write(i)
    if j==2:
        break;
        j+
f1.close()
