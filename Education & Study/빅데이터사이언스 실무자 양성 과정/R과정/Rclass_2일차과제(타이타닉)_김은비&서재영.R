library(dplyr)
titanic <- read.csv("C:/R/Rexample/data/tr_mod.csv")

P1 <- titanic %>% filter(Embarked == 'C' & Survived == 1)
dim(P1)
count(P1)
#93

P2 <- titanic %>% filter(Sex == 'female' & Survived == 1)
count(P2)
#233

P3 <- titanic %>% filter(Embarked == 'S' & Survived == 1)
count(P3)
#219

P4 <- titanic %>% filter(Embarked == 'Q' & Survived == 1)
count(P4)
#30

P5 <- titanic %>% filter(Age < 30 & Survived == 1)
count(P5)
#208

P6 <- titanic %>% filter(Sex == 'male' & Survived == 1)
count(P6)
#109

P7 <- titanic %>% filter(Pclass == 1 & Survived == 1)
count(P7)
#136

P8 <- titanic %>% filter(Pclass == 2 & Survived == 1)
count(P8)
#87

P9 <- titanic %>% filter(Pclass == 3 & Survived == 1)
count(P9)
#119

P10 <- titanic %>% filter(Sex == 'female' & Age < 30 & Survived == 1)
count(P10)
#141

P12 <- titanic %>% filter(Sex == 'male' & Age < 30 & Survived == 1)
count(P12)
#67

P11 <- titanic %>% filter(Survived == 1)
count(P11)
#342  ///890

P13 <- titanic %>% filter(Parch == 0 & Survived == 1)
count(P13)

P14 <- titanic %>% filter(Survived == 0)
count(P14)

P14 <- titanic %>% filter(Survived == 0)
count(P14)

P15 <- titanic %>% filter(Survived==1 & Parch == 0)
count(P15)
# 233

P16 <- titanic %>% filter(Survived==1 & Fare >= 32.20)
count(P16)
#126

P17 <- titanic %>% filter(Survived==1 & Fare < 32.20)
count(P17)
#216

P18 <- titanic %>% filter(Survived==1 & SibSp == 0)
count(P18)
#210

P19 <- titanic %>% filter(Sex=='female' & Survived==1 & Age >= 30)
count(P19)
#92

P20 <- titanic %>% filter(Sex=='male' & Survived==1 & Age >= 30)
count(P20)
#42
