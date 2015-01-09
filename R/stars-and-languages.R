# load required libraries
library("ggplot2")

# repository dataset
stats.df <- read.csv("data/stats.csv")

# create a new point graph
gplot <- ggplot(stats.df, aes(x = languages, y = stars))
gplot <- gplot + labs(x = "No. of Programming Languages", y = "No. of GitHub Stars")
gplot <- gplot + geom_point()