install.packages('gridExtra')
library(dplyr) ## 01: dplyr라이브러리 불러오기
library(ggplot2) ## 02: ggplot2 라이브러리 불러오기
library(gridExtra) ## 03: gridExtra 라이브러리 불러오기
df <- read.csv("C:/R/Rexample/data/tr_mod.csv") ## 04 : tr_mod.csv 파일 읽어오기
col(df) ## 05 : df 행열 확인하기
is(df) ## 06 : df 데이터 속성출력
colnames(df) ## 07 : df컬럼명 확인하기
## table을 통하여 변수의 값들이 몇 개씩 존재하는지, 데이터의 개수를 알 수 있다.
table(df$Pclass) ## 08 : Pclass 별 인원 파악하기
table(df$Embarked) ## 09 : Embarked 별 인원 파악하기
table(df$Survived) ## 10 : Survived 별 인원 파악하기
table(df$SibSp) ## 11 : SibSp 별 인원 파악하기기
max(df$Age) ## 12 : Age중 가장 많은 수
min(df$Age) ## 13 : Age중 가장 적은 수

p1 = ggplot(data = df, aes(x = Age, y = Survived, fill = Sex)) + ylim(0,14) + xlim(0,75) + geom_col() ## 14 : ggplot을 이용한 나이(Age)별 생존수(Survived)그래프
#p1
p2 = ggplot(data = df, aes(x = Sex, y = Survived, fill = Sex)) + geom_col() ## 15 : ggplot을 이용한 성별(Sex)별 생존수(Survived) 그래프
#p2
p3 = ggplot(data = df, aes(x = Pclass, y = Survived, fill = Sex)) + geom_col() ## 16 : ggplot을 이용한 Pclass 별 생존수(Survived) 그래프
#p3
p4 = ggplot(data = df, aes(x = Embarked, y = Survived, fill = Sex)) + geom_col() ## 17 : ggplot을 이용한 Embarked 별 생존수(Survived) 그래프
#p4
grid.arrange(p1, p2, p3, p4, ncol = 2, nrow = 2, top = "Titanic _ Survived") ## 18 : grid를 이용하여 그래프를 나열해 보자.
## 19 : 생존에 가장 큰 영향을 미치는 변수는 무엇인가?
#P1 ~ P4 기준으로 20 ~40대 사이의 여성이면서 1등석을 탔고 Southampton 정박소에서 탑승한 사람