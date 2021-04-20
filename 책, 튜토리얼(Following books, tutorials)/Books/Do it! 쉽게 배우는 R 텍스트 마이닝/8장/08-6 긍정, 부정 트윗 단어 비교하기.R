# 08-6 --------------------------------------------------------------------

# 두 글자 이상 한글 단어 추출
word_sentiment_tweet <- word_tweet_raw %>%
  filter(str_detect(word, "[가-힣]") &
           str_count(word) >= 2) %>%
  
  # tweet 결합
  left_join(tweet %>% select(candidate, status_id, score, sentiment),
            by = c("candidate", "status_id"))

glimpse(word_sentiment_tweet)


# -------------------------------------------------------------------------
# 감정 범주 및 단어별 빈도 구하기
frequency_sentiment <- word_sentiment_tweet %>%  
  
  group_by(status_id) %>%                        # 트윗별 분리
  distinct(word, .keep_all = T) %>%              # 중복 단어 제거
  ungroup() %>%
  
  count(candidate, sentiment, word, sort = T)

frequency_sentiment


# -------------------------------------------------------------------------
# Wide form으로 변환
wide_pos <- frequency_sentiment %>%
  filter(sentiment == "긍정" & !str_detect(word, "이낙연|이재명")) %>%
  pivot_wider(names_from = candidate,
              values_from = n,
              values_fill = list(n = 0))

# 로그 오즈비 구하기
log_odds_pos <- wide_pos %>%
  mutate(log_odds_ratio = log(((이낙연 + 1) / (sum(이낙연 + 1))) /
                                ((이재명 + 1) / (sum(이재명 + 1)))))


# -------------------------------------------------------------------------
# 불용어 확인
log_odds_pos %>%
  group_by(candidate = ifelse(log_odds_ratio > 0, "이낙연", "이재명")) %>%
  slice_max(abs(log_odds_ratio), n = 15, with_ties = F) %>%
  select(word) %>%
  print(n = Inf)

# 불용어 목록 생성
stopword_pos <- c("것이고", "그건", "그는")


# -------------------------------------------------------------------------
# 로그 오즈비 상하위 10개 단어 추출
top10_pos <- log_odds_pos %>%
  filter(!word %in% stopword_pos) %>%
  group_by(candidate = ifelse(log_odds_ratio > 0, "이낙연", "이재명")) %>%
  slice_max(abs(log_odds_ratio), n = 10, with_ties = F)

# 막대 그래프 생성
ggplot(top10_pos, aes(x = reorder(word, log_odds_ratio),
                      y = log_odds_ratio,
                      fill = candidate)) +
  geom_col() +
  coord_flip()


# -------------------------------------------------------------------------
ggplot(top10_pos, aes(x = reorder(word, log_odds_ratio),
                      y = log_odds_ratio,
                      fill = candidate)) +
  geom_col() +
  coord_flip() +
  scale_fill_manual(values = col_candidate) +
  
  labs(title = "차기 대선주자 긍정 트윗 주요 단어",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, fill = NULL) +
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12))


# -------------------------------------------------------------------------
# 단어 순서 지정해 factor 타입으로 변환
top10_pos <- top10_pos %>%
  ungroup() %>%
  mutate(word = reorder(word, log_odds_ratio))

# 롤리팝 차트 생성
ggplot(top10_pos, aes(x = word,
                      y = log_odds_ratio,
                      col = candidate)) +
  geom_segment(aes(x = word,                  # x축 시작점
                   xend = word,               # x축 끝점
                   y = 0,                     # y축 시작점
                   yend = log_odds_ratio)) +  # y축 끝점
  geom_point() +
  coord_flip()


# -------------------------------------------------------------------------
ggplot(top10_pos, aes(x = word,
                      y = log_odds_ratio,
                      col = candidate)) +
  
  geom_segment(aes(x = word,
                   xend = word,
                   y = 0,
                   yend = log_odds_ratio),
               size = 1.1) +
  
  geom_point(size = 3.5) +
  coord_flip() +
  scale_color_manual(values = col_candidate) +
  
  labs(title = "차기 대선주자 긍정 트윗 주요 단어",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, col = NULL) +
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12)) 


# -------------------------------------------------------------------------
# 이낙연 의원 긍정 트윗 추출
pos_nak <- tweet %>%
  filter(sentiment == "긍정" & candidate == "이낙연") %>%
  arrange(-score)

pos_nak %>% find_word(x = text, keyword = "음성")

pos_nak %>% find_word(x = text, keyword = "의원님")


# -------------------------------------------------------------------------
# 이재명 경기도지사 긍정 트윗 추출
pos_jae <- tweet %>%
  filter(sentiment == "긍정" & candidate == "이재명") %>%
  arrange(-score)

pos_jae %>% find_word(x = text, keyword = "경기도")

pos_jae %>% find_word(x = text, keyword = "이익을")


# -------------------------------------------------------------------------
pos_jae %>%
  filter(str_detect(text, "이익을")) %>%
  select(score)

pos_jae %>%
  filter(!str_detect(text, "이익을")) %>%
  select(score)


# -------------------------------------------------------------------------
# Wide form으로 변환
wide_neg <- frequency_sentiment %>%
  filter(sentiment == "부정" & !str_detect(word, "이낙연|이재명")) %>%
  pivot_wider(names_from = candidate,
              values_from = n,
              values_fill = list(n = 0))

# 로그 오즈비 구하기
log_odds_neg <- wide_neg %>%
  mutate(log_odds_ratio = log(((이낙연 + 1) / (sum(이낙연 + 1))) /
                                ((이재명 + 1) / (sum(이재명 + 1)))))


# -------------------------------------------------------------------------
# 불용어 확인
log_odds_neg %>%
  group_by(candidate = ifelse(log_odds_ratio > 0, "이낙연", "이재명")) %>%
  slice_max(abs(log_odds_ratio), n = 15, with_ties = F) %>%
  select(word) %>%
  print(n = Inf)

tweet %>%
  filter(candidate == "이재명") %>%
  find_word(x = text, keyword = "쓰나미급")

# 불용어 목록 생성
stopword_neg <- c("지금껏", "겪어보지", "대충격", "시작될", "그건", "주고")


# -------------------------------------------------------------------------
# 로그 오즈비 상하위 10개 단어 추출
top10_neg <- log_odds_neg %>%
  filter(!word %in% stopword_neg) %>%
  group_by(candidate = ifelse(log_odds_ratio > 0, "이낙연", "이재명")) %>%
  slice_max(abs(log_odds_ratio), n = 10, with_ties = F)

# 막대 그래프 생성
ggplot(top10_neg, aes(x = reorder(word, log_odds_ratio),
                      y = log_odds_ratio,
                      fill = candidate)) +
  geom_col() +
  coord_flip() +
  scale_fill_manual(values = col_candidate) +
  
  labs(title = "차기 대선주자 부정 트윗 주요 단어",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, fill = NULL) +
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12))


# -------------------------------------------------------------------------
# 단어 순서 지정해 factor 타입으로 변환
top10_neg <- top10_neg %>%
  ungroup() %>%
  mutate(word = reorder(word, log_odds_ratio))

# 롤리팝 차트 생성
ggplot(top10_neg, aes(x = word,
                      y = log_odds_ratio,
                      col = candidate)) +
  
  geom_segment(aes(x = word,
                   xend = word,
                   y = 0,
                   yend = log_odds_ratio),
               size = 1.1) +
  
  geom_point(size = 3.5) +
  coord_flip() +
  scale_color_manual(values = col_candidate) +
  
  labs(title = "차기 대선주자 부정 트윗 주요 단어",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, col = NULL) +
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12))


# -------------------------------------------------------------------------
# 이낙연 의원 부정 트윗 추출
neg_nak <- tweet %>%
  filter(sentiment == "부정" & candidate == "이낙연") %>%
  arrange(-score)

# 이재명 경기도지사 부정 트윗 추출
neg_jae <- tweet %>%
  filter(sentiment == "부정" & candidate == "이재명") %>%
  arrange(-score)


# -------------------------------------------------------------------------
neg_nak %>% find_word(x = text, keyword = "음성")

neg_nak %>% find_word(x = text, keyword = "의원님")

neg_jae %>% find_word(x = text, keyword = "경기도")

neg_jae %>% find_word(x = text, keyword = "쓰나미급")