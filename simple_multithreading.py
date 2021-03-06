import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

url_list = ["https://via.placeholder.com/400",
    "https://via.placeholder.com/410",
    "https://via.placeholder.com/420",
    "https://via.placeholder.com/430",
    "https://via.placeholder.com/440",
    "https://via.placeholder.com/450",
    "https://via.placeholder.com/460",
    "https://via.placeholder.com/470",
    "https://via.placeholder.com/480",
    "https://via.placeholder.com/490",
    "https://via.placeholder.com/500",
    "https://via.placeholder.com/510",
    "https://via.placeholder.com/520",
    "https://via.placeholder.com/530"
    ]

def download_file(url):
    html = requests.get(url, stream=True)
    return html.status_code

def sinlge_thread():
    start = time()

    for url in url_list:
        print(download_file(url))

    # print(f'Time taken: {time() - start}') # Only Available in python 3
    print("Time taken: %f" % (time() - start))


def multi_thread():
    start = time()

    processes = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in url_list:
            processes.append(executor.submit(download_file, url))

    for task in as_completed(processes):
        print(task.result())

    # print(f'Time taken: {time() - start}') # Only Available in python 3
    print("Time taken: %f" % (time() - start))


if __name__ == "__main__":
    sinlge_thread()
    multi_thread()
