# Thermokarst Mapping Toolkit

A modular toolkit for thermokarst segmentation workflows, designed for both interactive research and reproducible batch runs.

## What this repository provides

- **Notebook workflow** for exploratory analysis and rapid iteration.
- **Python script workflow** for repeatable execution and automation.
- **Flexible data ingestion** from:
  - local files on your machine,
  - mounted cloud/drive paths (for example Google Drive in Colab),
  - online sources via lightweight web scraping.

## Project structure

```text
.
├── notebooks/
│   └── thermokarst_workflow.ipynb
├── scripts/
│   └── run_pipeline.py
├── src/
│   └── thermokarst/
│       ├── __init__.py
│       ├── config.py
│       ├── data_sources.py
│       └── pipeline.py
├── thermokarst.ipynb
├── trainedUNet-general.h5
└── README.md
```

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage options

### 1) Notebook option

Open:

- `notebooks/thermokarst_workflow.ipynb`

This notebook demonstrates how to switch data sources and run a preprocessing workflow interactively.

### 2) Python script option

```bash
PYTHONPATH=src python scripts/run_pipeline.py --source local --path ./data/sample.csv
```

#### Load from mounted drive

```bash
PYTHONPATH=src python scripts/run_pipeline.py --source drive --path "/content/drive/MyDrive/thermokarst/sample.csv"
```

#### Load from online scraping

```bash
PYTHONPATH=src python scripts/run_pipeline.py \
  --source web \
  --url "https://example.com/thermokarst-data.html" \
  --selector "table"
```

## Notes

- The pretrained model file (`trainedUNet-general.h5`) is retained for downstream model-loading tasks.
- The modular `src/thermokarst` package is intentionally lightweight so you can connect it to your existing segmentation and training code.
