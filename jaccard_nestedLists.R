#This function finds Jaccard indices for each pair of sublists within two named vectors
#The output is a dataframe containing all statistics relevant to the computation
#Example named vector: list1 = list(one=c(1,2,3), two=c(2,3,4))

jaccards <- function(list1, list2){
	sapply(list1, function(x){
		jacc <- sapply(list1, function(x) sapply(list2, function(y) length(intersect(x,y))/length(union(x,y))))
		jacclong <- melt(jacc)
		intersects <- sapply(list1, function(x) sapply(list2, function(y) length(intersect(x,y))))
		unions <- sapply(list1, function(x) sapply(list2, function(y) length(union(x,y))))
		len1 <- t(as.data.frame(lapply(list1, length)))
		len2 <- t(as.data.frame(lapply(list2, length)))
		cbind(jacclong, List1=rep(len1, length(len2)), List2=rep(len2, length(len1)), Intersect=melt(intersects)[,3], Union=melt(unions)[,3])
	})
}
