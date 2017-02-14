mir = read.delim("C:/")
outliers <- length(boxplot(scale(t(mir)))$out)
newouts = 0

while(outliers >= newouts){
  boxplot(scale(t(mir)))
  mir <- remove_outliers(scale(t(mir)))
  newouts = length(boxplot(scale(t(mir))))
}