# txGenerator
Random Transaction Generator for Cosmos SDK Testnets


# Install Instructions
```
sudo apt install python3-pip -y

sudo pip install numpy

cd ~
mkdir scripts

curl https://raw.githubusercontent.com/artifactstaking/txGenerator/main/junoTxGenerator.py > ~/scripts/junoTxGenerator.py
```

# Update Config
```
sudo nano ~/scripts/junoTxGenerator.py
```
Edit the py file and modify your key name and change the wallet addresses that you want to send to.

# Set up Systemd

```
sudo tee /etc/systemd/system/txGen.service > /dev/null <<EOF  

[Unit]
Description=txGen
After=multi-user.target
[Service]
User=$YOURUSERNAME
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/$YOURUSERNAME/scripts/junoTxGenerator.py
[Install]
WantedBy=multi-user.target
EOF


sudo systemctl daemon-reload
sudo systemctl enable txGen.service
sudo systemctl start txGen.service
sudo systemctl status txGen.service
```
Make sure to change $YOURUSERNAME to the actual username that is running junod.

# That's it, you're done!