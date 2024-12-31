from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import shutil

class ArchiveDataOperator(BaseOperator):
    # Dieser benutzerdefinierte Operator verschiebt eine Datei nach der Verarbeitung in ein Archivverzeichnis.
    # Er wird typischerweise nach der Haupt-ETL-Pipeline ausgeführt, um die Organisation der Daten zu verbessern.
    # Der Operator verschiebt die verarbeitete Datei in das Archiv

    @apply_defaults
    def __init__(self, input_path, archive_path, *args, **kwargs):
        # Konstruktor des Operators, der den Pfad zur Eingabedatei und zum Archiv als Argumente entgegennimmt.
        # Diese Pfade werden später in der execute-Methode verwendet.
        super(ArchiveDataOperator, self).__init__(*args, **kwargs)
        self.input_path = input_path  # Pfad zur Eingabedatei
        self.archive_path = archive_path  # Pfad zum Archiv

    def execute(self, context):
        # Verschiebt die Datei ins Archiv
        shutil.move(self.input_path, self.archive_path)
        self.log.info(f"Daten wurden nach {self.archive_path} archiviert.")
