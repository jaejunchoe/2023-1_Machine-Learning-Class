# 2023-1_Machine-Learning-Class
국립금오공과대학교 2023-1학기 기계학습 수업 프로젝트_Prof. 김민준

<br/><br/>

# ✨ Team 4조
- 구성원
* 팀장: 정민규 - 국립금오공과대학교 디자인인공학전공 3학년
* 팀원: 김주환, 김호성, 전민욱, 최재준 - 국립금오공과대학교 산업경영공학전공 3학년 

<br/><br/>

# 🗂 Presentation
## 1. Data
- STATIZ(한국프로야구 기록 데이터베이스 및 온라인정보 제공)
1. 타자 데이터 추출 인자 (92개)
* '주요'지표 - 타율, 출루율, 장타율, OPS을 포함한 48개의 지표  
* '확장'지표 - wOBA, wRC, wRC/27, wRAA, wRC+을 포함한 총 18개
* '세부'지표 - 파크펙터 조정 wOBA , wRC, wRC/27, wRAA, wRC+을 포함한 총 26개

2. 투수 데이터 추출 인자 (72개)
* '주요'기록 - 승, 패, 홀드, 세이브, 이닝, ERA, FIP을 포함한 37개
* '확장'기록 - K/9, BB/9, K/BB, WHIP을 포함한 16개
* '세부'기록 - 파크펙터 조정 ERA, FIP, RA을 포함한 19개

3. 2019~2023년까지 FA권리를 행사한 실제 야구선수(83명) + 비FA계약(7명)을 맺은 총 90명의 기록지표
* 2019 두산 양의지, LG 박용택을 포함한 15명
* 2020 기아 안치홍, LG 오지환을 포함한 18명
* 2021 롯데 이대호, 두산 허경민을 포함한 15명
* 2022 LG 김현수, NC 나성범을 포함한 15명 + 비FA 삼성 구자욱을 포함한 4명
* 2023 NC 한현희, LG 유강남을 포함한 20명 + 비FA 롯데 박세웅을 포함한 3명



<br/><br/>
## 2. Problem Definition & Project Purpose
* Problem Definition: `FA 계약규모가 점점 커지면서 실력 대비 과도한 연봉을 받는 사례가 늘어나고 있다.`
* Project Purpose: `지난 5년간 FA 선수들와 비FA 선수들의 기록 통하여 2024년 FA를 자격을 갖출 예정인 KBO 선수들의 FA권리 행사시 1년치 연봉 예측`


![기계학습_텀프로젝트_디자인공학전공_4조](https://github.com/jaejunchoe/2023-1_Machine-Learning-Class/assets/157339263/da855a1e-01ec-437a-9d89-0dfacc2c1a31)


<br/><br/>
## 3. Modeling
- AI 모델 구현 로드맵
![기계학습 4조_발표 PPT_ver 06](https://github.com/user-attachments/assets/3b38857c-4ccf-437f-b962-13c19fd98192)

<br/>

- 사용 알고리즘: `RandomForestRegressor`

- 하이퍼파라미터: `GridSearchCV를 사용하여 n_estimators, max_depth, min_samples_split, min_samples_leaf 도출`


<br/><br/>
## 4. Data Analysis And Results 
- 예측 결과


     (1) 예측된 FA 최고 금액 계약 예상자 TOP 4
  
     ![슬라이드17](https://github.com/user-attachments/assets/a6163416-a5df-4c34-ba4a-cd53b85e5435)



     (2) 나머지 2024 FA 취득 예정자의 연봉 예측
  
     ![슬라이드18](https://github.com/user-attachments/assets/7c9d0e10-e224-4c65-a823-174d3663352f)



<br/><br/>
## 5. Conclusion & Comment
- 결정계수(R2 Score)값이 타자의 경우에는 약 0.52로 나왔지만 투수의 경우에는 약 0.31로 나와 전체적으로 봤을 때, 좋은 모델이라고 보기에는 어렵다.
- Correlation 분석에서 세이버매트릭스 지표가 FA금액을 결정하는데 있어 많은 연관성을 가졌다는 점에서 
- 세이버매트릭스(sabermetrics)처럼 통계적으로 세부적이고 과학적 지표가 효과가 있음을  확인할 수 있었다.
- 투수의 데이터 수가 타자에 비해서 적었다는 점에서 투수의 모델을 구성하고 분석하는데 있어서 아쉬움이 존재했다.
- 선수들의 FA금액을 판단하는데 있어서 지표만으로 판단하는 것을 섣부른 판단이라는 것을 알게 되었다.





