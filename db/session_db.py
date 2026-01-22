import tempfile
from sqlalchemy import create_engine

def create_session_engine():
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    engine = create_engine(f"sqlite:///{tmp.name}", echo=False)
    return engine, tmp.name