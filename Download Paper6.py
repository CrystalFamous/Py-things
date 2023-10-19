import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('requests')
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'w') as file:
        file.write(response.text)

download_file('https://raw.githubusercontent.com/CrystalFamous/Py-things/main/PapersV6.py', 'PapersV6.py')
