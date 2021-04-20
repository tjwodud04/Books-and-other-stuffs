# 08-4 --------------------------------------------------------------------

# 트윗 감정 점수 구하기
sentiment_tweet <- word_tweet %>%
  group_by(candidate, status_id) %>%
  summarise(score = sum(polarity)) %>%
  ungroup()

# 트윗 원문에 감정 점수 결합
tweet <- tweet %>%
  left_join(sentiment_tweet, by = c("candidate", "status_id"))

# 감정 점수 히스토그램
hist(tweet$score)


# -------------------------------------------------------------------------
ggplot(tweet, aes(x = score, fill = candidate)) +
  geom_density(adjust = 2, alpha = 0.6)


# -------------------------------------------------------------------------
ggplot(tweet, aes(x = score, fill = candidate)) +
  geom_density(adjust = 2, alpha = 0.6) +
  geom_vline(xintercept = 0,                   # 0점 위 세로선 표시
             linetype = "dashed",              # 점선 표시
             size = 0.5,
             alpha = 0.5) +
  
  scale_x_continuous(breaks = c(-5:5),         # x축 범위
                     limits = c(-5, 5)) +      # x축 간격
  scale_fill_manual(values = col_candidate) +
  
  labs(title = "차기 대선주자 감정 점수 분포",
       subtitle = "2020.8.13 ~ 2020.8.21",
       y = NULL, fill = NULL) +
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12),
        legend.position = "bottom",
        panel.grid = element_blank())          # 격자 삭제


# -------------------------------------------------------------------------
ggplot(tweet, aes(x = score, fill = candidate)) +
  geom_density() +
  facet_wrap(~ date)


# -------------------------------------------------------------------------
ggplot(tweet, aes(x = score, fill = candidate)) +
  geom_density(adjust = 2,
               alpha = 0.6) +
  
  geom_vline(xintercept = 0,
             linetype = "dashed",
             size = 0.5,
             alpha = 0.5) +
  
  facet_wrap(~ str_remove(date, "2020-"),                  # x축 년도 삭제
             scales = "free_y",
             ncol = 3,
             strip.position = "bottom") +
  
  scale_x_continuous(breaks = c(-5:5),
                     limits = c(-5, 5)) +
  scale_fill_manual(values = col_candidate) +
  
  labs(title = "차기 대선주자 일자별 감정 점수 분포",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, fill = NULL) +
  
  theme_bw(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12),
        legend.position = "bottom",
        panel.grid = element_blank(),
        axis.ticks = element_blank(),                      # 축 눈금 삭제
        axis.text = element_blank(),                       # 축 삭제
        strip.background = element_rect(colour = "black",  # 패널명 배경
                                        fill = "white"))  


# -------------------------------------------------------------------------
# 감정 분류 변수 생성
tweet <- tweet %>%
  mutate(sentiment = ifelse(score >= 1, "긍정",
                            ifelse(score <= -1, "부정", "중립")))

# 후보, 감정별 빈도 및 비율
frequency_sentiment <- tweet %>%
  group_by(candidate) %>%
  count(sentiment) %>%
  mutate(ratio = n/sum(n))

frequency_sentiment


# -------------------------------------------------------------------------
ggplot(frequency_sentiment, aes(x = sentiment, y = n, fill = sentiment)) +
  geom_col() +
  facet_wrap(~ candidate)


# -------------------------------------------------------------------------
# 순서 설정
frequency_sentiment$sentiment <- factor(frequency_sentiment$sentiment,
                                        levels = order_sentiment)


# -------------------------------------------------------------------------
library(scales)
ggplot(frequency_sentiment, aes(x = sentiment, y = n, fill = sentiment)) +
  geom_col(show.legend = F) +                   
  facet_wrap(~ candidate) +
  geom_text(aes(label = comma(n)), vjust = -0.5) +
  
  ylim(0, 3500) +
  scale_fill_manual(values = col_sentiment) +  # 막대 색깔
  
  labs(title = "차기 대선주자 트윗 감정 빈도",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL) +
  
  theme_bw(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12), 
        axis.text.y = element_blank(),
        axis.ticks.y = element_blank(),
        panel.grid = element_blank())


# -------------------------------------------------------------------------
ggplot(frequency_sentiment, aes(x = candidate, y = ratio, fill = sentiment)) +
  geom_col()


# -------------------------------------------------------------------------
# 막대 누적 순서 지정
frequency_sentiment$sentiment <- factor(frequency_sentiment$sentiment,
                                        levels = rev(order_sentiment))

ggplot(frequency_sentiment, aes(x = candidate, y = ratio, fill = sentiment)) +
  geom_col(show.legend = F, width = 0.7) +
  
  geom_text(aes(label = paste(sentiment, percent(ratio, accuracy = 0.1))),
            position = position_stack(vjust = 0.5)) +     # 수직 위치
  coord_flip() +
  scale_x_discrete(limits = c("이재명", "이낙연")) +
  
  labs(title = "차기 대선주자 트윗 감정 비율",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, fill = NULL) +
  
  theme_void(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12),
        legend.position = "bottom",
        axis.text.y = element_text(size = 12),            # y축 글자 크기
        plot.margin = margin(1, 1, 1, 1, unit = "line"))  # 여백 상우하좌, 단위