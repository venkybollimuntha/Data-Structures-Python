import requests

GITHUB_TOKEN = "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"
GITHUB_ENTERPRISE_URL = "https://github.sciencelogic.com/api/v3"
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



