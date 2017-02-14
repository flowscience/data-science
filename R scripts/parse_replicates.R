parse_replicates <- function(data_in, reps){
  group_data = c()
  start=1
  end = reps[1]
  for(i in seq(1,length(reps))){
    group_data[[length(group_data)+1]] <- data_in[start:end]
    start = end+1
    end = end + reps[i]
  }
  return(group_data)
}