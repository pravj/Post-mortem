# load required libraries
library("ggplot2")

stats.df <- read.csv("data/stats.csv")

gplot <- ggplot(stats.df, aes(x = languages, y = stars))
gplot <- gplot + labs(x = "No. of Programming Languages", y = "No. of GitHub Stars")
gplot <- gplot + geom_point()
