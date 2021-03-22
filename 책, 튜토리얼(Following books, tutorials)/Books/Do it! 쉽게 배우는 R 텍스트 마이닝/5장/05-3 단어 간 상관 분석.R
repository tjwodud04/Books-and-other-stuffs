# 파이 계수 구하기

word_cors <- comment %>%
  add_count(word) %>%
  filter(n >= 20) %>%
  pairwise_cor(item = word,
               feature = id,
               sort = T)

word_cors
# # A tibble: 29,412 x 3
# item1      item2      correlation
# <chr>      <chr>            <dbl>
#   1 올리다     블랙리스트       0.436
# 2 블랙리스트 올리다           0.436
# 3 역사       쓰다             0.370
# 4 쓰다       역사             0.370
# 5 감독님     봉준호           0.335
# 6 봉준호     감독님           0.335
# 7 박근혜     블랙리스트       0.322
# 8 블랙리스트 박근혜           0.322
# 9 가족       조국             0.306
# 10 조국       가족             0.306
# # ... with 29,402 more rows
# ---------------------------------------------------

# 특정 단어와 관련성이 큰 단어 살펴보기

word_cors %>% 
  filter(item1 == "대한민국")
# # A tibble: 171 x 3
# item1    item2  correlation
# <chr>    <chr>        <dbl>
#   1 대한민국 국민        0.182 
# 2 대한민국 자랑        0.157 
# 3 대한민국 위상        0.148 
# 4 대한민국 국격        0.129 
# 5 대한민국 위대한      0.100 
# 6 대한민국 세계        0.0906
# 7 대한민국 문화        0.0754
# 8 대한민국 감사합      0.0722
# 9 대한민국 축하        0.0715
# 10 대한민국 나라        0.0713
# # ... with 161 more rows

word_cors %>% 
  filter(item1 == "역사")
# # A tibble: 171 x 3
# item1 item2    correlation
# <chr> <chr>          <dbl>
#   1 역사  쓰다          0.370 
# 2 역사  최초          0.117 
# 3 역사  한국          0.0979
# 4 역사  순간          0.0908
# 5 역사  한국영화      0.0819
# 6 역사  아니다        0.0771
# 7 역사  감사          0.0653
# 8 역사  영광          0.0639
# 9 역사  영화제        0.0595
# 10 역사  오스카        0.0591
# # ... with 161 more rows
# ---------------------------------------------------

# 파이 계수로 막대 그래프 만들기

target <- c("대한민국", "역사", "수상소감", "조국", "박근혜", "블랙리스트")

top_cors <- word_cors %>%
  filter(item1 %in% target) %>%
  group_by(item1) %>%
  slice_max(correlation, n = 8)

top_cors$item1 <- factor(top_cors$item1, levels = target)

library(ggplot2)
ggplot(top_cors, aes(x = reorder_within(item2, correlation, item1),
                     y = correlation,
                     fill = item1)) +
  geom_col(show.legend = F) +
  facet_wrap(~ item1, scales = "free") +
  coord_flip() +
  scale_x_reordered() +
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))
# ---------------------------------------------------

# 파이 계수로 네트워크 그래프 만들기

set.seed(1234)
graph_cors <- word_cors %>%
  filter(correlation >= 0.15) %>%
  as_tbl_graph(directed = F) %>%
  mutate(centrality = centrality_degree(),
         group = as.factor(group_infomap()))

set.seed(1234)
ggraph(graph_cors, layout = "fr") +
  geom_edge_link(color = "gray50",
                 aes(edge_alpha = correlation,
                     edge_width = correlation),
                 show.legend = F) +
  scale_edge_width(range = c(1, 4)) +
  geom_node_point(aes(size = centrality,
                      color = group),
                  show.legend = F) +
  scale_size(range = c(5, 10)) +
  geom_node_text(aes(label = name),
                 repel = T,
                 size = 5,
                 family = "nanumgothic") +
  theme_graph()