# long form을 wide form으로 변환하기
df_long <- frequency %>%
  group_by(president) %>%
  slice_max(n, n = 10) %>%
  filter(word %in% c("국민", "우리", "정치", "행복"))
 
df_long
# # A tibble: 6 x 3
# # Groups:   president [2]
# president word      n
# <chr>     <chr> <int>
#   1 moon      국민     21
# 2 moon      우리     17
# 3 moon      정치     12
# 4 park      국민     72
# 5 park      행복     23
# 6 park      우리     10
----------------------------------------------------------
install.packages("tidyr")
library(tidyr)

df_wide <- df_long %>%
  pivot_wider(names_from = president,
              values_from = n)

df_wide
# # A tibble: 4 x 3
# word   moon  park
# <chr> <int> <int>
#   1 국민     21    72
# 2 우리     17    10
# 3 정치     12    NA
# 4 행복     NA    23

df_wide <- df_long %>%
  pivot_wider(names_from = president,
              values_from = n,
              values_fill = list(n = 0))

df_wide
# # A tibble: 4 x 3
# word   moon  park
# <chr> <int> <int>
#   1 국민     21    72
# 2 우리     17    10
# 3 정치     12     0
# 4 행복      0    23

frequency_wide <- frequency %>%
  pivot_wider(names_from = president,
              values_from = n,
              values_fill = list(n = 0))

frequency_wide
# # A tibble: 955 x 3
# word      moon  park
# <chr>    <int> <int>
#   1 가동         1     0
# 2 가사         1     0
# 3 가슴         2     0
# 4 가족         1     1
# 5 가족구조     1     0
# 6 가지         4     0
# 7 가치         3     1
# 8 각종         1     0
# 9 감당         1     0
# 10 강력         3     0
# # ... with 945 more rows
---------------------------------------------

# 오즈비 구하기

frequency_wide <- frequency_wide %>%
mutate(ratio_moon = ((moon + 1)/(sum(moon + 1))), 
       ratio_park = ((park + 1)/(sum(park + 1))))

frequency_wide
# # A tibble: 955 x 5
# word      moon  park ratio_moon ratio_park
# <chr>    <int> <int>      <dbl>      <dbl>
#   1 가동         1     0   0.000873   0.000552
# 2 가사         1     0   0.000873   0.000552
# 3 가슴         2     0   0.00131    0.000552
# 4 가족         1     1   0.000873   0.00110 
# 5 가족구조     1     0   0.000873   0.000552
# 6 가지         4     0   0.00218    0.000552
# 7 가치         3     1   0.00175    0.00110 
# 8 각종         1     0   0.000873   0.000552
# 9 감당         1     0   0.000873   0.000552
# 10 강력         3     0   0.00175    0.000552
# # ... with 945 more rows

frequency_wide <- frequency_wide %>%
  mutate(odds_ratio = ratio_moon/ratio_park)

frequency_wide %>%
  arrange(-odds_ratio)
# # A tibble: 955 x 6
# word      moon  park ratio_moon ratio_park odds_ratio
# <chr>    <int> <int>      <dbl>      <dbl>      <dbl>
#   1 복지국가     8     0    0.00393   0.000552       7.12
# 2 세상         6     0    0.00306   0.000552       5.54
# 3 여성         6     0    0.00306   0.000552       5.54
# 4 정의         6     0    0.00306   0.000552       5.54
# 5 강자         5     0    0.00262   0.000552       4.75
# 6 공평         5     0    0.00262   0.000552       4.75
# 7 대통령의     5     0    0.00262   0.000552       4.75
# 8 보통         5     0    0.00262   0.000552       4.75
# 9 상생         5     0    0.00262   0.000552       4.75
# 10 지방         5     0    0.00262   0.000552       4.75
# # ... with 945 more rows

frequency_wide %>%
  arrange(odds_ratio)
# # A tibble: 955 x 6
# word      moon  park ratio_moon ratio_park odds_ratio
# <chr>    <int> <int>      <dbl>      <dbl>      <dbl>
#   1 박근혜       0     8   0.000436    0.00496     0.0879
# 2 여러분       2    20   0.00131     0.0116      0.113 
# 3 행복         3    23   0.00175     0.0132      0.132 
# 4 실천         0     5   0.000436    0.00331     0.132 
# 5 정보         0     5   0.000436    0.00331     0.132 
# 6 투명         0     5   0.000436    0.00331     0.132 
# 7 과제         0     4   0.000436    0.00276     0.158 
# 8 국정운영     0     4   0.000436    0.00276     0.158 
# 9 시작         0     4   0.000436    0.00276     0.158 
# 10 지식         0     4   0.000436    0.00276     0.158 
# # ... with 945 more rows

frequency_wide <- frequency_wide %>%
  mutate(ratio_moon  = ((moon + 1)/(sum(moon + 1))),
         ratio_park  = ((park + 1)/(sum(park + 1))),
         odds_ratio = ratio_moon/ratio_park)

frequency_wide <- frequency_wide %>%
  mutate(odds_ratio = ((moon + 1)/(sum(moon + 1)))/
           ((park + 1)/(sum(park + 1))))
----------------------------------------------------------

# 상대적으로 중요한 단어 추출하기

top10 <- frequency_wide %>%
  filter(rank(odds_ratio) <= 10 | rank(-odds_ratio) <= 10)

top10 %>%
  arrange(-odds_ratio) %>%
  print(n = Inf)
# # A tibble: 20 x 6
# word      moon  park ratio_moon ratio_park odds_ratio
# <chr>    <int> <int>      <dbl>      <dbl>      <dbl>
#   1 복지국가     8     0   0.00393    0.000552     7.12  
# 2 세상         6     0   0.00306    0.000552     5.54  
# 3 여성         6     0   0.00306    0.000552     5.54  
# 4 정의         6     0   0.00306    0.000552     5.54  
# 5 강자         5     0   0.00262    0.000552     4.75  
# 6 공평         5     0   0.00262    0.000552     4.75  
# 7 대통령의     5     0   0.00262    0.000552     4.75  
# 8 보통         5     0   0.00262    0.000552     4.75  
# 9 상생         5     0   0.00262    0.000552     4.75  
# 10 지방         5     0   0.00262    0.000552     4.75  
# 11 과제         0     4   0.000436   0.00276      0.158 
# 12 국정운영     0     4   0.000436   0.00276      0.158 
# 13 시작         0     4   0.000436   0.00276      0.158 
# 14 지식         0     4   0.000436   0.00276      0.158 
# 15 행복         3    23   0.00175    0.0132       0.132 
# 16 실천         0     5   0.000436   0.00331      0.132 
# 17 정보         0     5   0.000436   0.00331      0.132 
# 18 투명         0     5   0.000436   0.00331      0.132 
# 19 여러분       2    20   0.00131    0.0116       0.113 
# 20 박근혜       0     8   0.000436   0.00496      0.0879
-----------------------------------------------------------
df <- tibble(x = c(2, 5, 10))
df %>% mutate(y = rank(x))
# # A tibble: 3 x 2
# x     y
# <dbl> <dbl>
#   1     2     1
# 2     5     2
# 3    10     3

df %>% mutate(y = rank(-x))
# # A tibble: 3 x 2
# x     y
# <dbl> <dbl>
#   1     2     3
# 2     5     2
# 3    10     1
-------------------------------------------------------------

#막대 그래프 만들기

top10 <- top10 %>%
  mutate(president = ifelse(odds_ratio > 1, "moon", "park"),
         n = ifelse(odds_ratio > 1, moon, park))

top10
# # A tibble: 20 x 8
# word      moon  park ratio_moon ratio_park odds_ratio president     n
# <chr>    <int> <int>      <dbl>      <dbl>      <dbl> <chr>     <int>
#   1 강자         5     0   0.00262    0.000552     4.75   moon          5
# 2 공평         5     0   0.00262    0.000552     4.75   moon          5
# 3 대통령의     5     0   0.00262    0.000552     4.75   moon          5
# 4 보통         5     0   0.00262    0.000552     4.75   moon          5
# 5 복지국가     8     0   0.00393    0.000552     7.12   moon          8
# 6 상생         5     0   0.00262    0.000552     4.75   moon          5
# 7 세상         6     0   0.00306    0.000552     5.54   moon          6
# 8 여러분       2    20   0.00131    0.0116       0.113  park         20
# 9 여성         6     0   0.00306    0.000552     5.54   moon          6
# 10 정의         6     0   0.00306    0.000552     5.54   moon          6
# 11 지방         5     0   0.00262    0.000552     4.75   moon          5
# 12 행복         3    23   0.00175    0.0132       0.132  park         23
# 13 과제         0     4   0.000436   0.00276      0.158  park          4
# 14 국정운영     0     4   0.000436   0.00276      0.158  park          4
# 15 박근혜       0     8   0.000436   0.00496      0.0879 park          8
# 16 시작         0     4   0.000436   0.00276      0.158  park          4
# 17 실천         0     5   0.000436   0.00331      0.132  park          5
# 18 정보         0     5   0.000436   0.00331      0.132  park          5
# 19 지식         0     4   0.000436   0.00276      0.158  park          4
# 20 투명         0     5   0.000436   0.00331      0.132  park          5
-----------------------------------------------------------------------------
  
ggplot(top10, aes(x = reorder_within(word, n, president),
                  y = n, fill = president)) + geom_col() + 
  coord_flip() + facet_wrap(~ president, scales = "free_y") + 
  scale_x_reordered()

ggplot(top10, aes(x = reorder_within(word, n, president),
                  y = n,
                  fill = president)) +
  geom_col() +
  coord_flip() +
  facet_wrap(~ president, scales = "free") +
  scale_x_reordered() +
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))
-----------------------------------------------------------------------------
  
# 주요 단어가 사용된 문장 살펴보기
  
speeches_sentence <- bind_speeches %>%
  as_tibble() %>%
  unnest_tokens(input = value,
                output = sentence,
                token = "sentences")

head(speeches_sentence)
# # A tibble: 6 x 2
# president sentence                                                    
# <chr>     <chr>                                                       
#   1 moon      "정권교체 하겠습니다!"                                      
# 2 moon      "정치교체 하겠습니다!"                                      
# 3 moon      "시대교체 하겠습니다!"                                      
# 4 moon      ""                                                          
# 5 moon      "‘불비불명(不飛不鳴)’이라는 고사가 있습니다."               
# 6 moon      "남쪽 언덕 나뭇가지에 앉아, 3년 동안 날지도 울지도 않는 새."

tail(speeches_sentence)
# # A tibble: 6 x 2
# president sentence                                                     
# <chr>     <chr>                                                        
#   1 park      국민 여러분의 행복이 곧 저의 행복입니다.                     
# 2 park      사랑하는 조국 대한민국과 국민 여러분을 위해, 앞으로 머나 먼 길, 끝까지 최선을 다해 뛰겠습니다.~
#   3 park      그 길을 함께 해주시길 부탁드립니다.                          
# 4 park      감사합니다.                                                  
# 5 park      2012년 7월 10일                                              
# 6 park      새누리당 예비후보 박근혜  

speeches_sentence %>%
  filter(president == "moon" & str_detect(sentence, "복지국가"))
# # A tibble: 8 x 2
# president sentence                                                     
# <chr>     <chr>                                                        
#   1 moon      ‘강한 복지국가’를 향해 담대하게 나아가겠습니다.              
# 2 moon      2백 년 전 이와 같은 소득재분배, 복지국가의 사상을 가진 위정자가 지구상 어디에 또 있었겠습니까?~
#   3 moon      이제 우리는 복지국가를 향해 담대하게 나아갈 때입니다.        
# 4 moon      부자감세, 4대강 사업 같은 시대착오적 과오를 청산하고, 하루빨리 복지국가로 가야 합니다.~
#   5 moon      우리는 지금 복지국가로 가느냐, 양극화의 분열된 국가로 가느냐 하는 절박한 싸움을 벌이고 있습니다.~
#   6 moon      강한 복지국가일수록 국가 경쟁력도 더 높습니다.               
# 7 moon      결국 복지국가로 가는 길은 사람에 대한 투자, 일자리 창출, 자영업 고통 경감, 삶의 질 향상 등 1석 4조~
#   8 moon      우리는 과감히 강한 보편적 복지국가로 가야 합니다.  

speeches_sentence %>%
  filter(president == "park" & str_detect(sentence, "행복"))
# # A tibble: 19 x 2
# president sentence                                                    
# <chr>     <chr>                                                       
#   1 park      저는 오늘, 국민 한 분 한 분의 꿈이 이루어지는 행복한 대한민국을 만들기 위해, 저의 모든 것을 바치겠다~
#   2 park      국가는 발전했고, 경제는 성장했다는데, 나의 삶은 나아지지 않았고, 나의 행복은 커지지 않았습니다.~
#   3 park      과거에는 국가의 발전이 국민의 행복으로 이어졌습니다.        
# 4 park      개인의 창의력이 중요한 지식기반사회에서는 국민 한 사람, 한 사람이 중요한 시대이고, 국민 개개인이 행복해~
#   5 park      이제 국정운영의 패러다임을 국가에서 국민으로, 개인의 삶과 행복 중심으로 확 바꿔야 합니다.~
#   6 park      국민 개개인의 꿈을 향한 노력이 국가를 발전시키고 국가 발전이 국민 행복으로 선순환되는 ‘국민행복의 길’,~
#   7 park      저는 ‘경제민주화 실현’, ‘일자리 창출’, 그리고 ‘한국형 복지의 확립’을 국민행복을 위한 3대 핵심과제~
#   8 park      국민행복의 길을 열어갈 첫 번째 과제로, 저는 경제민주화를 통해 중소기업인을 비롯한 경제적 약자들의 꿈이 ~
#   9 park      국민행복의 길을 열어갈 두 번째 과제로, 저는 좋은 일자리 창출을 통해 일하고 싶은 사람들이 꿈을 이룰 수~
#   10 park      국민행복의 길을 열어갈 세 번째 과제로, 우리의 실정에 맞으면서 국민에게 실질적인 도움을 주는 생애주기별 ~
#   11 park      저는 국민행복을 위해 ‘경제민주화-일자리-복지’를 아우르는 (가칭)‘오천만 국민행복 플랜’을 수립하여 추진~
#   12 park      모든 계층의 국민이 함께 참여해 만들고, 정부와 기업, 지역사회가 함께 연대해 실천해가는 국민행복의 청사진~
#   13 park      50년 전 경제개발 5개년 계획이 산업화의 기적을 이뤄냈듯,‘오천만 국민행복 플랜’을 통해, 앞으로 50년~
#   14 park      저는 지속가능한 국민 행복을 만들 수 있도록,사람에 대한 투자를 적극적으로 확대해 나갈 것입니다.~
#   15 park      저 박근혜, 경쟁과 입시에 매몰된 교육을‘함께하는 행복교육’으로 바꾸겠습니다.~
#   16 park      존경하는 국민여러분, 국민행복을 위한 노력이 안정적으로 이루어지기 위해서는 무엇보다 한반도에 평화가 정착되~
#   17 park      국민 여러분, 국민행복의 꿈을 이뤄내기 위해서는, 먼저 정부부터 변해야합니다.~
#   18 park      국민들이 꿈으로만 가졌던 행복한 삶을 실제로 이룰 수 있도록 도와드리는 대통령이 되고 싶습니다.~
#   19 park      국민 여러분의 행복이 곧 저의 행복입니다.
--------------------------------------------------------------------------------------------------------------------------
  
# 중요도가 비슷한 단어 살펴보기
  
frequency_wide %>%
  arrange(abs(1 - odds_ratio)) %>%
  head(10)
# # A tibble: 10 x 6
# word    moon  park ratio_moon ratio_park odds_ratio
# <chr>  <int> <int>      <dbl>      <dbl>      <dbl>
#   1 때문       4     3    0.00218    0.00221      0.989
# 2 강화       3     2    0.00175    0.00165      1.06 
# 3 부담       3     2    0.00175    0.00165      1.06 
# 4 세계       3     2    0.00175    0.00165      1.06 
# 5 책임       3     2    0.00175    0.00165      1.06 
# 6 협력       3     2    0.00175    0.00165      1.06 
# 7 거대       2     1    0.00131    0.00110      1.19 
# 8 교체       2     1    0.00131    0.00110      1.19 
# 9 근본적     2     1    0.00131    0.00110      1.19 
# 10 기반       2     1    0.00131    0.00110      1.19 

frequency_wide %>%
  filter(moon >= 5 & park >= 5) %>%
  arrange(abs(1 - odds_ratio)) %>%
  head(10)
# # A tibble: 10 x 6
# word      moon  park ratio_moon ratio_park odds_ratio
# <chr>    <int> <int>      <dbl>      <dbl>      <dbl>
#   1 사회        14     9    0.00655    0.00552      1.19 
# 2 사람         9     9    0.00436    0.00552      0.791
# 3 경제        15    15    0.00698    0.00883      0.791
# 4 지원         5     5    0.00262    0.00331      0.791
# 5 우리        17    10    0.00786    0.00607      1.29 
# 6 불안         7     8    0.00349    0.00496      0.703
# 7 산업         9     5    0.00436    0.00331      1.32 
# 8 대한민국    11     6    0.00524    0.00386      1.36 
# 9 국가         7    10    0.00349    0.00607      0.576
# 10 교육         6     9    0.00306    0.00552      0.554
