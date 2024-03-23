#Source: https://stackoverflow.com/questions/73978448/python-typeerror-str-object-is-not-callable-inside-a-loop
mi=[]
ni=[] 
for col in df.columns:
  # for ind in df.index:
    # print(df[j][i])
    zxt=df[col].tolist()
    

    for i in zxt:
      
        mi.append("") if(pd.isnull(i)) else mi.append(str(i))
    row3=""
    row2=""

    count=0
    str=""
    # print(mi)
    print("For Column",col)
    # -*- coding: utf-8 -*-
    def remove(x, replacer):
        global count
        count2=0
        for i in x:
            if f"'{i}'" == ascii(i):
                pass
            else:
                count=count+1
                print("flag hit")
                TestText2 = x.encode('utf8')
                print(TestText2,"\n")
                x=x.replace(i,replacer)
                
        return x
    for row in mi:
      remove(row,'')
      ni.append(row)

    print("characters out of order for",count,"times")
    mi.clear()