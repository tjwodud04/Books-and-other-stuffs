install.packages("multilinguer")
library(multilinguer)
install_jdk()

install.packages(c("stringr", "hash", "tau", "Sejong", "RSQLite", "devtools"), type = "binary")

install.packages("remotes")
remotes::install_github("haven-jeon/KoNLP", upgrade = "never", INSTALL_opts = c("--no-multiarch"))

library(KoNLP)

useNIADic()
------------------------------------------------
# 형태소분석기를 이용해 토큰화하기
  
library(dplyr)
text <- tibble(value = c("대한민국은 민주공화국이다.", "대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."))
text
# # A tibble: 2 x 1
# value
# <chr>
#   1 대한민국은 민주공화국이다.
# 2 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.

extractNoun(text$value)
# [[1]]
# [1] "대한민국"   "민주공화국"
# 
# [[2]]
# [1] "대한민국" "주권"     "국민"     "권력"     "국민"

library(tidytext)
text %>%
  unnest_tokens(input = value, output = word, token = extractNoun)
# # A tibble: 7 x 1
# word
# <chr>
#   1 대한민국
# 2 민주공화국
# 3 대한민국
# 4 주권
# 5 국민
# 6 권력
# 7 국민

raw_moon <- readLines("speech_moon.txt", encoding = "UTF-8")

library(stringr)
library(textclean)

moon <- raw_moon %>%
  str_replace_all("[^가-힣]", " ") %>%
  str_squish() %>%
  as_tibble()

word_noun <- moon %>%
  unnest_tokens(input = value, output = word, token = extractNoun)

word_noun
# # A tibble: 1,757 x 1
# word
# <chr>
#   1 "정권교체"
# 2 "하겠습니"
# 3 "정치"
# 4 "교체"
# 5 "하겠습니"
# 6 "시대"
# 7 "교체"
# 8 "하겠습니"
# 9 ""
# 10 "불비불명"
# # ... with 1,747 more rows
