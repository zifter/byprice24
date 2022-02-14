from pathlib import Path

BACKEND_DIR = Path(__file__).parent.parent.parent
TEST_DATA_DIR = BACKEND_DIR.joinpath('testdata')
FIXTURES_DIR = BACKEND_DIR.joinpath('fixtures')
TMP_DIR = BACKEND_DIR.joinpath('tmp')
