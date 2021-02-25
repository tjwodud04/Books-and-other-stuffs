# TF-IDF 구하기

install.packages("readr")
library(readr)

raw_speeches <- read_csv("speeches_presidents.csv")
raw_speeches
# # A tibble: 4 x 2
# president value                                                        
# <chr>     <chr>                                                        
#   1 문재인    "정권교체 하겠습니다!   정치교체 하겠습니다!   시대교체 하겠습니다!   ‘불비불명(不飛不鳴)’이라는 고~
# 2 박근혜    "존경하는 국민 여러분! 저는 오늘, 국민 한 분 한 분의 꿈이 이루어지는 행복한 대한민국을 만들기 위해, ~
#   3 이명박    "존경하는 국민 여러분, 사랑하는 한나라당 당원 동지 여러분! 저는 오늘 무거운 책임감을 갖고 이 자리에 섰~
# 4 노무현    "어느때인가 부터 제가 대통령이 되겠다고 말을 하기 시작했습니다. 많은 분들이 제게 \"무엇을 했느냐\"를 ~

speeches <- raw_speeches %>%
  mutate(value = str_replace_all(value, "[^가-힣]", " "),
         value = str_squish(value))

speeches <- speeches %>%
  unnest_tokens(input = value,
                output = word,
                token = extractNoun)

frequecy <- speeches %>%
  count(president, word) %>%
  filter(str_count(word) > 1)

frequecy
# # A tibble: 1,513 x 3
# president word      n
# <chr>     <chr> <int>
#   1 노무현    가슴      2
# 2 노무현    가훈      2
# 3 노무현    갈등      1
# 4 노무현    감옥      1
# 5 노무현    강자      1
# 6 노무현    개편      4
# 7 노무현    개혁      4
# 8 노무현    건국      1
# 9 노무현    경선      1
# 10 노무현    경쟁      1
# # ... with 1,503 more rows
----------------------------------

frequecy <- frequecy %>%
bind_tf_idf(term = word,
            document = president,
            n = n) %>%
arrange(-tf_idf)

frequecy
# # A tibble: 1,513 x 6
# president word         n      tf   idf tf_idf
# <chr>     <chr>    <int>   <dbl> <dbl>  <dbl>
#   1 노무현    공식         6 0.0163  1.39  0.0227
# 2 노무현    비젼         6 0.0163  1.39  0.0227
# 3 노무현    정계         6 0.0163  1.39  0.0227
# 4 이명박    리더십       6 0.0158  1.39  0.0219
# 5 노무현    권력         9 0.0245  0.693 0.0170
# 6 노무현    개편         4 0.0109  1.39  0.0151
# 7 이명박    당원         4 0.0105  1.39  0.0146
# 8 이명박    동지         4 0.0105  1.39  0.0146
# 9 이명박    일류국가     4 0.0105  1.39  0.0146
# 10 박근혜    박근혜       8 0.00962 1.39  0.0133
# # ... with 1,503 more rows

frequecy %>% filter(president == "문재인")
# # A tibble: 688 x 6
# president word         n      tf   idf  tf_idf
# <chr>     <chr>    <int>   <dbl> <dbl>   <dbl>
#   1 문재인    복지국가     8 0.00608 1.39  0.00843
# 2 문재인    여성         6 0.00456 1.39  0.00633
# 3 문재인    공평         5 0.00380 1.39  0.00527
# 4 문재인    담쟁이       5 0.00380 1.39  0.00527
# 5 문재인    대통령의     5 0.00380 1.39  0.00527
# 6 문재인    보통         5 0.00380 1.39  0.00527
# 7 문재인    상생         5 0.00380 1.39  0.00527
# 8 문재인    우리나라    10 0.00760 0.693 0.00527
# 9 문재인    지방         5 0.00380 1.39  0.00527
# 10 문재인    확대        10 0.00760 0.693 0.00527
# # ... with 678 more rows

frequecy %>% filter(president == "박근혜")
# # A tibble: 407 x 6
# president word         n      tf   idf  tf_idf
# <chr>     <chr>    <int>   <dbl> <dbl>   <dbl>
#   1 박근혜    박근혜       8 0.00962 1.39  0.0133 
# 2 박근혜    정보         5 0.00601 1.39  0.00833
# 3 박근혜    투명         5 0.00601 1.39  0.00833
# 4 박근혜    행복        23 0.0276  0.288 0.00795
# 5 박근혜    교육         9 0.0108  0.693 0.00750
# 6 박근혜    국정운영     4 0.00481 1.39  0.00666
# 7 박근혜    정부        17 0.0204  0.288 0.00588
# 8 박근혜    개개인       3 0.00361 1.39  0.00500
# 9 박근혜    개인         3 0.00361 1.39  0.00500
# 10 박근혜    공개         3 0.00361 1.39  0.00500
# # ... with 397 more rows

frequecy %>% filter(president == "이명박")
# # A tibble: 202 x 6
# president word         n      tf   idf  tf_idf
# <chr>     <chr>    <int>   <dbl> <dbl>   <dbl>
#   1 이명박    리더십       6 0.0158  1.39  0.0219 
# 2 이명박    당원         4 0.0105  1.39  0.0146 
# 3 이명박    동지         4 0.0105  1.39  0.0146 
# 4 이명박    일류국가     4 0.0105  1.39  0.0146 
# 5 이명박    한나라       7 0.0184  0.693 0.0128 
# 6 이명박    나라        15 0.0395  0.288 0.0114 
# 7 이명박    도약         3 0.00789 1.39  0.0109 
# 8 이명박    일하         3 0.00789 1.39  0.0109 
# 9 이명박    사랑         5 0.0132  0.693 0.00912
# 10 이명박    인생         5 0.0132  0.693 0.00912
# # ... with 192 more rows

frequecy %>% filter(president == "노무현")
# # A tibble: 216 x 6
# president word         n      tf   idf  tf_idf
# <chr>     <chr>    <int>   <dbl> <dbl>   <dbl>
#   1 노무현    공식         6 0.0163  1.39  0.0227 
# 2 노무현    비젼         6 0.0163  1.39  0.0227 
# 3 노무현    정계         6 0.0163  1.39  0.0227 
# 4 노무현    권력         9 0.0245  0.693 0.0170 
# 5 노무현    개편         4 0.0109  1.39  0.0151 
# 6 노무현    국회의원     3 0.00817 1.39  0.0113 
# 7 노무현    남북대화     3 0.00817 1.39  0.0113 
# 8 노무현    총리         3 0.00817 1.39  0.0113 
# 9 노무현    가훈         2 0.00545 1.39  0.00755
# 10 노무현    개혁         4 0.0109  0.693 0.00755
# # ... with 206 more rows
---------------------------------------------------
# 막대 그래프 만들기

top10 <- frequecy %>%
  group_by(president) %>%
  slice_max(tf_idf, n = 10, with_ties = F)

top10$president <- factor(top10$president,
                          levels = c("문재인", "박근혜", "이명박", "노무현"))

ggplot(top10, aes(x = reorder_within(word, tf_idf, president),
                  y = tf_idf,
                  fill = president)) +  
  geom_col(show.legend = F) +
  coord_flip() +
  facet_wrap(~ president, scales = "free", ncol = 2) +
  scale_x_reordered() +
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))