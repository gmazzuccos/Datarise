import pandas as pd

from utils.file_manager import (
    get_raw_files,
    create_directories,
    LANDING_PATH,
)

from utils.logger import get_logger

logger = get_logger()

create_directories()

files = get_raw_files()

logger.info(f"{len(files)} datasets found.")

for file in files:

    logger.info(f"Loading {file.name}")

    df = pd.read_csv(file)

    output_name = (
        file.stem
            .replace("_dataset", "")
            + ".parquet"
    )

    output = LANDING_PATH / output_name

    df.to_parquet(
        output,
        index=False
    )

    logger.info(
        f"{output_name} created ({len(df):,} rows)"
    )

logger.success("Landing Layer successfully generated.")