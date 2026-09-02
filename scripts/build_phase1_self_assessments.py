"""Compatibility entry point for the Phase 1 evidence workflow.

The former generator encoded the project that was replaced. Individual
evidence must not be regenerated from generic answers because it belongs to
each student. Benjamín's reviewed documents are maintained through
``fill_benjamin_phase1.py``. Daniel and Felipe must complete their own source
templates before a generator is added for them.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    benjamin = ROOT / "scripts" / "fill_benjamin_phase1.py"
    project_docs = ROOT / "docs" / "00-official-source.md"
    raise SystemExit(
        "No se generan autoevaluaciones individuales automáticamente. "
        f"Use {benjamin} para la evidencia revisada de Benjamín y "
        f"consulte {project_docs} para la definición vigente de Fix & Go."
    )


if __name__ == "__main__":
    main()
