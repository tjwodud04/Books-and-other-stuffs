# 07-4 --------------------------------------------------------------------

# 토큰화
pos_tada <- tada %>%
  unnest_tokens(input = reply,
                output = word_pos,
                token = SimplePos22,
                drop = F)

# 품사 태그 정리
separate_pos_tada <- pos_tada %>%
  separate_rows(word_pos, sep = "[+]") %>%                   # 품사 태그 분리
  filter(str_detect(word_pos, "/n|/pv|/pa")) %>%             # 품사 추출
  mutate(word = ifelse(str_detect(word_pos, "/pv|/pa"),      # "/pv", "/pa" 추출
                       str_replace(word_pos, "/.*$", "다"),  # "~다"로 바꾸기
                       str_remove(word_pos, "/.*$"))) %>%    # 태그 제거
  filter(str_count(word) >= 2) %>%                           # 2글자 이상 추출
  arrange(id)

separate_pos_tada %>%
  select(word)


# -------------------------------------------------------------------------
library(widyr)
word_cors <- separate_pos_tada %>%
  add_count(word) %>%
  filter(n >= 20) %>%
  pairwise_cor(item = word, feature = id, sort = T)

word_cors


# -------------------------------------------------------------------------
target <- c("타다", "정부", "택시")

# 상위 10개 추출
top_cors <- word_cors %>%
  filter(item1 %in% target) %>%
  group_by(item1) %>%
  slice_max(correlation, n = 10)

top_cors


# -------------------------------------------------------------------------
# 그래프 순서 정하기
top_cors$item1 <- factor(top_cors$item1, levels = target)

# 막대 그래프 만들기
ggplot(top_cors, aes(x = reorder_within(item2, correlation, item1),
                     y = correlation,
                     fill = item1)) +
  geom_col(show.legend = F) +
  facet_wrap(~ item1, scales = "free") +
  coord_flip() +
  scale_x_reordered() +
  
  labs(title = "타다 금지법 기사 댓글 주요 단어",
       subtitle = "파이 계수 Top 10",
       x = NULL) +
  
  theme_minimal() +
  theme(text = element_text(family = "nanumgothic"),
        plot.title = element_text(size = 14, face = "bold"),
        plot.subtitle = element_text(size = 12),
        strip.text = element_text(size = 11))


# -------------------------------------------------------------------------
# 네트워크 그래프 데이터 만들기
library(tidygraph)
set.seed(1234)
graph_cors <- word_cors %>%
  filter(correlation >= 0.15) %>%
  as_tbl_graph(directed = F) %>%
  mutate(centrality = centrality_degree(),       # 중심성
         group = as.factor(group_infomap()))     # 커뮤니티

# 네트워크 그래프 만들기
library(ggraph)
set.seed(1234)
ggraph(graph_cors, layout = "fr") +              # 레이아웃
  
  geom_edge_link(color = "gray50",               # 엣지 색깔
                 aes(edge_alpha = correlation,   # 엣지 명암
                     edge_width = correlation),  # 엣지 두께
                 show.legend = F) +              # 범례 삭제
  scale_edge_width(range = c(1, 4)) +            # 엣지 두께 범위
  
  geom_node_point(aes(size = centrality,         # 노드 크기
                      color = group),            # 노드 색깔
                  show.legend = F) +             # 범례 삭제
  scale_size(range = c(5, 10)) +                 # 노드 크기 범위
  
  geom_node_text(aes(label = name),              # 텍스트 표시
                 repel = T,                      # 노드밖 표시
                 size = 5,                       # 텍스트 크기
                 family = "nanumgothic") +       # 폰트
  
  theme_graph()                                  # 배경 삭제


# -------------------------------------------------------------------------
tada %>%
  filter(str_detect(reply_raw, "선거")) %>%
  find_word(x = reply_raw, keyword = "내년", n = 10)

tada %>%
  filter(str_detect(reply_raw, "내년")) %>%
  find_word(x = reply_raw, keyword = "총선", n = 10)

tada %>%
  filter(str_detect(reply_raw, "목적지")) %>%
  find_word(x = reply_raw, keyword = "손님", n = 10)

tada %>%
  filter(str_detect(reply_raw, "손님")) %>%
  find_word(x = reply_raw, keyword = "골라", n = 10)


# -------------------------------------------------------------------------

separate_pos_tada %>%
  filter(word == "고르다") %>%
  pull(reply_raw)


# -------------------------------------------------------------------------
# 한 댓글이 하나의 행을 구성하도록 결합
line_comment <- separate_pos_tada %>%
  group_by(id) %>%
  summarise(sentence = paste(word, collapse = " "))

# 바이그램으로 토큰화
bigram_comment <- line_comment %>%
  unnest_tokens(input = sentence,
                output = bigram,
                token = "ngrams",
                n = 2)

bigram_comment


# -------------------------------------------------------------------------
# 바이그램 분리하기
bigram_seprated <- bigram_comment %>%
  separate(bigram, c("word1", "word2"), sep = " ")

# 단어쌍 빈도 구하기
pair_bigram <- bigram_seprated %>%
  count(word1, word2, sort = T) %>%
  na.omit()

pair_bigram


# -------------------------------------------------------------------------
# 네트워크 그래프 데이터 만들기
set.seed(1234)
graph_bigram <- pair_bigram %>%
  filter(n >= 8) %>%
  as_tbl_graph(directed = F) %>%
  mutate(centrality = centrality_degree(),       # 중심성
         group = as.factor(group_infomap()))     # 커뮤니티

# 네트워크 그래프 만들기
set.seed(1234)
ggraph(graph_bigram, layout = "fr") +            # 레이아웃
  
  geom_edge_link(color = "gray50",               # 엣지 색깔
                 alpha = 0.5) +                  # 엣지 명암
  
  geom_node_point(aes(size = centrality,         # 노드 크기
                      color = group),            # 노드 색깔
                  show.legend = F) +             # 범례 삭제
  scale_size(range = c(5, 15)) +                 # 노드 크기 범위
  
  geom_node_text(aes(label = name),              # 텍스트 표시
                 repel = T,                      # 노드밖 표시
                 size = 5,                       # 텍스트 크기
                 family = "nanumgothic") +       # 폰트
  
  theme_graph()                                  # 배경 삭제


# -------------------------------------------------------------------------
line_tada <- line_comment %>%
  left_join(tada, by = "id")

line_tada %>%
  select(sentence)


# -------------------------------------------------------------------------
line_tada %>%
  filter(str_detect(sentence, "시대 역행")) %>%
  find_word(x = reply_raw, keyword = "역행", n = 10)

line_tada %>%
  filter(str_detect(sentence, "시대 뒤떨어지다")) %>%
  find_word(x = reply_raw, keyword = "뒤떨어", n = 10)

line_tada %>%
  filter(str_detect(sentence, "택시 면허")) %>%
  find_word(x = reply_raw, keyword = "면허", n = 10)

line_tada %>%
  filter(str_detect(sentence, "면허 사다")) %>%
  find_word(x = reply_raw, keyword = "사서", n = 10)