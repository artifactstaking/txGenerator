import os, time
import numpy as np

UPDATE_PERIOD = 20

#Global parameters, replace with chain specific parameters
binaryLocation = '~/go/bin/junod'
keyName = 'the name of your key'
amount = '10000'
denom = 'ujuno'
chainID = 'lucina'

#Comma delimited list of addresses to send to
#these are Juno Lucina testnet wallets
addressList = ['juno1u6qhl98e09es6xheeyefm6cnvyscyksyrm2vg8', 'juno12purckg7d6ugetj57wqn0fw9ag2gl0vkx68vt6']


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
    
    