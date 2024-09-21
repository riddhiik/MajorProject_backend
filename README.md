# Start the application

```bash
# Make you have python 3.12+ installed
# create virtual envirionment
python3 -m venv .env

# activat the envirionment
.env/bin/activate
#.\env\Scripts\activate

# install dependencies
pip install -r requirements.txt

# make sure you have the .env
cp code/.env.sample code/.env

# run dev code
cd code
uvicorn main:app --port 8000 --reload