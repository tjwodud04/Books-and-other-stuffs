install.packages("ldatuning")
library(ldatuning)

models <- FindTopicsNumber(dtm = dtm_comment,
                           topics = 2:20,
                           return_models = T,
                           control = list(seed = 1234))

models %>%
  select(topics, Griffiths2004)

FindTopicsNumber_plot(models)
# topics Griffiths2004
# 1      20     -127213.1
# 2      19     -127445.4
# 3      18     -126984.0
# 4      17     -127317.9
# 5      16     -127139.2
# 6      15     -126643.9
# 7      14     -126742.4
# 8      13     -126720.4
# 9      12     -127429.4
# 10     11     -126677.9
# 11     10     -127039.5
# 12      9     -127133.2
# 13      8     -127234.1
# 14      7     -128079.5
# 15      6     -128948.9
# 16      5     -129672.9
# 17      4     -131006.8
# 18      3     -133171.8
# 19      2     -137154.4

optimal_model <- models %>%
  filter(topics == 8) %>%
  pull(LDA_model) %>%
  .[[1]]             

tidy(optimal_model, matrix = "beta")
# # A tibble: 47,960 x 3
# topic term       beta
# <int> <chr>     <dbl>
#   1     1 한국  0.000405 
# 2     2 한국  0.0000364
# 3     3 한국  0.0000353
# 4     4 한국  0.00295  
# 5     5 한국  0.0000353
# 6     6 한국  0.0000356
# 7     7 한국  0.00661  
# 8     8 한국  0.0593   
# 9     1 자랑  0.0181   
# 10     2 자랑  0.00440  
# # ... with 47,950 more rows

tidy(lda_model, matrix = "beta")
# # A tibble: 47,960 x 3
# topic term       beta
# <int> <chr>     <dbl>
#   1     1 한국  0.000405 
# 2     2 한국  0.0000364
# 3     3 한국  0.0000353
# 4     4 한국  0.00295  
# 5     5 한국  0.0000353
# 6     6 한국  0.0000356
# 7     7 한국  0.00661  
# 8     8 한국  0.0593   
# 9     1 자랑  0.0181   
# 10     2 자랑  0.00440  
# # ... with 47,950 more rows