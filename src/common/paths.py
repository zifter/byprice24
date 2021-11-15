from pathlib import Path

REPO_DIR = Path(__file__).parent.parent.parent
TEST_DATA_DIR = REPO_DIR.joinpath('testdata')
TMP_DIR = REPO_DIR.joinpath('tmp')
