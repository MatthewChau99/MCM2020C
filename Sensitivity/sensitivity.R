############################
# clean environment
# load packages
############################
# remove objects
rm(list=ls())
# detach all libraries
detachAllPackages <- function() {
  basic.packages <- c("package:stats","package:graphics","package:grDevices","package:utils","package:datasets","package:methods","package:base")
  package.list <- search()[ifelse(unlist(gregexpr("package:",search()))==1,TRUE,FALSE)]
  package.list <- setdiff(package.list,basic.packages)
  if (length(package.list)>0)  for (package in package.list) detach(package, character.only=TRUE)
}
detachAllPackages()

# load libraries
pkgTest <- function(pkg){
  new.pkg <- pkg[!(pkg %in% installed.packages()[, "Package"])]
  if (length(new.pkg)) 
    install.packages(new.pkg, dependencies = TRUE)
  sapply(pkg, require, character.only = TRUE)
}

lapply(c("stringr", "dplyr", "plyr", "tidyverse", "rvest", "zoo", "XML", "tidyr", "lubridate", "readr"), pkgTest)

##########################
# star rating
##########################
setwd('~/Documents/GitHub/MCM2020E/')
df <- read.csv("final_score.csv", encoding="UTF-8", stringsAsFactors=FALSE)
df_a <- df %>%
  mutate(total_score = 0.469*avg_rating + 0.531*evaluation_score)
# write.csv(df_a, "true_final_score.csv")

setwd('~/Documents/GitHub/MCM2020E/Sensitivity/')
df_b <- df %>%
  mutate(total_score = 0.2*avg_rating + 0.8*evaluation_score)
write.csv(df_b, "0208.csv")
df_c <- df %>%
  mutate(total_score = 0.3*avg_rating + 0.7*evaluation_score)
write.csv(df_c, "0307.csv")
df_d <- df %>%
  mutate(total_score = 0.7*avg_rating + 0.3*evaluation_score)
write.csv(df_d, "0703.csv")
df_e <- df %>%
  mutate(total_score = 0.8*avg_rating + 0.2*evaluation_score)
write.csv(df_e, "0802.csv")
