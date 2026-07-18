from kubernetes import client, config
import random

config.load_kube_config()

v1 = client.CoreV1Api()
namespace = "default"
label_selector = "app=main-app"

pods = v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
random_pod = random.choice(pods.items)
deleting_pod_name = random_pod.metadata.name
v1.delete_namespaced_pod(name=deleting_pod_name, namespace=namespace)