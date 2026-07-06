from pathlib import Path

import pandas as pd

from src.configs.settings import RAW_PATH

class FileManager:

    @staticmethod
    def discover_csv_files() -> list[Path]:
        return sorted(RAW_PATH.glob("*.csv"))

    @staticmethod
    def read_csv(path: Path) -> pd.DataFrame:
        return pd.read_csv(path)

    @staticmethod
    def save_parquet(df: pd.DataFrame, destination: Path) -> None:
        df.to_parquet(destination, index=False)