# 08-5 --------------------------------------------------------------------

# 날짜, 후보, 감정별 빈도
sentiment_candidate <- tweet %>%
  count(date, candidate, sentiment)

sentiment_candidate


# -------------------------------------------------------------------------
## 트윗 감정 추이 선 그래프
ggplot(sentiment_candidate, aes(x = date, y = n, col = sentiment)) +
  geom_line() +
  geom_point() +
  facet_wrap(~ candidate, nrow = 2, scales = "free_x")


# -------------------------------------------------------------------------
# 중립 트윗 제외
tweet_polar <- sentiment_candidate %>%
  filter(sentiment != "중립")

ggplot(tweet_polar, aes(x = date, y = n, col = sentiment)) +
  geom_line() +
  geom_point() +
  facet_wrap(~ candidate, nrow = 2, scales = "free_x")


# -------------------------------------------------------------------------
# 색깔 목록 생성
col_polar <- c("#619CFF", "#F8766D")

ggplot(tweet_polar, aes(x = date, y = n, col = sentiment)) +
  geom_line(size = 1) +
  geom_point(size = 2) +
  facet_wrap(~ candidate, nrow = 2, scales = "free_x") +
  
  scale_x_date(date_labels = "%m/%d",
               date_breaks  = "1 day") +
  ylim(0, 250) +
  scale_color_manual(values = col_polar) +
  
  labs(title = "차기 대선주자 트윗 감정 추이",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, col = NULL) +
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12),
        panel.grid.minor.x = element_blank(),
        panel.spacing = unit(2, "lines"))  # 그래프 간격


# -------------------------------------------------------------------------
ggplot(tweet_polar, aes(x = date, y = n, fill = sentiment)) +
  geom_area(position = "dodge", alpha = 0.7) +
  facet_wrap(~ candidate, nrow = 2, scales = "free_x")


# -------------------------------------------------------------------------
ggplot(tweet_polar, aes(x = date, y = n, fill = sentiment)) +
  geom_area(position = "dodge", alpha = 0.7) +
  facet_wrap(~ candidate, nrow = 2, scales = "free_x") +
  
  scale_x_date(date_labels = "%m/%d", date_breaks  = "1 day") +
  ylim(0, 250) +
  scale_fill_manual(values = col_polar) +
  
  labs(title = "차기 대선주자 트윗 감정 추이",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, fill = NULL) +
  
  theme_gray(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12), 
        panel.grid = element_blank(),
        panel.spacing = unit(2, "lines"))  # 그래프 간격 띄우기