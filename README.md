# collect-stock-info
Simple api to collect information of stock market values and return avg, std and more 


# Set up
```commandline
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements.txt
create and full .env file (check env_template)
uvicorn main:app --port=5001 --host 0.0.0.0
```

## Set up testing environment
```commandline
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements.txt
create and full .env file (check env_template)
export ENVFILE=.
uvicorn application:app --port=5001 --host 0.0.0.0 &
cd tests
uvicorn mock_api:app --port=6001 --host 0.0.0.0 &
uvicorn mock_api:app --port=6002 --host 0.0.0.0 &
uvicorn mock_api:app --port=6003 --host 0.0.0.0 &
cd ..
python -m unittest discover tests
```