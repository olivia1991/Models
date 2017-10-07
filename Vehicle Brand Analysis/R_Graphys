ds_challenge_v2_1_data_1 <- read.csv("~/Desktop/ds_challenge_v2_1_data_1.csv")
View(ds_challenge_v2_1_data_1)

#What fraction of the driver signups took a first trip?

summary(ds_challenge_v2_1_data_1)

length(na.omit(ds_challenge_v2_1_data_1$first_completed_date))
Fraction=length(na.omit(ds_challenge_v2_1_data_1$first_completed_date))/nrow(ds_challenge_v2_1_data)
Fraction

attach(ds_challenge_v2_1_data_1)


#Picture

table(first_completed_date,city_name)
table(Dummy_first_complete,city_name)
barplot(table(Dummy_first_complete,city_name),main ="City VS Complete",col=c("blue","red"))
legend(xinch(7),y=yinch(4.5),c("No Start","Star"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1,border="black")
lines(table(Dummy_first_complete,city_name)[1,],col='green',lwd=2.5,lty=2)
lines(table(Dummy_first_complete,city_name)[2,],col='orange',lwd=2.5)
legend(xinch(7),y=yinch(2.5),c("NS_Line","S_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")


table(Dummy_first_complete,signup_os)
barplot(table(Dummy_first_complete,signup_os),main ="Signup_os VS Complete",col=c("blue","red"))
legend(xinch(7),y=yinch(4.5),c("No Start","Star"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1)
lines(table(Dummy_first_complete,signup_os)[1,],col='green',lwd=2.5,lty=2)
lines(table(Dummy_first_complete,signup_os)[2,],col='orange',lwd=2.5)
legend(xinch(7),y=yinch(2.5),c("NS_Line","S_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")


table(Dummy_first_complete,signup_channel)
barplot(table(Dummy_first_complete,signup_channel),main ="Signup_channel VS Complete",col=c("blue","red"))
legend(xinch(7),y=yinch(4.5),c("No Start","Star"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1)
lines(table(Dummy_first_complete,signup_channel)[1,],col='green',lwd=2.5,lty=2)
lines(table(Dummy_first_complete,signup_channel)[2,],col='orange',lwd=2.5)
legend(xinch(7),y=yinch(2.5),c("NS_Line","S_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")


table_make=table(Dummy_first_complete,vehicle_make)[,-1]
table_make
barplot(table_make,main ="Vehicle_make VS Complete",col=c("blue","red"))
legend(xinch(7),y=yinch(4.5),c("No Start","Star"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1)
lines(table_make[1,],col='green',lwd=2.5,lty=2)
lines(table_make[2,],col='orange',lwd=2.5)
legend(xinch(7),y=yinch(2.5),c("NS_Line","S_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")


table(Dummy_first_complete,vehicle_model)
a=table(Dummy_first_complete,vehicle_model)[,-1]
a
barplot(a,main ="Vehicle_model VS Complete",col=c("blue","red"),cex.names = 0.5)
legend(xinch(7),y=yinch(4.5),c("No Start","Star"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1)
lines(a[1,],col='green',lwd=2.5,lty=2)
lines(a[2,],col='orange',lwd=2.5)
legend(xinch(7),y=yinch(2.5),c("NS_Line","S_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")


table(Dummy_first_complete,vehicle_year)
barplot(table(Dummy_first_complete,vehicle_year),main ="vehicle_year VS Complete",col=c("blue","red"))
legend(xinch(7),y=yinch(4.5),c("No Start","Star"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1)
lines(table(Dummy_first_complete,vehicle_year)[1,],col='green',lwd=2.5,lty=2)
lines(table(Dummy_first_complete,vehicle_year)[2,],col='orange',lwd=2.5)
legend(xinch(7),y=yinch(2.5),c("NS_Line","S_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")

# date transfter

da_sign_up <- strptime(signup_date, format= "%m/%d/%y")
da_bgc=strptime(bgc_date, format= "%m/%d/%y")
da_comp=strptime(first_completed_date, format= "%m/%d/%y")

# new colume for time difference between two of three variables

#a_bgc  VS  da_sign_up
df1=da_bgc-da_sign_up
ds_challenge_v2_1_data_1$df1=df1
df1=df1/60/24/60
ds_challenge_v2_1_data_1$df1=df1

#first_completed_date  VS  da_sign_up
df2=da_comp-da_sign_up
ds_challenge_v2_1_data_1$df2=df2
df2=df2/60/24/60
ds_challenge_v2_1_data_1$df2=df2

#a_bgc  VS  first_completed_date
df3=da_comp-da_bgc
ds_challenge_v2_1_data_1$df3=df3
df3=df3/60/24/60
ds_challenge_v2_1_data_1$df3=df3


##Pcitures

##a_bgc  VS  da_sign_up

table(Dummy_first_complete,df1)
barplot(table(Dummy_first_complete,df1),main ="Backgroud Check and Sign Up",col=c("blue","red"),xlab="Days betwwem Bgc and Signup")
legend(xinch(3.8),y=yinch(3.6),c("No Finish","Finish"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1)
lines(table(Dummy_first_complete,df1)[-1,],col='green',lwd=2.5,lty=2)
lines(table(Dummy_first_complete,df1)[-2,],col='orange',lwd=2.5)
legend(xinch(3.8),y=yinch(2.5),c("NF_Line","F_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")

#first_completed_date  VS  da_sign_up
table(Dummy_first_complete,df2)
barplot(table(Dummy_first_complete,df2),main ="Complete First Trip and Sign Up",col=c("blue","red"),xlab="Days between Complete First Trip and Sign Up")
legend(xinch(6),y=yinch(3.6),c("No Finish","Finish"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1)
lines(table(Dummy_first_complete,df2)[-1,],col='green',lwd=2.5,lty=2)
lines(table(Dummy_first_complete,df2)[-2,],col='orange',lwd=2.5)
legend(xinch(6),y=yinch(2.5),c("NF_Line","F_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")


#a_bgc  VS  first_completed_date

table(Dummy_first_complete,df3)
barplot(table(Dummy_first_complete,df3),main ="First Trip and Background Check",col=c("blue","red"),xlab="Days between Bgc and first_completed_date")
legend(xinch(6),y=yinch(3.6),c("No Finish","Finish"), lty=c(1,1),lwd=c(2.5,2.5),col=c("blue","red"),xpd=TRUE,cex=1)
lines(table(Dummy_first_complete,df3)[-1,],col='green',lwd=2.5,lty=2)
lines(table(Dummy_first_complete,df3)[-2,],col='orange',lwd=2.5)
legend(xinch(6),y=yinch(2.5),c("NF_Line","F_Line"), lty=c(2.5,1),lwd=c(2.5,2.5),col=c("green","orange"),xpd=TRUE,cex=1,border="black")


