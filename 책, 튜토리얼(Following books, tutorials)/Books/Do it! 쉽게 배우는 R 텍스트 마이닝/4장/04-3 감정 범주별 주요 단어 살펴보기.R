# 감정 범주별 단어 빈도 구하기

comment <- score_comment %>%
  unnest_tokens(input = reply,
                output = word,
                token = "words",
                drop = F) %>%
  filter(str_detect(word, "[가-힣]") & str_count(word) >= 2)

frequency_word <- comment %>%
  filter(str_count(word) >= 2) %>%
  count(sentiment, word, sort = T)

frequency_word %>%
  filter(sentiment == "pos")
# # A tibble: 5,234 x 3
# sentiment word           n
# <chr>     <chr>      <int>
#   1 pos       봉준호       106
# 2 pos       정말          97
# 3 pos       대단하다      83
# 4 pos       진짜          79
# 5 pos       자랑스럽다    78
# 6 pos       축하          63
# 7 pos       대한민국      61
# 8 pos       영화          58
# 9 pos       멋지다        55
# 10 pos       기생충        53
# # ... with 5,224 more rows

frequency_word %>%
  filter(sentiment == "neg")
# # A tibble: 4,080 x 3
# sentiment word             n
# <chr>     <chr>        <int>
#   1 neg       소름            49
# 2 neg       봉준호          47
# 3 neg       기생충          33
# 4 neg       이런            33
# 5 neg       정말            32
# 6 neg       진짜            26
# 7 neg       좌빨            21
# 8 neg       너무            20
# 9 neg       블랙리스트에    19
# 10 neg       영화            18
# # ... with 4,070 more rows
# --------------------------------------

# 상대적으로 자주 사용된 단어 비교하기

library(tidyr)

comment_wide <- frequency_word %>%
  filter(sentiment != "neu") %>%
  pivot_wider(names_from = sentiment,
              values_from = n,
              values_fill = list(n = 0))

comment_wide
# # A tibble: 8,380 x 3
# word         pos   neg
# <chr>      <int> <int>
#   1 봉준호       106    47
# 2 정말          97    32
# 3 대단하다      83     1
# 4 진짜          79    26
# 5 자랑스럽다    78     1
# 6 축하          63     0
# 7 대한민국      61     4
# 8 영화          58    18
# 9 멋지다        55     0
# 10 기생충        53    33
# # ... with 8,370 more rows

comment_wide <- comment_wide %>%
  mutate(log_odds_ratio = log(((pos + 1) / (sum(pos + 1))) /
                                ((neg + 1) / (sum(neg + 1)))))

comment_wide
# # A tibble: 8,380 x 4
# word         pos   neg log_odds_ratio
# <chr>      <int> <int>          <dbl>
#   1 봉준호       106    47          0.589
# 2 정말          97    32          0.876
# 3 대단하다      83     1          3.52 
# 4 진짜          79    26          0.873
# 5 자랑스럽다    78     1          3.46 
# 6 축하          63     0          3.95 
# 7 대한민국      61     4          2.30 
# 8 영화          58    18          0.920
# 9 멋지다        55     0          3.81 
# 10 기생충        53    33          0.250
# # ... with 8,370 more rows

top10 <- comment_wide %>%
  group_by(sentiment = ifelse(log_odds_ratio > 0, "pos", "neg")) %>%
  slice_max(abs(log_odds_ratio), n = 10)

top10 %>% print(n = Inf)
# # A tibble: 30 x 5
# # Groups:   sentiment [2]
# word         pos   neg log_odds_ratio sentiment
# <chr>      <int> <int>          <dbl> <chr>    
#   1 소름           2    49          -3.03 neg      
# 2 좌빨           1    21          -2.61 neg      
# 3 못한           0     7          -2.29 neg      
# 4 미친           0     7          -2.29 neg      
# 5 좌좀           0     6          -2.16 neg      
# 6 소름이         1    12          -2.08 neg      
# 7 가난한         0     5          -2.00 neg      
# 8 모르는         0     5          -2.00 neg      
# 9 아쉽다         0     5          -2.00 neg      
# 10 닭그네         0     4          -1.82 neg      
# 11 돋았다         0     4          -1.82 neg      
# 12 두고           0     4          -1.82 neg      
# 13 못하고         0     4          -1.82 neg      
# 14 사회적         0     4          -1.82 neg      
# 15 싫다           0     4          -1.82 neg      
# 16 있는데         0     4          -1.82 neg      
# 17 정권이         0     4          -1.82 neg      
# 18 지들이         0     4          -1.82 neg      
# 19 틀딱           0     4          -1.82 neg      
# 20 힘든           0     4          -1.82 neg      
# 21 축하          63     0           3.95 pos      
# 22 멋지다        55     0           3.81 pos      
# 23 대단한        47     0           3.66 pos      
# 24 좋은          42     0           3.55 pos      
# 25 대단하다      83     1           3.52 pos      
# 26 자랑스럽다    78     1           3.46 pos      
# 27 최고          27     0           3.12 pos      
# 28 세계적인      24     0           3.01 pos      
# 29 최고의        23     0           2.97 pos      
# 30 위대한        22     0           2.92 pos 

top10 <- comment_wide %>%
  group_by(sentiment = ifelse(log_odds_ratio > 0, "pos", "neg")) %>%
  slice_max(abs(log_odds_ratio), n = 10, with_ties = F)

top10 %>% print(n = Inf)
# # A tibble: 20 x 5
# # Groups:   sentiment [2]
# word         pos   neg log_odds_ratio sentiment
# <chr>      <int> <int>          <dbl> <chr>    
#   1 소름           2    49          -3.03 neg      
# 2 좌빨           1    21          -2.61 neg      
# 3 못한           0     7          -2.29 neg      
# 4 미친           0     7          -2.29 neg      
# 5 좌좀           0     6          -2.16 neg      
# 6 소름이         1    12          -2.08 neg      
# 7 가난한         0     5          -2.00 neg      
# 8 모르는         0     5          -2.00 neg      
# 9 아쉽다         0     5          -2.00 neg      
# 10 닭그네         0     4          -1.82 neg      
# 11 축하          63     0           3.95 pos      
# 12 멋지다        55     0           3.81 pos      
# 13 대단한        47     0           3.66 pos      
# 14 좋은          42     0           3.55 pos      
# 15 대단하다      83     1           3.52 pos      
# 16 자랑스럽다    78     1           3.46 pos      
# 17 최고          27     0           3.12 pos      
# 18 세계적인      24     0           3.01 pos      
# 19 최고의        23     0           2.97 pos      
# 20 위대한        22     0           2.92 pos

ggplot(top10, aes(x = reorder(word, log_odds_ratio),
                  y = log_odds_ratio,
                  fill = sentiment)) +
  geom_col() +
  coord_flip() +
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))