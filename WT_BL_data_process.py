#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:08:16 2022

@author: hansteven86
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:35:21 2022

@author: hansteven86
"""

import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats



#####wind tunnel data process with pandas

df = pd.read_csv('lab1file2.csv')
#print(df)

cols1 = ['P 1','P 2','P 3','P 4','P 5'
        ,'P 6','P 7','P 8','P 9','P 10']
cols2 = ['P 11','P 12','P 13','P 14','P 15'
        ,'P 16','P 17','P 18','P 19','P 20']

p_ave_lst_mbar = []
for items in cols1:
    p = df[items].iloc[1:104]
    p_num = p.apply(pd.to_numeric)
    p_ave = p_num.mean()
    p_ave_lst_mbar.append(p_ave)

#print(p_ave_lst_mbar)

ptotal_ave_lst_mbar = []
for item in cols2:
    ptotal = df[item].iloc[1:104]
    ptotal_num = ptotal.apply(pd.to_numeric)
    ptotal_ave = ptotal_num.mean()
    ptotal_ave_lst_mbar.append(ptotal_ave)

ptotal_mean = stats.mean(ptotal_ave_lst_mbar)
#print(ptotal_mean)

q_quant = df.iloc[1:104,1]
#print(q_quant)
q_quant_num = q_quant.apply(pd.to_numeric)
q_ave = q_quant_num.mean()
#print(q_ave)

q_processed = []
for values in p_ave_lst_mbar:
    q = abs(values-q_ave-ptotal_mean)
    q_pascal = q*100
    q_processed.append(q_pascal)
#print(q_processed)

rho = 1.19
v = []
for value in q_processed:
    val = (2*value/rho)**0.5
    v.append(val)
#print(v)
height = [0.2, 0.16, 0.12, 0.1, 0.08, 0.06, 0.04, 0.03, 0.025, 0.018]

plt.figure(1)
plt.plot(height,v,'o')
plt.xlabel('port height from plate (m)')
plt.ylabel('velocity experienced by port (m/s)')
plt.title('boundary layer theory plot (v/h)')
plt.grid()
    
    



































