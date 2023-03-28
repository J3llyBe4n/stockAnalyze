import pandas as pd
#meplolib 쉽게 해주는놈
import seaborn as sns

#종목코드 앞자리 0 날라가서 object 형태로 바로 가져오기
df = pd.read_csv("krx.csv",dtype={"Code": object})
df.shape

#df.tail() df.head() 끝에서 몇개 앞에서 몇개 가져오기 df.sample() 랜덤값 돌려주기 한개



