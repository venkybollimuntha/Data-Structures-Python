import requests

GITHUB_TOKEN = ""
GITHUB_ENTERPRISE_URL = ""
REPO = "SRE/test-vtest3"
FILE_PATH = "README.md"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.raw",
}

url = f"{GITHUB_ENTERPRISE_URL}/repos/{REPO}/contents/{FILE_PATH}"
print(url)

response = requests.get(url, headers=headers)

if response.status_code == 200:
    FILE_CONTENT = response.text
    print(FILE_CONTENT)
else:
    print(f"Failed to retrieve file. Status code: {response.status_code}")



