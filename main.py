import pandas as pd
import FinanceDataReader as fdr

#fdr.stockListing("종목이름") 해당 시장 전부다 불러오기
#KOSPI KOSDAQ KONEW NASDAQ NYSE SP500
df_krx = fdr.StockListing("KRX")

#전체 데이터 출력
print(df_krx)

#위에 5개 불러오기
print(df_krx.head())

#불러온 df 속해있는 행렬 보기 // 소스 뒤져보니까 얘는 함수가 아님
print(df_krx.shape)

#데이터 column 정보보기
print(df_krx.info())

#전체 기술 통계 확인
print(df_krx.describe())

#unique 값 정리해서 볼 수 있음
print(df_krx.nunique())

#해당 folder krx.csv 로 저장하기
df_krx.to_csv("krx.csv", index=False)

#도로 읽어오기
print(pd.read_csv("krx.csv"))


# 추가
#현재 받아들여지는 종목 이름이 영어로 나옴
#컬럼 영어를 -> 한글 바꾸고 df에 다시 씌우기
'''
url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
df_listing = pd.read_html(url, header=0)[0]
cols_ren = {'회사이름':'Name', '코드':'Symbol', '업종':'Sector', '주요제품':'Industry', 
                    '상장일':'ListingDate', '결산월':'SettleMonth',  '대표자ㅣ름':'Representative', 
                    '홈페이지':'HomePage', '지역':'Region', }
df = df_listing.rename(columns = cols_ren)
df['Symbol'] = df['Symbol'].apply(lambda x: '{:06d}'.format(x))
df['ListingDate'] = pd.to_datetime(df['ListingDate'])
df
'''

#다시 바낌 ㅋㅋ 아ㅏㅏㅏㅓㅏ아아아ㅏㅁ니ㅏㅜㅇㄹㅍㅇㅁ나ㅣㅜ로니ㅏㅓㅁ개ㅔㅑㅓㅏ4제ㅑㅐ'ㅓㅏㄱㄹ234ㅈ댜ㅐㅓ'ㅁㅈㄱ허ㅏ뉴ㅜ;ㅑㅇㅊ히ㅏㅜㅍㅌ