import os, time
import numpy as np

UPDATE_PERIOD = 20

#Global parameters, replace with chain specific parameters
binaryLocation = 'binary location'
keyName = 'the name of your key'
amount = 'amount of coins to send'
denom = 'denomination of coinds to send'
chainID = 'chain-id'

#Comma delimited list of addresses to send to
addressList = ['addresses', 'of_target', 'wallets']


#Working loop
while True:
    for address in addressList:
        
        #Execute the Cosmos SDK bank send command to a subshell
        bankSend = '%s tx bank send %s %s %s%s --chain-id=%s -y' % (binaryLocation, keyName, address, amount, denom, chainID)
        os.system(bankSend)
        
        ##Generate random wait time in seconds using a Poisson distribution with lambda = 30. 
        ##Lambda is the mean, which basically means this script will send a TX about every 30 seconds, give or take. 
        randomWait = np.random.poisson(30, 1)
        
    time.sleep(randomWait.item(0))
    
    