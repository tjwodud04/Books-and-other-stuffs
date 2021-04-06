# 토픽별 단어 확률, beta 추출하기

term_topic <- tidy(lda_model, matrix = "beta")
term_topic
# # A tibble: 47,960 x 3
# topic term       beta
# <int> <chr>     <dbl>
#   1     1 한국  0.000405 
# 2     2 한국  0.0000364
# 3     3 한국  0.0000353
# 4     4 한국  0.00295  
# 5     5 한국  0.0000353
# 6     6 한국  0.0000356
# 7     7 한국  0.00661  
# 8     8 한국  0.0593   
# 9     1 자랑  0.0181   
# 10     2 자랑  0.00440  
# # ... with 47,950 more rows

term_topic %>%
  count(topic)
# # A tibble: 8 x 2
# topic     n
# * <int> <int>
#   1     1  5995
# 2     2  5995
# 3     3  5995
# 4     4  5995
# 5     5  5995
# 6     6  5995
# 7     7  5995
# 8     8  5995

term_topic %>%
  filter(topic == 1) %>%
  summarise(sum_beta = sum(beta))
# # A tibble: 1 x 1
# sum_beta
# <dbl>
#   1        1

term_topic %>%
  filter(term == "작품상")
# # A tibble: 8 x 3
# topic term        beta
# <int> <chr>      <dbl>
#   1     1 작품상 0.0000368
# 2     2 작품상 0.000763 
# 3     3 작품상 0.0000353
# 4     4 작품상 0.0000364
# 5     5 작품상 0.0000353
# 6     6 작품상 0.0695   
# 7     7 작품상 0.000727 
# 8     8 작품상 0.000388
# -------------------------------------------------------------------------

# 토픽별 주요 단어 살펴보기

term_topic %>%
  filter(topic == 6) %>%
  arrange(-beta)
# # A tibble: 5,995 x 3
# topic term        beta
# <int> <chr>      <dbl>
#   1     6 작품상   0.0695 
# 2     6 감독상   0.0318 
# 3     6 한국영화 0.0228 
# 4     6 수상     0.0214 
# 5     6 각본상   0.0154 
# 6     6 나라     0.0143 
# 7     6 호감     0.0136 
# 8     6 감격     0.0129 
# 9     6 순간     0.0125 
# 10     6 눈물     0.00788
# # ... with 5,985 more rows

terms(lda_model, 20) %>%
  data.frame()
# Topic.1 Topic.2 Topic.3    Topic.4    Topic.5  Topic.6    Topic.7
# 1      작품    대박    조국       역사       자랑   작품상 블랙리스트
# 2      진심  시상식  문재인   우리나라       우리   감독상     박근혜
# 3      정치    오늘    가족       세계       최고 한국영화       사람
# 4      자랑    국민    문화     오스카       감사     수상     송강호
# 5  수상소감    소름  대통령       수상       생각   각본상     이미경
# 6      댓글    정치    자랑     빨갱이       소식     나라 자유한국당
# 7      외국    배우    때문     영화계   국위선양     호감       정권
# 8      경사    계획    인정 아카데미상       감동     감격       소감
# 9      훌륭    축하    정부       인간       하나     순간       보수
# 10     좌파    위상    강국       얘기 방탄소년단     눈물       인정
# 11     왜구    최고    호감       로컬     영화상   전세계     마지막
# 12     배우    한번    와우       내용   한국영화     진정       기생
# 13     예술    쾌거    사건       좌파       정도   노벨상       하나
# 14   전세계    생각    국격       정신       와우     소식     네이버
# 15   아시아    중국    고생       의미       조선     기사       한국
# 16     호감    다음    덕분       생각       존경     문화     이야기
# 17     토착    기분    기대       상상       후보     국제     부회장
# 18     발전    왕이    정말       국민       우한     각본     쓰레기
# 19   사람들    세상    해도       나라       시대     다들       좌파
# 20     수준    자랑    눈물       정부       행복     발표       영광
# Topic.8
# 1          한국
# 2          미국
# 3        한국인
# 4          세계
# 5          좌파
# 6          배우
# 7          감동
# 8          누구
# 9          사회
# 10         자유
# 11         현실
# 12         영광
# 13         위대
# 14       영화제
# 15         이해
# 16         자신
# 17 최우수작품상
# 18         예상
# 19   황금종려상
# 20         이유

# -------------------------------------------------------------------------
# 토픽별 주요 단어 시각화하기

top_term_topic <- term_topic %>%
  group_by(topic) %>%
  slice_max(beta, n = 10)

install.packages("scales")
library(scales)
library(ggplot2)

ggplot(top_term_topic,
       aes(x = reorder_within(term, beta, topic),
           y = beta,
           fill = factor(topic))) +
  geom_col(show.legend = F) +
  facet_wrap(~ topic, scales = "free", ncol = 4) +
  coord_flip() +
  scale_x_reordered() +
  scale_y_continuous(n.breaks = 4,
                     labels = number_format(accuracy = .01)) + 
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))