import os
import subprocess

# Infos Render PostgreSQL
PG_USER = "mlflow_db_hisu_user"
PG_PASSWORD = "AasxbT5V64Q68UZO1uf4e0dpQW6noX5S"
PG_HOST = "dpg-cvfco68fnakc739n1b3g-a"
PG_PORT = "5432"
PG_DATABASE = "mlflow-db"

# 👉 URI pour SQLAlchemy (backend store MLflow)
backend_store_uri = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}"

# Artifacts dans un dossier temporaire
artifact_path = "/tmp/mlruns"
os.makedirs(artifact_path, exist_ok=True)

# Lancement du serveur MLflow
subprocess.run([
    "mlflow", "server",
    "--backend-store-uri", backend_store_uri,
    "--default-artifact-root", f"file:{artifact_path}",
    "--host", "0.0.0.0",
    "--port", "10000",
    "--serve-artifacts"
])

