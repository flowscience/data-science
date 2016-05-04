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