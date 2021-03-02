# 텍스트 합치기

library(dplyr)

raw_moon <- readLines("speech_moon.txt", encoding = "UTF-8")

moon <- raw_moon %>%
  as_tibble() %>%
  mutate(president = "moon")

raw_park <- readLines("speech_park.txt", encoding = "UTF-8")

park <- raw_park %>%
  as_tibble() %>%
  mutate(president = "park")

bind_speeches <- bind_rows(moon, park) %>%
  select(president, value)

head(bind_speeches)
# # A tibble: 6 x 2
# president value
# <chr>     <chr>
#   1 moon      "정권교체 하겠습니다!"
# 2 moon      "  정치교체 하겠습니다!"
# 3 moon      "  시대교체 하겠습니다!"
# 4 moon      "  "
# 5 moon      "  ‘불비불명(不飛不鳴)’이라는 고사가 있습니다. 남쪽 언덕 나뭇가지에 앉아, 3년 동안 날지도 울지도 않~
# 6 moon      ""

tail(bind_speeches)
# # A tibble: 6 x 2
#   president value
#   <chr>     <chr>
# 1 park      "국민들이 꿈으로만 가졌던 행복한 삶을 실제로 이룰 수 있도록 도와드리는 대통령이 되고 싶습니다. 국민 여러~
#   2 park      ""
# 3 park      "감사합니다."
# 4 park      ""
# 5 park      "2012년 7월 10일"
# 6 park      "새누리당 예비후보 박근혜"
-------------------------------------------------------------------
  
  #집단별 단어 빈도 구하기
  
  library(stringr)

speeches <- bind_speeches %>%
  mutate(value = str_replace_all(value, "[^가-힣]", " "), value = str_squish(value))

speeches
# # A tibble: 213 x 2
# president value
# <chr>     <chr>
#   1 moon      "정권교체 하겠습니다"
# 2 moon      "정치교체 하겠습니다"
# 3 moon      "시대교체 하겠습니다"
# 4 moon      ""
# 5 moon      "불비불명 이라는 고사가 있습니다 남쪽 언덕 나뭇가지에 앉아 년 동안 날지도 울지도 않는 새 그러나 그 새~
#  6 moon      ""
#  7 moon      "그 동안 정치와 거리를 둬 왔습니다 그러나 암울한 시대가 저를 정치로 불러냈습니다 더 이상 남쪽 나뭇가지~
#   8 moon      ""
# 9 moon      ""
# 10 moon      "우리나라 대통령 이 되겠습니다"
# # ... with 203 more rows

library(tidytext)
library(KoNLP)

speeches <- speeches %>%
  unnest_tokens(input = value, output = word, token = extractNoun)

speeches
# # A tibble: 2,997 x 2
# president word
# <chr>     <chr>
#   1 moon      "정권교체"
# 2 moon      "하겠습니"
# 3 moon      "정치"
# 4 moon      "교체"
# 5 moon      "하겠습니"
# 6 moon      "시대"
# 7 moon      "교체"
# 8 moon      "하겠습니"
# 9 moon      ""
# 10 moon      "불비불명"
# # ... with 2,987 more rows

df <- tibble(class = c("a", "a", "a", "b", "b", "b"), sex = c("female", "male", "female", "male", "male", "female"))

df
# # A tibble: 6 x 2
# class sex
# <chr> <chr>
#   1 a     female
# 2 a     male
# 3 a     female
# 4 b     male
# 5 b     male
# 6 b     female

df %>% count(class, sex)
# # A tibble: 4 x 3
# class sex        n
# <chr> <chr>  <int>
#   1 a     female     2
# 2 a     male       1
# 3 b     female     1
# 4 b     male       2

frequency <- speeches %>%
  count(president, word) %>%
  filter(str_count(word) > 1)

head(frequency)
# # A tibble: 6 x 3
# president word         n
# <chr>     <chr>    <int>
#   1 moon      가동         1
# 2 moon      가사         1
# 3 moon      가슴         2
# 4 moon      가족         1
# 5 moon      가족구조     1
# 6 moon      가지         4
-----------------------------------------------
  
# 자주 사용된 단어 추출하기
  
df <- tibble(x = c(1:100))
df
# # A tibble: 100 x 1
# x
# <int>
#   1     1
# 2     2
# 3     3
# 4     4
# 5     5
# 6     6
# 7     7
# 8     8
# 9     9
# 10    10
# # ... with 90 more rows

df %>%
  slice_max(x, n = 3)
# # A tibble: 3 x 1
# x
# <int>
#   1   100
# 2    99
# 3    98

top10 <- frequency %>%
  group_by(president) %>%
  slice_max(n, n = 10)

top10
## A tibble: 22 x 3
## Groups:   president [2]
# president word       n
# <chr>     <chr>  <int>
#   1 moon      국민      21
# 2 moon      일자리    21
# 3 moon      나라      19
# 4 moon      우리      17
# 5 moon      경제      15
# 6 moon      사회      14
# 7 moon      성장      13
# 8 moon      대통령    12
# 9 moon      정치      12
# 10 moon      하게      12
# # ... with 12 more rows

top10 %>%
  filter(president == "park") %>%
  print(n = Inf)
# # A tibble: 12 x 3
# # Groups:   president [1]
# president word       n
# <chr>     <chr>  <int>
#   1 park      국민      72
# 2 park      행복      23
# 3 park      여러분    20
# 4 park      정부      17
# 5 park      경제      15
# 6 park      신뢰      11
# 7 park      국가      10
# 8 park      우리      10
# 9 park      교육       9
# 10 park      사람       9
# 11 park      사회       9
# 12 park      일자리     9
--------------------------------------------------
  
#빈도 동점 단어 제외하고 추출하기
  
df <- tibble(x = c("A", "B", "C", "D"), y = c(4, 3, 2, 2))

df %>%
  slice_max(y, n = 3)
# # A tibble: 4 x 2
# x         y
# <chr> <dbl>
#   1 A         4
# 2 B         3
# 3 C         2
# 4 D         2

df %>%
  slice_max(y, n = 3, with_ties = F)
# # A tibble: 3 x 2
# x         y
# <chr> <dbl>
#   1 A         4
# 2 B         3
# 3 C         2

top10 <- frequency %>%
  group_by(president) %>%
  slice_max(n, n = 10, with_ties = F)

top10
# # A tibble: 20 x 3
# # Groups:   president [2]
# president word       n
# <chr>     <chr>  <int>
#   1 moon      국민      21
# 2 moon      일자리    21
# 3 moon      나라      19
# 4 moon      우리      17
# 5 moon      경제      15
# 6 moon      사회      14
# 7 moon      성장      13
# 8 moon      대통령    12
# 9 moon      정치      12
# 10 moon      하게      12
# 11 park      국민      72
# 12 park      행복      23
# 13 park      여러분    20
# 14 park      정부      17
# 15 park      경제      15
# 16 park      신뢰      11
# 17 park      국가      10
# 18 park      우리      10
# 19 park      교육       9
# 20 park      사람       9
----------------------------------------------
  
# 막대 그래프 만들기
  
ggplot(top10, aes(x = reorder(word, n), y = n, fill = president)) +
  geom_col() + coord_flip() + facet_wrap(~ president, scales = "free_y")

top10 <- frequency %>%
  filter(word != "국민") %>%
  group_by(president) %>%
  slice_max(n, n = 10, with_ties = F)

top10
# # A tibble: 20 x 3
# # Groups:   president [2]
# president word         n
# <chr>     <chr>    <int>
#   1 moon      일자리      21
# 2 moon      나라        19
# 3 moon      우리        17
# 4 moon      경제        15
# 5 moon      사회        14
# 6 moon      성장        13
# 7 moon      대통령      12
# 8 moon      정치        12
# 9 moon      하게        12
# 10 moon      대한민국    11
# 11 park      행복        23
# 12 park      여러분      20
# 13 park      정부        17
# 14 park      경제        15
# 15 park      신뢰        11
# 16 park      국가        10
# 17 park      우리        10
# 18 park      교육         9
# 19 park      사람         9
# 20 park      사회         9

ggplot(top10, aes(x = reorder(word, n), y = n, fill = president)) +
  geom_col() + coord_flip() + facet_wrap(~ president, scales = "free_y")

ggplot(top10, aes(x = reorder_within(word, n, president), y = n, fill = president)) + geom_col() + coord_flip() + facet_wrap(~ president, scales = "free_y")

ggplot(top10, aes(x = reorder_within(word, n, president), y = n, fill = president)) + geom_col() + coord_flip() + facet_wrap(~ president, scales = "free_y") + scale_x_reordered() + labs(x = NULL) + theme(text = element_text(family = "nanumgothic"))

df_long <- frequency %>%
  group_by(president) %>%
  slice_max(n, n = 10) %>%
  filter(word %in% c("국민", "우리", "정치", "행복"))

df_long
# # A tibble: 6 x 3
# # Groups:   president [2]
# president word      n
# <chr>     <chr> <int>
#   1 moon      국민     21
# 2 moon      우리     17
# 3 moon      정치     12
# 4 park      국민     72
# 5 park      행복     23
# 6 park      우리     10

