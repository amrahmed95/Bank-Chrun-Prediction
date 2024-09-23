import re
import requests

# Function to get the latest version from PyPI
def get_latest_version(package_name):
    response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
    if response.status_code == 200:
        return response.json()['info']['version']
    return None

# Load requirements.txt
with open('requirements.txt', 'r') as file:
    lines = file.readlines()

# Replace local paths with latest versions
updated_lines = []
for line in lines:
    if "@ file://" in line:
        package_name = re.split(r'[@]', line)[0].strip()
        latest_version = get_latest_version(package_name)
        if latest_version:
            updated_lines.append(f"{package_name}=={latest_version}\n")
        else:
            updated_lines.append(line)  # Keep original line if version not found
    else:
        updated_lines.append(line)

# Write back to requirements.txt
with open('requirements.txt', 'w') as file:
    file.writelines(updated_lines)
