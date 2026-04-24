"""Core pipeline utilities for reusable script/notebook workflows."""

from __future__ import annotations

import pandas as pd

from .config import PipelineConfig
from .data_sources import load_data


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    normalized = df.copy()
    normalized.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]
    return normalized


def run_basic_workflow(config: PipelineConfig) -> pd.DataFrame:
    """Load data and apply minimal normalization for downstream modeling."""
    df = load_data(config)
    return _normalize_columns(df)
