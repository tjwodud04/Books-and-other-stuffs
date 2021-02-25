# 로그 오즈비 구하기

frequency_wide <- frequency_wide %>%
  mutate(log_odds_ratio = log(odds_ratio))

frequency_wide %>%
  arrange(-log_odds_ratio)
# # A tibble: 955 x 7
# word      moon  park ratio_moon ratio_park odds_ratio log_odds_ratio
# <chr>    <int> <int>      <dbl>      <dbl>      <dbl>          <dbl>
#   1 복지국가     8     0    0.00393   0.000552       7.12           1.96
# 2 세상         6     0    0.00306   0.000552       5.54           1.71
# 3 여성         6     0    0.00306   0.000552       5.54           1.71
# 4 정의         6     0    0.00306   0.000552       5.54           1.71
# 5 강자         5     0    0.00262   0.000552       4.75           1.56
# 6 공평         5     0    0.00262   0.000552       4.75           1.56
# 7 대통령의     5     0    0.00262   0.000552       4.75           1.56
# 8 보통         5     0    0.00262   0.000552       4.75           1.56
# 9 상생         5     0    0.00262   0.000552       4.75           1.56
# 10 지방         5     0    0.00262   0.000552       4.75           1.56
# # ... with 945 more rows

frequency_wide %>%
  arrange(log_odds_ratio)
# # A tibble: 955 x 7
# word      moon  park ratio_moon ratio_park odds_ratio log_odds_ratio
# <chr>    <int> <int>      <dbl>      <dbl>      <dbl>          <dbl>
#   1 박근혜       0     8   0.000436    0.00496     0.0879          -2.43
# 2 여러분       2    20   0.00131     0.0116      0.113           -2.18
# 3 행복         3    23   0.00175     0.0132      0.132           -2.03
# 4 실천         0     5   0.000436    0.00331     0.132           -2.03
# 5 정보         0     5   0.000436    0.00331     0.132           -2.03
# 6 투명         0     5   0.000436    0.00331     0.132           -2.03
# 7 과제         0     4   0.000436    0.00276     0.158           -1.84
# 8 국정운영     0     4   0.000436    0.00276     0.158           -1.84
# 9 시작         0     4   0.000436    0.00276     0.158           -1.84
# 10 지식         0     4   0.000436    0.00276     0.158           -1.84
# # ... with 945 more rows

frequency_wide %>%
  arrange(abs(log_odds_ratio))
# # A tibble: 955 x 7
# word    moon  park ratio_moon ratio_park odds_ratio log_odds_ratio
# <chr>  <int> <int>      <dbl>      <dbl>      <dbl>          <dbl>
#   1 때문       4     3    0.00218    0.00221      0.989        -0.0109
# 2 강화       3     2    0.00175    0.00165      1.06          0.0537
# 3 부담       3     2    0.00175    0.00165      1.06          0.0537
# 4 세계       3     2    0.00175    0.00165      1.06          0.0537
# 5 책임       3     2    0.00175    0.00165      1.06          0.0537
# 6 협력       3     2    0.00175    0.00165      1.06          0.0537
# 7 거대       2     1    0.00131    0.00110      1.19          0.171 
# 8 교체       2     1    0.00131    0.00110      1.19          0.171 
# 9 근본적     2     1    0.00131    0.00110      1.19          0.171 
# 10 기반       2     1    0.00131    0.00110      1.19          0.171 
# # ... with 945 more rows

frequency_wide <- frequency_wide %>%
  mutate(log_odds_ratio = log(((moon + 1) / (sum(moon + 1))) /
                                ((park + 1) / (sum(park + 1)))))
--------------------------------------------------------------------
# 로그 오즈비를 이용해 중요한 단어 비교하기
  
top10 <- frequency_wide %>%
  group_by(president = ifelse(log_odds_ratio > 0, "moon", "park")) %>%
  slice_max(abs(log_odds_ratio), n = 10, with_ties = F)

top10 %>% 
  arrange(-log_odds_ratio) %>% 
  select(word, log_odds_ratio, president) %>% 
  print(n = Inf)
# # A tibble: 20 x 3
# # Groups:   president [2]
# word     log_odds_ratio president
# <chr>             <dbl> <chr>    
#   1 복지국가           1.96 moon     
# 2 세상               1.71 moon     
# 3 여성               1.71 moon     
# 4 정의               1.71 moon     
# 5 강자               1.56 moon     
# 6 공평               1.56 moon     
# 7 대통령의           1.56 moon     
# 8 보통               1.56 moon     
# 9 상생               1.56 moon     
# 10 지방               1.56 moon     
# 11 과제              -1.84 park     
# 12 국정운영          -1.84 park     
# 13 시작              -1.84 park     
# 14 지식              -1.84 park     
# 15 행복              -2.03 park     
# 16 실천              -2.03 park     
# 17 정보              -2.03 park     
# 18 투명              -2.03 park     
# 19 여러분            -2.18 park     
# 20 박근혜            -2.43 park 
-------------------------------------------------
# 막대 그래프 만들기

ggplot(top10, aes(x = reorder(word, log_odds_ratio),
       y = log_odds_ratio, fill = president)) + 
  geom_col() + coord_flip() + labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))