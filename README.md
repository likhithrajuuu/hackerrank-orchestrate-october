# hackerrank-orchestrate-october
## How to run this application in your local computer

### Step 1: Look at the file `.env.example` and replicate the environment variables
Check the file `.env.example` and then replicate them into a new file called `.env` in the project root folder. They may include API Keys which are considered secret and add the same file to your `.gitignore` file by listing `.env` in that file.

### Step 2 : Create the python virtual environment
Use the following command to run the virtual environment in your local computer
```bash
python3 -m venv .venv
```

### Step 3 : Install the dependencies
There are some dependencies that this application would require please install them using the following command
```bash
pip install -r requirements.txt
```

### Step 4 : Run this application
Finally run this application using the following command which ever is suitable to you
```bash
uvicorn main:app --reload
```

or if you need more control you can go with this:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

