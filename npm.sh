cd ./rpi_server/app/vuejs
if [ ! -d "node_modules" ]; then
    npm install
fi
npm run dev
