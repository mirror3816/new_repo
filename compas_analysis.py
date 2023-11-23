import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 읽기
file_path = 'cox-violent-parsed_filt_usable.csv'
df = pd.read_csv(file_path)

# 데이터 정보 확인
print(df.info())

# 상위 5개 행 확인
print(df.head())

# 기술통계량 확인
print(df.describe())

# 성별에 따른 평균 나이 시각화
sns.barplot(x='sex', y='age', data=df)
plt.title('Average Age by Gender')
plt.show()

# 인종에 따른 범죄 기록 수 시각화
sns.countplot(x='race', data=df)
plt.title('Number of Offenses by Race')
plt.show()

# 범죄 등급에 따른 평균 나이 시각화
sns.barplot(x='decile_score', y='age', data=df)
plt.title('Average Age by Decile Score')
plt.show()

# 폭력 예측 여부에 따른 성별 분포 시각화
sns.countplot(x='is_violent_recid', hue='sex', data=df)
plt.title('Distribution of Gender by Violent Recidivism')
plt.show()
