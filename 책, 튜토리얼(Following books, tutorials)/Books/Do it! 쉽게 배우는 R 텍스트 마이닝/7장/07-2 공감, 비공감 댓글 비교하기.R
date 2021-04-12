# 로그 오즈비 구하기

word_sympathy <- word_noun %>%
  rename(like = sympathyCount,
         dislike = antipathyCount) %>%
  
  mutate(diff = like - dislike,
         sympathy = ifelse(diff >=  1, "like",
                           ifelse(diff <= -1, "dislike", "neutral")))

word_sympathy %>%
  distinct(id, .keep_all = T) %>%
  count(sympathy, sort = T)
# # A tibble: 3 x 2
# sympathy     n
# <chr>    <int>
#   1 neutral   2299
# 2 like      2055
# 3 dislike    757

frequency_sympathy <- word_sympathy %>%
  count(sympathy, word) %>% 
  filter(str_count(word) > 1 &
           sympathy != "centrism")

library(tidyr)

frequency_wide <- frequency_sympathy %>%
  pivot_wider(names_from = sympathy,
              values_from = n,
              values_fill = list(n = 0))

frequency_wide <- frequency_wide %>%
  mutate(log_odds_ratio = log(((like    + 1) / (sum(like    + 1))) /
                                ((dislike + 1) / (sum(dislike + 1)))))

frequency_wide %>%
  arrange(-log_odds_ratio)
# # A tibble: 11,115 x 5
# word     dislike  like neutral log_odds_ratio
# <chr>      <int> <int>   <int>          <dbl>
#   1 조합           0    25      12           2.79
# 2 승용차         0    11      11           2.01
# 3 타고           0    11       7           2.01
# 4 무능           0    10       5           1.93
# 5 마차           0     9      13           1.83
# 6 베트남         0     9       7           1.83
# 7 수수료         0     9       2           1.83
# 8 스타트업       0     9      18           1.83
# 9 전기           0     9       2           1.83
# 10 개혁           1    18      20           1.78
# # ... with 11,105 more rows
# -------------------------------------------------------------------------

# 주요 단어 비교하기

top10_odds <- frequency_wide %>%
  filter(like >= 20 | dislike >= 20) %>%
  group_by(sympathy = ifelse(log_odds_ratio > 0, "like", "dislike")) %>%
  slice_max(abs(log_odds_ratio), n = 10, with_ties = F)

top10_odds %>%
  arrange(log_odds_ratio)
# # A tibble: 20 x 6
# # Groups:   sympathy [2]
# word     dislike  like neutral log_odds_ratio sympathy
# <chr>      <int> <int>   <int>          <dbl> <chr>   
#   1 렌트카        26    21      35        -0.676  dislike 
# 2 한국          31    26      49        -0.641  dislike 
# 3 댓글          20    17      18        -0.625  dislike 
# 4 개인          19    23      29        -0.289  dislike 
# 5 이재웅        25    33      37        -0.203  dislike 
# 6 반대          19    26      39        -0.171  dislike 
# 7 렌터카        15    21      19        -0.153  dislike 
# 8 불법         111   156     130        -0.133  dislike 
# 9 공유          29    42      30        -0.111  dislike 
# 10 자기          17    26      28        -0.0655 dislike 
# 11 시대          15    89      63         1.26   like    
# 12 콜택시         5    34      11         1.29   like    
# 13 승차거부      14    94      74         1.37   like    
# 14 이나라         2    20      22         1.47   like    
# 15 거부           2    21      10         1.52   like    
# 16 노조           2    21      17         1.52   like    
# 17 선택           4    39      22         1.61   like    
# 18 동남아         2    25      18         1.69   like    
# 19 소비자         4    44      28         1.73   like    
# 20 조합           0    25      12         2.79   like    

col_sentiment <- c("#619CFF", "#F8766D")

top10_odds$sympathy <- factor(top10_odds$sympathy,
                              levels = c("like", "dislike"))

ggplot(top10_odds, aes(x = reorder(word, log_odds_ratio),
                       y = log_odds_ratio,
                       fill = sympathy)) +
  geom_col() +
  coord_flip() +
  scale_fill_manual(values = col_sentiment,    
                    labels = c("공감", "비공감")) +
  
  labs(title = "타다 금지법 기사 댓글 주요 단어",
       subtitle = "공감 vs 비공감 로그 오즈비 Top 10",
       x = NULL, fill = NULL) +
  
  theme_minimal() +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12))
# -------------------------------------------------------------------------

# 댓글 내용 살펴보기

tada %>%
  filter(str_detect(reply_raw, "조합")) %>%
  head(3) %>%
  pull(reply)
# [1] "우리나라가 안되는 이유 기득권 특히 전국 노동조합 금속노조 환경단체 택시조합 수많은 조합업체 택시는 기득권만 내세우지 말고 국민들이 왜 싫어하는지 알기나 하길"                                                                     
# [2] "수십만 재개발재건축 조합원이 피해보는 분양가상한제는 공익을 위해 사익은 희생될수 있다가 니네 논리잔아 개쓰렉 정권아"                                                                                                              
# [3] "그럼 국민들의 피해는 모르겠니 어째 택시조합에서 나오는 표가 무시 못할거 같아 이번 선거에서 진정한 국민의 힘이 무엇인지 보여주고 너네들에게 헬조선에서 허우적대고 있는 국민의 피눈물에 대한 책임을 꼭 물을줄 알아라 에라이 카악 퇫"

library(crayon)
font <- combine_styles(make_style("ivory"),
                       make_style("deeppink", bg = TRUE),
                       make_style("bold"))
font

font("폰트를 적용해 출력") %>% cat()

keyword <- "조합"

tada %>%
  filter(str_detect(reply_raw, keyword)) %>%
  head(3) %>%
  mutate(reply = paste0(str_replace_all(reply,
                                        keyword,
                                        font(keyword)))) %>% 
  pull(reply) %>%                                            
  cat(sep = "\n\n")                                          

find_word <- function(df, x, keyword, n = 6) {
  
  font <- combine_styles(make_style("ivory"),
                         make_style("deeppink", bg = TRUE),
                         make_style("bold"))
  
  df %>%
    filter(str_detect({{x}}, keyword)) %>%              
    head(n) %>%                                         
    mutate(x = paste0("[", row_number(), "] ", {{x}}),  
           x = paste0(str_replace_all(x,
                                      keyword,
                                      font(keyword)))) %>%
    pull(x) %>%                                         
    cat(sep = "\n\n")                                   
}

tada %>% find_word(x = reply_raw, keyword = "조합", n = 2)

tada %>% find_word(reply_raw, "조합", 2)

tada <- tada %>%
  left_join(word_sympathy %>%
              distinct(id, .keep_all = T) %>% 
              select(id, sympathy, diff),     
            by = "id")

reply_like <- tada %>%
  filter(sympathy == "like") %>%     
  arrange(-diff)                     

reply_dislike <- tada %>%
  filter(sympathy == "dislike") %>%
  arrange(diff)                    

reply_like %>% find_word(x = reply_raw, keyword = "조합", n = 10)

reply_like %>% find_word(x = reply_raw, keyword = "소비자", n = 10)

reply_like %>% find_word(x = reply_raw, keyword = "동남아", n = 10)

reply_dislike %>% find_word(x = reply_raw, keyword = "렌트카", n = 10)

reply_dislike %>%
  filter(!str_detect(reply, "한국당")) %>%
  find_word(x = reply, keyword = "한국", n = 10)

reply_dislike %>% find_word(x = reply, keyword = "댓글", n = 10)