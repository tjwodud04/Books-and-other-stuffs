# 토픽별 주요 문서 살펴보고 토픽 이름 짓기기

comment_topic <- news_comment_topic %>%
  mutate(reply = str_squish(replace_html(reply))) %>%
  arrange(-gamma)

comment_topic %>%
  select(gamma, reply)
# # A tibble: 5,328 x 2
# gamma reply                                                           
# <dbl> <chr>                                                           
#   1 0.264 "도서관서 여자화장실서 나오는 남자사서보고 카메라있는지없는지 확인했다가 없는줄알고잊고살다 시비거는사람 계속만나다 ~
#  2 0.260 "봉준호 송강호 블랙리스트 올리고 CJ 이미경 대표는 박근혜가 보기싫다는 말한마디에 경영권 포기하고 미국으로 도피~
#   3 0.239 "보수정권때 블랙리스트에 오른 봉준호 송강호가 보기싫다는 박근혜의 말한마디에 경영권 마져 포기하고 미국으로 도피했~
#  4 0.238 "도서관서 여자화장실서 나오는 남자사서보고 카메라있는지없는지 확인했다가 없는줄알고잊고살다 시비거는사람 계속만나다 ~
#   5 0.235 "당초 \"1917\"과 \"기생충\"의 접전을[초기엔 1917이 훨씬 우세]예상했지만, 1917은 기술관련부분만~
#  6 0.234 "박그네 밑에서 블랙리스트 있었는데 ㅋㅋㅋㅋㅋㅋㅋ 이미경이는 박근혜가 부회장 그만두라 해서 미국으로 쫓겨났지? ㅋ~
#   7 0.226 "위대한ㅡ 박정희 삼성이 대한민국을 세계에 우뚝 세워 놨기에 가능한 일..... 개대중과 좌빨 기생충은 한국은 농사~
#  8 0.225 "기생충 영화보고 좌빨이 얼마나 기생충인지 못느낀 사람 제정신이야? 좌빨이 얼마나 사회악적인 기생충인지 고발하는 ~
#   9 0.225 "봉준호 감독과 송강호 배우는 이명박그네 정권 시절 문화계 블랙리스트 였다는 사실을 잊으면 안된다."~
#   10 0.224 "나중에 기생충 정부 영화 한편 나오겠네. 남자 주연 문xx ,여자주연 김정x 남자 조연 조x, 여자 조연 정경x~
# # ... with 5,318 more rows

# -------------------------------------------------------------------------
# 토픽 1 내용 살펴보기
comment_topic %>%
  filter(topic == 1 & str_detect(reply, "작품")) %>%
  head(50) %>%
  pull(reply)

comment_topic %>%
  filter(topic == 1 & str_detect(reply, "진심")) %>%
  head(50) %>%
  pull(reply)

comment_topic %>%
  filter(topic == 1 & str_detect(reply, "정치")) %>%
  head(50) %>%
  pull(reply)

name_topic <- tibble(topic = 1:8,
                     name = c("1. 작품상 수상 축하, 정치적 댓글 비판",
                              "2. 수상 축하, 시상식 감상",
                              "3. 조국 가족, 정치적 해석",
                              "4. 새 역사 쓴 세계적인 영화",
                              "5. 자랑스럽고 감사한 마음",
                              "6. 놀라운 4관왕 수상",
                              "7. 문화계 블랙리스트, 보수 정당 비판",
                              "8. 한국의 세계적 위상"))
# -------------------------------------------------------------------------

# 토픽 이름과 주요 단어 시각화하기
top_term_topic_name <- top_term_topic %>%
  left_join(name_topic, name_topic, by = "topic")

top_term_topic_name
# # A tibble: 83 x 4
# # Groups:   topic [8]
# topic term        beta name                                 
# <int> <chr>      <dbl> <chr>                                
#   1     1 작품     0.0299  1. 작품상 수상 축하, 정치적 댓글 비판
# 2     1 진심     0.0240  1. 작품상 수상 축하, 정치적 댓글 비판
# 3     1 정치     0.0192  1. 작품상 수상 축하, 정치적 댓글 비판
# 4     1 자랑     0.0181  1. 작품상 수상 축하, 정치적 댓글 비판
# 5     1 수상소감 0.0166  1. 작품상 수상 축하, 정치적 댓글 비판
# 6     1 댓글     0.0151  1. 작품상 수상 축하, 정치적 댓글 비판
# 7     1 외국     0.0122  1. 작품상 수상 축하, 정치적 댓글 비판
# 8     1 경사     0.0107  1. 작품상 수상 축하, 정치적 댓글 비판
# 9     1 훌륭     0.00998 1. 작품상 수상 축하, 정치적 댓글 비판
# 10     1 좌파     0.00814 1. 작품상 수상 축하, 정치적 댓글 비판
# # ... with 73 more rows

ggplot(top_term_topic_name,
       aes(x = reorder_within(term, beta, name),
           y = beta,
           fill = factor(topic))) +
  geom_col(show.legend = F) +
  facet_wrap(~ name, scales = "free", ncol = 2) +
  coord_flip() +
  scale_x_reordered() +
  
  labs(title = "영화 기생충 아카데미상 수상 기사 댓글 토픽",
       subtitle = "토픽별 주요 단어 Top 10",
       x = NULL, y = NULL) +
  
  theme_minimal() +
  theme(text = element_text(family = "nanumgothic"),
        title = element_text(size = 12),
        axis.text.x = element_blank(),
        axis.ticks.x = element_blank())
