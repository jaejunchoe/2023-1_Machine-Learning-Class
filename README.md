# 2023-1_Machine-Learning-Class
국립금오공과대학교 2023-1학기 기계학습 수업 프로젝트_Prof. 김민준

<br/><br/>

# ✨ Team K2R1
- 구성원
* 팀장: 정민규 - 국립금오공과대학교 산업경영공학전공 3학년
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
- 프로야구 관련 신문기사 탐색
* Problem Definition: `FA 계약규모가 점점 커지면서 실력 대비 과도한 연봉을 받는 사례가 늘어나고 있다.`

* Project Purpose: `지난 5년간 FA 선수들와 비FA 선수들의 기록 통하여 2024년 FA를 자격을 갖출 예정인 KBO 선수들의 FA 연봉 예측`


![기계학습_텀프로젝트_디자인공학전공_4조](https://github.com/jaejunchoe/2023-1_Machine-Learning-Class/assets/157339263/da855a1e-01ec-437a-9d89-0dfacc2c1a31)


<br/><br/>
## 3. Modeling
- AI 모델 구현 로드맵
![image](https://github.com/jaejunchoe/2023-Gumi-Industrial-Complex-Energy-Self-Sufficiency-Datathon/assets/157339263/b790f4db-db7f-46ac-b2f4-7a73f2e42b43)

<br/>

- 사용 알고리즘
  
(1) Linear Models (선형모델) – 'Linear Regression', 'SVR'

(2) Neural Networks (인공신경망) – 'Neural Network', 'MLPRegression'

(3) Ensemble Models (앙상블) – 'Random Forest', 'Neural Network', 'Voting', 'Stacking'

(4) Gradient Boosting (그래디언트 부스팅) – 'LGBM Regression', 'Gradient Boosting Regression'

(5) RNN – 'LSTM'

(6) KNN - 'KNN'

<br/><br/>
## 4. Data Analysis And Results 
- Clustering & AI Model 학습 결과

  **최적 예측 모델** = `Ensemble Model` 


     (1) 구미산단 데이터톤 전력사용량 데이터
     ![image](https://github.com/jaejunchoe/2023-Gumi-Industrial-Complex-Energy-Self-Sufficiency-Datathon/assets/157339263/4c01505b-8f5a-4e1f-882f-9826820a92cd)



     (2) 구미산단 데이터톤 태양광 발전량 데이터
     ![image](https://github.com/jaejunchoe/2023-Gumi-Industrial-Complex-Energy-Self-Sufficiency-Datathon/assets/157339263/3271426a-e849-440e-bb21-a1c0e6078cbb)



     (3) 구미 에너지자급자족사업 참여기업 A사 전력량 데이터
     ![image](https://github.com/jaejunchoe/2023-Gumi-Industrial-Complex-Energy-Self-Sufficiency-Datathon/assets/157339263/81966e72-1443-41c7-b2b9-28e19919435f)

<br/><br/>
## 5. Conclusion & Comment
- 데이터의 크기 및 규모가 크고 개인 노트북을 사용하기에 모델 실행과 디버깅을 하기에 많은 시간이 소요되어 어려움이 존재했다.
- 팀원 모두가 데이터톤의 경험이 전무했기에 EDA에서 많은 시간이 소요되었다. 특히, 전력량의 시차 연관성을 파악에 많은 고민을 했다.
- Clustering에서 K-Means Clustering으로만 진행하다가 교수님의 자문을 통해 시계열 클러스터링을 통해서 비슷한 패턴을 갖는 기업끼리 Clustering을 하니 훨씬 수월하게 진행되었다. 
- 여러 알고리즘들을 구현 및 적용하여 결과를 비교하면서 해당 데이터의 최적 알고리즘을 도출할 수 있었다.
- 1가지의 알고리즘을 사용한 것과 여러 알고리즘을 활용하는 Ensemble Model의 평가지표값이 차이가 크게 존재하지 않았다. 





