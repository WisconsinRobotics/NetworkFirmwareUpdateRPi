# NetworkFirmwareUpdateRPi
This repository contains the Raspberry Pi portion of our network firmware update tool.  
It contains the code that will run our flask server and the bootstrap-vue files that create our web interface

NetworkFirmwareUpdateRPi/rpi_server/app/routes.py is our main flask file.  This is where we specify responses to different urls and where POST requests are handled
NetworkFirmwareUpdateRPi/rpi_server/app/templates/index.html is the html file of our homepage

To run the local flask server:
            -Navigate to the /rpi_server directory
            -Type the following:
                    FLASK_APP=routes.py flask run
            -The program will output an url, e.g. "http://127.0.0.1:5000/"
            -Paste this url into a web browser and the webpage should pop up
            -Use the 'Choose file' button in the bottom left corner to open a file explorer to choose the firmware image you want to upload
            -Click the 'send' button once you've chosen the file.  So far this will download the chosen file to a local directory specified in routes.py.  We are still working on the actual flashing of the image once it has been downloaded to the local server
