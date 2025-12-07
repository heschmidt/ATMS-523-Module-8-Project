import cdsapi
from pathlib import Path

OUTDIR = Path("ATMS523_module8_project")
OUTDIR.mkdir(parents=True, exist_ok=True)

DATASET = "reanalysis-era5-land-monthly-means"

YEARS = [str(y) for y in range(1950, 2025)] 
MONTHS = ["06", "07", "08"]                

AREA = [51.0,-126.5,30.0,-69.5,]
 
TARGET = OUTDIR / "era5land_monthly_Tmean_JJA_1950_2024_UScities.nc"

def main():
    c = cdsapi.Client()

    request = {
        "format": "netcdf",
        "product_type": "monthly_averaged_reanalysis",
        "variable": [
            "2m_temperature",
        ],
        "year": YEARS,
        "month": MONTHS,
        "time": "00:00",
        "area": AREA,  
    }

    c.retrieve(DATASET, request, str(TARGET))

if __name__ == "__main__":
    main()
