df <- data.frame(var1=c(1,3,5),
                 var2=c(2,4,6))
df

names(df)
##파생변수
df$sum <- df$var1 + df$var2
df

df$sub <- df$var1 - df$var2
df

df$divide <- df$var1 / df$var2
df

df$multiple <- df$var1 * df$var2
df

install.packages('ggplot2')
library(ggplot2)
mpg

dat <- mpg
names(dat)
?mtcars

dat$total <- dat$hwy + dat$cty
dat
?hist
hist(dat$total)
?qplot
qplot(dat$total, geom = "point")
