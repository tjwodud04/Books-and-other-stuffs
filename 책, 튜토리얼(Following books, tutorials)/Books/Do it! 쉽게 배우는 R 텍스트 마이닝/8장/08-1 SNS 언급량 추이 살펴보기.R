# 08-1 --------------------------------------------------------------------

# 데이터 불러오기
library(dplyr)
library(readr)
bind_tweet <- bind_rows(
  read_csv("tweet_nak.csv") %>% mutate(candidate = "이낙연"),
  read_csv("tweet_jae.csv") %>% mutate(candidate = "이재명"))

glimpse(bind_tweet)


# -------------------------------------------------------------------------
install.packages("lubridate")
library(lubridate)
library(textclean)
library(stringr)

set.seed(1234)
tweet <- bind_tweet %>%
  
  mutate(text = replace_tag(str_to_lower(text)),  # id 태그 제거
         text = str_squish(replace_html(text)),   # html 특수 문자 제거
         date = date(created_at)) %>%             # 날짜 변수 생성
  
  filter(!str_detect(text, "https://")) %>%       # 광고 트윗 제거
  
  group_by(candidate) %>%                         # 중복 글 제거
  distinct(text, .keep_all = T) %>%
  
  group_by(candidate, date, screen_name) %>%      # 사용자별 하루 최대 5개 추출
  slice_sample(n = 5) %>%
  ungroup()

glimpse(tweet)


# -------------------------------------------------------------------------
# 날짜, 후보별 빈도
frequency_date <- tweet %>%
  count(date, candidate)

frequency_date

# 선 그래프
library(ggplot2)
ggplot(frequency_date, aes(x = date, y = n, col = candidate)) +
  geom_line()


# -------------------------------------------------------------------------
# 후보 색상 목록 생성
col_candidate <- c("#619CFF", "#B79F00")

ggplot(frequency_date, aes(x = date, y = n, col = candidate)) +  
  geom_line(size = 1) +
  geom_point(size = 2) +
  
  scale_x_date(date_labels = "%m/%d",                         # x축 날짜 포맷
               date_breaks  = "1 day") +                      # x축 날짜 간격
  scale_y_continuous(limits = c(0, 1200),                     # y축 범위
                     breaks = seq(0, 1200, 300)) +            # y축 간격
  scale_color_manual(values = col_candidate) +                # 선 색깔
  
  labs(title = "차기 대선주자 트위터 언급량 추이",            # 그래프 제목
       subtitle = "2020.8.13 ~ 2020.8.21",                    # 보조 제목
       x = NULL, y = NULL, col = NULL) +                      # 축 이름 삭제
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),  # 제목 폰트
        plot.subtitle = element_text(size = 12),              # 부제목 폰트
        panel.grid.minor.x = element_blank())                 # x축 보조축 삭제


# -------------------------------------------------------------------------
library(scales)
show_col(hue_pal()(6))


# -------------------------------------------------------------------------
# 영역 그래프
ggplot(frequency_date, aes(x = date, y = n, fill = candidate)) +
  geom_area(position = "dodge", alpha = 0.6)


# -------------------------------------------------------------------------
ggplot(frequency_date, aes(x = date, y = n, fill = candidate)) +
  geom_area(position = "dodge", alpha = 0.6) +
  geom_line(size = 0.5, alpha = 0.5) +
  
  scale_x_date(date_labels = "%m/%d", date_breaks  = "1 day") +
  scale_y_continuous(limits = c(0, 1200),
                     breaks = seq(0, 1200, 300)) +
  scale_fill_manual(values = col_candidate) +
  
  labs(title = "차기 대선주자 트위터 언급량 추이",
       subtitle = "2020.8.13 ~ 2020.8.21",
       x = NULL, y = NULL, fill = NULL) +
  
  theme_minimal(12) +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12),            
        panel.grid.minor.x = element_blank(),
        panel.grid.minor.y = element_blank())  # y축 보조축 삭제