import os, time
import numpy as np

UPDATE_PERIOD = 30

#Global parameters, replace with chain specific parameters
binaryLocation = '~/go/bin/evmosd'
amount = '100000'
denom = 'aphoton'
chainID = 'evmosd_9000-1'
gas = '200000'

address1 = 'wallet1_address'
keyName1 = 'wallet1'
address2 = 'wallet2_address'
keyName2 = 'wallet2'

addressList = [[address1,keyName1], [address2, keyName2]]



#Working loop
while True:
    for address in addressList:
        
        #Execute the Cosmos SDK bank send command to a subshell
        bankSend = '%s tx bank send %s %s %s%s --chain-id=%s --gas=%s -y' % (binaryLocation, address[1], address[0], amount, denom, chainID, gas)
        os.system(bankSend)
        
        ##Generate random wait time in seconds using a Poisson distribution with lambda = UPDATE_PERIOD. 
        ##Lambda is the mean, which basically means that if UPDATE_PERIOD = 30 then this script will send a TX about every 30 seconds, give or take. 
        randomWait = np.random.poisson(int(UPDATE_PERIOD), 1)
        
    time.sleep(randomWait.item(0))
    
    