import os
import subprocess

# Crée le dossier de stockage des runs si besoin
os.makedirs("mlruns", exist_ok=True)

# Lance le serveur MLflow
subprocess.run([
    "mlflow", "server",
    "--backend-store-uri", "sqlite:///mlflow.db",
    "--default-artifact-root", "file:/app/mlruns",
    "--host", "0.0.0.0",
    "--port", "10000"
])
