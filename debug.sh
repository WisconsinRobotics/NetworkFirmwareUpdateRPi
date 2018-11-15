# Set the path variable for the server script
export FLASK_APP='rpi_server/app/routes.py'

# Set the env variable to dev/debug
export FLASK_ENV='development'

# Run the server locally
flask run
