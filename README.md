# NetworkFirmwareUpdateRPi
This repository contains the Raspberry Pi portion of our network firmware update tool.
It contains the code that will run our flask server and the bootstrap-vue files that create our web interface

NetworkFirmwareUpdateRPi/rpi_server/app/routes.py is our main flask file.  This is where we specify responses to different urls and where POST requests are handled
NetworkFirmwareUpdateRPi/rpi_server/app/templates/index.html is the html file of our homepage

To set up Flask with Python 3 on Linux:
            -Run the following commands to set up Python 3:
                    >sudo apt-get update
                    >sudo apt-get install python3 python3-pip
            -Run the following commands to set up Flask:
                    >python3 -m pip install flask

To run the Flask server:
            -Navigate to the /NetworkFirmwareUpdate directory in a terminal
            -Launch the NPM server:
                    >sh npm.sh
            -Launch the Flask server:
                    >sh run.sh
            -(Optionally, run debug.sh to locally launch in debug mode)
            -Open a web browser
            -Connect to (Pi's IP address):8080
            -(In debug mode, use localhost:8080)
            -Select Upload
                -Select the Browse... bar to choose a .bin file
         or -Select History
                -Select a radio button to choose an available image
            -Select Flash (filename).bin to flash to the robot
            -So far this will download the chosen file to a local directory
             specified in routes.py.  We are still working on the flashing
             of the image to the microcontroller, so far it just connects.

To set up the Raspberry Pi:
            -Connect power to the Pi
            -Connect the Pi to the microcontroller via ethernet cable
            -Connect to the same wireless lan as the Pi
            -Determine the IP address of the Pi (currently DHCP)
            -Connect to the Pi wirelessly via ssh:
                    >ssh pi@192.168.1.200
            -Follow instructions to run the Flask server above

To set up the Microcontroller:
            -Connect power to the board
            -Connect the Pi to the board via ethernet cable
            - run these commands to set up the network interface on the Pi
                >ip addr add 192.168.0.11/24 dev eth0
                >ip route add 192.168.0.10 dev eth0
                Where eth0 is your ethernet interface

To run python unit testing and get python code coverage:
            -Navigate to /rpi_server/app/tests
            -Run the unit test by typing 'pytest'
            -Measure code coverage by typing:
                -'coverage run -m pytest'
                -'coverage report -m'


