# NetworkFirmwareUpdateRPi
This repository contains the Raspberry Pi portion of our network firmware update
tool. It contains the code that will run our flask server and the bootstrap-vue
files that create our web interface.

NetworkFirmwareUpdateRPi/rpi_server/app/routes.py is our main flask file.  This is where we specify responses to different urls and where POST requests are handled
NetworkFirmwareUpdateRPi/rpi_server/app/templates/index.html is the html file of our homepage

To run the Flask server:

1. Navigate to the /NetworkFirmwareUpdate directory in a terminal
2. Launch the Flask server:
   >sh run.sh
    * Optionally, use debug.sh to locally launch in debug mode
      >sh debug.sh
4. Open a web browser
5. Connect to (Pi's IP address):5000
    * (In debug mode, use localhost:8080)
6. Select a file
    * Select Upload
      * the Browse... bar to choose a .bin file
    * Select History
      * Select a radio button to choose an available image
7. Select Flash (filename).bin to flash to the robot
    * So far this will download the chosen file to a local directory
      specified in routes.py.  We are still working on the flashing
      of the image to the microcontroller, so far it just connects.

To set up the Raspberry Pi:

1. Connect power to the Pi
2. Connect the Pi to the microcontroller via ethernet cable
3. Connect to the same wireless lan as the Pi
4. Determine the IP address of the Pi (currently DHCP)
5. Connect to the Pi wirelessly via ssh:
    >ssh pi@192.168.1.200
6. Follow instructions to run the Flask server above

To set up the Microcontroller:
1. Connect power to the board
2. Connect the Pi to the board via ethernet cable
3. run these commands to set up the network interface on the Pi
    >ip addr add 192.168.0.11/24 dev eth0
    
    >ip route add 192.168.0.10 dev eth0
    * Where eth0 is your ethernet interface
