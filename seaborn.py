#meplolib 쉽게 해주는놈 = seaborn
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

#a = pd.Series([1,2,3,4,5]).plot()
#들어간 데이터는 리스트
plt.plot([1,3,4,8])

#그래프 이름 박기
plt.title("test")
plt.grid()

#그래프 그리기
plt.show()

#한글 폰트 해결해주기 지금 다 깨짐!
