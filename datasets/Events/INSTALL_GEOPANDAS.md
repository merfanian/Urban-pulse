# Installing Geopandas (Optional)

Geopandas provides better accuracy for neighborhood assignment using shapefiles, but it requires system libraries.

## Installation Instructions for Fedora:

1. **Install system dependencies:**
   ```bash
   sudo dnf install gdal-devel proj-devel geos-devel gdal
   ```

2. **Activate your virtual environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install geopandas:**
   ```bash
   pip install geopandas
   ```

## Note:

If you don't install geopandas, the notebook will automatically fall back to using reverse geocoding via the Nominatim API. This works but is slower and may be slightly less accurate than using the Chicago Community Areas shapefile.

