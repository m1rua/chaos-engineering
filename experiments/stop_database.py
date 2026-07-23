from kubernetes import client, config

congig.load_kube_config()
v1=clint.CoreV1Api()

namespace = "default"
label_selector = "app=postgres"

pgsql_pod = v1.list_namespaced_pod(namespace=namespace, label_selector=label_selector)
pgsql_pod_name = pgsql_pod.items.metadata.name

stop_database_script = "sh", "-c", "pkill postgress"
restart_database_script = "sh -c "