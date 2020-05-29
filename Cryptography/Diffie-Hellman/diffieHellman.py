# Developed By: Alexander Besuden
# Date Created: 5/26/2020
# 
# This Python module was developed to perform a Diffie-Hellman key exchange.

import random

secretSeed = 0
isSecretSeedSet = False
primeModulous_G = 17
primitivePrime_G = 3


def __errorCheck__(checkErr, funName):
    # This is a private function that is used to for error checking in function arguments

    if (not checkErr.isdigit()):
        raise Exception ("Error: " + funName + " function requires the argument be of <type: int> and it is of " + str(type(checkErr)) + ".")
    if ((checkErr%10) != 0):
        raise Exception ("Error: " + funName + " function requires a whole number and the argument has a remander of " + str(checkErr%10))
    return checkErr

def setPrimeModulous(setter):
    # This function is used to set the prime modulous for the Diffie-Hellman key calculation

    global primeModulous_G
    primeModulous_G = __errorCheck__(setter, "setPrimeModulous")

def setPrimitivePrime(setter):
    # This function is used to set the prime modulous for the Diffie-Hellman key calculation

    global primitivePrime_G
    primitivePrime_G = __errorCheck__(setter, "setPrimitivePrime")


def setSecretSeed(secSeed=0):
    # This function's default is to generate a random number to seed into
    # the keyExchange() function. However, a developer can overwrite the
    # the default and choose there own number (aka. brute force attacks).
    # @Param: integer
    # @Return: integer
    
    global secretSeed               # import global seed
    global isSecretSeedSet          # import flag

    if ((isSecretSeedSet) & (secSeed == 0)):
        return secretSeed           # return developer specified seed

    if (secSeed == 0):
        secSeed = random.randint(17,98)
    else:
        __errorCheck__(secSeed, setSecretSeed)     # check user input
        secretSeed = secSeed        # set seed value
        isSecretSeedSet = True      # change flag

    return secSeed

def publicKeyExchange():
    # This function is used to generate a secret key between two connections.

    # import globals
    global primeModulous_G
    global primitivePrime_G
    global secretSeed

    # set values
    primeModulous = primeModulous_G
    primitivePrime = primitivePrime_G

    # calculate Diffie-Hellman key
    privateKey = setSecretSeed()
    secretSeed = privateKey

    publicKey = (primitivePrime**privateKey)%primeModulous
    return publicKey

def generateSharedKey(senderKey):
    # this function is used to return the generated Diffie-Hellman key

    __errorCheck__(senderKey, generateSharedKey)

    return ((senderKey**secretSeed)%primeModulous_G)