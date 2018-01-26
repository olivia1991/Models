#coding

log_var = c(TRUE,FALSE, T, F)
int_var = c(1L, 6L, 10L)
dbl_var = c(1, 2.5, 4.5)
chr_var = c('these are', 'some strings')

c(1,c(2, c(3,4)))

str(int_var)
str(c("a",1))
as.numeric(c(F,F,T))

x = list(1:3,'a',c(T,F,T), c(2.3,5.9))

df = data.frame(x = 1:3, y = c("a","b","c"), stringsAsFactors = FALSE)

train = read.csv("~/Desktop/Bit/train_2016_v2.csv", stringsAsFactors = FALSE)
property = read.csv("~/Desktop/Bit/properties_2016.csv", stringsAsFactors = FALSE)
property = subset(property, parcelid %in% train$parcelid)


length(unique(train$parcelid))
property = subset(property, parcelid %in% train$parcelid)
train = merge(train, property, by = 'parcelid', all.x = T) #left outer join
write.csv(train, 'train_property.csv')  # save this data_fram

num.NA = sort(colSums(sapply(train, is.na))) #summary count of NA for each factor
remain.col = names(num.NA)[which(num.NA<= 0.2*dim(train)[1])]
train = train[, remain.col]
summary(train$logerror)
plot(density(train$logerror)) ##density --PDF, CDF --ecdf
head(train$transactiondate)
barplot(table(train$transactiondate))  #barplot ->Table

#must add as.data  Catergorical data -> Date
with(train,plot(as.Date(train$transactiondate), logerror))

train$txnmonth = sapply(strsplit(train$transactiondate, '-'), function(x) x[2])
table(train$txnmonth)

#check trend of logerror for each month
#boxplot(subset(train, txnmonth == '01')$logerror,
#        subset(train, txnmonth == '06')$logerror)

#ZOOM IN boxplot
boxplot(subset(train, txnmonth == '01'& abs(logerror)<0.05)$logerror,
        subset(train, txnmonth == '06'& abs(logerror)<0.05)$logerror)

#BOXPLOT for each month
library(lattice)
bwplot(logerror ~ txnmonth, data = subset(train, abs(logerror)<0.05))
err.month = by(train, train$txnmonth, function(x){
  mmran = mean(x$logerror) ## "return mean(x$logerror)" is also fine
})

plot(names(err.month), err.month, type = 'l')
# names(err.month) show the each month

#Correlation is for Continuous VS Continuous 

correlation = cor(train[,c('logerror', 'bathroomcnt.x','bedroomcnt.x')])
library(corrplot)
corrplot(correlation)