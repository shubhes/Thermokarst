"""Data loading utilities for local, drive, and web sources."""

from __future__ import annotations

from io import StringIO
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

from .config import PipelineConfig


SUPPORTED_SUFFIXES = {".csv", ".json", ".xlsx", ".parquet"}


def _read_structured_file(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_SUFFIXES:
        raise ValueError(
            f"Unsupported file extension '{suffix}'. Supported: {sorted(SUPPORTED_SUFFIXES)}"
        )

    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix == ".json":
        return pd.read_json(path)
    if suffix == ".xlsx":
        return pd.read_excel(path)
    return pd.read_parquet(path)


def load_local(path: str) -> pd.DataFrame:
    file_path = Path(path).expanduser().resolve()
    if not file_path.exists():
        raise FileNotFoundError(f"Local path not found: {file_path}")
    return _read_structured_file(file_path)


def load_drive(path: str) -> pd.DataFrame:
    # Drive data is treated like a mounted filesystem path.
    return load_local(path)


def load_web_table(url: str, selector: str = "table") -> pd.DataFrame:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    node = soup.select_one(selector)
    if node is None:
        raise ValueError(f"No element found for selector: '{selector}'")

    tables = pd.read_html(StringIO(str(node)))
    if not tables:
        raise ValueError("No tabular content found in scraped element.")

    return tables[0]


def load_data(config: PipelineConfig) -> pd.DataFrame:
    if config.source == "local":
        if not config.path:
            raise ValueError("'path' is required when source='local'.")
        return load_local(config.path)

    if config.source == "drive":
        if not config.path:
            raise ValueError("'path' is required when source='drive'.")
        return load_drive(config.path)

    if config.source == "web":
        if not config.url:
            raise ValueError("'url' is required when source='web'.")
        return load_web_table(config.url, config.selector or "table")

    raise ValueError(f"Unsupported source: {config.source}")
