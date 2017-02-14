gse <- read.delim("C:/Users/Eli/Desktop/otx_targets/gse6308_otxTargs_clones-JGI.txt", row.names="Clone", stringsAsFactors=FALSE)
gse2 <- gse[,3:16]
gse3 <- sapply(gse2, as.numeric)
rownames(gse3) <- row.names(gse2)

targets <- read.delim("C:/Users/Eli/Desktop/otx_targets/gse6308_limma_sample_table_E16-ITB.txt", stringsAsFactors=FALSE)
targs <- targets[,3:5]
design <- modelMatrix(targs, ref="FE")

fit <- lmFit(gse3, design)

contrast.matrix <- makeContrasts(levels=design, E16, E32, E64, EG, LG, EN, ITB, E32-E16, E64-E32, EG-E64, LG-EG, EN-LG, ITB-EN)
fit2 <- contrasts.fit(fit, contrast.matrix)
fit2 <- eBayes(fit2)
fit <- eBayes(fit)
topTable(fit2, coef=1, adjust="BH")
topTable(fit2, coef=2, adjust="BH")
topTable(fit2, coef=3, adjust="BH")
results <- decideTests(fit, method="global")
length(which(results == 1))
results2 <- decideTests(fit2, method="global")
length(which(results2 == 1))

arrayw <- arrayWeights(gse3)
barplot(arrayw, xlab="Array", ylab="Weight", col="white", las=2)

fitw <- lmFit(gse3, design, weights=arrayw)
fitw2 <- contrasts.fit(fitw, contrast.matrix)
fitw2 <- eBayes(fitw2)
fitw <- eBayes(fitw)


topTable(fitw, coef=1, adjust="BH")
resultsw <- decideTests(fitw, method="global")
length(which(resultsw == 1))
resultsw2 <- decideTests(fitw2, method="global")
length(which(resultsw2 == 1))

fitd <- topTable(fit, n=length(rownames(gse3)))
fit2d <- topTable(fit2, n=length(rownames(gse3)))
fitwd <- topTable(fitw, n=length(rownames(gse3)))
fitw2d <- topTable(fitw2, n=length(rownames(gse3)))
write.table(fitd, "C:/users/eli/desktop/limma_gse6308_E32-EN_topTable.txt", quote=FALSE, sep='\t')
write.table(fit2d, "C:/users/eli/desktop/limma_gse6308_E32-EN_topTable_fitContrast.txt", quote=FALSE, sep='\t')
write.table(fitwd, "C:/users/eli/desktop/limma_gse6308_E32-EN_topTable_weughted.txt", quote=FALSE, sep='\t')
write.table(fitw2d, "C:/users/eli/desktop/limma_gse6308_E32-EN_topTable_weughted_fitContrasts.txt", quote=FALSE, sep='\t')