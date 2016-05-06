import pandas as pd
from scipy import stats
from scipy.stats import ks_2samp

s=[{"date":"20150929","histogram":[4176,924,254,269,213,249,296,209,91,29,21,12,6,5,0,0,0,0,0,0]},
   {"date":"20150930","histogram":[4690,951,250,233,197,185,250,236,97,44,33,14,8,2,2,0,0,0,0,0]},
   {"date":"20151001","histogram":[59,250,192,146,157,319,748,996,1080,741,352,176,109,76,10,2,0,0,0,0]}]

for indx, items in enumerate(s):
    if indx < len(s) - 1:
        t1 = pd.Series(items['histogram'])
        t2 = pd.Series(s[indx+1]['histogram'])
        z_stat, p_val = stats.ttest_ind(t1, t2)
        m_stat, m_val = ks_2samp(t1,t2)
        if m_val <= 0.5:
            print s[indx+1]['date']
            break
        
    
    
