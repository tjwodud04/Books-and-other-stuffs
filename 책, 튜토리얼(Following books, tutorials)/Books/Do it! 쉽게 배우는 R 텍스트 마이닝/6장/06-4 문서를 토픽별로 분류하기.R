# 문서별 토픽 확률, gamma 추출하기

doc_topic <- tidy(lda_model, matrix = "gamma")
doc_topic
# # A tibble: 25,624 x 3
# document topic  gamma
# <chr>    <int>  <dbl>
#   1 35           1 0.151 
# 2 206          1 0.15  
# 3 566          1 0.110 
# 4 578          1 0.114 
# 5 598          1 0.110 
# 6 1173         1 0.110 
# 7 1599         1 0.114 
# 8 1762         1 0.0962
# 9 2240         1 0.125 
# 10 2307         1 0.135 
# # ... with 25,614 more rows

doc_topic %>%
  count(topic)
# # A tibble: 8 x 2
# topic     n
# * <int> <int>
#   1     1  3203
# 2     2  3203
# 3     3  3203
# 4     4  3203
# 5     5  3203
# 6     6  3203
# 7     7  3203
# 8     8  3203

doc_topic %>%
  filter(document == 1) %>%
  summarise(sum_gamma = sum(gamma))
# # A tibble: 1 x 1
# sum_gamma
# <dbl>
#   1         1
# -------------------------------------------------------------------------

# 문서를 확률이 가장 높은 토픽으로 분류하기

doc_class <- doc_topic %>%
  group_by(document) %>%
  slice_max(gamma, n = 1)

doc_class
# # A tibble: 5,328 x 3
# # Groups:   document [3,203]
# document topic gamma
# <chr>    <int> <dbl>
#   1 1            5 0.159
# 2 10           8 0.168
# 3 100          5 0.153
# 4 1000         7 0.15 
# 5 1001         1 0.137
# 6 1001         3 0.137
# 7 1001         7 0.137
# 8 1002         3 0.137
# 9 1002         7 0.137
# 10 1002         8 0.137
# # ... with 5,318 more rows

doc_class$document <- as.integer(doc_class$document)

news_comment_topic <- raw_news_comment %>%
  left_join(doc_class, by = c("id" = "document"))

news_comment_topic %>%
  select(id, topic)
# # A tibble: 6,275 x 2
# id topic
# <int> <int>
#   1     1     5
# 2     2     1
# 3     2     5
# 4     2     6
# 5     3     2
# 6     3     8
# 7     4     4
# 8     5     5
# 9     5     6
# 10     6     3
# # ... with 6,265 more rows

news_comment_topic %>%
  count(topic)
# # A tibble: 9 x 2
# topic     n
# * <int> <int>
#   1     1   660
# 2     2   704
# 3     3   663
# 4     4   609
# 5     5   708
# 6     6   690
# 7     7   649
# 8     8   645
# 9    NA   947

news_comment_topic <- news_comment_topic %>%
  na.omit()

doc_topic %>%
  group_by(document) %>%
  slice_max(gamma, n = 1) %>%
  count(document) %>%
  filter(n >= 2)
# # A tibble: 1,301 x 2
# # Groups:   document [1,301]
# document     n
# <chr>    <int>
#   1 1001         3
# 2 1002         3
# 3 1009         3
# 4 1010         2
# 5 1023         2
# 6 1027         2
# 7 103          2
# 8 1036         3
# 9 1038         2
# 10 104          2
# # ... with 1,291 more rows

set.seed(1234)
doc_class_unique <- doc_topic %>%
  group_by(document) %>%
  slice_max(gamma, n = 1) %>%
  slice_sample(n = 1)

doc_class_unique
# # A tibble: 3,203 x 3
# # Groups:   document [3,203]
# document topic gamma
# <chr>    <int> <dbl>
#   1 1            5 0.159
# 2 10           8 0.168
# 3 100          5 0.153
# 4 1000         7 0.15 
# 5 1001         1 0.137
# 6 1002         8 0.137
# 7 1003         8 0.142
# 8 1004         2 0.156
# 9 1005         2 0.171
# 10 1006         7 0.171
# # ... with 3,193 more rows

doc_class_unique %>%
  count(document, sort = T)
# # A tibble: 3,203 x 2
# # Groups:   document [3,203]
# document     n
# <chr>    <int>
#   1 1            1
# 2 10           1
# 3 100          1
# 4 1000         1
# 5 1001         1
# 6 1002         1
# 7 1003         1
# 8 1004         1
# 9 1005         1
# 10 1006         1
# # ... with 3,193 more rows
# -------------------------------------------------------------------------

# 토픽별 문서 수와 단어 시각화하기

top_terms <- term_topic %>%
  group_by(topic) %>%
  slice_max(beta, n = 6, with_ties = F) %>%
  summarise(term = paste(term, collapse = ", "))

top_terms
# # A tibble: 8 x 2
# topic term                                                
# <int> <chr>                                               
#   1     1 작품, 진심, 정치, 자랑, 수상소감, 댓글              
# 2     2 대박, 시상식, 오늘, 국민, 소름, 정치                
# 3     3 조국, 문재인, 가족, 문화, 대통령, 자랑              
# 4     4 역사, 우리나라, 세계, 오스카, 수상, 빨갱이          
# 5     5 자랑, 우리, 최고, 감사, 생각, 소식                  
# 6     6 작품상, 감독상, 한국영화, 수상, 각본상, 나라        
# 7     7 블랙리스트, 박근혜, 사람, 송강호, 이미경, 자유한국당
# 8     8 한국, 미국, 한국인, 세계, 좌파, 배우    

count_topic <- news_comment_topic %>%
  count(topic)

count_topic
# # A tibble: 8 x 2
# topic     n
# * <int> <int>
#   1     1   660
# 2     2   704
# 3     3   663
# 4     4   609
# 5     5   708
# 6     6   690
# 7     7   649
# 8     8   645

count_topic_word <- count_topic %>%
  left_join(top_terms, by = "topic") %>%
  mutate(topic_name = paste("Topic", topic))

count_topic_word
# # A tibble: 8 x 4
# topic     n term                                             topic_name
# <int> <int> <chr>                                            <chr>     
#   1     1   660 작품, 진심, 정치, 자랑, 수상소감, 댓글           Topic 1   
# 2     2   704 대박, 시상식, 오늘, 국민, 소름, 정치             Topic 2   
# 3     3   663 조국, 문재인, 가족, 문화, 대통령, 자랑           Topic 3   
# 4     4   609 역사, 우리나라, 세계, 오스카, 수상, 빨갱이       Topic 4   
# 5     5   708 자랑, 우리, 최고, 감사, 생각, 소식               Topic 5   
# 6     6   690 작품상, 감독상, 한국영화, 수상, 각본상, 나라     Topic 6   
# 7     7   649 블랙리스트, 박근혜, 사람, 송강호, 이미경, 자유한국당~ Topic 7   
# 8     8   645 한국, 미국, 한국인, 세계, 좌파, 배우             Topic 8   # A tibble: 8 x 4
# topic     n term                                             topic_name
# <int> <int> <chr>                                            <chr>     
#   1     1   660 작품, 진심, 정치, 자랑, 수상소감, 댓글           Topic 1   
# 2     2   704 대박, 시상식, 오늘, 국민, 소름, 정치             Topic 2   
# 3     3   663 조국, 문재인, 가족, 문화, 대통령, 자랑           Topic 3   
# 4     4   609 역사, 우리나라, 세계, 오스카, 수상, 빨갱이       Topic 4   
# 5     5   708 자랑, 우리, 최고, 감사, 생각, 소식               Topic 5   
# 6     6   690 작품상, 감독상, 한국영화, 수상, 각본상, 나라     Topic 6   
# 7     7   649 블랙리스트, 박근혜, 사람, 송강호, 이미경, 자유한국당~ Topic 7   
# 8     8   645 한국, 미국, 한국인, 세계, 좌파, 배우             Topic 8   

ggplot(count_topic_word,
       aes(x = reorder(topic_name, n),
           y = n,
           fill = topic_name)) +
  geom_col(show.legend = F) +
  coord_flip() +
  
  geom_text(aes(label = n) ,                # 문서 빈도 표시
            hjust = -0.2) +                 # 막대 밖에 표시
  
  geom_text(aes(label = term),              # 주요 단어 표시
            hjust = 1.03,                   # 막대 안에 표시
            col = "white",                  # 색깔
            fontface = "bold",              # 두껍게
            family = "nanumgothic") +       # 폰트
  
  scale_y_continuous(expand = c(0, 0),      # y축-막대 간격 줄이기
                     limits = c(0, 820)) +  # y축 범위
  labs(x = NULL)