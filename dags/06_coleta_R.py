from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client import models as k8s
from datetime import datetime

# --- CONFIGURAÇÕES DO PROJETO ---
REPO_GIT = "https://github.com/gibsrs7/poc-airflow-hop.git"
BRANCH = "main"
PASTA_PROJETO = "estudos-hop" # Nome da pasta dentro do Git
NOME_PIPELINE = "dummy.hpl"   # Nome do arquivo do pipeline
# --------------------------------

with DAG(
    '06_Coleta_R',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['poc', 'etl','R']
)
as dag:

