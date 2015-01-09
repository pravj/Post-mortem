# repository dataset
stats.df <- read.csv("data/stats.csv")

# dataset ordered according to languages used
language.ordered.df <- stats.df[with(stats.df, order(-languages)), ]
