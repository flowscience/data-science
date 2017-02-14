plotNodes <- function(cors, steps = 100){
  xvals <- seq(from = 1, to = 0, by = ((0-1)/(steps)))
  data <- data.frame()
  for(i in seq(from = 0, to = 1, by = ((1-0)/(steps)))){
    nodes1 <- c(unique(subset(cors[,1], cors[,3] >= i)))
    nodes2 <- c(unique(subset(cors[,2], cors[,3] >= i)))
    nodes <- length(union(nodes1, nodes2))
    data <- rbind(data, c(i, nodes))
  }
  colnames(data) <- c("Correlation Coefficient", "Nodes")
  plot(data, main="Node Distribution", col="blue", pch=20, lwd=0.7)
  abline(v=0.8, col="red", lty=2, lwd=2)
  #return(data)
  
}