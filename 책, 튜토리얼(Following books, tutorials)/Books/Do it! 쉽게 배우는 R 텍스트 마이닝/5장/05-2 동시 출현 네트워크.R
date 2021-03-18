# 네트워크 그래프 데이터 만들기

install.packages("tidygraph")
library(tidygraph)

graph_comment <- pair %>%
  filter(n >= 25) %>%
  as_tbl_graph()

graph_comment
# # A tbl_graph: 30 nodes and 108 edges
# #
# # A directed simple graph with 2 components
# #
# # Node Data: 30 x 1 (active)
# name  
# <chr> 
#   1 영화  
# 2 기생충
# 3 감독  
# 4 봉준호
# 5 감독님
# 6 만들다
# # ... with 24 more rows
# #
# # Edge Data: 108 x 3
# from    to     n
# <int> <int> <dbl>
#   1     1     2   111
# 2     2     1   111
# 3     3     4    86
# # ... with 105 more rows
# ---------------------------------------------
# 네트워크 그래프 만들기

install.packages("ggraph")
library(ggraph)

ggraph(graph_comment) +
  geom_edge_link() +
  geom_node_point() +
  geom_node_text(aes(label = name))

library(showtext)
font_add_google(name = "Nanum Gothic", family = "nanumgothic")
showtext_auto()

set.seed(1234)
ggraph(graph_comment, layout = "fr") +
  geom_edge_link(color = "gray50",
                 alpha = 0.5) + 
  geom_node_point(color = "lightcoral",
                  size = 5) +
  geom_node_text(aes(label = name),
                 repel = T,
                 size = 5,
                 family = "nanumgothic") +
  theme_graph()

word_network <- function(x) {
  ggraph(x, layout = "fr") +
    geom_edge_link(color = "gray50",
                   alpha = 0.5) +
    geom_node_point(color = "lightcoral",
                    size = 5) +
    geom_node_text(aes(label = name),
                   repel = T,
                   size = 5,
                   family = "nanumgothic") +
    theme_graph()
}

set.seed(1234)
word_network(graph_comment)
# ---------------------------------------------

# 유의어 처리하기

library(stringr)
comment <- comment %>%
  mutate(word = ifelse(str_detect(word, "감독") &
                         !str_detect(word, "감독상"), "봉준호", word), 
         word = ifelse(word == "오르다", "올리다", word),
         word = ifelse(str_detect(word, "축하"), "축하", word))

library(widyr)
pair <- comment %>%
  pairwise_count(item = word,
                 feature = id,
                 sort = T)

graph_comment <- pair %>%
  filter(n >= 25) %>%
  as_tbl_graph()

set.seed(1234)
word_network(graph_comment)
# ---------------------------------------------

# 연결 중심성과 커뮤니티 표현하기

set.seed(1234)
graph_comment <- pair %>%
  filter(n >= 25) %>%
  as_tbl_graph(directed = F) %>%
  mutate(centrality = centrality_degree(),
         group = as.factor(group_infomap()))

graph_comment
# # A tbl_graph: 36 nodes and 152 edges
# #
# # An undirected multigraph with 1 component
# #
# # Node Data: 36 x 3 (active)
# name       centrality group
# <chr>           <dbl> <fct>
#   1 봉준호             62 4    
# 2 축하               34 2    
# 3 영화               26 3    
# 4 블랙리스트          6 6    
# 5 기생충             26 1    
# 6 대한민국           10 3    
# # ... with 30 more rows
# #
# # Edge Data: 152 x 3
# from    to     n
# <int> <int> <dbl>
#   1     1     2   198
# 2     1     2   198
# 3     1     3   119
# # ... with 149 more rows

set.seed(1234)
ggraph(graph_comment, layout = "fr") +
  
  geom_edge_link(color = "gray50",
                 alpha = 0.5) +
  
  geom_node_point(aes(size = centrality,
                      color = group),
                  show.legend = F) +
  scale_size(range = c(5, 15)) +
  
  geom_node_text(aes(label = name),
                 repel = T,
                 size = 5,
                 family = "nanumgothic") +
  
  theme_graph()
# ---------------------------------------------

graph_comment %>%
  filter(name == "봉준호")
# # A tbl_graph: 1 nodes and 0 edges
# #
# # An unrooted tree
# #
# # Node Data: 1 x 3 (active)
# name   centrality group
# <chr>       <dbl> <fct>
#   1 봉준호         62 4    
# #
# # Edge Data: 0 x 3
# # ... with 3 variables: from <int>, to <int>, n <dbl>

graph_comment %>%
  filter(group == 4) %>%
  arrange(-centrality) %>%
  data.frame()
# name centrality group
# 1 봉준호         62     4
# 2   받다         10     4
# 3   자랑          6     4
# 4 만들다          4     4

graph_comment %>%
  arrange(-centrality)
# # A tbl_graph: 36 nodes and 152 edges
# #
# # An undirected multigraph with 1 component
# #
# # Node Data: 36 x 3 (active)
# name     centrality group
# <chr>         <dbl> <fct>
#   1 봉준호           62 4    
# 2 축하             34 2    
# 3 영화             26 3    
# 4 기생충           26 1    
# 5 작품상           14 5    
# 6 대한민국         10 3    
# # ... with 30 more rows
# #
# # Edge Data: 152 x 3
# from    to     n
# <int> <int> <dbl>
#   1     1     2   198
# 2     1     2   198
# 3     1     3   119
# # ... with 149 more rows

graph_comment %>%
  filter(group == 2) %>%
  arrange(-centrality) %>%
  data.frame()
# name centrality group
# 1   축하         34     2
# 2   좋다          8     2
# 3   진심          4     2
# 4   수상          4     2
# 5   없다          4     2
# 6   대단          2     2
# 7 기쁘다          2     2

news_comment %>%
  filter(str_detect(reply, "봉준호") & str_detect(reply, "대박")) %>%
  select(reply)
# # A tibble: 19 x 1
# reply                                                                 
# <chr>                                                                 
#   1 대박 대박 진짜 대박 봉준호 감독님과 우리 배우들 너무 다랑스러워요     
# 2 내가 죽기전에 아카데미에서 한국어를 들을줄이야 봉준호대박 기생충대박  
# 3 대박 관왕이라니 축하합니다 봉준호를 배출한 충무로 그리고 문화강국 대한 민국~
#   4 우와 대박 진자 대단하다 봉준호                                        
# 5 봉준호 경사났네 대박중에 대에박 축하합니다                            
# 6 봉준호 작품상 탔다 대박                                               
# 7 봉준호 군대 면제시켜도될듯 대박 여윽시 위대한 한국에는 위대한 봉준호 형님이 계시지 여윽시 미쳤습니다 아카데미는 별거 아닌것~
#   8 아니 다른상을 받은것도 충분히 대단하고 굉장하지만 최고의 영예인 작품상을 받은거는 기생충이 작년 전세계 최고의 영화라는거를 ~
#   9 봉준호 군대 면제시켜도될듯 대박 여윽시 위대한 한국에는 위대한 봉준호 형님이 계시지~
#   10 봉준호감독님대박 축하합니다                                           
# 11 와 봉준호 대박 축하드려요                                             
# 12 대박이다 감격의 한해입니다 봉준호 감독님 정말 축하드립니다            
# 13 좌파영화인 봉준호가 좌파영화로 아카데미 작품상 대박 배 아프겠다 안보겄다던 쓰레기들~
#   14 각본상 외국여영화상 수상 대박입니다 축하하고 잠시후에 봉준호 감독상과 영어 아닌 언어로 외국영화가 수상한 적이 없는 작품상도~
#   15 한국 역사상 최초인 오스카상 관왕 진짜 대박 대한민국 위상과 국격을 세계인들에게 널리 알린 봉준호 감독과 출연배우 당신들은 ~
#   16 미쳣다 감독상은 진짜 예상못햇는데 마틴 스콜쎄지 퀜틴타란티노 스티븐스필버그가 왓다갓다하는 시상식에 봉준호라니 대박~
#   17 봉준호감독 짱 가 대박났네                                             
# 18 와 대박 소름돋아 으악 봉준호 감독님 너무너무 축하드려요               
# 19 와 진짜 대박이다 봉준호 언젠가 정말 세계적으로 인정 받는 날이 올줄은 알았지만 와와 짐작하는 팬조차도 놀라자빠짐~

news_comment %>%
  filter(str_detect(reply, "박근혜") & str_detect(reply, "블랙리스트")) %>%
  select(reply)
# # A tibble: 63 x 1
# reply                                                                 
# <chr>                                                                 
#   1 일베와 자한당이 싫어하는 봉준호 감독이 아카데미에서 상받으니 쪽바리들처럼 엄청 싫어 하는구만 하긴 박근혜때 자한당이랑 봉감독~
#   2 박근혜 블랙리스트 로 낙인찍은 봉준호 감독님이 아시아 최초로 오스카에서 상을 받아버렸네 개꼬소~
#   3 우리나라에서만 좌파다 빨갱이다 라고 비하함 박근혜 때 이런 세계적 감독을 블랙리스트에 올렸음~
#   4 박근혜 최순실 블랙리스트에 오른 훌륭하신 감독님 축하합니다            
# 5 박근혜정부가 얼마나 썩고 무능했냐면 각종 영화제에서 최고상 수상을 받는 유능한 감독을 블랙리스트에 넣어 불이익을 주었다는것~
#   6 넷상 보수들 만큼 이중적인 새 끼들 없음 봉준호 송강호 보고 종북좌빨 홍어드립 치던거 생각나네 그리고 이런분들 가지고 블랙리~
#   7 박근혜 자한당 독재시절 봉준호 송강호를 블랙리스트 올려놓고 활동 방해 감시하면서 괴롭혔던 황교안이 이번에는 종로에 출마했단다~
#   8 대단합니다 김연아 방탄 봉준호 스포츠 음악 영화 못하는게 없어요 좌빨 감독이라 좌파 배우라 박근혜 때 블랙리스트 올라서 참 ~
#   9 송강호 봉준호 박근혜 이명박 시절 블랙리스트 이제 어떻게 깔려구        
# 10 이명박근혜정권당시 좌파감독이라고 블랙리스트까지 올랏던 봉준호 역사적위업을 달성햇네 자유망국당아그들과일베충식히들은 배 많이 아~
#   # ... with 53 more rows

news_comment %>%
  filter(str_detect(reply, "기생충") & str_detect(reply, "조국")) %>%
  select(reply)
# # A tibble: 64 x 1
# reply                                                                 
# <chr>                                                                 
#   1 조국이가 받아야 한다 기생충 스토리 제공                               
# 2 한번도경험하지 못한 조국가족사기단기생충 개봉박두                     
# 3 와 조국 가족 사기단 부제 기생충 최고                                  
# 4 문재인과 조국 기생충 리얼                                             
# 5 기생충은 좌좀 조국 가족을 패러디한 영화라서 우파들도 열광하고 있는 것이다 같은 영화라도 보는 사람에 따라 보이는 것도 다른~
#   6 조국 가족이 기생충 영화를 꼭 봐야되는데                               
# 7 좌파 인생영화인데 좌파 기생충들에게 이 상을 받쳐라 조국 서울대 문서위조학과 교수님 포함~
#   8 기생충 조국 봉준호 만세                                               
# 9 봉준호감독님 글로벌 영화계 큰상수상을 진심으로 축하합니다 다만 기생충 작품은 조국 정경심 자녀입시비리협의로 국내영화팬과 국민~
#   10 기생충보면서 조국생각난사람 나쁜일라나 봉준호 감독님이 현 시대를 참 잘 반영해서 만드신것같아요 조국 뿐만이 아니고 정치인들 ~
#   # ... with 54 more rows
