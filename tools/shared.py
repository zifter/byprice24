from pathlib import Path

TOOLS_DIR = Path(__file__).parent.absolute()
DATA_DIR = TOOLS_DIR / 'data'
REPO_DIR = TOOLS_DIR.parent
BACKEND_DIR = REPO_DIR / 'backend'
BACKEND_FIXTURES_DIR = BACKEND_DIR / 'fixtures'
