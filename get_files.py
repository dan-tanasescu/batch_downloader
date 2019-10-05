from tqdm import tqdm
import requests
import sys

def download(url):
        buffer_size = 1024
        response = requests.get(url, stream=True)
        file_size = int(response.headers.get("Content-Length", 0))
        filename = url.split("/")[-1]
        progress = tqdm(response.iter_content(buffer_size), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
        
        with open(filename, "wb") as f:
            for data in progress:
                f.write(data)
                progress.update(len(data))

if len(sys.argv) == 1:
    print("Usage: python get_file.py <file_name>")
elif len(sys.argv) > 2:
    print("Too many arguments! Only one is required.")
else:
    batch_file = sys.argv[1]
                
    batch_list = [line.strip() for line in open(batch_file, 'r')]

    for adress in batch_list:

        if adress != "":
            download(adress)
