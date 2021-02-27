# 기본적인 전처리

raw_news_comment <- read_csv("news_comment_parasite.csv")

install.packages("textclean")
library(textclean)

news_comment <- raw_news_comment %>%
  mutate(id = row_number(),
         reply = str_squish(replace_html(reply)))

glimpse(news_comment)
# Rows: 4,150
# Columns: 6
# $ reg_time <dttm> 2020-02-10 16:59:02, 2020-02-10 13:32:24, 2020-02-...
# $ reply    <chr> "정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하...
# $ press    <chr> "MBC", "SBS", "한겨레", "한겨레", "한겨레", "한겨레", "한겨레", "한...
# $ title    <chr> "'기생충' 아카데미 작품상까지 4관왕…영화사 새로 썼다", "[영상] '기생충' 봉준호, ...
# $ url      <chr> "https://news.naver.com/main/read.nhn?mode=LSD&mid=...
# $ id       <int> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ...
--------------------------------------------------------------------
  
# 단어 기준으로 토큰화하고 감정 점수 부여하기
  
word_comment <- news_comment %>%
  unnest_tokens(input = reply,
                output = word,
                token = "words",
                drop = F)

word_comment %>%
  select(word, reply)
# # A tibble: 37,718 x 2
# word   reply                                                          
# <chr>  <chr>                                                          
#   1 정말   정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   2 우리   정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   3 집에   정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   4 좋은   정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   5 일이   정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   6 생겨   정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   7 기쁘고 정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   8 행복한 정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   9 것처럼 정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   10 나의   정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복~
#   # ... with 37,708 more rows

word_comment <- word_comment %>%
  left_join(dic, by = "word") %>%
  mutate(polarity = ifelse(is.na(polarity), 0, polarity))

word_comment %>%
  select(word, polarity)
# # A tibble: 37,718 x 2
# word   polarity
# <chr>     <dbl>
#   1 정말          0
# 2 우리          0
# 3 집에          0
# 4 좋은          2
# 5 일이          0
# 6 생겨          0
# 7 기쁘고        2
# 8 행복한        2
# 9 것처럼        0
# 10 나의          0
# # ... with 37,708 more rows
----------------------------------------------------------------
  
# 자주 사용된 감정 단어 살펴보기

word_comment <- word_comment %>%
  mutate(sentiment = ifelse(polarity ==  2, "pos",
                     ifelse(polarity == -2, "neg", "neu")))

word_comment %>%
  count(sentiment)
# # A tibble: 3 x 2
# sentiment     n
# * <chr>     <int>
#   1 neg         285
# 2 neu       36671
# 3 pos         762

top10_sentiment <- word_comment %>%
  filter(sentiment != "neu") %>%
  count(sentiment, word) %>%
  group_by(sentiment) %>%
  slice_max(n, n = 10)

top10_sentiment
# # A tibble: 22 x 3
# # Groups:   sentiment [2]
# sentiment word       n
# <chr>     <chr>  <int>
#   1 neg       소름      56
# 2 neg       소름이    16
# 3 neg       아니다    15
# 4 neg       우울한     9
# 5 neg       해         8
# 6 neg       미친       7
# 7 neg       가난한     5
# 8 neg       어려운     5
# 9 neg       힘든       5
# 10 neg       더러운     4
# # ... with 12 more rows

library(ggplot2)
ggplot(top10_sentiment, aes(x = reorder(word, n), 
                            y = n, 
                            fill = sentiment)) +
  geom_col() +
  coord_flip() +
  geom_text(aes(label = n), hjust = -0.3) +
  facet_wrap(~ sentiment, scales = "free") +
  scale_y_continuous(expand = expansion(mult = c(0.05, 0.15))) +  
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))
------------------------------------------------------------------
  
#댓글별 감정 점수 구하고 내용 살펴보기
  
score_comment <- word_comment %>%
  group_by(id, reply) %>%
  summarise(score = sum(polarity)) %>%
  ungroup()

score_comment %>% 
  select(score, reply)
# # A tibble: 4,140 x 2
# score reply                                                           
# <dbl> <chr>                                                           
#   1     6 정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복하~
#   2     6 와 너무 기쁘다! 이 시국에 정말 내 일같이 기쁘고 감사하다!!! 축하드려요 진심으로!!!~
#   3     4 우리나라의 영화감독분들 그리고 앞으로 그 꿈을 그리는 분들에게 큰 영감을 주시게된 봉감독님 그리고 공동각본쓴 한진~
#   4     3 봉준호 감독과 우리나라 대한민국 모두 자랑스럽다. 세계 어디를 가고 우리는 한국인입니다. 모두 힘내고 열심히 삽시~
#   5     0 노벨상 탄느낌이네요 축하축하 합니다                             
# 6     0 기생충 상 받을때 박수 쳤어요.감독상도 기대해요.봉준호 감독 화이팅^^~
#   7     0 대한민국 영화사를 새로 쓰고 계시네요 ㅊㅊㅊ                     
# 8     0 저런게 아카데미상 받으면 '태극기 휘날리며'' '광해' '명량''은 전부문 휩쓸어야겠다.~
#   9     0 다시한번 보여주세요 영화관에서 보고싶은디                       
# 10     2 대한민국 BTS와함께 봉준호감독님까지 대단하고 한국의 문화에 자긍심을 가지게합니다♡~
#   # ... with 4,130 more rows

score_comment %>%
  select(score, reply) %>% 
  arrange(-score)
# # A tibble: 4,140 x 2
# score reply                                                           
# <dbl> <chr>                                                           
#   1    11 아니 다른상을 받은것도 충분히 대단하고 굉장하지만 최고의 영예인 작품상을 받은거는 기생충이 작년 전세계 최고의 영~
#   2     9 봉준호의 위대한 업적은 진보 영화계의 위대한 업적이고 대한민국의 업적입니다. 이런 세계적인 감독이 존경하는 대통령~
#   3     7 이 수상소식을 듣고 억수로 기뻐하는 가족이 있을것 같다. SNS를 통해 자기들을 내세우고 싶어 못견뎌하는 가족이 ~
#   4     7 감사 감사 감사 수상 소감도 3관왕 답네요                         
# 5     6 정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복하~
#   6     6 와 너무 기쁘다! 이 시국에 정말 내 일같이 기쁘고 감사하다!!! 축하드려요 진심으로!!!~
#   7     6 축하 축하 축하 모두들 수고 하셨어요 기생충 화이팅               
# 8     6 축하!!!! 축하!!!!! 오스카의 정복은 무엇보다 시나리오의 힘이다. 작가의 사나리오, 감독의 연출, 배우의 연~
#   9     6 조여정 ㆍ예쁜얼굴때문에 연기력을 제대로 평가받지 못해 안타깝던 내가 좋아하는 배우 싸이코 를 착하게 연기하고 바보~
#   10     6 좋은 걸 좋다고 말하지 못하는 인간들이 참 불쌍해지네....댓글 보니 인생을 자기가 만든 감옥속에 살고 있는 사람~
#   # ... with 4,130 more rows

score_comment %>%
  select(score, reply) %>% 
  arrange(score)
# # A tibble: 4,140 x 2
# score reply                                                           
# <dbl> <chr>                                                           
#   1    -7 기생충 영화 한국인 으로써 싫다 대단히 싫다!! 가난한 서민들의 마지막 자존심을 발골 성형한체 부위별로 대단히 높~
#   2    -6 이 페미민국이 잘 되는 게 아주 싫다. 최악의 나쁜일들과 불운, 불행, 어둡고 암울함만 이 페미민국에 가득하기를~
#   3    -5 특정 인물의 성공을 국가의 부흥으로 연관짓는 것은 미개한 발상이다. 봉준호의 성공을 두고 한국 문화의 성장을 미뤄~
#   4    -4 좌파들이 나라 망신 다 시킨다..ㅠ 설레발 오지게 치더니..꼴랑 각본상 하나?ㅎㅎ bts는 뭐..? 말도 안되는 ~
#   5    -4 부패한 386 민주화 세대 정권의 무분별한 포퓰리즘으로 탄생한 좀비들의 살인을 그린 기생충! 무능한 괴뢰정권의 실~
#   6    -4 기생충 내용은 좋은데 제목이 그래요. 극 중 송강호가족이 부잣집에 대해서 기생충이란 말인가요? 가난한 사람이 기생~
#   7    -4 이런 감독과 이런 배우보고 좌좀 이라고 지1랄하던 그분들 다 어디계시냐? 별점 테러하고 기생충보고 노잼 OOO 영~
#   8    -4 축하합니다. 근데 현실 세계인 한국에선 그보다 훨씬 나쁜 넘인 조로남불 좃국가족과 문재앙을 둘러싸고 죄를 무마하려~
#   9    -4 큰일이다....국제적 망신이다...전 세계사람들이 우리나라를 기생충으로 보면 어쩔래?ㅠㅠ 좌파들이 문제여...ㅠ ~
#   10    -4 더럽고 추잡한 그들만의 리그                                     
# # ... with 4,130 more rows

score_comment %>%
  count(score) %>%
  print(n = Inf)
# # A tibble: 17 x 2
# score     n
# * <dbl> <int>
#   1    -7     1
# 2    -6     1
# 3    -5     1
# 4    -4    17
# 5    -3    35
# 6    -2   175
# 7    -1   206
# 8     0  2897
# 9     1   222
# 10     2   432
# 11     3    57
# 12     4    71
# 13     5     7
# 14     6    14
# 15     7     2
# 16     9     1
# 17    11     1
------------------------------------------------------
  
# 감정 경향 살펴보기

score_comment %>%
  count(score) %>%
  print(n = Inf)
# # A tibble: 17 x 2
# score     n
# * <dbl> <int>
#   1    -7     1
# 2    -6     1
# 3    -5     1
# 4    -4    17
# 5    -3    35
# 6    -2   175
# 7    -1   206
# 8     0  2897
# 9     1   222
# 10     2   432
# 11     3    57
# 12     4    71
# 13     5     7
# 14     6    14
# 15     7     2
# 16     9     1
# 17    11     1  

score_comment <- score_comment %>%
  mutate(sentiment = ifelse(score >=  1, "pos",
                     ifelse(score <= -1, "neg", "neu")))

frequency_score <- score_comment %>%
  count(sentiment) %>%
  mutate(ratio = n/sum(n)*100)

frequency_score
# # A tibble: 3 x 3
# sentiment     n ratio
# * <chr>     <int> <dbl>
#   1 neg         436  10.5
# 2 neu        2897  70.0
# 3 pos         807  19.5

ggplot(frequency_score, aes(x = sentiment, y = n, fill = sentiment)) +
  geom_col() +
  geom_text(aes(label = n), vjust = -0.3) + 
  scale_x_discrete(limits = c("pos", "neu", "neg"))

df <- tibble(contry = c("Korea", "Korea", "Japen", "Japen"),
             sex = c("M", "F", "M", "F"),                   
             ratio = c(60, 40, 30, 70))                     
df
# # A tibble: 4 x 3
# contry sex   ratio
# <chr>  <chr> <dbl>
#   1 Korea  M        60
# 2 Korea  F        40
# 3 Japen  M        30
# 4 Japen  F        70

ggplot(df, aes(x = contry, y = ratio, fill = sex)) + geom_col()

ggplot(df, aes(x = contry, y = ratio, fill = sex)) + 
  geom_col() +
  geom_text(aes(label = paste0(ratio, "%")),
            position = position_stack(vjust = 0.5))

frequency_score$dummy <- 0
frequency_score
# # A tibble: 3 x 4
# sentiment     n ratio dummy
# <chr>     <int> <dbl> <dbl>
#   1 neg         436  10.5     0
# 2 neu        2897  70.0     0
# 3 pos         807  19.5     0

ggplot(frequency_score, aes(x = dummy, y = ratio, fill = sentiment)) +
  geom_col() +
  geom_text(aes(label = paste0(round(ratio, 1), "%")),      
            position = position_stack(vjust = 0.5)) + 
  theme(axis.title.x = element_blank(),
        axis.text.x  = element_blank(),
        axis.ticks.x = element_blank())
