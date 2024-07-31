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
    
def pareto_frontier(data):
    """
    Find the Pareto frontier from a given set of points.
    
    Args:
    - data: numpy array of points (each point is an array of objective values [number_of_parameters, accuracy])
    
    Returns:
    - numpy array of Pareto frontier points
    """
    num_points = data.shape[0]
    is_pareto = np.ones(num_points, dtype=bool)  # Initialize all points as Pareto optimal
    
    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                # Check if point j dominates point i
                if (data[j][1] >= data[i][1] and data[j][0] <= data[i][0]) and \
                   (data[j][1] > data[i][1] or data[j][0] < data[i][0]):
                    is_pareto[i] = False
                    break

    return data[is_pareto]


# URL of the page containing the JSON data
url = 'https://paperswithcode.com/sota/image-classification-on-cifar-10'

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
        if(model["raw_metrics"]["PARAMS"]!=None and model["raw_metrics"]["Percentage correct"]!=None):
            metrics.append([float(model["raw_metrics"]["PARAMS"]), float(model["raw_metrics"]["Percentage correct"])])
        #print(model["metrics"]["PARAMS"])
    print(len(metrics))
    data = np.array(metrics)
    n_params, accs = data[:,0], data[:,1]
    data = np.array(sorted(data, key=lambda x: x[0], reverse=False))
    pareto_points = pareto_frontier(data[:,:2])
    
    plt.figure()
    #print(n_params, len(n_params), accs, len(accs))
    plt.scatter(n_params,accs)
    plt.plot(pareto_points[:, 0], pareto_points[:, 1], color='g', marker='', lw=3, label="Pareto frontier")


    '''sorted_data = sorted(data, key=lambda x: x[3], reverse=True)[:5]
    high_nParams = []
    high_accs = []
    for item in sorted_data:
        high_nParams.append(item[0])
        high_accs.append(item[1])
    #print(sorted_data[:]["nParams"])
    plt.scatter(high_nParams,high_accs, s=50, c="red")'''
    plt.xlabel("Nb.of Params")
    plt.ylabel("Avg. Accuracy")
    plt.xlim(-0.01e9, 0.41e9)


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
