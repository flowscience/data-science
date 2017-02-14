#This function takes the results of CCA
# and tests independence of successive dimensions
# using Wilks's Lambda.

dim.test <- function(res){
  ev = (1 - res$cor^2)
  n = dim(data1)[1]
  p = length(data1)
  q = length(data2)
  k = min(p, q)
  m = n - 3/2 - (p + q)/2
  w = rev(cumprod(rev(ev)))
  
  # initialize
  d1 = d2 = f <- vector("numeric", k)
  
  for (i in 1:k) {
    s = sqrt((p^2 * q^2 - 4)/(p^2 + q^2 - 5))
    si = 1/s
    d1[i] = p * q
    d2[i] = m * s - p * q/2 + 1
    r = (1 - w[i]^si)/w[i]^si
    f[i] = r * d2[i]/d1[i]
    p = p - 1
    q = q - 1
  }
  
  pv = pf(f, d1, d2, lower.tail = FALSE)
  (dmat <- cbind(WilksL = w, F = f, df1 = d1, df2 = d2, p = pv))
}
