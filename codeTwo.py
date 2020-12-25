import pandas as pd
df = pd.DataFrame({'User': [1,2,3,4],'Pr': ['0','11','21','12'], 'Lf': ['11','12','13','14'],  'Rf': ['21','22','23','24']})
#print(df)
pr = df.Pr.to_list()

for i in pr:
    df1 = df.loc[df['Pr'] == i]
    print(df1.to_string(index=False))
    x = df1.Lf.to_string(index=False)
    tt = str(x) # <-------------------------- int vs str problem Don't Work properly

    print(tt)
    print(df.Pr == tt)
    #print(df.Pr == x) # <--- This line also give error output
   
    
    
