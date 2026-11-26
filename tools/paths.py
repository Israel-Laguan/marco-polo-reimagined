"""Repository paths shared by the manuscript tools."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT = ROOT / "manuscript"
RESEARCH = ROOT / "research"
REGISTRY = RESEARCH / "registry"
EDITORIAL = ROOT / "editorial"
MATERIALS = ROOT / "materials"
ASSETS = MANUSCRIPT / "assets"
BIBLIOGRAPHY = MANUSCRIPT / "bibliography.bib"
