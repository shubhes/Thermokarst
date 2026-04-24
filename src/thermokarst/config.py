"""Configuration objects for thermokarst workflows."""

from dataclasses import dataclass
from typing import Literal, Optional

DataSource = Literal["local", "drive", "web"]


@dataclass
class PipelineConfig:
    """Configuration for selecting and loading tabular data."""

    source: DataSource
    path: Optional[str] = None
    url: Optional[str] = None
    selector: Optional[str] = "table"
