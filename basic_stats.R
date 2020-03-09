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
hair_dryer <- read.delim2("hair_dryer.tsv", stringsAsFactors = F, encoding = "UTF-8")
pacifier <- read.delim2("pacifier.tsv", stringsAsFactors = F, encoding = "UTF-8")
microwave <- read.delim2("microwave.tsv", stringsAsFactors = F, encoding = "UTF-8")

mean(hair_dryer$star_rating)
mean(microwave$star_rating)
mean(pacifier$star_rating)

sd(hair_dryer$star_rating)
sd(microwave$star_rating)
sd(pacifier$star_rating)

# number of observation
nrow(hair_dryer)
nrow(microwave)
nrow(pacifier)

# number of products
h <- hair_dryer$product_id %>%
  unique() %>%
  count()
p <- pacifier$product_id %>%
  unique() %>%
  count()
m <- microwave$product_id %>%
  unique() %>%
  count()

##########################
# review rating
##########################
df <- read.csv("~/Desktop/output_reorganized.csv", encoding="UTF-8", stringsAsFactors=FALSE)
hair_dryer <- df %>%
  filter(product_type=="hair_dryer")
pacifier <- df %>%
  filter(product_type=="pacifier")
microwave <- df %>%
  filter(product_type=="microwave")

mean(hair_dryer$evaluation_score)
mean(microwave$evaluation_score)
mean(pacifier$evaluation_score)

mean(hair_dryer$avg_rating)
mean(microwave$avg_rating)
mean(pacifier$avg_rating)

sd(hair_dryer$evaluation_score)
sd(microwave$evaluation_score)
sd(pacifier$evaluation_score)

sd(hair_dryer$avg_rating)
sd(microwave$avg_rating)
sd(pacifier$avg_rating)

setwd('~/Documents/GitHub/MCM2020E/')
df <- read.csv("final_score.csv", encoding="UTF-8", stringsAsFactors=FALSE)
df <- df %>%
  mutate(total_score = 0.469*avg_rating + 0.531*evaluation_score)

hair_dryer <- df %>%
  filter(product_type=="hair_dryer")
pacifier <- df %>%
  filter(product_type=="pacifier")
microwave <- df %>%
  filter(product_type=="microwave")

mean(hair_dryer$total_score)
mean(microwave$total_score)
mean(pacifier$total_score)

sd(hair_dryer$total_score)
sd(microwave$total_score)
sd(pacifier$total_score)

#################################
# something totally different
# i'm so tired and i dont know
# what i am exactly doing
#################################
# 0208
df <- read.csv("~/Documents/GitHub/MCM2020E/Sensitivity/0208.csv")

hair_dryer <- df %>%
  filter(product_type=="hair_dryer")
pacifier <- df %>%
  filter(product_type=="pacifier")
microwave <- df %>%
  filter(product_type=="microwave")

mean(hair_dryer$total_score)
mean(microwave$total_score)
mean(pacifier$total_score)

sd(hair_dryer$total_score)
sd(microwave$total_score)
sd(pacifier$total_score)

# 0802
df <- read.csv("~/Documents/GitHub/MCM2020E/Sensitivity/0802.csv")

hair_dryer <- df %>%
  filter(product_type=="hair_dryer")
pacifier <- df %>%
  filter(product_type=="pacifier")
microwave <- df %>%
  filter(product_type=="microwave")

mean(hair_dryer$total_score)
mean(microwave$total_score)
mean(pacifier$total_score)

sd(hair_dryer$total_score)
sd(microwave$total_score)
sd(pacifier$total_score)
