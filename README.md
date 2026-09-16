# refaktorering_orderrapportering
Individuell inlämningsuppgift

## Miljö
- Python 3.13.13
- Beroenden: pandas (körning), pytest (tester) – definierade i `pyproject.toml`

## Kom igång

    # klona projektet
    git clone https://github.com/MalinMo/refaktorering_orderrapportering.git
    
    # Skapa och aktivera virtuell miljö
    python -m venv .venv
    .venv\Scripts\activate      # Windows
    # source .venv/bin/activate   # macOS/Linux
    
    # installera beroenden + testberoenden
    pip install -e ".[test]"

`pip install -e ".[test]"` installerar projektet i "editable"-läge (ändringar
i koden slår igenom direkt utan ominstallation) tillsammans med pytest, som
är definierat under `[project.optional-dependencies]` i `pyproject.toml`.

## Köra programmet
Lägg indatan i `data/orders.csv` (eller ändra sökvägen via `ReportConfig`),
kör sedan:

    python -m order_report

Programmet loggar sin körning i terminalen och sparar fyra rapporter i
`output/` (mappen skapas automatiskt om den saknas):

- `overview.csv` – övergripande nyckeltal
- `sales_by_category.csv` – försäljning per produktkategori
- `sales_by_region.csv` – försäljning per region
- `returns_by_category.csv` – returer per produktkategor

## Projektstruktur

    src/order_report/
        __init__.py             Publikt API (ReportConfig, run_report)
        __main__.py             Startpunkt (python -m order_report)
        config.py               ReportConfig – sökvägar för in- och utdata
        validation.py           Validering och städning av indata
        processing.py           Beräkningar och sammanställningar
        io.py                   Inläsning och sparande av csv-filer
        pipeline.py             Orkestrerar hela flödet (run_report)
        logging_config.py       Central konfiguration av loggning

    tests/
        test_validation.py
        test_processing.py
        test_io.py

    code_review.md              Kodgranskning av originalkoden
    reflection.md               Reflektion kring refaktoreringen

## Kodgranskning
Se `code_review.md` för en genomgång av problemen i originalkoden och de förbättringar som gjordes.

## Reflektion
Se `reflection.md` för en kort reflektion kring refaktoreringen.