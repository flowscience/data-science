### Partial correlation coefficient
### From formulas in Sheskin, 3e
### a,b=variables to be correlated, c=variable to be partialled out of both
pcor = function(a,b,c)
{
  (cor(a,b)-cor(a,c)*cor(b,c))/sqrt((1-cor(a,c)^2)*(1-cor(b,c)^2))
}
### end of script