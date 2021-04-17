# 08-3 --------------------------------------------------------------------

# 감정 사전 불러오기
dic <- read_csv("knu_sentiment_lexicon.csv")

# 감정 점수 부여, 감정 극성 분류
word_tweet <- word_tweet_raw %>%
  left_join(dic, by = "word") %>%                              # 감정 점수 부여
  mutate(polarity = ifelse(is.na(polarity), 0, polarity),      # NA를 0으로 변환
         sentiment = ifelse(polarity ==  2, "긍정",            # 감정 범주 분류
                            ifelse(polarity == -2, "부정", "중립")))


# -------------------------------------------------------------------------
# 자주 언급한 단어 추출
top10_word <- word_tweet %>%
  
  # 불용어 제거
  filter(!(candidate == "이낙연" & str_detect(word, "이낙연")) &
           !(candidate == "이재명" & str_detect(word, "이재명"))) %>%
  
  filter(str_count(word) >= 2) %>%
  count(candidate, sentiment, word) %>%
  
  group_by(candidate, sentiment) %>%
  slice_max(n, n = 10, with_ties = F)

top10_word


# -------------------------------------------------------------------------
ggplot(top10_word, aes(x = reorder_within(word, n, candidate),
                       y = n,
                       fill = sentiment)) +
  geom_col() +
  coord_flip() +
  facet_wrap(candidate ~ sentiment,  # 후보, 감정 범주별 그래프 생성
             scales = "free") +
  scale_x_reordered()


# -------------------------------------------------------------------------
col_sentiment <- c("#619CFF", "#00BA38", "#F8766D")  # 감정 색깔 목록
order_sentiment <- c("긍정", "중립", "부정")         # 감정 범주 목록

# 그래프 순서 지정
top10_word$sentiment <- factor(top10_word$sentiment,
                               levels = order_sentiment)

ggplot(top10_word, aes(x = reorder_within(word, n, candidate),
                       y = n,
                       fill = sentiment)) +
  geom_col() +
  coord_flip() +
  facet_wrap(candidate ~ sentiment,
             scales = "free") +
  scale_x_reordered() +
  scale_fill_manual(values = col_sentiment) +
  
  labs(title = "차기 대선주자 감정 단어",
       subtitle = "감정 극성별 빈도 Top 10",
       x = NULL, y = NULL, fill = NULL) +
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12),
        legend.position = "bottom")  # 범례 위치