from pathlib import Path

from flask.cli import load_dotenv

from models.base import Base

from nguylinc_python_utils.connexion import setup_app
from nguylinc_python_utils.sqlalchemy import init_db

load_dotenv()
session = init_db(Base)
schema_path = Path(__file__).parent / "openapi.yaml"
app = setup_app(session, schema_path)

if __name__ == "__main__":
    app.run(f"{Path(__file__).stem}:app", port=8080, reload=True)
