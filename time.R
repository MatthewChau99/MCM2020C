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
# 201508
h201508 <- hair_dryer %>%
  filter(review_date < "2015-08-01")
write.csv(h201508, "h201508.csv")
p201508 <- pacifier %>%
  filter(review_date < "2015-08-01")
write.csv(p201508, "p201508.csv")
m201508 <- microwave %>%
  filter(review_date < "2015-08-01")
write.csv(m201508, "m201508.csv")

# 201507
h201507 <- hair_dryer %>%
  filter(review_date < "2015-07-01")
write.csv(h201507, "h201507.csv")
p201507 <- pacifier %>%
  filter(review_date < "2015-07-01")
write.csv(p201507, "p201507.csv")
m201507 <- microwave %>%
  filter(review_date < "2015-07-01")
write.csv(m201507, "m201507.csv")

# 201507
h201507 <- hair_dryer %>%
  filter(review_date < "2015-07-01")
write.csv(h201507, "h201507.csv")
p201507 <- pacifier %>%
  filter(review_date < "2015-07-01")
write.csv(p201507, "p201507.csv")
m201507 <- microwave %>%
  filter(review_date < "2015-07-01")
write.csv(m201507, "m201507.csv")

# 201506
h201506 <- hair_dryer %>%
  filter(review_date < "2015-06-01")
write.csv(h201506, "h201506.csv")
p201506 <- pacifier %>%
  filter(review_date < "2015-06-01")
write.csv(p201506, "p201506.csv")
m201506 <- microwave %>%
  filter(review_date < "2015-06-01")
write.csv(m201506, "m201506.csv")

# 201505
h201505 <- hair_dryer %>%
  filter(review_date < "2015-05-01")
write.csv(h201505, "h201505.csv")
p201505 <- pacifier %>%
  filter(review_date < "2015-05-01")
write.csv(p201505, "p201505.csv")
m201505 <- microwave %>%
  filter(review_date < "2015-05-01")
write.csv(m201505, "m201505.csv")

# 201504
h201504 <- hair_dryer %>%
  filter(review_date < "2015-04-01")
write.csv(h201504, "h201504.csv")
p201504 <- pacifier %>%
  filter(review_date < "2015-04-01")
write.csv(p201504, "p201504.csv")
m201504 <- microwave %>%
  filter(review_date < "2015-04-01")
write.csv(m201504, "m201504.csv")

# 201503
h201503 <- hair_dryer %>%
  filter(review_date < "2015-03-01")
write.csv(h201503, "h201503.csv")
p201503 <- pacifier %>%
  filter(review_date < "2015-03-01")
write.csv(p201503, "p201503.csv")
m201503 <- microwave %>%
  filter(review_date < "2015-03-01")
write.csv(m201503, "m201503.csv")

# 201502
h201502 <- hair_dryer %>%
  filter(review_date < "2015-02-01")
write.csv(h201502, "h201502.csv")
p201502 <- pacifier %>%
  filter(review_date < "2015-02-01")
write.csv(p201502, "p201502.csv")
m201502 <- microwave %>%
  filter(review_date < "2015-02-01")
write.csv(m201502, "m201502.csv")

# 201501
h201501 <- hair_dryer %>%
  filter(review_date < "2015-01-01")
write.csv(h201501, "h201501.csv")
p201501 <- pacifier %>%
  filter(review_date < "2015-01-01")
write.csv(p201501, "p201501.csv")
m201501 <- microwave %>%
  filter(review_date < "2015-01-01")
write.csv(m201501, "m201501.csv")

# 201412
h201412 <- hair_dryer %>%
  filter(review_date < "2014-12-01")
write.csv(h201412, "h201412.csv")
p201412 <- pacifier %>%
  filter(review_date < "2014-12-01")
write.csv(p201412, "p201412.csv")
m201412 <- microwave %>%
  filter(review_date < "2014-12-01")
write.csv(m201412, "m201412.csv")

# 201411
h201411 <- hair_dryer %>%
  filter(review_date < "2014-11-01")
write.csv(h201411, "h201411.csv")
p201411 <- pacifier %>%
  filter(review_date < "2014-11-01")
write.csv(p201411, "p201411.csv")
m201411 <- microwave %>%
  filter(review_date < "2014-11-01")
write.csv(m201411, "m201411.csv")

# 201410
h201410 <- hair_dryer %>%
  filter(review_date < "2014-10-01")
write.csv(h201410, "h201410.csv")
p201410 <- pacifier %>%
  filter(review_date < "2014-10-01")
write.csv(p201410, "p201410.csv")
m201410 <- microwave %>%
  filter(review_date < "2014-10-01")
write.csv(m201410, "m201410.csv")

# 201409
h201409 <- hair_dryer %>%
  filter(review_date < "2014-09-01")
write.csv(h201409, "h201409.csv")
p201409 <- pacifier %>%
  filter(review_date < "2014-09-01")
write.csv(p201409, "p201409.csv")
m201409 <- microwave %>%
  filter(review_date < "2014-09-01")
write.csv(m201409, "m201409.csv")

# 201408
h201408 <- hair_dryer %>%
  filter(review_date < "2014-08-01")
write.csv(h201408, "h201408.csv")
p201408 <- pacifier %>%
  filter(review_date < "2014-08-01")
write.csv(p201408, "p201408.csv")
m201408 <- microwave %>%
  filter(review_date < "2014-08-01")
write.csv(m201408, "m201408.csv")

# 201407
h201407 <- hair_dryer %>%
  filter(review_date < "2014-07-01")
write.csv(h201407, "h201407.csv")
p201407 <- pacifier %>%
  filter(review_date < "2014-07-01")
write.csv(p201407, "p201407.csv")
m201407 <- microwave %>%
  filter(review_date < "2014-07-01")
write.csv(m201407, "m201407.csv")

# 201406
h201406 <- hair_dryer %>%
  filter(review_date < "2014-06-01")
write.csv(h201406, "h201406.csv")
p201406 <- pacifier %>%
  filter(review_date < "2014-06-01")
write.csv(p201406, "p201406.csv")
m201406 <- microwave %>%
  filter(review_date < "2014-06-01")
write.csv(m201406, "m201406.csv")

#########################
# 201405
h201405 <- hair_dryer %>%
  filter(review_date < "2014-05-01")
write.csv(h201405, "h201405.csv")
p201405 <- pacifier %>%
  filter(review_date < "2014-05-01")
write.csv(p201405, "p201405.csv")
m201405 <- microwave %>%
  filter(review_date < "2014-05-01")
write.csv(m201405, "m201405.csv")

# 201404
h201404 <- hair_dryer %>%
  filter(review_date < "2014-04-01")
write.csv(h201404, "h201404.csv")
p201404 <- pacifier %>%
  filter(review_date < "2014-04-01")
write.csv(p201404, "p201404.csv")
m201404 <- microwave %>%
  filter(review_date < "2014-04-01")
write.csv(m201404, "m201404.csv")

# 201403
h201403 <- hair_dryer %>%
  filter(review_date < "2014-03-01")
write.csv(h201403, "h201403.csv")
p201403 <- pacifier %>%
  filter(review_date < "2014-03-01")
write.csv(p201403, "p201403.csv")
m201403 <- microwave %>%
  filter(review_date < "2014-03-01")
write.csv(m201403, "m201403.csv")

# 201402
h201402 <- hair_dryer %>%
  filter(review_date < "2014-02-01")
write.csv(h201402, "h201402.csv")
p201402 <- pacifier %>%
  filter(review_date < "2014-02-01")
write.csv(p201402, "p201402.csv")
m201402 <- microwave %>%
  filter(review_date < "2014-02-01")
write.csv(m201402, "m201402.csv")

# 201401
h201401 <- hair_dryer %>%
  filter(review_date < "2014-01-01")
write.csv(h201401, "h201401.csv")
p201401 <- pacifier %>%
  filter(review_date < "2014-01-01")
write.csv(p201401, "p201401.csv")
m201401 <- microwave %>%
  filter(review_date < "2014-01-01")
write.csv(m201401, "m201401.csv")


# 201312
h201312 <- hair_dryer %>%
  filter(review_date < "2013-12-01")
write.csv(h201312, "h201312.csv")
p201312 <- pacifier %>%
  filter(review_date < "2013-12-01")
write.csv(p201312, "p201312.csv")
m201312 <- microwave %>%
  filter(review_date < "2013-12-01")
write.csv(m201312, "m201312.csv")

# 201311
h201311 <- hair_dryer %>%
  filter(review_date < "2013-11-01")
write.csv(h201311, "h201311.csv")
p201311 <- pacifier %>%
  filter(review_date < "2013-11-01")
write.csv(p201311, "p201311.csv")
m201311 <- microwave %>%
  filter(review_date < "2013-11-01")
write.csv(m201311, "m201311.csv")

# 201310
h201310 <- hair_dryer %>%
  filter(review_date < "2013-10-01")
write.csv(h201310, "h201310.csv")
p201310 <- pacifier %>%
  filter(review_date < "2013-10-01")
write.csv(p201310, "p201310.csv")
m201310 <- microwave %>%
  filter(review_date < "2013-10-01")
write.csv(m201310, "m201310.csv")

# 201309
h201309 <- hair_dryer %>%
  filter(review_date < "2013-09-01")
write.csv(h201309, "h201309.csv")
p201309 <- pacifier %>%
  filter(review_date < "2013-09-01")
write.csv(p201309, "p201309.csv")
m201309 <- microwave %>%
  filter(review_date < "2013-09-01")
write.csv(m201309, "m201309.csv")

# 201308
h201308 <- hair_dryer %>%
  filter(review_date < "2013-08-01")
write.csv(h201308, "h201308.csv")
p201308 <- pacifier %>%
  filter(review_date < "2013-08-01")
write.csv(p201308, "p201308.csv")
m201308 <- microwave %>%
  filter(review_date < "2013-08-01")
write.csv(m201308, "m201308.csv")

# 201307
h201307 <- hair_dryer %>%
  filter(review_date < "2013-07-01")
write.csv(h201307, "h201307.csv")
p201307 <- pacifier %>%
  filter(review_date < "2013-07-01")
write.csv(p201307, "p201307.csv")
m201307 <- microwave %>%
  filter(review_date < "2013-07-01")
write.csv(m201307, "m201307.csv")

# 201306
h201306 <- hair_dryer %>%
  filter(review_date < "2013-06-01")
write.csv(h201306, "h201306.csv")
p201306 <- pacifier %>%
  filter(review_date < "2013-06-01")
write.csv(p201306, "p201306.csv")
m201306 <- microwave %>%
  filter(review_date < "2013-06-01")
write.csv(m201306, "m201306.csv")

#########################
# 201305
h201305 <- hair_dryer %>%
  filter(review_date < "2013-05-01")
write.csv(h201305, "h201305.csv")
p201305 <- pacifier %>%
  filter(review_date < "2013-05-01")
write.csv(p201305, "p201305.csv")
m201305 <- microwave %>%
  filter(review_date < "2013-05-01")
write.csv(m201305, "m201305.csv")

# 201304
h201304 <- hair_dryer %>%
  filter(review_date < "2013-04-01")
write.csv(h201304, "h201304.csv")
p201304 <- pacifier %>%
  filter(review_date < "2013-04-01")
write.csv(p201304, "p201304.csv")
m201304 <- microwave %>%
  filter(review_date < "2013-04-01")
write.csv(m201304, "m201304.csv")

# 201303
h201303 <- hair_dryer %>%
  filter(review_date < "2013-03-01")
write.csv(h201303, "h201303.csv")
p201303 <- pacifier %>%
  filter(review_date < "2013-03-01")
write.csv(p201303, "p201303.csv")
m201303 <- microwave %>%
  filter(review_date < "2013-03-01")
write.csv(m201303, "m201303.csv")

# 201302
h201302 <- hair_dryer %>%
  filter(review_date < "2013-02-01")
write.csv(h201302, "h201302.csv")
p201302 <- pacifier %>%
  filter(review_date < "2013-02-01")
write.csv(p201302, "p201302.csv")
m201302 <- microwave %>%
  filter(review_date < "2013-02-01")
write.csv(m201302, "m201302.csv")

# 201301
h201301 <- hair_dryer %>%
  filter(review_date < "2013-01-01")
write.csv(h201301, "h201301.csv")
p201301 <- pacifier %>%
  filter(review_date < "2013-01-01")
write.csv(p201301, "p201301.csv")
m201301 <- microwave %>%
  filter(review_date < "2013-01-01")
write.csv(m201301, "m201301.csv")


# 201212
h201212 <- hair_dryer %>%
  filter(review_date < "2012-12-01")
write.csv(h201212, "h201212.csv")
p201212 <- pacifier %>%
  filter(review_date < "2012-12-01")
write.csv(p201212, "p201212.csv")
m201212 <- microwave %>%
  filter(review_date < "2012-12-01")
write.csv(m201212, "m201212.csv")

# 201211
h201211 <- hair_dryer %>%
  filter(review_date < "2012-11-01")
write.csv(h201211, "h201211.csv")
p201211 <- pacifier %>%
  filter(review_date < "2012-11-01")
write.csv(p201211, "p201211.csv")
m201211 <- microwave %>%
  filter(review_date < "2012-11-01")
write.csv(m201211, "m201211.csv")

# 201210
h201210 <- hair_dryer %>%
  filter(review_date < "2012-10-01")
write.csv(h201210, "h201210.csv")
p201210 <- pacifier %>%
  filter(review_date < "2012-10-01")
write.csv(p201210, "p201210.csv")
m201210 <- microwave %>%
  filter(review_date < "2012-10-01")
write.csv(m201210, "m201210.csv")

# 201209
h201209 <- hair_dryer %>%
  filter(review_date < "2012-09-01")
write.csv(h201209, "h201209.csv")
p201209 <- pacifier %>%
  filter(review_date < "2012-09-01")
write.csv(p201209, "p201209.csv")
m201209 <- microwave %>%
  filter(review_date < "2012-09-01")
write.csv(m201209, "m201209.csv")

# 201208
h201208 <- hair_dryer %>%
  filter(review_date < "2012-08-01")
write.csv(h201208, "h201208.csv")
p201208 <- pacifier %>%
  filter(review_date < "2012-08-01")
write.csv(p201208, "p201208.csv")
m201208 <- microwave %>%
  filter(review_date < "2012-08-01")
write.csv(m201208, "m201208.csv")

# 201207
h201207 <- hair_dryer %>%
  filter(review_date < "2012-07-01")
write.csv(h201207, "h201207.csv")
p201207 <- pacifier %>%
  filter(review_date < "2012-07-01")
write.csv(p201207, "p201207.csv")
m201207 <- microwave %>%
  filter(review_date < "2012-07-01")
write.csv(m201207, "m201207.csv")

# 201206
h201206 <- hair_dryer %>%
  filter(review_date < "2012-06-01")
write.csv(h201206, "h201206.csv")
p201206 <- pacifier %>%
  filter(review_date < "2012-06-01")
write.csv(p201206, "p201206.csv")
m201206 <- microwave %>%
  filter(review_date < "2012-06-01")
write.csv(m201206, "m201206.csv")

#########################
# 201205
h201205 <- hair_dryer %>%
  filter(review_date < "2012-05-01")
write.csv(h201205, "h201205.csv")
p201205 <- pacifier %>%
  filter(review_date < "2012-05-01")
write.csv(p201205, "p201205.csv")
m201205 <- microwave %>%
  filter(review_date < "2012-05-01")
write.csv(m201205, "m201205.csv")

# 201204
h201204 <- hair_dryer %>%
  filter(review_date < "2012-04-01")
write.csv(h201204, "h201204.csv")
p201204 <- pacifier %>%
  filter(review_date < "2012-04-01")
write.csv(p201204, "p201204.csv")
m201204 <- microwave %>%
  filter(review_date < "2012-04-01")
write.csv(m201204, "m201204.csv")

# 201203
h201203 <- hair_dryer %>%
  filter(review_date < "2012-03-01")
write.csv(h201203, "h201203.csv")
p201203 <- pacifier %>%
  filter(review_date < "2012-03-01")
write.csv(p201203, "p201203.csv")
m201203 <- microwave %>%
  filter(review_date < "2012-03-01")
write.csv(m201203, "m201203.csv")

# 201202
h201202 <- hair_dryer %>%
  filter(review_date < "2012-02-01")
write.csv(h201202, "h201202.csv")
p201202 <- pacifier %>%
  filter(review_date < "2012-02-01")
write.csv(p201202, "p201202.csv")
m201202 <- microwave %>%
  filter(review_date < "2012-02-01")
write.csv(m201202, "m201202.csv")

# 201201
h201201 <- hair_dryer %>%
  filter(review_date < "2012-01-01")
write.csv(h201201, "h201201.csv")
p201201 <- pacifier %>%
  filter(review_date < "2012-01-01")
write.csv(p201201, "p201201.csv")
m201201 <- microwave %>%
  filter(review_date < "2012-01-01")
write.csv(m201201, "m201201.csv")





