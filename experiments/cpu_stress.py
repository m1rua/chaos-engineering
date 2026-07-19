from kubernetes import client, config
from kubernetes.stream import stream
import random
config.load_kube_config()
v1 = client.CoreV1Api()

namespace = "default"
label_selector = "app=main-app"

pods = v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
random_pod = random.choice(pods.items)
cpu_stress_pod = random_pod.metadata.name

cpu_stress_script = ["python3", "-c", "import time; start_time = time.time(); duration = 30; \nwhile time.time() - start_time < duration: 1+1"]

result = stream(v1.connect_get_namespaced_pod_exec,name=cpu_stress_pod, namespace=namespace, command=cpu_stress_script, stderr=True, stdin=False, stdout=True, tty=False)
print(result)
