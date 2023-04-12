echo [$(date)]: "STARTING"
echo [$(date)]: "Creating conda env with version 3.10"
conda create --prefix ./env python=3.10 -y
echo [$(date)]: "Activating env"
source activate ./env
echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"