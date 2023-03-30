import pandas as pd

#종목코드 앞자리 0 날라가서 object 형태로 바로 가져오기
df = pd.read_csv("krx.csv",dtype={"Code": object})
print(df)

print(df.describe())
#df.tail() df.head() 끝에서 몇개 앞에서 몇개 가져오기 df.sample() 랜덤값 돌려주기 한개

#1번 행만 다 불러오기 2개 이상의 행을 가져올때도 리스트 형태로 빼야함
### 중요 .loc[행, 열] or .loc[조건식, 열]
df.loc[1]
df.loc[[0,1]]
df.loc[[1,2,3]]


#name 칼럼을 가진 열만 쫙 불러오기 참고 2개 이상의 칼럼을 일괄 출력할때는 리스트 형태로 뽑아야함
df["Name"]
df[["Code", "Name"]]

#만약 위 4개 출력할때, df타입으로 가져오려면 중괄호 하나 더 씌워서 df 형식으로 형 변환 발라줌
df[["Name"]]

#df 내에서 중괄호 하나면 type가 series고, 그걸 df 형태로 바꾸러면 []하나 더 씌워줌

#특정 행열 가져오는거 1번 행에 column이 name 인놈만 땡기기
df.loc[1, "Name"]

#행열 둘다 다중이면 둘다 싸주면댐
z =df.loc[[1,2,3],["Name","Code"]]
print(z)

#특정 값을 찾기 //특정한 값을 찾으려면 df로 한번더 감싸주면댐 if문 개념
df[df["Name"] == '카카오']

#종목 파이가 코스피인 것들 중에 종목번호가 005930인것을 뿌리는 것 조건이 2개일때! 논리 연산자 사용하고 boolean
#함수를 리턴하므로 그걸 df로 다시싸서 value 값을 챙겨오기
df[(df["Market"] == "KOSPI") & (df["Code"] == "005930")]

#위 조건 주석이 조건문일때, 부합하는 조건 중 원하는 column만 뺴오고싶을떄 .loc[조건 , 원하는 칼럼]
a =df.loc[(df["Market"] == "KOSPI") & (df["Code"] == "005930"),["Code"]]
print(a)
print(type(a))

#위 조건에서 종목파이가 kospi 인걸 변수로 지정하면 boolean 으로 들어가므로, df 프레임으로 한번 씌워줘야함
print("-------------------------")
b = df["Market"] == "KOSPI"
c = df["Code"] == "005930"
print(df[b])
print(type(b))
print(c)

#조건 두개에 대한 걸 변수에 저장 후, name,column 칼럼명 데이타만 뽑아낼때
d =df.loc[b & c, ["Name","Code"]]
print(d)

#특정 column의 데이터 타입 변환 series 타입은 찾는 column 명에 중괄호 하나 더 씌워버리기
print(df["Name"])
print(type(df["Name"]))
print("-------------------")
print(type(df[["Name"]])) #(df[["Name"]])
print("-------------")
for i in range(5):
    print(df.loc[i,["Name","Code"]])

print(type(z))
print(z)





