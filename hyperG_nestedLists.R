hyperG <- function(list1, list2){
		library(reshape2)
		uni1 <- sum(sapply(list1, length))
		uni2 <- sum(sapply(list1, length))
		universe <- max(c(uni1,uni2))
		universe=1904
		intersects <- sapply(list1, function(x) sapply(list2, function(y) length(intersect(x,y))))
		len1 <- t(as.data.frame(lapply(list1, length)))
		len2 <- t(as.data.frame(lapply(list2, length)))
		out <- cbind(melt(intersects), len_Var1=rep(len1, each=length(len2)), len_Var2=rep(len2, times=length(len1)))
		out <- subset(out, len_Var1 >= 5 & len_Var2 >=5)
		pvalue <- apply(out[,3:5], 1, function(x) 1-phyper(x[1],x[2],universe-x[2],x[3]))
		FDR <- p.adjust(pvalue, method='fdr')
		out <- cbind(out, pvalue, FDR)
		colnames(out) <- c('Var1', 'Var2', 'Overlap', 'len_Var1', 'len_Var2', 'pvalue', 'FDR')
		out
}

#Probability of getting 100 or more white balls in a sample of size 400 from an urn 
#with 3000 white balls and 12000 black balls
# white balls retrieved = overlap-1 (e.g. 100 or more)
# total white balls = cluster size
# total black balls = universe - cluster size
# total draws = category size
#cluster/category size are interchangable, but universe must always substact the former
#1-phyper(white balls, total white balls, black balls, size)
#1-phyper(99, 3000, 12000, 400)
#1-phyper(overlap-1, cluster size, universe-cluster size, category size)
