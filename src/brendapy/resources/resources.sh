"""
Release of the latest resources.
"""
# compress local data
DATA_ZIP="brendapy-data-v0.5.0.zip"
cd brendapy
zip -r $DATA_ZIP data/

# upload data on server
scp $DATA_ZIP mkoenig@mkproxy:/home/mkoenig
rm $DATA_ZIP

# move to web resources
ssh mkproxy
sudo mv $DATA_ZIP /var/www/html/brendapy/

# restore data (for local development)
cd brendapy
wget http://141.20.66.64/brendapy/$DATA_ZIP
unzip $DATA_ZIP
