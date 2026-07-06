from pathlib import Path

PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]

SRC_PATH: Path = PROJECT_ROOT / "src"

CONFIG_PATH: Path = SRC_PATH / "configs"

DATA_PATH: Path = PROJECT_ROOT / "data"

RAW_PATH: Path = DATA_PATH / "raw" / "olist"

LANDING_PATH: Path = DATA_PATH / "landing"

BRONZE_PATH: Path = DATA_PATH / "bronze"

SILVER_PATH: Path = DATA_PATH / "silver"

GOLD_PATH: Path = DATA_PATH / "gold"

LOG_PATH: Path = PROJECT_ROOT / "logs"

TEST_PATH: Path = PROJECT_ROOT / "tests"

DASHBOARD_PATH: Path = PROJECT_ROOT / "dashboards"


def ensure_project_structure() -> None:
    # Creates all required directories for the platform.

    for directory in [
        LANDING_PATH,
        BRONZE_PATH,
        SILVER_PATH,
        GOLD_PATH,
        LOG_PATH,
    ]:
        directory.mkdir(parents=True, exist_ok=True)