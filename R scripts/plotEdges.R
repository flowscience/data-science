plotEdges <- function(cors, steps = 100){
  library(igraph)
  g <- graph.data.frame(cors, directed=F)
  g <- simplify(g, edge.attr.comb="sum", remove.loops=FALSE)
  DF <- get.data.frame(g)
  data <- data.frame()
  for(i in seq(from = 0, to = 1, by = ((1-0)/(steps)))){
    edges <- length(t(unique(subset(DF[1:2], DF[,3] > i)))[1,])
    data <- rbind(data, c(i, edges))
  }
  colnames(data) <- c("Correlation Coefficient", "Edges")
  plot(data, main="Edge Distribution", col="blue", pch=20, lwd=0.7)
  abline(v=0.6, col="red", lty=2, lwd=2)
  #return(data)
  
}