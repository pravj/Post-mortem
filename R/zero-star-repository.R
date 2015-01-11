# repository data.frame
stats.df <- read.csv("data/stats.csv")

# data.frame of repositories with zero programming language
zero.language.df <- stats.df[stats.df$languages == 0, ]
zero.language.df$index <- 1:nrow(zero.language.df)

# ordered according to no. of stars
ordered.zero.language.df <- zero.language.df[with(zero.language.df, order(-stars)), ]

# render a graph for repositories with 0 stars
gplot <- ggplot(zero.language.df, aes(y = stars, x = index))
gplot <- gplot + labs(x = "Repository Index", y = "GitHub Stars", title = "Repositories having >= 500 stars without a programming language")
gplot <- gplot + geom_point()