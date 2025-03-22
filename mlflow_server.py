import os
import subprocess

# Chemins dans /tmp pour éviter les problèmes de permissions
ARTIFACT_PATH = "/tmp/mlruns"
DB_PATH = "/tmp/mlflow.db"

os.makedirs(ARTIFACT_PATH, exist_ok=True)

subprocess.run([
    "mlflow", "server",
    "--backend-store-uri", f"sqlite:///{DB_PATH}",
    "--default-artifact-root", f"file:{ARTIFACT_PATH}",
    "--host", "0.0.0.0",
    "--port", "10000",
    "--serve-artifacts"
])

