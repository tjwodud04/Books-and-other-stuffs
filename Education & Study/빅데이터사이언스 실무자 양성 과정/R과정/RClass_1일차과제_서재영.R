install.packages("dplyr")
library(dplyr)
search()

df_exam <- read.csv("C:\\R\\Rexample\\data\\csv_exam.csv")
df_exam$mean <- ((df_exam$math + df_exam$english + df_exam$science) /3)
df_exam
write.csv(df_exam, file = "C:\\R\\Rexample\\result.csv")

test_1 <- data.frame(name = c( 'hanna', 'joy', 'tei', 'cabin', 'mike' , 'beky', 'mimi', 'daniel', 'hans', 'rucy'), class = c(1, 2, 3, 3, 4, 3, 3, 2, 1, 2))

test_2 <- data.frame(name = c( 'hanna', 'mimi', 'daniel', 'mike', 'beky' , 'joy', 'tei', 'cabin', 'hans', 'rucy '), english = c(55, 50, 45, 60, 70, 80, 90, 85, 65, 60), math = c(70, 83, 60, 95, 80, 75, 45, 60, 70, 80))

df <- merge(test_1, test_2, by = "name")

dim(df)
head(df, 3)
tail(df, 3)
colnames(df)
