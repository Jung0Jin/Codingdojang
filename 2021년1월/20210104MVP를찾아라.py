# https://codingdojang.com/scode/642?answer_mode=hide

import pandas as pd

PlayerName = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5']
KDA = ['1/6/3','5/6/2','4/1/4','6/3/2','4/5/7','4/3/2','1/4/6','5/1/4','6/4/1','4/5/1']

PlayerData = pd.DataFrame(KDA,PlayerName,['kda'])

def CP(kda):
    kda_str=kda.split('/')
    CalculPoint = '('+kda_str[0]+'*2'+'+'+kda_str[1]+')'+'/'+kda_str[2]
    return eval(CalculPoint)

CPData=pd.DataFrame(PlayerData['kda'].apply(CP)).rename(columns={'kda':'CP'}) #KDA 데이터에 함수 적용

pd.concat([PlayerData,CPData],axis=1) #적용된 데이터 붙여서 CP를 Dataframe으로 확인

MVP=list(PlayerData[(CPData['CP']==max(CPData['CP']))].index)[0] #MVP 탐색

print ('POTG : '+ MVP)
