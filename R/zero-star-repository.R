# repository data.frame
stats.df <- read.csv("data/stats.csv")

# data.frame of repositories with zero programming language
zero.language.df <- stats.df[stats.df$languages == 0, ]

# ordered according to no. of stars
ordered.zero.language.df <- zero.language.df[with(zero.language.df, order(-stars)), ]