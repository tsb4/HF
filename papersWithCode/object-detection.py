import requests
from bs4 import BeautifulSoup
import json
import matplotlib.pyplot as plt
import numpy as np

def convert_to_float(s):
    # Check if the string ends with 'M' and remove it
    if s.endswith('M'):
        number = float(s[:-1])  # Convert the part before 'M' to a float
        return number * 1e6     # Multiply by 1 million
    else:
        # Handle other cases as needed
        return float(s)

# URL of the page containing the JSON data
url ='https://paperswithcode.com/sota/object-detection-on-coco'
metric1 = 'box mAP'
metric2 = 'Params (M)'

# Fetch the content of the webpage
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Parse the webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the <script> tag with the JSON data
script_tag = soup.find('script', {'id': 'evaluation-table-data', 'type': 'application/json'})

metrics = []
# Extract the JSON data
if script_tag:
    json_data = script_tag.string
    # Parse the JSON data
    data = json.loads(json_data)
    print(len(data))
    for model in data[:]:
        print(model)
        if(model["raw_metrics"][metric2]!=None and model["raw_metrics"][metric1]!=None):
            metrics.append([float(model["raw_metrics"][metric2]), float(model["raw_metrics"][metric1])])
        #print(model["metrics"]["PARAMS"])
    print(len(metrics))
    data = np.array(metrics)
    n_params, accs = data[:,0], data[:,1]
    
    plt.figure()
    #print(n_params, len(n_params), accs, len(accs))
    plt.scatter(n_params,accs)
    '''sorted_data = sorted(data, key=lambda x: x[3], reverse=True)[:5]
    high_nParams = []
    high_accs = []
    for item in sorted_data:
        high_nParams.append(item[0])
        high_accs.append(item[1])
    #print(sorted_data[:]["nParams"])
    plt.scatter(high_nParams,high_accs, s=50, c="red")'''
    plt.xlabel(metric2)
    plt.ylabel(metric1)


    #for i in range(len(n_params)):
    #    plt.annotate(downloads[i], (n_params[i], accs[i]), textcoords="offset points", xytext=(0,5), ha='center')
    task = url.split('/')[-1]
    plt.savefig(f'Figures/{task}.png')
    plt.show()


    #created, all_time, last_month, total_params = infos(str(model_repo.repo_id))
    #model_stats = ModelStats(created, all_time, last_month, total_params)
    #print(model_stats)

    raise(0)
    
    # Print the parsed JSON data (or process it as needed)
    print(json.dumps(data, indent=4))
else:
    print("No JSON data found in the specified <script> tag.")
