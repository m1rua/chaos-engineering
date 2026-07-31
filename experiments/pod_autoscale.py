from kubernetes import config, client
from kubernetes.stream import stream

config.load_kube_config()
v1 = client.CoreV1Api()

namespace = 'default'
label_selector = "app=main-app"
pods = v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
autoscale_pod = pods.items
autoscale_pod_name = autoscale_pod[0].metadata.name
http_script = ["python3", "-c", "import time; import requests; from concurrent.futures import ThreadPoolExecutor; start_time = time.time(); duration = 30; \nwhile time.time() - start_time < duration: \n    with ThreadPoolExecutor(max_workers=100) as executor: \n        for i in range(100): executor.submit(requests.get, 'http://main-app:80/health')"]

stream(v1.connect_get_namespaced_pod_exec, namespace=namespace, name=autoscale_pod_name, command=http_script, stderr=True, stdin=False, stdout=True, tty=False)
