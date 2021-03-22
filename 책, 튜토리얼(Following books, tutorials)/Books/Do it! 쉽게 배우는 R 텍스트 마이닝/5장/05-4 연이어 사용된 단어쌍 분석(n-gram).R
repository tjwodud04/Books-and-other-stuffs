# n-gram으로 토큰화하기

text <- tibble(value = "대한민국은 민주공화국이다. 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.")

text %>%
  unnest_tokens(input = value,
                output = word,
                token = "ngrams",
                n = 2)
# # A tibble: 9 x 1
# word                     
# <chr>                    
#   1 대한민국은 민주공화국이다
# 2 민주공화국이다 대한민국의
# 3 대한민국의 주권은        
# 4 주권은 국민에게          
# 5 국민에게 있고            
# 6 있고 모든                
# 7 모든 권력은              
# 8 권력은 국민으로부터      
# 9 국민으로부터 나온다      

text %>%
  unnest_tokens(input = value,
                output = word,
                token = "ngrams",
                n = 3)
# # A tibble: 8 x 1
# word                                
# <chr>                               
#   1 대한민국은 민주공화국이다 대한민국의
# 2 민주공화국이다 대한민국의 주권은    
# 3 대한민국의 주권은 국민에게          
# 4 주권은 국민에게 있고                
# 5 국민에게 있고 모든                  
# 6 있고 모든 권력은                    
# 7 모든 권력은 국민으로부터            
# 8 권력은 국민으로부터 나온다 

text %>%
  unnest_tokens(input = value,
                output = word,
                token = "words")
# # A tibble: 10 x 1
# word          
# <chr>         
#   1 대한민국은    
# 2 민주공화국이다
# 3 대한민국의    
# 4 주권은        
# 5 국민에게      
# 6 있고          
# 7 모든          
# 8 권력은        
# 9 국민으로부터  
# 10 나온다

text %>%
  unnest_tokens(input = value,
                output = word,
                token = "ngrams",
                n = 1)
# # A tibble: 10 x 1
# word          
# <chr>         
#   1 대한민국은    
# 2 민주공화국이다
# 3 대한민국의    
# 4 주권은        
# 5 국민에게      
# 6 있고          
# 7 모든          
# 8 권력은        
# 9 국민으로부터  
# 10 나온다

comment_new <- comment_pos %>%
  separate_rows(word, sep = "[+]") %>%
  filter(str_detect(word, "/n|/pv|/pa")) %>%
  mutate(word = ifelse(str_detect(word, "/pv|/pa"),
                       str_replace(word, "/.*$", "다"),
                       str_remove(word, "/.*$"))) %>%
  filter(str_count(word) >= 2) %>%
  arrange(id)

comment_new <- comment_new %>%
  mutate(word = ifelse(str_detect(word, "감독") &
                         !str_detect(word, "감독상"), "봉준호", word), 
         word = ifelse(word  == "오르다", "올리다", word),
         word = ifelse(str_detect(word, "축하"), "축하", word))

comment_new %>%
  select(word)
# # A tibble: 26,860 x 1
# word  
# <chr> 
#   1 우리  
# 2 좋다  
# 3 생기다
# 4 기쁘다
# 5 행복한
# 6 행복  
# 7 축하  
# 8 행복  
# 9 기쁘다
# 10 기쁘다
# # ... with 26,850 more rows

line_comment <- comment_new %>%
  group_by(id) %>%
  summarise(sentence = paste(word, collapse = " "))

line_comment
# # A tibble: 4,007 x 2
# id sentence                                                        
# * <int> <chr>                                                           
#   1     1 우리 좋다 생기다 기쁘다 행복한 행복 축하 행복 기쁘다            
# 2     2 기쁘다 시국 기쁘다 감사하다 축하 진심                           
# 3     3 우리나라 봉준호 불다 크다 영감 봉준호 공동각본쓴 한진 작가님 축하 축하 드리다~
#   4     4 봉준호 봉준호 우리나라 대한민국 자랑 세계 어디 우리 한국인 힘내다 삽시~
#   5     5 노벨상 탄느낌이네요 축하                                        
# 6     6 기생충 받다 박수 치다 감독상 기대다 봉준호 봉준호               
# 7     7 대한민국 영화사 쓰다 계시다                                     
# 8     8 아카데미상 받다 태극기 휘날리다 광해 명량 전부문 휩쓸어야겠     
# 9     9 다시한번 보이다 영화관                                          
# 10    10 대한민국 봉준호 대단 한국의 문화 자긍심 가지                    
# # ... with 3,997 more rows

bigram_comment <- line_comment %>%
  unnest_tokens(input = sentence,
                output = bigram,
                token = "ngrams",
                n = 2)

bigram_comment
# # A tibble: 23,348 x 2
# id bigram       
# <int> <chr>        
#   1     1 우리 좋다    
# 2     1 좋다 생기다  
# 3     1 생기다 기쁘다
# 4     1 기쁘다 행복한
# 5     1 행복한 행복  
# 6     1 행복 축하    
# 7     1 축하 행복    
# 8     1 행복 기쁘다  
# 9     2 기쁘다 시국  
# 10     2 시국 기쁘다  
# # ... with 23,338 more rows
# ----------------------------------------------

# 연이어 사용된 단어쌍 빈도 구하기

bigram_seprated <- bigram_comment %>%
  separate(bigram, c("word1", "word2"), sep = " ")

bigram_seprated
# # A tibble: 23,348 x 3
# id word1  word2 
# <int> <chr>  <chr> 
#   1     1 우리   좋다  
# 2     1 좋다   생기다
# 3     1 생기다 기쁘다
# 4     1 기쁘다 행복한
# 5     1 행복한 행복  
# 6     1 행복   축하  
# 7     1 축하   행복  
# 8     1 행복   기쁘다
# 9     2 기쁘다 시국  
# 10     2 시국   기쁘다
# # ... with 23,338 more rows

pair_bigram <- bigram_seprated %>%
  count(word1, word2, sort = T) %>%
  na.omit()

pair_bigram
# # A tibble: 19,030 x 3
# word1      word2          n
# <chr>      <chr>      <int>
#   1 봉준호     봉준호       155
# 2 블랙리스트 올리다        64
# 3 진심       축하          64
# 4 봉준호     축하          57
# 5 봉준호     송강호        34
# 6 영화       만들다        31
# 7 축하       봉준호        31
# 8 대단       축하          27
# 9 봉준호     블랙리스트    27
# 10 대박       축하          26
# # ... with 19,020 more rows

pair %>%
  filter(item1 == "대한민국")
# # A tibble: 1,024 x 3
# item1    item2          n
# <chr>    <chr>      <dbl>
#   1 대한민국 자랑          44
# 2 대한민국 봉준호        38
# 3 대한민국 영화          30
# 4 대한민국 축하          27
# 5 대한민국 기생충        27
# 6 대한민국 국민          22
# 7 대한민국 축하드리다    19
# 8 대한민국 감독          18
# 9 대한민국 세계          16
# 10 대한민국 아카데미      16
# # ... with 1,014 more rows

pair_bigram %>%
  filter(word1 == "대한민국")
# # A tibble: 109 x 3
# word1    word2      n
# <chr>    <chr>  <int>
#   1 대한민국 국민      21
# 2 대한민국 자랑      15
# 3 대한민국 영화      11
# 4 대한민국 국격       8
# 5 대한민국 위상       7
# 6 대한민국 만세       6
# 7 대한민국 봉준호     5
# 8 대한민국 문화       4
# 9 대한민국 영광       4
# 10 대한민국 기생충     3
# # ... with 99 more rows

pair %>%
  filter(item1 == "아카데미")
# # A tibble: 1,261 x 3
# item1    item2      n
# <chr>    <chr>  <dbl>
#   1 아카데미 기생충    47
# 2 아카데미 작품상    44
# 3 아카데미 영화      42
# 4 아카데미 봉준호    25
# 5 아카데미 받다      23
# 6 아카데미 한국      23
# 7 아카데미 아니다    23
# 8 아카데미 수상      22
# 9 아카데미 미국      22
# 10 아카데미 시상식    20
# # ... with 1,251 more rows

pair_bigram %>%
  filter(word1 == "아카데미")
# # A tibble: 141 x 3
# word1    word2      n
# <chr>    <chr>  <int>
#   1 아카데미 작품상    22
# 2 아카데미 시상식    19
# 3 아카데미 수상       7
# 4 아카데미 감독상     6
# 5 아카데미 로컬       6
# 6 아카데미 개부문     4
# 7 아카데미 받다       4
# 8 아카데미 빨갱이     4
# 9 아카데미 역사       4
# 10 아카데미 왕이       4
# # ... with 131 more rows
# ----------------------------------------------

# n-gram으로 네트워크 그래프 만들기

word_network <- function(x) {
  ggraph(x, layout = "fr") +
    geom_edge_link(color = "gray50",
                   alpha = 0.5) +
    geom_node_point(color = "lightcoral",
                    size = 5) +
    geom_node_text(aes(label = name),
                   repel = T,
                   size = 5,
                   family = "nanumgothic") +
    theme_graph()
}

graph_bigram <- pair_bigram %>%
  filter(n >= 8) %>%
  as_tbl_graph()

set.seed(1234)
word_network(graph_bigram)

bigram_seprated <- bigram_seprated %>%
  mutate(word1 = ifelse(str_detect(word1, "대단"), "대단", word1),
         word2 = ifelse(str_detect(word2, "대단"), "대단", word2),
         
         word1 = ifelse(str_detect(word1, "자랑"), "자랑", word1),
         word2 = ifelse(str_detect(word2, "자랑"), "자랑", word2),
         
         word1 = ifelse(str_detect(word1, "짝짝짝"), "짝짝짝", word1),
         word2 = ifelse(str_detect(word2, "짝짝짝"), "짝짝짝", word2)) %>%
  
  filter(word1 != word2)

pair_bigram <- bigram_seprated %>%
  count(word1, word2, sort = T) %>%
  na.omit()

bigram_seprated_new <- bigram_seprated %>%
  mutate_at(vars("word1", "word2"),
            ~ case_when(
              str_detect(., "대단") ~ "대단",
              str_detect(., "자랑") ~ "자랑",
              str_detect(., "짝짝짝") ~ "짝짝짝",
              T ~ .))

set.seed(1234)
graph_bigram <- pair_bigram %>%
  filter(n >= 8) %>%
  as_tbl_graph(directed = F) %>%
  mutate(centrality = centrality_degree(),
         group = as.factor(group_infomap()))


set.seed(1234)
ggraph(graph_bigram, layout = "fr") +
  geom_edge_link(color = "gray50",
                 alpha = 0.5) +
  geom_node_point(aes(size = centrality,
                      color = group),
                  show.legend = F) +
  scale_size(range = c(4, 8)) +
  geom_node_text(aes(label = name),
                 repel = T,
                 size = 5,
                 family = "nanumgothic") +
  theme_graph()