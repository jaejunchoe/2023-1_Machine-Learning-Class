# -*- coding: utf-8 -*-
"""[기계학습] term_project 상관계수

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QPKzk6n3MOEqvY3CuQZxGf6TNTZxeuBm
"""

import numpy as np
import pandas as pd
from google.colab import drive
from sklearn.preprocessing import LabelEncoder

# 5개년 FA선수 데이터 불러오기
filename = '/content/5개년 FA선수 Data.xlsx'
df = pd.read_excel(filename)

#선수명 제거
df.drop('선수명', axis=1, inplace=True)

# 포지션(타자) 열 레이블 인코딩
label_encoder = LabelEncoder()
df['포지션(타자)'] = label_encoder.fit_transform(df['포지션(타자)'])

# 선수명과 포지션(타자) 열 데이터 유형을 숫자형으로 변환
df['포지션(타자)'] = df['포지션(타자)'].astype(int)

# 타자 데이터와 투수 데이터를 저장할 변수 초기화
타자_df = pd.DataFrame()
투수_df = pd.DataFrame()

# 열 이름을 확인하면서 "(타자)"를 포함하는 열은 타자 데이터로, "(투수)"를 포함하는 열은 투수 데이터로 분류
for column in df.columns:
    if "(타자)" in column:
        타자_df[column] = df[column]
    if "(투수)" in column:
        투수_df[column] = df[column]

# 연봉 열 넣기
타자_df["FA 연봉(억)"] = df["FA 연봉(억)"]
투수_df["FA 연봉(억)"] = df["FA 연봉(억)"]

#결측치 제거
타자_df = 타자_df.dropna().reset_index(drop=True) #재정렬
투수_df = 투수_df.dropna().reset_index(drop=True)

# "FA 연봉(억)" 열 제거 및 따로 정의
타자_salary = 타자_df.pop("FA 연봉(억)") #이제 df_removed에는 연봉이 제거됨
투수_salary = 투수_df.pop("FA 연봉(억)")

import pandas as pd
# X값과 y값 간의 상관 관계 계산
타자correlation_matrix = 타자_df.corrwith(타자_salary)

# 상관 관계 출력
print(타자correlation_matrix)

import pandas as pd
# X값과 y값 간의 상관 관계 계산
투수correlation_matrix = 투수_df.corrwith(투수_salary)

# 상관 관계 출력
print(투수correlation_matrix)

output_file_2 = "/content/타자correlation_matrix.txt"  # 저장할 파일 경로와 이름 지정

with open(output_file_2, "w") as f:
    for feature, value in 타자correlation_matrix.items():
        f.write(f"{feature}: {value}\n")


output_file_2 = "/content/투수correlation_matrix.txt"  # 저장할 파일 경로와 이름 지정

with open(output_file_2, "w") as f:
    for feature, value in 투수correlation_matrix.items():
        f.write(f"{feature}: {value}\n")