library(mltools)
library(data.table)

setwd("/home/chocomenta/Desktop/code/tarefa1")
df <- read.table("crx.data", header = FALSE, sep = ",")
#fix(df)
head(df)

df <- na.omit(df)
df2 <- df[,c(1,4,5,6,7,9,10,12,13,16)]

temp1 <- unique(df2$V1)
temp2 <- unique(df2$V4)
temp3 <- unique(df2$V5)
temp4 <- unique(df2$V6)
temp5 <- unique(df2$V7)
temp6 <- unique(df2$V9)
temp7 <- unique(df2$V10)
temp8 <- unique(df2$V12)
temp9 <- unique(df2$V13)
temp10 <- unique(df2$V16)

#for (i in 1:10){
#  aux = paste("temp", i, sep = "")
#  head(aux)
#}

head(temp1)
head(temp2)
head(temp3)
head(temp4)
head(temp5)
head(temp6)
head(temp7)
head(temp8)
head(temp9)
head(temp10)

ohot <- one_hot(as.data.table(df2))
fix(ohot)
