# 기본적인 전처리

library(readr)
library(dplyr)

raw_tada <- read_csv("news_comment_tada.csv") %>%
  mutate(id = row_number())

glimpse(raw_tada)
# Rows: 5,270
# Columns: 8
# $ reg_time       <dttm> 2019-12-05 20:29:54, 2019-12-05 18:11:40, 20...
# $ reply          <chr> "祝[RHG::분단韓백년]결론:진정성!!<U+2714>결과적으로 타다는 택시가 맞...
# $ press          <chr> "연합뉴스", "연합뉴스", "연합뉴스", "연합뉴스", "연합뉴스", "연합뉴스...
# $ title          <chr> "'타다 금지법', 국토위 법안소위 통과", "'타다 금지법', 국토위 법안소위 ...
# $ url            <chr> "https://news.naver.com/main/read.nhn?mode=LS...
# $ sympathyCount  <dbl> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,...
# $ antipathyCount <dbl> 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, ...
# $ id             <int> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14...

library(stringr)
library(textclean)

tada <- raw_tada %>%
  filter(str_count(reply, " ") >= 1) %>%                  
  mutate(reply_raw = str_squish(replace_html(reply)),      
         reply = str_replace_all(reply, "[^가-힣]", " "), 
         reply = str_squish(reply))                   
# -------------------------------------------------------------------------

# 주요 단어 분석하기

library(tidytext)
library(KoNLP)

word_noun <- tada %>%
  unnest_tokens(input = reply,
                output = word,
                token = extractNoun,
                drop = F)

frequency <- word_noun %>%
  count(word, sort = T) %>%
  filter(str_count(word) > 1)

frequency %>%
  head(30) %>%
  print(n = Inf)
# # A tibble: 30 x 2
# word         n
# <chr>    <int>
#   1 택시      3057
# 2 기사       761
# 3 국민       564
# 4 혁신       451
# 5 서비스     416
# 6 들이       402
# 7 불법       397
# 8 생각       325
# 9 산업       291
# 10 나라       278
# 11 영업       269
# 12 사업       261
# 13 사람       241
# 14 우버       237
# 15 진짜       234
# 16 정부       221
# 17 국회의원   210
# 18 이용       203
# 19 면허       202
# 20 하면       193
# 21 하게       185
# 22 승차거부   182
# 23 해서       181
# 24 규제       180
# 25 문제       177
# 26 운전       175
# 27 정치       169
# 28 국회       168
# 29 시대       167
# 30 우리나라   151

stopword_noun <- c("들이", "하면", "하게", "해서")

top20_noun <- frequency %>%
  filter(!word %in% stopword_noun) %>%
  head(20)

top20_noun %>%
  print(n = Inf)
# # A tibble: 20 x 2
# word         n
# <chr>    <int>
#   1 택시      3057
# 2 기사       761
# 3 국민       564
# 4 혁신       451
# 5 서비스     416
# 6 불법       397
# 7 생각       325
# 8 산업       291
# 9 나라       278
# 10 영업       269
# 11 사업       261
# 12 사람       241
# 13 우버       237
# 14 진짜       234
# 15 정부       221
# 16 국회의원   210
# 17 이용       203
# 18 면허       202
# 19 승차거부   182
# 20 규제       180

install.packages("scales")
library(scales)
library(ggplot2)

ggplot(top20_noun, aes(x = reorder(word, n), y = n)) +
  geom_col() +
  coord_flip() +
  geom_text(aes(label = comma(n, accuracy = 1)), hjust = -0.3) +  
  scale_y_continuous(limits = c(0, 3200)) +
  
  labs(title = "타다 금지법 기사 댓글 주요 단어",
       subtitle = "언급 빈도 Top 20",
       x = NULL) +
  
  theme_minimal() +
  theme(text = element_text(family = "nanumgothic", size = 12),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 13))       