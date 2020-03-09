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
df <- read.csv("~/Desktop/output_reorganized.csv", encoding="UTF-8", stringsAsFactors=FALSE)
df<- unique(df)
hair_dryer <- df %>%
  filter(product_type=="hair_dryer")
pacifier <- df %>%
  filter(product_type=="pacifier")
microwave <- df %>%
  filter(product_type=="microwave")

library("ggpubr")
ggscatter(hair_dryer, x = "avg_rating", y = "evaluation_score", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Average Star Rating of Hair Dryer", ylab = "Average Review Rating of Hair Dryer", 
          color = "red3")

ggscatter(microwave, x = "avg_rating", y = "evaluation_score", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Average Star Rating of Microwave", ylab = "Average Review Rating of Microwave",
          color = "darkorange2")

ggscatter(pacifier, x = "avg_rating", y = "evaluation_score", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Average Star Rating of Pacifier", ylab = "Average Review Rating of Pacifier",
          color = "dodgerblue4")



