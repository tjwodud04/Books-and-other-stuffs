library(readr)
library(dplyr)
raw_news_comment <- read_csv("news_comment_BTS.csv")
glimpse(raw_news_comment)
# Rows: 1,200
# Columns: 5
# $ reg_time <dttm> 2020-09-01 22:58:09, 2020-09-01 09:56:46, 2020-09-...
# $ reply    <chr> "국보소년단<U+0001F49C>", "아줌마가 들어도 좋더라", "팩트체크\n\n현재 빌보...
# $ press    <chr> "한국경제", "한국경제", "한국경제", "한국경제", "한국경제", "한국경제", "한국...
# $ title    <chr> "[속보]BTS '다이너마이트', 한국 가수 최초로 빌보드 싱글 1위", "[속보]BTS '...
# $ url      <chr> "https://news.naver.com/main/read.nhn?mode=LSD&mid=...

library(stringr)
library(textclean)
news_comment <- raw_news_comment %>%
  mutate(id = row_number(),
         reply = str_squish(replace_html(reply)))

news_comment %>%
  select(id, reply)
# # A tibble: 1,200 x 2
# id reply                                                           
# <int> <chr>                                                           
#   1     1 국보소년단                                                      
#   2     2 아줌마가 들어도 좋더라                                          
#   3     3 팩트체크 현재 빌보드 HOT 100 1위 방탄소년단[BTS] 2위 Cardi B ft. Megan Thee Sta~
#   4     4 방탄소년단이 한국사람이라 너무 자랑스러워요 ㅠㅠ 우리오래오래 함께하자!~
#   5     5 대단한 BTS, 월드 클래스는 다르네^^ 좋은 소식!! 응원해요         
#   6     6 정국오빠 생일과 더불어 빌보드 1위기사라니ㅠㅠ축제구나           
#   7     7 정말 축하하고 응원하지만 집에서 여러 계정으로 스트리밍 돌리고 사재기하고 다른 팬덤 테러하는 애들은 개념보고 놀랐~
#   8     8 기자는 자고 일어났지만, 팬들은 못자고 발표 기다림               
#   9     9 자랑스럽다!!!!!! 축하합니다!!!!                                 
#   10    10 SuperM 늘 응원하고 사랑합니다~                                  
#   # ... with 1,190 more rows
# -------------------------------------------------------------

library(tidytext)
library(KoNLP)
word_comment <- news_comment %>%
  unnest_tokens(input = reply,
                output = word,
                token = "words",
                drop = F)

word_comment %>%
  select(word)
# # A tibble: 11,673 x 1
# word      
# <chr>     
#   1 국보소년단
# 2 아줌마가  
# 3 들어도    
# 4 좋더라    
# 5 팩트체크  
# 6 현재      
# 7 빌보드    
# 8 hot       
# 9 100       
# 10 1         
# # ... with 11,663 more rows

dic <- read_csv("knu_sentiment_lexicon.csv")

word_comment <- word_comment %>%
  left_join(dic, by = "word") %>%
  mutate(polarity = ifelse(is.na(polarity), 0, polarity))

word_comment %>%
  select(word, polarity) %>%
  arrange(-polarity)
# # A tibble: 11,673 x 2
# word       polarity
# <chr>         <dbl>
#   1 대단한            2
# 2 좋은              2
# 3 자랑스럽다        2
# 4 자랑스럽다        2
# 5 자랑스럽다        2
# 6 장하다            2
# 7 꾸준히            2
# 8 행복한            2
# 9 대단한            2
# 10 대단한            2
# # ... with 11,663 more rows

score_comment <- word_comment %>%
  group_by(id, reply) %>%
  summarise(score = sum(polarity)) %>%
  ungroup()

score_comment %>%
  select(score, reply) %>%
  arrange(-score)
# # A tibble: 1,194 x 2
# score reply                                                           
# <dbl> <chr>                                                           
#   1     8 멋지다, 자랑스럽다, 대단하다 방탄소년단!!! 다이너마이트 빌보드 핫100 1위 진심으로 축하해요! 정국이 생일인~
#   2     7 팬은 아니야. 그래서 저 노력과 업적이 더 대단해보여. 정말 멋지다. 잘생긴 사람 예쁜 사람 돈 많은 사람 이런 ~
#   3     6 축하 합니다 우리에 보물이네 대한미국에 애국자 들이다 나라 홍보도하고 달라도벌고 코로나만 아니면 관광객 유도 자랑~
#   4     6 우리딸이 보는 눈이 있네 호르몬전쟁 노래부터 애네들 좋아했는데 그때는 주변에 우리딸이 방탄 좋아한다면 아무도 모를~
#   5     6 ㅜㅜ . 진짜 이 코로나에 너희들이 빛이여. 핫백 1위라니. 모든 기록을 다 갱신해버리는구나. . 진정 감사하고 ~
#   6     6 축하 축하 아미분들도 축하^^                                     
#   7     6 정말 대단하고 자랑스럽습니다.. 국격이 업그레이드 된거 같습니다..축하 축하...~
#   8     6 빌보드 핫100 1위 축하해요 여기까지 오느라 힘들었을텐데 수고했어요 앞으로도 좋은 노래 많이 들려주세요! 좋은 ~
#   9     6 진짜 대단하다. K팝 아시아 최고 넘어서 빌보드 1위 등극 이제 BTS가 그냥 최고네. 이 기록은 정말 수십년동안~
#   10     6 정국이 생일에 빌보드 핫100 1위라니... 정말 뜻깊은 하루네요ㅠㅠ 좋은 음악과 완벽한 무대 그리고 선한 영향력~
#   # ... with 1,184 more rows
# -------------------------------------------------------------

score_comment <- score_comment %>%
  mutate(sentiment = ifelse(score >=  1, "pos",
                            ifelse(score <= -1, "neg", "neu")))

score_comment %>%
  select(sentiment, reply)
# # A tibble: 1,194 x 2
# sentiment reply                                                       
#   <chr>       <chr>                                                       
#   1 neu       국보소년단                                                  
#   2 neu       아줌마가 들어도 좋더라                                      
#   3 pos       팩트체크 현재 빌보드 HOT 100 1위 방탄소년단[BTS] 2위 Cardi B ft. Megan Thee~
#   4 neg       방탄소년단이 한국사람이라 너무 자랑스러워요 ㅠㅠ 우리오래오래 함께하자!~
#   5 pos       대단한 BTS, 월드 클래스는 다르네^^ 좋은 소식!! 응원해요     
#   6 neg       정국오빠 생일과 더불어 빌보드 1위기사라니ㅠㅠ축제구나       
#   7 neu       정말 축하하고 응원하지만 집에서 여러 계정으로 스트리밍 돌리고 사재기하고 다른 팬덤 테러하는 애들은 개념보~
#   8 neu       기자는 자고 일어났지만, 팬들은 못자고 발표 기다림           
#   9 pos       자랑스럽다!!!!!! 축하합니다!!!!                             
#   10 neu       SuperM 늘 응원하고 사랑합니다~                              
#   # ... with 1,184 more rows

frequency_score <- score_comment %>%
  count(sentiment)

frequency_score
# # A tibble: 3 x 2
# sentiment     n
# * <chr>     <int>
#   1 neg         113
# 2 neu         743
# 3 pos         338

library(ggplot2)
ggplot(frequency_score, aes(x = sentiment, y = n, fill = sentiment)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.3)
# -------------------------------------------------------------

comment <- score_comment %>%
  unnest_tokens(input = reply,
                output = word,
                token = "words",
                drop = F)

frequency_word <- comment %>%
  count(sentiment, word, sort = T)

frequency_word
# # A tibble: 6,900 x 3
# sentiment word           n
# <chr>     <chr>      <int>
#   1 neu       1            126
# 2 pos       진짜          90
# 3 pos       1             82
# 4 neu       진짜          79
# 5 pos       자랑스럽다    77
# 6 neu       bts           72
# 7 pos       너무          70
# 8 neu       빌보드        66
# 9 pos       정말          57
# 10 neu       군면제        48
# # ... with 6,890 more rows

library(tidyr)
comment_wide <- frequency_word %>%
  filter(sentiment != "neu") %>%
  pivot_wider(names_from = sentiment,
              values_from = n,
              values_fill = list(n = 0))

comment_wide
# # A tibble: 3,247 x 3
# word         pos   neg
# <chr>      <int> <int>
#   1 진짜          90    20
# 2 1             82    29
# 3 자랑스럽다    77     0
# 4 너무          70    14
# 5 정말          57     5
# 6 위            46    11
# 7 빌보드        40    15
# 8 방탄          39     8
# 9 방탄소년단    39    13
# 10 bts           37    21
# # ... with 3,237 more rows

comment_wide <- comment_wide %>%
  mutate(log_odds_ratio = log(((pos + 1) / (sum(pos + 1))) /
                                ((neg + 1) / (sum(neg + 1)))))

comment_wide
# # A tibble: 3,247 x 4
# word         pos   neg log_odds_ratio
# <chr>      <int> <int>          <dbl>
#   1 진짜          90    20          1.03 
# 2 1             82    29          0.586
# 3 자랑스럽다    77     0          3.93 
# 4 너무          70    14          1.12 
# 5 정말          57     5          1.84 
# 6 위            46    11          0.934
# 7 빌보드        40    15          0.510
# 8 방탄          39     8          1.06 
# 9 방탄소년단    39    13          0.618
# 10 bts           37    21          0.115
# # ... with 3,237 more rows

top10 <- comment_wide %>%
  group_by(sentiment = ifelse(log_odds_ratio > 0, "pos", "neg")) %>%
  slice_max(abs(log_odds_ratio), n = 10)

top10
# # A tibble: 25 x 5
# # Groups:   sentiment [2]
# word     pos   neg log_odds_ratio sentiment
# <chr>  <int> <int>          <dbl> <chr>    
#   1 국내       0     5          -2.22 neg      
# 2 모르는     0     4          -2.04 neg      
# 3 없어서     0     4          -2.04 neg      
# 4 있다       0     4          -2.04 neg      
# 5 널리       0     3          -1.82 neg      
# 6 독도       0     3          -1.82 neg      
# 7 보다       0     3          -1.82 neg      
# 8 아니다     0     3          -1.82 neg      
# 9 없다       0     3          -1.82 neg      
# 10 케이팝     0     3          -1.82 neg      
# # ... with 15 more rows
# -------------------------------------------------------------

ggplot(top10, aes(x = reorder(word, log_odds_ratio),
                  y = log_odds_ratio,
                  fill = sentiment)) +
  geom_col() +
  coord_flip() +
  labs(x = NULL)
# -------------------------------------------------------------

score_comment %>%
  filter(str_detect(reply, "자랑스럽다")) %>%
  arrange(-score) %>%
  
  
  select(reply)
# # A tibble: 82 x 1
# reply                                                                 
# <chr>                                                                 
#   1 멋지다, 자랑스럽다, 대단하다 방탄소년단!!! 다이너마이트 빌보드 핫100 1위 진심으로 축하해요! 정국이 생일인데 최고의 ~
#   2 축하 합니다 우리에 보물이네 대한미국에 애국자 들이다 나라 홍보도하고 달라도벌고 코로나만 아니면 관광객 유도 자랑스럽다 정치~
#   3 자랑스러운 방탄소년단.... 아~~이거 방탄소년단 아입니까!!!! 사랑하는 막둥이정국 생일에 빌보드핫백1위 너희가 정말 자랑~
#   4 자랑스럽다 역사적인 길들을 함께 걸어갈 수 있어 감사하다               
# 5 아시아에서 60년만에 빌보드 핫백 차트 1위 아시아에서 최초로 200차트와 핫백 차트 동시 진입 너무 멋지고 자랑스럽다ㅜㅜㅜ~
#   6 와 진짜 너무 대단하고 자랑스럽다 ! 진짜 꿈인지 생시인지 모르겠네요! 이건 정말 방탄소년단이었기에 가능한 일이었어요 . 다~
#   7 정말 대단하고 자랑스럽다~                                             
#   8 이건 진짜 대서특필 감이다.. 혼란스러운 이 시국에 이렇게 기쁜 소식이라니 진짜 고맙다 대한민국 국민으로서 너무 자랑스럽다~
#   9 진짜 대박이다 방탄 역사를 썼다 대단하고 자랑스럽다!!!!                
#   10 정말 너무 자랑스럽다. 역사의 순간에 있다는 게 고맙고 뿌듯하다         
# # ... with 72 more rows