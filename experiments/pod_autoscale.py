import requests
import time
from concurrent.futures import ThreadPoolExecutor
start_time = time.time()
duration = 30

while time.time() - start_time < duration:
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100):
            executor.submit(requests.get, "http://localhost:8000/health")