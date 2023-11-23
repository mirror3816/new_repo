from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)

# CSV 파일 읽기
file_path = 'cox-violent-parsed_filt_usable.csv'
df = pd.read_csv(file_path)

@app.route('/')
def index():
    # 성별에 따른 평균 나이 시각화
    gender_age_plot = plot_to_base64(sns.barplot, x='sex', y='age', data=df, title='Average Age by Gender')

    # 인종에 따른 범죄 기록 수 시각화
    race_plot = plot_to_base64(sns.countplot, x='race', data=df, title='Number of Offenses by Race')

    # 범죄 등급에 따른 평균 나이 시각화
    decile_score_plot = plot_to_base64(sns.barplot, x='decile_score', y='age', data=df, title='Average Age by Decile Score')

    # 폭력 예측 여부에 따른 성별 분포 시각화
    violent_recid_plot = plot_to_base64(sns.countplot, x='is_violent_recid', hue='sex', data=df, title='Distribution of Gender by Violent Recidivism')

    return render_template('index.html', gender_age_plot=gender_age_plot, race_plot=race_plot,
                           decile_score_plot=decile_score_plot, violent_recid_plot=violent_recid_plot)

def plot_to_base64(plot_function, **kwargs):
    plt.figure(figsize=(8, 6))
    plot_function(**kwargs)
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return base64.b64encode(img.getvalue()).decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)

