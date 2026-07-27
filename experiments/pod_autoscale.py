import requests
import time
from kubernetes import config, client
from kubernetes.stream import stream
from concurrent.futures import ThreadPoolExecutor

config.load_kube_config()
v1 = client.CoreV1Api()

start_time = time.time()
duration = 30

while time.time() - start_time < duration:
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(100):
            executor.submit(requests.get, "http://localhost:8000/health")