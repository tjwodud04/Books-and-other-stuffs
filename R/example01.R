## 데이터 다루기

kor <- c(80, 80, 90)
eng <- c(90, 80, 80)
math <- c(95, 100, 70)

data.frame

df_score <- data.frame(kor, eng, math)
df_score

is(df_score)
class(df_score)
mean(df_score)
mean(df_score$kor)
mean(df_score$eng)
mean(df_score$math)

#한글 변수명은 지양하기기
제품 <- c('사과', '딸기', '수박')
가격 <- c(60000, 8000, 120000)
판매량 <- c(10, 5, 5)

data.frame

df_score02 <- data.frame(제품, 가격, 판매량)
df_score02

mean(df_score02$가격)
mean(df_score02$판매량)
class(df_score02$판매량)
class(df_score02$가격)
class(df_score02$제품) #factor : 범주형
summary(df_score02)

install.packages("readxl")
library(readxl)
search()

df_exam <- read_excel('C:\\R\\Rexample\\data\\excel_exam.xlsx')
df_exam
dim(df_exam)
names(df_exam)
head(df_exam,7)
summary(df_exam)
is(df_exam)

df_exam_csv <- read.csv('C:\\R\\Rexample\\data\\csv_exam.csv', header = T)
df_exam_csv

?read.csv

df_score03 <- data.frame(kor,eng,math)
df_score03

df_score2 <- data.frame(product = c('사과','딸기','수박'), price=c(6000,8000,12000), 판매량=c(10,5,5), 매출액= c(60000, 40000, 60000))
df_score2
write.csv(df_score2, file="C:\\R\\Rexample\\df_score.csv")

View(df_score2)

#numeric <- 실수 정수 다 포함
#범주형 데이터가 몇 개로 되어 있는가

mtcars
dim(mtcars)
names(mtcars)
head(mtcars)
summary(mtcars)
is(mtcars)
str(mtcars)
tail(mtcars)

##dplyr
install.packages("dplyr")
library(dplyr)
install.packages("ggplot2")
library(ggplot2)
df_new <- mpg
#rm(all_df)

names(df_new)

#컬럼 이름 변경?
#cty -> city
#hwy -> highway
#dplyr :: rename(데이터셋, 변경할 변수명 = 현재변수명)

df_new <- rename(df_new, city = cty)
df_new <- rename(df_new, highway = hwy)
df_new <- rename(df_new, fuel = fl)
names(df_new)
