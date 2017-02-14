#This function is currently incomplete/not working. 
#This function should take a properly formatted data frame containing global
# network statistics and associated label variables and plot the size of 
# each network (nodes x edges) as a line plot labeled with correlation values.
plotNetworkSizes <- function(data){
  group <- factor(data$Expression.Filter)
  for(item in levels(group)){
    print i
    #plot(~Nodes+Edges, data=data, subset = item, main=item)
  }
}


x <- read.delim("C:/users/eli/desktop/coexpression_networks/
                network_summary_statistics_tsv.txt", stringsAsFactors=TRUE)

#Generate an x-y line plot for variables Nodes & Edges in data frame "x" 
#   by a subset (5cpm3) of the grouping variable "Expression.Filter"
plot(subset(x, Expression.Filter=="5cpm3", select=c(Nodes,Edges)), type="l",
     col="orange", lwd=2, main="Network Size (5cpm3)")
#Add labels to the points indicating the values for the expression correlation
#   associated with each node-edge pair plotted above.
#   Note: these values are indicated in the grouping variable "Corr..Min"
text(subset(x, Expression.Filter=="5cpm3", select=Nodes)[1:6,1], 
     y = subset(x, Expression.Filter=="5cpm3", select=Edges)[1:6,1], 
     labels = subset(x, Expression.Filter=="5cpm3", select=Corr..Min)[1:6,1], 
     col="blue")