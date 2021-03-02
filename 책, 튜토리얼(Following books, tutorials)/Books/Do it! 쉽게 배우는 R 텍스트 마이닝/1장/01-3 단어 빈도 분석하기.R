# 단어 빈도 구하기
word_space <- word_space %>%
  count(word, sort = T)
word_space
# # A tibble: 1,440 x 2
# word             n
# <chr>        <int>
#   1 합니다          27
# 2 수              16
# 3 있습니다        13
# 4 저는            13
# 5 등              12
# 6 있는            12
# 7 함께            12
# 8 만들겠습니다    11
# 9 일자리          10
# 10 국민의           9
# # ... with 1,430 more rows
------------------------------------------------------
  # 한 글자로 된 단어 제거하기
  str_count("배")
str_count("사과")
# [1] 1
# [1] 2

word_space <- word_space %>%
  filter(str_count(word) > 1)
word_space
# # A tibble: 1,384 x 2
# word             n
# <chr>        <int>
#   1 합니다          27
# 2 있습니다        13
# 3 저는            13
# 4 있는            12
# 5 함께            12
# 6 만들겠습니다    11
# 7 일자리          10
# 8 국민의           9
# 9 우리             9
# 10 우리나라         9
# # ... with 1,374 more rows

# 한 번에 작업하기
word_space <- word_space %>%
  count(word, sort = T) %>%
  filter(str_count(word) > 1)
------------------------------------------------------
  
# 자주 사용된 단어 추출하기
top20 <- word_space %>%
  head(20)
top20
# # A tibble: 20 x 2
# word             n
# <chr>        <int>
#   1 합니다          27
# 2 있습니다        13
# 3 저는            13
# 4 있는            12
# 5 함께            12
# 6 만들겠습니다    11
# 7 일자리          10
# 8 국민의           9
# 9 우리             9
# 10 우리나라         9
# 11 새로운           8
# 12 위해             8
# 13 그리고           7
# 14 나라             7
# 15 나라가           7
# 16 지금             7
# 17 낡은             6
# 18 대통령이         6
# 19 되겠습니다       6
# 20 없는             6
-------------------------------------------
  
# 막대 그래프 만들기
install.packages("ggplot2")
library(ggplot2)

ggplot(top20, aes(x = reorder(word, n), y = n)) + geom_col() + coord_flip()

# 그래프 다듬기
ggplot(top20, aes(x = reorder(word, n), y = n)) +  geom_col() + coord_flip() + geom_text(aes(label = n), hjust = -0.3) + labs(title = "문재인 대통령 출마 연설문 단어 빈도", x = NULL, y = NULL) + theme(title = element_text(size = 12))
-------------------------------------------
  
# 워드 클라우드 만들기
  
install.packages("ggwordcloud")
library(ggwordcloud)

ggplot(word_space, aes(label = word, size = n)) + geom_text_wordcloud(seed = 1234) + scale_radius(limits = c(3, NA), range = c(3, 30))

# 그래프 다듬기
ggplot(word_space, aes(label = word, size = n, col = n)) + geom_text_wordcloud(seed = 1234) + scale_radius(limits = c(3, NA), range = c(3, 30)) + scale_color_gradient(low = "#66aaf2", high = "#004EA1") + theme_minimal()
-------------------------------------------
  
# 그래프 폰트 바꾸기
install.packages("showtext")
library(showtext)

font_add_google(name = "Nanum Gothic", family = "nanumgothic")
showtext_auto()

ggplot(word_space, aes(label = word, size = n, col = n)) + geom_text_wordcloud(seed = 1234, family = "nanumgothic") + scale_radius(limits = c(3, NA), range = c(3, 30)) + scale_color_gradient(low = "#66aaf2", high = "#004EA1") + theme_minimal()
--------------------
font_add_google(name = "Black Han Sans", family = "blackhansans")
showtext_auto()

ggplot(word_space, aes(label = word, size = n, col = n)) + geom_text_wordcloud(seed = 1234, family = "blackhansans") + scale_radius(limits = c(3, NA), range = c(3, 30)) + scale_color_gradient(low = "#66aaf2", high = "#004EA1") + theme_minimal()
--------------------
font_add_google(name = "Gamja Flower", family = "gamjaflower")
showtext_auto()

ggplot(top20, aes(x = reorder(word, n), y = n)) +
  geom_col() +
  coord_flip() +
  geom_text(aes(label = n), hjust = -0.3) +
  labs(title = "문재인 대통령 출마 연설문 단어 빈도", x = NULL, y = NULL) + theme(title = element_text(size = 12), text = element_text(family = "gamjaflower"))
