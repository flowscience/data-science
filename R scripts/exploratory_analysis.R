#Produce a histogram for each variable in a dataset.
all.hist <- function(x){
  sapply(names(x), function(i)hist(x[,i], main = i,
      xlab="Value", col="lightblue")) 
}

#Produce a kernel density plot w/normal curve for each
#variable in a dataset.
all.density.plot <- function(x){
  sapply(names(x), function(i)plot(density(x[,i]),
        main = i, xlab="Value", col="red", lwd=2))  
}

#Produce a pairwise scatterplot matrix with histograms
#on the diagonal and correlation statistics in the 
#upper panel



