from kubernetes import client, config
from kubernetes.stream import stream
import random
import time
config.load_kube_config()
v1 = client.CoreV1Api()

namespace = "default"
label_selector = "app=main-app"

pods = v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
random_pod = random.choice(pods.items)
network_delay_pod = random_pod.metadata.name
network_delay_script = ["sh", "-c", "tc qdisc add dev eth0 root netem delay 120ms loss 15% duplicate 12%"]
network_delay_fix_script = ["sh", "-c", "tc qdisc delete dev eth0 root"]

print("был выбран ", network_delay_pod)

stream (v1.connect_get_namespaced_pod_exec, name=network_delay_pod, namespace=namespace, command=network_delay_script, stderr=True, stdin=False, stdout=True, tty=False)
time.sleep(30)
stream (v1.connect_get_namespaced_pod_exec, name=network_delay_pod, namespace=namespace, command=network_delay_fix_script, stderr=True, stdin=False, stdout=True, tty=False)