from kubernetes import client, config
from kubernetes.stream import stream
config.load_kube_config()
v1=client.CoreV1Api()

namespace = "default"
label_selector = "app=postgres"

pod = v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
pgsql_pod = pod.items
pgsql_pod_name = pgsql_pod[0].metadata.name
stop_database_script = ["sh", "-c", "pkill postgres"]

stream(v1.connect_get_namespaced_pod_exec, name=pgsql_pod_name, namespace=namespace, command=stop_database_script, stderr=True, stdin=False, stdout=True, tty=False)