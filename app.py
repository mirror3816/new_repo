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


# 인종에 따른 범죄 기록 수 시각화
@app.route('/number_of_offenses_by_race')
def number_of_offenses_by_race():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='race', data=df)
    plt.title('Number of Offenses by Race')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True, port=1234)

