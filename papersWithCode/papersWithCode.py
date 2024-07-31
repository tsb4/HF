import requests

# Example task ID for "Image Classification on CIFAR-10"
task_id = '10-shot-image-generation'#'image-classification-on-cifar-10'
url = f'https://paperswithcode.com/api/v1/tasks/{task_id}/leaderboard'

response = requests.get(url)
print(response)
data = response.json()

# Collecting model details
model_details = []
for entry in data['results']:
    model_name = entry['model']['name']
    paper_title = entry['paper']['title']
    accuracy = entry['metric']['value']  # Assuming 'value' holds the accuracy
    params = entry.get('params', 'N/A')  # Not all entries may have parameter info
    model_details.append({
        'Model Name': model_name,
        'Paper Title': paper_title,
        'Accuracy': accuracy,
        'Parameters': params
    })

# Displaying the first 5 model details
for detail in model_details[:5]:
    print(f"Model Name: {detail['Model Name']}")
    print(f"Paper Title: {detail['Paper Title']}")
    print(f"Accuracy: {detail['Accuracy']}")
    print(f"Parameters: {detail['Parameters']}")
    print('-' * 40)
