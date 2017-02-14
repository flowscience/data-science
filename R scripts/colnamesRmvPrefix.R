# Handy function to strip prefixes from the column names (of cosmetic value only!) since the reshape process will add a prefix:
colnamesRmvPrefix <- function(df, prefix) {
  names <- colnames(df)
  indices <- (substr(names,1,nchar(prefix))==prefix)
  names[indices] <- substr(names[indices], nchar(prefix)+1, nchar(names[indices]))
  return(names)
}