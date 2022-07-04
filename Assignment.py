import pandas as pd

df_2 = pd.read_csv("deliveries.csv")

#Homeground
x = df_2.loc[[i for i in range(248)],['batting_team','bowling_team','batsman','bowler','innings']]
y_1 = set(x.loc[[i for i in range(125)],['batsman']]['batsman'])
z_1 = set(x.loc[[i for i in range(126,248)],['bowler']]['bowler'])


print('Homeground\n')
print(y_1|z_1,'\n')

#Non Homeground
y_2 = set(x.loc[[i for i in range(125)],['bowler']]['bowler'])
z_2 = set(x.loc[[i for i in range(125,248)],['batsman']]['batsman'])

print('Non Homeground\n')
print(set(z_2|y_2))








