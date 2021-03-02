# 감정 단어가 사용된 원문 살펴보기

score_comment %>%
  filter(str_detect(reply, "소름")) %>%
  select(reply)
# # A tibble: 131 x 1
# reply                                                                 
# <chr>                                                                 
#   1 소름돋네요                                                            
# 2 와..진짜소름 저 소리처음질렀어요 눈물나요.. ㅠㅠ                      
# 3 생중계 보며 봉준호 할 때 소름이~~~!! ㅠㅠ 수상소감들으며 함께 가슴이 벅차네요. 축하합니다. 자랑스럽습니다!!! 노미네~
#   4 와 보다가 소름 짝 수고들하셨어요                                      
# 5 한국어 소감 듣는데 소름돋네 축하드립니다                              
# 6 대단하다!! 봉준호 이름 나오자마자 소름                                
# 7 와우 브라보~ 키아누리브스의 봉준호, 순간 소름이.. 멋지십니다.         
# 8 소름 돋네요. 축하합니다                                               
# 9 소름.... 기생충 각본집 산거 다시한번 잘했다는 생각이ㅠㅠㅠ 축하해요!!!!!!~
#   10 소름끼쳤어요 너무 멋집니다 ^^!!!!                                     
#   # ... with 121 more rows

score_comment %>%
  filter(str_detect(reply, "미친")) %>%
  select(reply)
# # A tibble: 15 x 1
# reply                                                                 
# <chr>                                                                 
#   1 와 3관왕 미친                                                         
# 2 미친거야 이건~~                                                       
#   3 Korea 대단합니다 김연아 방탄 봉준호 스포츠 음악 영화 못하는게 없어요 좌빨 감독이라 좌파 배우라 박근혜 때 블랙리스트 ~
#   4 청룡영화제에서 다른나라가 상을 휩쓴거죠? 와..미쳤다 미국영화제에서 한국이 빅5중에 3개를 타다니ㄷㄷ와..미친거같음~
#   5 설마했는데 감독상, 작품상, 각본상을 죄다 휩쓸어버릴 줄이야. 이건 미친 꿈이야!!!! 대박~~!!!~
#   6 완전 완전...미친촌재감~이런게 바로 애국이지~ 존경합니다~              
#   7 이세상엔 참 미 친 인간들이 많다는걸 댓글에서 다시한번 느낀다..모두가 축하해줘야할 일에 되도않는걸 갖다붙여 말하는 미친 쓰~
#   8 올해 아카데미 최다 수상작이기도 하다 이건 진짜 미친사건이다           
# 9 CJ회장이 저기서 왜 언급되는지... 미친 부회장.. 공과사 구분 못하는 정권의 홍위병~
#   10 미친봉                                                                
# 11 미친 3관왕 ㄷㄷㄷㄷㄷ                                                 
# 12 진짜 미친일...                                                        
# 13 나도모르게 보다가 육성으로 미친...ㅋㅋㅋㅋ 대박ㅜ                     
# 14 헐...감독상...미친...미쳤다..소름돋는다...                            
# 15 인정할건인정하자 봉감독 송배우 이배우 조배우등 인정하자 또 가로세로 ㅆㄹㄱ들은 송강호 까든데 미친방송은 구독말고 구취 냄새난~

dic %>% filter(word %in% c("소름", "소름이", "미친"))
# # A tibble: 3 x 2
# word   polarity
# <chr>     <dbl>
#   1 소름이       -2
# 2 소름         -2
# 3 미친         -2
# --------------------------------------------------------------------

# 감정 사전 수정하기

new_dic <- dic %>%
  mutate(polarity = ifelse(word %in% c("소름", "소름이", "미친"), 2, polarity))

new_dic %>% filter(word %in% c("소름", "소름이", "미친"))
# # A tibble: 3 x 2
# word   polarity
# <chr>     <dbl>
#   1 소름이        2
# 2 소름          2
# 3 미친          2
# --------------------------------------------------------------------

# 수정한 사전으로 감정 점수 부여하기

new_word_comment <- word_comment %>%
  select(-polarity) %>%
  left_join(new_dic, by = "word") %>%
  mutate(polarity = ifelse(is.na(polarity), 0, polarity))
# --------------------------------------------------------------------

# 댓글별 감정 점수 구하기

new_score_comment <- new_word_comment %>%
  group_by(id, reply) %>%
  summarise(score = sum(polarity)) %>%
  ungroup()

new_score_comment %>%
  select(score, reply) %>%
  arrange(-score)
# # A tibble: 4,140 x 2
# score reply                                                           
# <dbl> <chr>                                                           
#   1    11 아니 다른상을 받은것도 충분히 대단하고 굉장하지만 최고의 영예인 작품상을 받은거는 기생충이 작년 전세계 최고의 영~
#   2     9 봉준호의 위대한 업적은 진보 영화계의 위대한 업적이고 대한민국의 업적입니다. 이런 세계적인 감독이 존경하는 대통령~
#   3     8 소름 소름 진짜 멋지다 대단하다                                  
# 4     7 이 수상소식을 듣고 억수로 기뻐하는 가족이 있을것 같다. SNS를 통해 자기들을 내세우고 싶어 못견뎌하는 가족이 ~
#   5     7 감사 감사 감사 수상 소감도 3관왕 답네요                         
# 6     6 정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복하~
#   7     6 와 너무 기쁘다! 이 시국에 정말 내 일같이 기쁘고 감사하다!!! 축하드려요 진심으로!!!~
#   8     6 축하 축하 축하 모두들 수고 하셨어요 기생충 화이팅               
# 9     6 생중계 보며 봉준호 할 때 소름이~~~!! ㅠㅠ 수상소감들으며 함께 가슴이 벅차네요. 축하합니다. 자랑스럽습니다!~
#   10     6 축하!!!! 축하!!!!! 오스카의 정복은 무엇보다 시나리오의 힘이다. 작가의 사나리오, 감독의 연출, 배우의 연~
#   # ... with 4,130 more rows
# --------------------------------------------------------------------

# 감정 경향 살펴보기

new_score_comment <- new_score_comment %>%
  mutate(sentiment = ifelse(score >=  1, "pos",
                     ifelse(score <= -1, "neg", "neu")))

score_comment %>%
  count(sentiment) %>%
  mutate(ratio = n/sum(n)*100)
# # A tibble: 3 x 3
# sentiment     n ratio
# * <chr>     <int> <dbl>
#   1 neg         436  10.5
# 2 neu        2897  70.0
# 3 pos         807  19.5

new_score_comment %>%
  count(sentiment) %>%
  mutate(ratio = n/sum(n)*100)
# # A tibble: 3 x 3
# sentiment     n ratio
# * <chr>     <int> <dbl>
#   1 neg         368  8.89
# 2 neu        2890 69.8 
# 3 pos         882 21.3

word <- "소름|소름이|미친"

score_comment %>%
  filter(str_detect(reply, word)) %>%
  count(sentiment)
# # A tibble: 3 x 2
# sentiment     n
# * <chr>     <int>
#   1 neg          73
# 2 neu          63
# 3 pos           9

new_score_comment %>%
  filter(str_detect(reply, word)) %>%
  count(sentiment)
# # A tibble: 3 x 2
# sentiment     n
# * <chr>     <int>
#   1 neg           5
# 2 neu          56
# 3 pos          84

df <- tibble(sentence = c("이번 에피소드 쩐다", 
                          "이 영화 핵노잼")) %>% 
  unnest_tokens(input = sentence, 
                output = word, 
                token = "words", 
                drop = F)

df %>% 
  left_join(dic, by = "word") %>%
  mutate(polarity = ifelse(is.na(polarity), 0, polarity)) %>% 
  group_by(sentence) %>% 
  summarise(score = sum(polarity))
# # A tibble: 2 x 2
# sentence           score
# * <chr>              <dbl>
#   1 이 영화 핵노잼         0
# 2 이번 에피소드 쩐다     0

newword <- tibble(word = c("쩐다", "핵노잼"), 
                  polarity = c(2, -2))

newword_dic <- bind_rows(dic, newword)

df %>% 
  left_join(newword_dic, by = "word") %>%
  mutate(polarity = ifelse(is.na(polarity), 0, polarity)) %>% 
  group_by(sentence) %>% 
  summarise(score = sum(polarity))

# # A tibble: 2 x 2
# sentence           score
# * <chr>              <dbl>
#   1 이 영화 핵노잼        -2
# 2 이번 에피소드 쩐다     2
# --------------------------------------------------------------------

# 감정 범주별 주요 단어 살펴보기

new_comment <- new_score_comment %>%
  unnest_tokens(input = reply,
                output = word,
                token = "words",
                drop = F) %>%
  filter(str_detect(word, "[가-힣]") &
           str_count(word) >= 2)

new_frequency_word <- new_comment %>%
  count(sentiment, word, sort = T)

new_comment_wide <- new_frequency_word %>%
  filter(sentiment != "neu") %>%
  pivot_wider(names_from = sentiment,
              values_from = n,
              values_fill = list(n = 0))

new_comment_wide <- new_comment_wide %>%
  mutate(log_odds_ratio = log(((pos + 1) / (sum(pos + 1))) /
                                ((neg + 1) / (sum(neg + 1)))))

new_top10 <- new_comment_wide %>%
  group_by(sentiment = ifelse(log_odds_ratio > 0, "pos", "neg")) %>%
  slice_max(abs(log_odds_ratio), n = 10, with_ties = F)

ggplot(new_top10, aes(x = reorder(word, log_odds_ratio),
                      y = log_odds_ratio,
                      fill = sentiment)) +
  geom_col() +
  coord_flip() +
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))

top10 %>% 
  select(-pos, -neg) %>% 
  arrange(-log_odds_ratio) %>% 
  print(n = Inf)
# # A tibble: 20 x 3
# # Groups:   sentiment [2]
# word       log_odds_ratio sentiment
# <chr>               <dbl> <chr>    
#   1 축하                 3.95 pos      
# 2 멋지다               3.81 pos      
# 3 대단한               3.66 pos      
# 4 좋은                 3.55 pos      
# 5 대단하다             3.52 pos      
# 6 자랑스럽다           3.46 pos      
# 7 최고                 3.12 pos      
# 8 세계적인             3.01 pos      
# 9 최고의               2.97 pos      
# 10 위대한               2.92 pos      
# 11 닭그네              -1.82 neg      
# 12 가난한              -2.00 neg      
# 13 모르는              -2.00 neg      
# 14 아쉽다              -2.00 neg      
# 15 소름이              -2.08 neg      
# 16 좌좀                -2.16 neg      
# 17 못한                -2.29 neg      
# 18 미친                -2.29 neg      
# 19 좌빨                -2.61 neg      
# 20 소름                -3.03 neg  

new_top10 %>%
  select(-pos, -neg) %>%
  arrange(-log_odds_ratio) %>%
  print(n = Inf)
# # A tibble: 20 x 3
# # Groups:   sentiment [2]
# word       log_odds_ratio sentiment
# <chr>               <dbl> <chr>    
#   1 축하                 3.88 pos      
# 2 멋지다               3.76 pos      
# 3 소름                 3.76 pos      
# 4 대단한               3.59 pos      
# 5 대단하다             3.49 pos      
# 6 좋은                 3.48 pos      
# 7 자랑스럽다           3.40 pos      
# 8 최고                 3.09 pos      
# 9 세계적인             2.94 pos      
# 10 최고의               2.90 pos      
# 11 닭그네              -1.89 neg      
# 12 못하고              -1.89 neg      
# 13 사회적              -1.89 neg      
# 14 싫다                -1.89 neg      
# 15 가난한              -2.07 neg      
# 16 모르는              -2.07 neg      
# 17 아쉽다              -2.07 neg      
# 18 좌좀                -2.22 neg      
# 19 못한                -2.36 neg      
# 20 좌빨                -2.68 neg  

new_comment_wide %>%
  filter(word == "미친")
# # A tibble: 1 x 4
# word    pos   neg log_odds_ratio
# <chr> <int> <int>          <dbl>
#   1 미친      7     0           1.80

new_score_comment %>%
  filter(sentiment == "pos" & str_detect(reply, "축하")) %>%
  select(reply)
# # A tibble: 189 x 1
# reply                                                                 
# <chr>                                                                 
#   1 정말 우리 집에 좋은 일이 생겨 기쁘고 행복한 것처럼!! 나의 일인 양 행복합니다!! 축하드립니다^^ 정말 행복하고 기쁘네요~
#   2 와 너무 기쁘다! 이 시국에 정말 내 일같이 기쁘고 감사하다!!! 축하드려요 진심으로!!!~
#   3 우리나라의 영화감독분들 그리고 앞으로 그 꿈을 그리는 분들에게 큰 영감을 주시게된 봉감독님 그리고 공동각본쓴 한진원 작가님께~
#   4 아카데미나 다른 상이나 지들만의 잔치지~ 난 대한민국에서 받는 상이 제일 가치 있다고 본다 우선 축하 합니다~
#   5 정부에 빨대 꼽은 정치시민단체 기생충들이 득실거리는 떼한민국애서 훌륭한 영화 기생충이 오스카작품상을 받는 쾌거를 이루었습니다~
#   6 대단해요 나는 안봤는데 그렇게 잘 만들어 한국인의 기백을 세계에 알리는 큰 일을 하신데 다시한번 축하드립니다~
#   7 나한테 돌아오는게 하나도 없는데 왜이렇게 자랑스럽지?ㅎㅎㅎ 축하 합니다~작품상 수상도 기대해 봅니다~^^~
#   8 한국영화 100년사에 한횟을 긋네요. 정말 축하 합니다                    
# 9 와 대단하다 진짜 축하드려요!!! 대박 진짜                              
# 10 각본상, 국제 영화상 수상 축하. 편집상은 꽝남.                         
# # ... with 179 more rows

new_score_comment %>%
  filter(sentiment == "pos" & str_detect(reply, "소름")) %>%
  select(reply)
# # A tibble: 77 x 1
# reply                                                                 
# <chr>                                                                 
#   1 생중계 보며 봉준호 할 때 소름이~~~!! ㅠㅠ 수상소감들으며 함께 가슴이 벅차네요. 축하합니다. 자랑스럽습니다!!! 노미네~
#   2 와 보다가 소름 짝 수고들하셨어요                                      
# 3 대단하다!! 봉준호 이름 나오자마자 소름                                
# 4 와우 브라보~ 키아누리브스의 봉준호, 순간 소름이.. 멋지십니다.         
# 5 소름 돋네요. 축하합니다                                               
# 6 소름.... 기생충 각본집 산거 다시한번 잘했다는 생각이ㅠㅠㅠ 축하해요!!!!!!~
#   7 봉준호 아저씨 우리나라 자랑입니다 헐리웃 배우들과 화면에 같이 비춰지는게 아직도 믿기지 않아요 소름이 돋을 정도..~
#   8 추카해요. 봉준호하는데 막 완전 소름 돋았어요.                         
# 9 소름돋아서 닭살돋고.. 그냥 막 감동이라 눈물이 나려했어요.. 대단하고 자랑스럽습니다.~
#   10 한국 영화 최초 아카데미상 수상, 92년 역사의 국제 장편 영화상과 최우수작품상 동시 수상, 칸 영화제 황금종려상과 동시 수~
#   # ... with 67 more rows

new_score_comment %>%
  filter(sentiment == "neg" & str_detect(reply, "좌빨")) %>%
  select(reply)
# # A tibble: 34 x 1
# reply                                                                 
# <chr>                                                                 
#   1 자칭 보수들은 분노의 타이핑중 ㅋㅋㅋㅋㅋㅋ전세계를 좌빨로 몰수는 없고 자존심에 본인 눈깔과 생각이 틀린걸 인정은 못하겠고ㅋ ~
#   2 자칭보수 왈 : 미국에 로비했다 ㅋㅋ좌빨영화가 상받을리 없다 ㅋㅋㅋㅋㅋㅋㅋ 본인들의 편협한 눈알과 망상을 인정할수는 없어서 ~
#   3 좌빨 봉준호 영화는 쳐다도 안본다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ               
# 4 봉준호 그렇게 미국 싫어하는데 상은 쳐 받으러 가는 좌빨 수준ㅋㅋㅋ     
# 5 좌빨 기생충들은 댓글도 달지마라 미국 영화제 수상이 니들하고 뭔상관인데.~
#   6 얘들은 왜 인정을 안하냐? ㅋㅋ 니들 이미 변호인 찍을대 부터 송강호 욕해대고 좌빨 연예인라면서 신나게 깟잖아. 안그래? 인~
#   7 넷상 보수들 만큼 이중적인 새1끼들 없음. 봉준호 송강호 보고 종북좌빨 홍어드립 치던거 생각나네. ㅋㅋㅋ 그리고 이런분들 가~
#   8 우선 축하합니다.그리고 다음에는 조씨가족을 모델로한 뻔뻔하고 거짓말을 밥 먹듯이 하는 스스로를 강남 좌빨이고 사회주의자라고 ~
#   9 Korea 대단합니다 김연아 방탄 봉준호 스포츠 음악 영화 못하는게 없어요 좌빨 감독이라 좌파 배우라 박근혜 때 블랙리스트 ~
#   10 좌빨 감독이라고 블랙리스트에 올랐던 사람을 세계인이 인정해주네. 방구석에 앉아서 댓글 올리는 수구 꼴통들아, 광화문 태극기들~
#   # ... with 24 more rows
new_score_comment %>%
  filter(sentiment == "neg" & str_detect(reply, "못한")) %>%
  select(reply)
# # A tibble: 7 x 1
# reply                                                                  
# <chr>                                                                  
#   1 한번도경험하지. 못한 조국가족사기단기생충. 개봉박두                    
# 2 여기서 정치얘기하는 건 학창시절 공부 못한 거 인증하는 꼴... 주제좀 벗어나지 말아라~
#   3 이 기사를 반문으로 먹고 사는 자유왜국당과, mb아바타 간철수 댓글알바들이 매우 싫어 합니다!대한민국 문재인 정부가 망해야 지~
#   4 한국미국일본 vs 주적북한,중국러시아 이 구도인 현 시대 상황 속에서, 미국 일본을 멀리하고 북한중국에 안달나서 나라를 말아먹~
#   5 친일수꼴 들과 자한당넘들이 나라에 경사만 있으면 엄청 싫어합니다, 맨날 사고만 나길 빌고 있는듯.. 기생충보다 못한 인생들,,~
#   6 각본상,국제상,감독상 ...어디서 듣도보도 못한 아차상 같은 쩌리처리용 상 아닌가? 아카데미 진짜상은 작품상, 남우주연상,여우~
#   7 난 밥을 먹고 기생충은 오스카를 먹다, 기생충은 대한민국의 국격을 높였는데 난 무엇인가? 기생충 보다 못한 인간은 아닐지??~