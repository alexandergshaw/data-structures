"""Makes `from solution import ...` resolve to THIS folder's solution.py.

Each assignment folder has its own `solution.py`. When the Testing panel (or
pytest) runs more than one folder in a single session, Python would otherwise
cache the first `solution` module it sees and reuse it everywhere. To keep every
folder independent we (1) put this folder at the front of the import path and
(2) drop any stale cached `solution` module before this folder's tests import.

This file runs automatically — you never need to touch it.
"""

import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, HERE)
# Drop a `solution` cached from a sibling folder so the correct one is loaded.
sys.modules.pop("solution", None)
