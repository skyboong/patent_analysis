# IPC 코드 정보 찾기 
# 2022.9.17(Sat)
# by B.K. Choi
# warning : 엑셀 파일 읽어야 하기에 시간소모됨 

import pandas as pd
from pandas import DataFrame, Series



def count_method(data, sep=';', option='int', kind=1) -> dict:
    """

    couting 방법 :

    kind : 1 특허건수
           2 피인용회수

    option : 'int' 정수
             'float' 분수

    return
    ------
    dict()

    Example
    -------
    출원인별 피인용수 : 분수 기준
    count_method(['출원인1;출원인2',10], sep=';', option='float', kind=2)

    """
    dic1 = {}
    len_x = 0 # 출원인 수

    if kind == 1:  # 특허 건수 계산할 때,
        if pd.isna(data):
            return {}

        x1 = data.split(sep)
        x2 = sorted(set(x1))  # 중복된 것 제거
        x3 = [each1.strip() for each1 in x2 if each1.strip() != '']
        len_x = len(x3)

        if option in [1, 'int']:
            for each3 in x3:
                dic1[each3] = 1
        else:
            for each3 in x3:
                dic1[each3] = 1 / len(x3)

    else:  # 피인용수 계산 할 때, data 는
        # data[0] : 출원인
        # data[1] : 피인용수

        x = data[0] # 출원인
        citation_no = data[1]

        if pd.isna(x):
            return {}
        if pd.isna(citation_no):
            citation_no=0

        x1 = x.split(sep)
        x2 = sorted(set(x1))  # 중복된 것 제거
        x3 = [each1.strip() for each1 in x2 if each1.strip() != '']

        len_x = len(x3)

        if option in [1, 'int']:
            for each3 in x3:
                dic1[each3] = citation_no
        else:
            #print(".")
            # 배분하기
            for each3 in x3:
                dic1[each3] = citation_no / len_x

        #if (citation_no > 56) and (len_x >2) :
        #    # print(f" 출원인 : {x}, 출원인수 : {len_x}, dic1={dic1}")
        #    print(f"\noption : {option}, dic1={dic1}")

    return dic1



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
