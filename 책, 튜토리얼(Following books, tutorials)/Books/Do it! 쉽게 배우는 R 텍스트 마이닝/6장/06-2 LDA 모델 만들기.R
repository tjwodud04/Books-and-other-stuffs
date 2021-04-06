# 전처리하기 --------------------------------------------------------------------

library(readr)
library(dplyr)

raw_news_comment <- read_csv("news_comment_parasite.csv") %>%
  mutate(id = row_number())

library(stringr)
library(textclean)

news_comment <- raw_news_comment %>%
  mutate(reply = str_replace_all(reply, "[^가-힣]", " "),
         reply = str_squish(reply)) %>%
  
  distinct(reply, .keep_all = T) %>%
  
  filter(str_count(reply, boundary("word")) >= 3)

library(tidytext)
library(KoNLP)

comment <- news_comment %>%
  unnest_tokens(input = reply,
                output = word,
                token = extractNoun,
                drop = F) %>%
  filter(str_count(word) > 1) %>%
  
  group_by(id) %>%
  distinct(word, .keep_all = T) %>%
  ungroup() %>%
  select(id, word)

comment
# # A tibble: 21,457 x 2
# id word    
# <int> <chr>   
#   1     1 우리    
# 2     1 행복    
# 3     2 시국    
# 4     2 감사    
# 5     2 하다    
# 6     2 진심    
# 7     3 우리나라
# 8     3 영화감독
# 9     3 영감    
# 10     3 봉감    
# # ... with 21,447 more rows
-------------------------------------------------------------------------

# LDA 모델 만들기
  
count_word <- comment %>%
  add_count(word) %>%
  filter(n <= 200) %>%
  select(-n)

count_word %>%
  count(word, sort = T) %>%
  print(n = 200)
# # A tibble: 6,022 x 2
# word             n
# <chr>        <int>
#   1 작품상         200
# 2 자랑           193
# 3 블랙리스트     173
# 4 조국           170
# 5 한국           165
# 6 대박           148
# 7 세계           140
# 8 수상           135
# 9 미국           128
# 10 들이           123
# 11 정치           108
# 12 역사           102
# 13 오스카         101
# 14 우리나라        96
# 15 감독상          93
# 16 진심            93
# 17 좌파            90
# 18 작품            87
# 19 한국영화        87
# 20 사람            86
# 21 배우            85
# 22 박근혜          84
# 23 국민            80
# 24 하다            80
# 25 최고            79
# 26 호감            79
# 27 우리            78
# 28 문화            75
# 29 생각            71
# 30 수상소감        68
# 31 감사            67
# 32 가족            65
# 33 나라            65
# 34 오늘            63
# 35 시상식          61
# 36 문재인          60
# 37 자랑스럽습니    60
# 38 송강호          59
# 39 소름            57
# 40 정권            54
# 41 각본상          53
# 42 감동            53
# 43 댓글            51
# 44 빨갱이          51
# 45 인정            48
# 46 소식            47
# 47 자한            47
# 48 소감            45
# 49 이미경          44
# 50 하나            43
# 51 한국인          43
# 52 대통령          42
# 53 정부            42
# 54 아카데미상      39
# 55 하게            39
# 56 위상            38
# 57 문재            37
# 58 쾌거            37
# 59 감격            36
# 60 순간            36
# 61 외국            36
# 62 전세계          36
# 63 호가            36
# 64 하면            35
# 65 눈물            34
# 66 보수            34
# 67 와우            34
# 68 현실            34
# 69 기사            33
# 70 영광            33
# 71 영화계          33
# 72 경사            32
# 73 사회            31
# 74 한국의          31
# 75 국제            30
# 76 누구            30
# 77 때문            29
# 78 마지막          29
# 79 얘기            29
# 80 인간            29
# 81 자랑스럽        29
# 82 해서            29
# 83 이번            28
# 84 훌륭            28
# 85 그네            27
# 86 기분            27
# 87 로컬            27
# 88 사람들          27
# 89 영화제          27
# 90 정도            27
# 91 뉴스            26
# 92 왜구            26
# 93 하네            26
# 94 자유            25
# 95 추카            25
# 96 기생            24
# 97 반미            24
# 98 영화상          24
# 99 이야기          24
# 100 정경            24
# 101 해요            24
# 102 내용            23
# 103 당신            23
# 104 세상            23
# 105 수준            23
# 106 위대            23
# 107 이것            23
# 108 일본            23
# 109 국위선양        22
# 110 니들            22
# 111 다시            22
# 112 중국            22
# 113 진정            22
# 114 계획            21
# 115 국가            21
# 116 네이버          21
# 117 숟가락          21
# 118 쓰레기          21
# 119 왕이            21
# 120 재미            21
# 121 정신            21
# 122 존경            21
# 123 행복            21
# 124 국격            20
# 125 문화계          20
# 126 예술            20
# 127 코로나          20
# 128 하기            20
# 129 하지            20
# 130 가슴            19
# 131 강국            19
# 132 사건            19
# 133 아시아          19
# 134 완전            19
# 135 우파            19
# 136 중요            19
# 137 최초            19
# 138 부회장          18
# 139 사실            18
# 140 소리            18
# 141 제작            18
# 142 각본            17
# 143 발전            17
# 144 스텝            17
# 145 시절            17
# 146 실화            17
# 147 올해            17
# 148 의미            17
# 149 자기            17
# 150 자신            17
# 151 천재            17
# 152 토착            17
# 153 한거            17
# 154 한번            17
# 155 해주            17
# 156 그것            16
# 157 노벨상          16
# 158 다들            16
# 159 다음            16
# 160 모두            16
# 161 박수            16
# 162 상상            16
# 163 시대            16
# 164 어디            16
# 165 여기            16
# 166 오스카상        16
# 167 최우수작품상    16
# 168 한국어          16
# 169 후보            16
# 170 고생            15
# 171 기대            15
# 172 덕분            15
# 173 발표            15
# 174 상은            15
# 175 예상            15
# 176 월드컵          15
# 177 응원            15
# 178 이해            15
# 179 조선            15
# 180 한류            15
# 181 해외            15
# 182 까지            14
# 183 대한            14
# 184 리스            14
# 185 모습            14
# 186 바이러스        14
# 187 생중계          14
# 188 여자            14
# 189 예전            14
# 190 이거            14
# 191 이름            14
# 192 장면            14
# 193 표현            14
# 194 하신            14
# 195 한국적          14
# 196 한마디          14
# 197 황금종려상      14
# 198 김연아          13
# 199 만큼            13
# 200 방탄            13
# # ... with 5,822 more rows

stopword <- c("들이", "하다", "하게", "하면", "해서", "이번", "하네",
              "해요", "이것", "니들", "하기", "하지", "한거", "해주",
              "그것", "어디", "여기", "까지", "이거", "하신", "만큼")

count_word <- count_word %>%
  filter(!word %in% stopword) %>%
  mutate(word = recode(word,
                       "자랑스럽습니" = "자랑",
                       "자랑스럽" = "자랑",
                       "자한" = "자유한국당",
                       "문재" = "문재인",
                       "한국의" = "한국",
                       "그네" = "박근혜",
                       "추카" = "축하",
                       "정경" = "정경심",
                       "방탄" = "방탄소년단"))

stopword <- tibble(word = c("들이", "하다", "하게", "하면", "해서", "이번", "하네",
                            "해요", "이것", "니들", "하기", "하지", "한거", "해주",
                            "그것", "어디", "여기", "까지", "이거", "하신", "만큼"))

library(readr)

write_csv(stopword, "stopword.csv")

stopword <- read_csv("stopword.csv")

count_word <- count_word %>%
  filter(!word %in% stopword$word)

count_word <- count_word %>%
  anti_join(stopword, by = "word")

count_word_doc <- count_word %>%
  count(id, word, sort = T)

count_word_doc
# # A tibble: 17,592 x 3
# id word           n
# <int> <chr>      <int>
#   1    35 한국           2
# 2   206 자랑           2
# 3   566 자랑           2
# 4   578 자랑           2
# 5   598 자랑           2
# 6  1173 한국           2
# 7  1599 한국           2
# 8  1762 한국           2
# 9  2240 한국           2
# 10  2307 방탄소년단     2
# # ... with 17,582 more rows

install.packages("tm")

dtm_comment <- count_word_doc %>%
  cast_dtm(document = id, term = word, value = n)

dtm_comment
# <<DocumentTermMatrix (documents: 3203, terms: 5995)>>
#   Non-/sparse entries: 17592/19184393
# Sparsity           : 100%
# Maximal term length: 35
# Weighting          : term frequency (tf)

as.matrix(dtm_comment)[1:8, 1:8]
# Terms
# Docs   한국 자랑 방탄소년단 박근혜 우리 행복 감사 시국
# 35      2    0          0      0    0    0    0    0
# 206     0    2          0      0    0    0    0    0
# 566     1    2          0      0    0    0    0    0
# 578     0    2          0      0    0    0    0    0
# 598     0    2          0      0    0    0    0    0
# 1173    2    0          0      0    0    0    0    0
# 1599    2    1          0      0    0    0    0    0
# 1762    2    0          0      0    0    0    0    0

install.packages("topicmodels")
library(topicmodels)

lda_model <- LDA(dtm_comment,
                 k = 8,
                 method = "Gibbs",
                 control = list(seed = 1234))
lda_model
# A LDA_Gibbs topic model with 8 topics.

glimpse(lda_model)
# Formal class 'LDA_Gibbs' [package "topicmodels"] with 16 slots
# ..@ seedwords      : NULL
# ..@ z              : int [1:17604] 8 8 4 3 7 4 3 1 1 1 ...
# ..@ alpha          : num 6.25
# ..@ call           : language LDA(x = dtm_comment, k = 8, method = "Gibbs", control = list(seed = 1234))
# ..@ Dim            : int [1:2] 3203 5995
# ..@ control        :Formal class 'LDA_Gibbscontrol' [package "topicmodels"] with 14 slots
# ..@ k              : int 8
# ..@ terms          : chr [1:5995] "한국" "자랑" "방탄소년단" "박근혜" ...
# ..@ documents      : chr [1:3203] "35" "206" "566" "578" ...
# ..@ beta           : num [1:8, 1:5995] -7.81 -10.22 -10.25 -5.83 -10.25 ...
# ..@ gamma          : num [1:3203, 1:8] 0.151 0.15 0.11 0.114 0.11 ...
# ..@ wordassignments:List of 5
# .. ..$ i   : int [1:17592] 1 1 1 1 1 1 1 1 1 1 ...
# .. ..$ j   : int [1:17592] 1 98 99 100 101 102 103 104 105 106 ...
# .. ..$ v   : num [1:17592] 8 4 3 7 4 3 7 2 8 6 ...
# .. ..$ nrow: int 3203
# .. ..$ ncol: int 5995
# .. ..- attr(*, "class")= chr "simple_triplet_matrix"
# ..@ loglikelihood  : num -126429
# ..@ iter           : int 2000
# ..@ logLiks        : num(0) 
# ..@ n              : int 17604