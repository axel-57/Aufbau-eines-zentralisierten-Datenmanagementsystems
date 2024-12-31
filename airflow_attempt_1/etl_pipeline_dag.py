from airflow import DAG  # Importiert das DAG-Modul von Airflow
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator  # Importiert den SparkSubmitOperator
from airflow.operators.dummy import DummyOperator  # Importiert einen DummyOperator für Platzhalter-Aufgaben
from airflow.operators.python import PythonOperator  # Importiert den PythonOperator für individuelle Logik
from datetime import datetime, timedelta  # Importiert Module für Datum und Zeit

# Standard-Argumente für die DAG
default_args = {
    'owner': 'airflow',  # Besitzer der DAG
    'depends_on_past': False,  # Keine Abhängigkeit von vorherigen Ausführungen
    'email': ['admin@example.com'],  # Benachrichtigungs-E-Mail
    'email_on_failure': True,  # Sende eine E-Mail bei Fehlern
    'email_on_retry': False,  # Keine E-Mail bei Wiederholungsversuchen
    'retries': 3,  # Anzahl der Wiederholungen bei Fehlern (erhöht für höhere Robustheit)
    'retry_exponential_backoff': False,  # Aktiviert exponentielles Backoff
    'retry_delay': timedelta(minutes=3),  # Zeitabstand zwischen Wiederholungen
}

# DAG erstellen
with DAG(
    'pyspark_etl_pipeline',                # Name der DAG
    default_args=default_args,             # Standard-Argumente
    description='ETL Pipeline orchestriert mit Airflow',  # Beschreibung der DAG
    schedule_interval='@daily',            # Tägliche Ausführung
    start_date=datetime(2024, 1, 1),       # Startdatum der DAG
    catchup=False,                         # Keine Nachholung von fehlenden Ausführungen
) as dag:

    # Start-Task
    start = DummyOperator(task_id='start')  # Definiert einen Dummy-Startpunkt

    # PySpark Script-Task
    run_etl = SparkSubmitOperator(
        task_id='run_pyspark_etl',  # Name der Aufgabe
        application='/home/maxpower/airflow/dags/amazon_v2_cleanup.py',  # Pfad zum PySpark-Skript
        conn_id='spark_default',  # Spark-Verbindung, konfiguriert in Airflow
        verbose=True  # Aktiviert detaillierte Logs
    )

    # End-Task
    end = DummyOperator(task_id='end')  # Definiert einen Dummy-Endpunkt

    # Aufgaben-Reihenfolge definieren
    start >> run_etl >> end  # Verknüpft die Aufgaben in der richtigen Reihenfolge
