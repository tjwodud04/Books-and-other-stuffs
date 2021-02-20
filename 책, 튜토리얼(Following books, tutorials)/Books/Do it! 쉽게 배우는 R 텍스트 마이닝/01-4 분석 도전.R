# Q1 speecha_park.txt 전처리 / 띄어쓰기 기준 토큰화
raw_park <- readLines("speech_park.txt", encoding = "UTF-8")
head(raw_park)

park <- raw_park %>%
str_replace_all("[^가-힣]", " ") %>%
str_squish() %>%
as_tibble()

park <- raw_park %>%
str_replace_all("[^가-힣]", " ") %>%
str_squish() %>%
as_tibble()

# Q2 Top 20

word_space <- word_space %>%
count(word, sort = T) %>%
filter(str_count(word) > 1)

top20 <- word_space %>%
head(20)

# Q3 Graph

ggplot(top20, aes(x = reorder(word, n), y = n)) +  geom_col() + coord_flip() + geom_text(aes(label = n), hjust = -0.3) + labs(title = "박근혜 대통령 출마 연설문 단어 빈도", x = NULL, y = NULL) + theme(title = element_text(size = 12))