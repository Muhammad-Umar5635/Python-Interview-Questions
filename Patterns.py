#
##
###
####
#####
######
#######
########
#########
##########
for i in range(1, 11):
    print("#" * i)


#                  #
##                ##
###              ###
####            ####
#####          #####
######        ######
#######      #######
########    ########
#########  #########
####################
for i in range(1, 11):
    print("#" * i +" "* (20 - (2*i)) + "#" * i)

       #
      ###
     #####
    #######
     #####
      ###
       #
def display_pattern(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        hashes = '#' * (2 * i - 1)
        print(spaces + hashes)

    for i in range(height - 1, 0, -1):
        spaces = ' ' * (height - i)
        hashes = '#' * (2 * i - 1)
        print(spaces + hashes)

if __name__ == "__main__":
    height = 6
    display_pattern(height)