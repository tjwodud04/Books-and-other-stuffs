# 감정 사전 살펴보기

library(readr)
dic <- read_csv("knu_sentiment_lexicon.csv")

library(dplyr)

dic %>% 
  filter(polarity == 2) %>% 
  arrange(word)
# # A tibble: 2,602 x 2
# word              polarity
# <chr>                <dbl>
#   1 가능성이 늘어나다        2
# 2 가능성이 있다고          2
# 3 가능하다                 2
# 4 가볍고 상쾌하다          2
# 5 가볍고 상쾌한            2
# 6 가볍고 시원하게          2
# 7 가볍고 편안하게          2
# 8 가볍고 환하게            2
# 9 가운데에서 뛰어남        2
# 10 가장 거룩한              2
# # ... with 2,592 more rows

dic %>%
  filter(polarity == -2) %>%
  arrange(word)
# # A tibble: 4,799 x 2
# word            polarity
# <chr>              <dbl>
#   1 가난                  -2
# 2 가난뱅이              -2
# 3 가난살이              -2
# 4 가난살이하다          -2
# 5 가난설음              -2
# 6 가난에                -2
# 7 가난에 쪼들려서       -2
# 8 가난하게              -2
# 9 가난하고              -2
# 10 가난하고 어렵다       -2
# # ... with 4,789 more rows

dic %>% 
  filter(word %in% c("좋은", "나쁜"))
# # A tibble: 2 x 2
# word  polarity
# <chr>    <dbl>
#   1 좋은         2
# 2 나쁜        -2

dic %>% 
  filter(word %in% c("기쁜", "슬픈"))
# # A tibble: 2 x 2
# word  polarity
# <chr>    <dbl>
#   1 슬픈        -2
# 2 기쁜         2

dic %>%
  filter(word %in% c("행복하다", "좌절하다"))
# # A tibble: 2 x 2
# word     polarity
# <chr>       <dbl>
#   1 행복하다        2
# 2 좌절하다       -2

library(stringr)
dic %>% 
  filter(!str_detect(word, "[가-힣]")) %>% 
  arrange(word)
# # A tibble: 77 x 2
# word  polarity
# <chr>    <dbl>
# 1 -_-^        -1
# 2 (-;          1
# 3 (-_-)       -1
# 4 (;_;)       -1
# 5 (^-^)        1
# 6 (^^)         1
# 7 (^^*         1
# 8 (^_^)        1
# 9 (^_^;       -1
# 10 (^o^)        1
# # ... with 67 more rows

dic %>% 
  mutate(sentiment = ifelse(polarity >=  1, "pos",
                     ifelse(polarity <= -1, "neg", "neu"))) %>% 
  count(sentiment)
# # A tibble: 3 x 2
# sentiment     n
# * <chr>     <int>
#   1 neg        9829
# 2 neu         154
# 3 pos        4871
-----------------------------------------------------------------

# 문장의 감정 점수 구하기

df <- tibble(sentence = c("디자인 예쁘고 마감도 좋아서 만족스럽다.",
                          "디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다."))
df
# # A tibble: 2 x 1
# sentence                                            
# <chr>                                               
#   1 디자인 예쁘고 마감도 좋아서 만족스럽다.             
# 2 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.

library(tidytext)
df <- df %>% 
  unnest_tokens(input = sentence,
                output = word,
                token = "words",
                drop = F)

df %>% print(n = Inf)
# # A tibble: 12 x 2
# sentence                                             word      
# <chr>                                                <chr>     
#   1 디자인 예쁘고 마감도 좋아서 만족스럽다.              디자인    
# 2 디자인 예쁘고 마감도 좋아서 만족스럽다.              예쁘고    
# 3 디자인 예쁘고 마감도 좋아서 만족스럽다.              마감도    
# 4 디자인 예쁘고 마감도 좋아서 만족스럽다.              좋아서    
# 5 디자인 예쁘고 마감도 좋아서 만족스럽다.              만족스럽다
# 6 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다. 디자인은  
# 7 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다. 괜찮다    
# 8 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다. 그런데    
# 9 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다. 마감이    
# 10 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다. 나쁘고    
# 11 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다. 가격도    
# 12 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다. 비싸다 

df <- df %>% 
  left_join(dic, by = "word") %>% 
  mutate(polarity = ifelse(is.na(polarity), 0, polarity))

df %>% print(n = Inf)
# # A tibble: 12 x 3
# sentence                                            word      polarity
# <chr>                                               <chr>        <dbl>
#   1 디자인 예쁘고 마감도 좋아서 만족스럽다.             디자인           0
# 2 디자인 예쁘고 마감도 좋아서 만족스럽다.             예쁘고           2
# 3 디자인 예쁘고 마감도 좋아서 만족스럽다.             마감도           0
# 4 디자인 예쁘고 마감도 좋아서 만족스럽다.             좋아서           2
# 5 디자인 예쁘고 마감도 좋아서 만족스럽다.             만족스럽다~        2
# 6 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.~ 디자인은         0
# 7 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.~ 괜찮다           1
# 8 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.~ 그런데           0
# 9 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.~ 마감이           0
# 10 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.~ 나쁘고          -2
# 11 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.~ 가격도           0
# 12 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.~ 비싸다          -2

score_df <- df %>%
  group_by(sentence) %>%
  summarise(score  = sum(polarity))

score_df
# # A tibble: 2 x 2
# sentence                                             score
# * <chr>                                                <dbl>
#   1 디자인 예쁘고 마감도 좋아서 만족스럽다.                  6
# 2 디자인은 괜찮다. 그런데 마감이 나쁘고 가격도 비싸다.    -3

