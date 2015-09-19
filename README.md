# wakeup
A clock which uses 32x32 LED panels to blast you into awaked-ness. Written in python, uses a ton of adafruit repos including 
Uses RPIB+ and https://www.adafruit.com/products/2345

Notes:

To set up real time clock:
sudo apt-get install python-smbus
sudo apt-get install i2c-tools

refer to https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

Other libraries of conern:
sudo apt-get update
sudo apt-get install python-dev python-imaging
wget https://github.com/adafruit/rpi-rgb-led-matrix/archive/master.zip
unzip master.zip
cd rpi-rgb-led-matrix-master/
make
