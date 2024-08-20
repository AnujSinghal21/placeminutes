import requests
import re
import json

# URL containing company openings information
url = 'https://spo-backend.vercel.app/_next/static/chunks/857.4f4f460734e7178c.js'

# Send a GET request to the URL
response = requests.get(url)

# Extract the JSON data from the response
pattern = r'JSON\.parse\(\s*(\'|\")((?:\\.|[^\1])*)\1\s*\)'
matches = re.findall(pattern, response.text, re.DOTALL)

if len(matches) == 1:
    json_string = matches[0][1]
    json_string = json_string.replace('\\\'', '\'')
    json_string = re.sub(r'\\x([0-9A-Fa-f]{2})', lambda match: chr(int(match.group(1), 16)), json_string) 
    try:
        parsed_json = json.loads(json_string)
    except json.JSONDecodeError:
        print("Invalid JSON:")
        with open('invalid_json.txt', 'w') as f:
            f.write(json_string)
        exit(0)

    with open('data/performas_data.json' , 'w') as f:
        f.write(json.dumps(parsed_json, indent=4))
    print("JSON data extracted successfully")
else:
    print("No JSON data found in the response")
# Print the response
# print(response.text)
