#!/usr/bin/env python3
"""Convert an HTML file to a PNG image."""

import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright


def html_to_png(
    input_path: Path,
    output_path: Path | None = None,
    *,
    width: int = 1280,
    height: int = 720,
    full_page: bool = True,
) -> Path:
    input_path = input_path.resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"HTML file not found: {input_path}")

    if output_path is None:
        output_path = input_path.with_suffix(".png")
    else:
        output_path = output_path.resolve()

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(input_path.as_uri(), wait_until="networkidle")
        page.screenshot(path=str(output_path), full_page=full_page)
        browser.close()

    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert an HTML file to PNG.")
    parser.add_argument("input", type=Path, help="Path to the HTML file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output PNG path (default: same name as input with .png extension)",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1280,
        help="Viewport width in pixels (default: 1280)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=720,
        help="Viewport height in pixels (default: 720)",
    )
    parser.add_argument(
        "--no-full-page",
        action="store_true",
        help="Capture only the viewport instead of the full page",
    )
    args = parser.parse_args()

    output = html_to_png(
        args.input,
        args.output,
        width=args.width,
        height=args.height,
        full_page=not args.no_full_page,
    )
    print(f"Saved: {output}")


if __name__ == "__main__":
    main()
