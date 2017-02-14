#This function takes a correlation matrix, separates
#each row into a numeric vector, runs p.adjust on the
#vectors, then rbind them back into a new matrix.

adjust_cor <- function(cor){
  out <- data.frame()
  for(i in 1:nrow(cor)){
    vec <- lapply(cor, 1)
    vec <- p.adjust(vec, method="holm")
    out <- rbind(out, vec)    
  }
  
}