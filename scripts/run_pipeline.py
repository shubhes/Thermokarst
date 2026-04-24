#!/usr/bin/env python3
"""CLI entrypoint for thermokarst data loading and preprocessing."""

from __future__ import annotations

import argparse



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run thermokarst data ingestion workflow.")
    parser.add_argument("--source", choices=["local", "drive", "web"], required=True)
    parser.add_argument("--path", help="Path for local or drive sources.")
    parser.add_argument("--url", help="URL for web scraping source.")
    parser.add_argument(
        "--selector",
        default="table",
        help="CSS selector to extract tabular web content (default: table).",
    )
    parser.add_argument(
        "--preview-rows",
        type=int,
        default=5,
        help="Number of rows to print from the loaded dataset.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    from thermokarst.config import PipelineConfig
    from thermokarst.pipeline import run_basic_workflow

    config = PipelineConfig(
        source=args.source,
        path=args.path,
        url=args.url,
        selector=args.selector,
    )

    df = run_basic_workflow(config)
    print(f"Loaded dataset with shape: {df.shape}")
    print(df.head(args.preview_rows).to_string(index=False))


if __name__ == "__main__":
    main()
