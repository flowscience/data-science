library(energy)
library(combinat)
source("C:/users/eli/desktop/r_scripts/parse_replicates.r")
x_file <- read.table()
y_file <- read.table()

a = c("a", "b", "c")
b = c(1,2,3)
x = c('xa1','xa2','xa3','xb1','xb2','xb3','xc1','xc2','xc3','xd1','xd2','xd3')
y = c('ya1','ya2','ya3','yb1','yb2','yb3','yc1','yc2','yc3','yd1','yd2','yd3')

#One liner to get 6 combinations for a 3-replicate group
combinations <- expand.grid(permn(x[1:3]),permn(y[1:3]))[seq(1,36,6),]
x <- as.numeric(unlist(list(combinations[1])))
y <- as.numeric(unlist(list(combinations[2])))

groupComb <- function(x_in, y_in, reps){
  #x_in and y_in should be arrays
  xparse <- parse_replicates(x, reps)
  yparse <- parse_replicates(y, reps)
  xperm <- lapply(xparse, permn)
  yperm <- lapply(yparse, permn)
  #Need to adjust parameter on next line to accept all inputs
  #combinations <- expand.grid(permn(x[1:3]),permn(y[1:3]))[seq(1,36,6),]
  combinations <- lapply(xperm, expand.grid, yperm)
  x <- as.numeric(unlist(list(combinations[1])))
  y <- as.numeric(unlist(list(combinations[2])))
}

groupCor <- function(x_in, y_in, method){
  apply(x_in, 1, parse_replicates)
  apply(y_in, 1, parse_replicates)
  
  return(dcor(x,y))
}
