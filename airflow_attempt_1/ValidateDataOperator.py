from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import os

class ValidateDataOperator(BaseOperator):
    # Dieser benutzerdefinierte Operator überprüft, ob eine Eingabedatei vorhanden ist.
    # Er wird typischerweise vor der Haupt-ETL-Pipeline ausgeführt, um sicherzustellen,
    # dass alle benötigten Daten für die Verarbeitung bereitstehen.
    # Der Operator prüft, ob die Eingabedatei vorhanden ist

    @apply_defaults
    def __init__(self, input_path, *args, **kwargs):
        # Konstruktor des Operators, der den Pfad zur Eingabedatei als Argument entgegennimmt.
        # Der Pfad wird später in der execute-Methode verwendet.
        super(ValidateDataOperator, self).__init__(*args, **kwargs)
        self.input_path = input_path  # Pfad zur Eingabedatei

    def execute(self, context):
        # Hauptmethode des Operators, die während der DAG-Ausführung aufgerufen wird.
        # Diese Methode verschiebt die Datei vom Eingabepfad in das Archivverzeichnis.
        # Hauptmethode des Operators, die während der DAG-Ausführung aufgerufen wird.
        # Diese Methode überprüft, ob die Datei unter dem angegebenen Pfad existiert.
        # Überprüfen, ob die Datei existiert
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Eingabedatei nicht gefunden: {self.input_path}")
        self.log.info(f"Eingabedatei gefunden: {self.input_path}")
