# IPC 코드 정보 찾기 
# 2022.9.17(Sat)
# by B.K. Choi
# warning : 엑셀 파일 읽어야 하기에 시간소모됨 

import pandas as pd
from pandas import DataFrame, Series

def find_ipc_code_single(ptn=None, file_ipc_code="./dic/IPC 분류표_'22.1월 버전.xlsx", col='코드') -> DataFrame:
    """
    한개의 ptn 입력 받아서 ipc 코드 정보 찾고, 데이터 프레임으로 리턴해 주기
    """
    print(f"* pattern={ptn}, sheet_name = {ptn[0]}")
    df=pd.read_excel(file_ipc_code, sheet_name=ptn[0])
    df1=df[df[col].str.contains(ptn, case=False, na=False)]
    return df1

def find_ipc_code_multiple(ptns=None, file_ipc_code="./dic/IPC 분류표_'22.1월 버전.xlsx") -> DataFrame:
    """
    다수의 ptns 입력 받아서 ipc 코드 정보 찾고, 데이터 프레임으로 리턴해 주기
    
    아래 kipris site에서 IPC 엑셀파일 다운로드
    http://www.kipris.or.kr/kpat/remocon/srchIpc/srchIpcFrame.jsp?myConcern=&codeType=IPC
    
    Example
    -------
    names2 = ['F02B39/00', 'F02B37/18', 'F01D25/16', 'F01D17/16', 'F02B39/14']
    df_ipc = find_ipc_code_multiple(names2)
    print(df_ipc.head(1))
    """
    df_list = []
    for ptn in ptns:
        df_temp = find_ipc_code_single(ptn, file_ipc_code=file_ipc_code)
        if len(df_temp)>0:
            df_list.append(df_temp)
    df = pd.concat(df_list, axis=0)
    return df    


if __name__ == '__main__':
    print(__file__)
    names2 = ['F02B39/00', 'F02B37/18', 'F01D25/16', 'F01D17/16', 'F02B39/14']
    df_ipc = find_ipc_code_multiple(names2)
    print(df_ipc.head(1))
