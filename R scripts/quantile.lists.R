quantile.lists <- function(data){
  
  contrasts <- colnames(logFC)
  DE.quantiles <- list()
  
  #Make lists of DE genes and aggregate
  for(stage in contrasts){
    print(stage)
    #DEstage <- subset(logFC, stage >= quantile(logFC[,stage])[4] | stage <= quantile(logFC[,stage])[2], select=row.names(logFC))
    #DEstage <- subset(lfc, lfc$E32 <= quantile(lfc$E32)[2], select=Clone)
    DEstage <- subset(lfc, lfc$stage <= quantile(lfc$stage)[2], select=Clone)
    print(DEstage)
    DE.quantiles <- append(DE.quantiles, DEstage)
  }
  
  DE.quantiles
}