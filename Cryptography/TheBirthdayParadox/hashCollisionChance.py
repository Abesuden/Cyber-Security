# Developed By: Alexander Besuden
# Date Created: 5/26/2020
# 
#                     -== The Birthday Paradox ==-
# This Python module is designed to calculate the chance of a hash collision
# based on the number of instances of produced digests that are 128 to 512 bits
# in length. This is based off of "The Birthday Paradox" and has a higher chance
# of occuring even with lower numbers. For instance, with 32 hashed documents,
# there is a 50% chance that 2 hashes will have a collision.
# --> reference: Vsauce2 - The Birthday Paradox [found on: YouTube.com]

import math

def hashCC(liveDigests, bitLength=128):
    # This function is used to calculate the chance of a hash collision
    # @Params: integer, integer
    #              |       '--> bit length of encryption (aka. days in year)
    #              '----------> number of "messages" (aka. people)
    #             .-----------> chance of hash collision
    # @Return: float

    # error checking
    if (not liveDigests.isdigit()):
        raise Exception ("Error: hashCC function requires the first argument be of <type: int> and it is of " + str(type(liveDigests)) + ".")
    if ((liveDigests%10) != 0):
        raise Exception ("Error: hashCC function requires a whole number and the first argument has a remander of " + str(liveDigests%10))
    if (not bitLength.isdigit()):
        raise Exception ("Error: hashCC function requires the second argument be of <type: int> and it is of " + str(type(bitLength)) + ".")
    if ((bitLength%10) != 0):
        raise Exception ("Error: hashCC function requires a whole number and the second argument has a remander of " + str(bitLength%10))


    calcChance = (((math.factorial((bitLength - 1))) / (math.factorial((bitLength - liveDigests) * (bitLength**(liveDigests - 1)))))) - 1

    return calcChance