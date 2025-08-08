```
# Create Virtual Environment: 
conda create -p venv_project python=3.10 -y
```

```
# Activate the Virtual Environment:
conda activate venv_project

```

```
# Clone the Github Repository:
git clone https://github.com/Soumadeep555/customer_support_system.git
```

```
# Install the dependencies via the requirements.txt file
pip install -r requirements.txt
```

```
# Run the Application:
uvicorn main:app --reload --port 8001
```
