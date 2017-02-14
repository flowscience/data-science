# Program to find the
# factors of a number

get_factors <- function(x) {
  #print(paste("The factors of",x,"are:"))
  temp = list()
  for(i in 1:x) {
    if((x %% i) == 0) {
      temp[length(temp)+1L] <- i
    }
  }
  return(temp)
}