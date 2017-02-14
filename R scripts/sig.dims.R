#dmat = result matrix from Wilks lambda tests
# 	of canonical dimension significance
#CCA = results file from CCA
#dims = the number of dimensions to be retained
# 	selected based on eigenvalues/scree plot
#load = minimum loading on CC's to retain variables

sig.dims <- function(dmat, cca, dims, load){
  #Initialize vector of high eigenvalue dimensions
  dims = c(1:dims)
  
  #Select dimensions which p < 0.05
  sigdims <- which(dmat[,5] < 0.05)
  
  #Intersect significant and selected dimensions
  keep <- intersect(dims, sigdims)
    
  #Subset the CCA results
  lapply(cca$scores, function(x) subset(x, x[,1] >= load, select=keep))
}