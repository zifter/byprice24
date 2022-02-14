import os
import sys

from common.paths import BACKEND_DIR

from . import manage  # noqa: F401
from . import run_scrapy  # noqa: F401

sys.path.insert(0, os.path.join(BACKEND_DIR, 'src'))
