
python_3=$(which python3)
if [ -z "$python_3" ]; then
  echo "Python 3 is not installed.  To install Python 3, run: sudo apt-get install python3"
  exit 1
elif [ -n "$python_3" ]; then
  echo "Python 3 is installed"
fi


node_js=$(which node)
if [ -z "$node_js" ]; then
  echo "node.js is not installed.  To install node.js/npm go to https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions-enterprise-linux-fedora-and-snap-packages"
  exit 1
elif [ -n "$node_js" ]; then
  echo "node.js is installed"
fi

npm=$(which npm)
if [ -z "$npm" ]; then
  echo "npm is not installed.  To install node.js/npm go to https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions-enterprise-linux-fedora-and-snap-packages"
  exit 1
elif [ -n "$npm" ]; then
  echo "npm is installed"
fi

pip3=$(which pip3)
if [ -z "$pip3" ]; then
  echo "pip3 is not installed.  To install pip3, run: sudo apt install python3-pip"
  exit 1
elif [ -n "$pip3" ]; then
  echo "pip3 is installed"
fi

flask=$(which flask)
if [ -z "$flask" ]; then
  echo "flask is not installed, installing flask"
  pip3 install flask
elif [ -n "$flask" ]; then
  echo "flask is installed"
fi


pytest=$(which pytest)
if [ -z "$pytest" ]; then
  echo "pytest is not installed, installing flask"
  pip3 install pytest
elif [ -n "$pytest" ]; then
  echo "pytest is installed"
fi

coverage=$(which coverage)
if [ -z "$coverage" ]; then
  echo "coverage is not installed, installing flask"
  pip install pytest coverage
elif [ -n "$coverage" ]; then
  echo "coverage is installed"
fi

npm install


