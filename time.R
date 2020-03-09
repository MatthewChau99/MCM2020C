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
# time dependency
##########################
setwd('~/Documents/GitHub/MCM2020E/')
hair_dryer <- read.delim2("hair_dryer.tsv", stringsAsFactors = F, encoding = "UTF-8")
pacifier <- read.delim2("pacifier.tsv", stringsAsFactors = F, encoding = "UTF-8")
microwave <- read.delim2("microwave.tsv", stringsAsFactors = F, encoding = "UTF-8")

hair_dryer$review_date <- as.Date(hair_dryer$review_date, format = "%m/%d/%Y")
hair_dryer <- hair_dryer %>%
  filter(review_date >= "2012-01-01")
pacifier$review_date <- as.Date(pacifier$review_date, format = "%m/%d/%Y")
pacifier <- pacifier %>%
  filter(review_date >= "2012-01-01")
microwave$review_date <- as.Date(microwave$review_date, format = "%m/%d/%Y")
microwave <- microwave %>%
  filter(review_date >= "2012-01-01")

setwd('~/Documents/GitHub/MCM2020E/Time')
for i in 1:12{
  for j in 1:12{
    
  }
}

  

