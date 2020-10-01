'''A few pattern printing exercises'''

##Pattern one -- printing the pattern below to the console

#####
#####
#####
#####
#####

for i in range(0,5):
    for j in range(0,5):
        print("#",end='')
    print("")

print("")
##Pattern two -- printing the pattern below to the console

#
##
###
####
#####

for i in range(0,5):
    for j in range(0,i+1):
        print("#",end='')
    print("")

print("")

##Pattern three -- printing the pattern below to the console

     #
    ##
   ###
  ####
 #####

for i in range(0,5):
    for j in range(5-i,0,-1):
        print(" ",end='')
    for k in range(0,i+1):
        print("#",end='')
    print("")

print("")
