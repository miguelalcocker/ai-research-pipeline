# Installation & Execution Guide

## Prerequisites

- **Python 3.8+** (tested on Python 3.8, 3.9, 3.10, 3.11)
- **Internet connection** (for API access)
- **~500MB free disk space** (for output files and cache)

## Quick Start (Automated Installation)

The script automatically installs all required dependencies. Simply run:

```bash
python extract_ai_research_data.py
```

The script will:
1. Check for missing packages
2. Auto-install them via pip
3. Start the data extraction process

**Estimated runtime:** 15-30 minutes

## Manual Installation (Optional)

If you prefer to install dependencies manually:

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install individually
pip install requests pandas numpy pyyaml tqdm python-dateutil geopy jinja2
```

## Configuration

### Basic Configuration
The `config.yaml` file contains all configurable parameters:

- **Data collection limits**: `min_papers`, `max_papers`
- **Date range**: `start_year`, `end_year`
- **API settings**: Rate limits, timeouts
- **AI subfield keywords**: Customize classification
- **Quality thresholds**: Minimum abstract length, etc.

### OpenAlex API Email (Optional)

For faster rate limits, add your email to `config.yaml`:

```yaml
apis:
  openalex:
    email: "your.email@example.com"  # Gets you into the "polite pool"
```

No API key needed - OpenAlex is completely open!

### Adjusting Data Volume

To extract fewer papers (faster execution):

```yaml
data_collection:
  min_papers: 1000
  max_papers: 5000
```

To extract more papers (richer dataset):

```yaml
data_collection:
  min_papers: 10000
  max_papers: 20000
```

## Execution

### Standard Execution

```bash
python extract_ai_research_data.py
```

### With Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Run script
python extract_ai_research_data.py

# Deactivate when done
deactivate
```

### Check Progress

The script provides:
- **Real-time progress bars** for each stage
- **Console output** with current status
- **Log file**: `output/logs/extraction_log.txt`

You can tail the log in another terminal:

```bash
tail -f output/logs/extraction_log.txt
```

## Output Files

After successful execution, you'll find:

```
output/
├── data/
│   ├── fact_publications.csv
│   ├── dim_authors.csv
│   ├── dim_institutions.csv
│   ├── dim_venues.csv
│   └── dim_time.csv
├── logs/
│   ├── extraction_log.txt
│   └── data_quality_report.html
└── README.md
```

## Troubleshooting

### Issue: "Connection timeout" or "Rate limit exceeded"

**Solution:** Increase the rate limit delay in `config.yaml`:

```yaml
apis:
  openalex:
    rate_limit_delay: 0.5  # Increase from 0.1 to 0.5
```

### Issue: "Not enough publications extracted"

**Possible causes:**
1. Overly restrictive filters
2. Network issues during extraction

**Solutions:**
- Broaden the search terms in `config.yaml` → `core_concepts`
- Increase `max_papers` limit
- Check your internet connection

### Issue: "ModuleNotFoundError"

**Solution:** The auto-installer should handle this, but if it fails:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: Script runs but no CSV files generated

**Solution:** Check the logs:

```bash
cat output/logs/extraction_log.txt
```

Look for error messages indicating what went wrong.

## Performance Optimization

### Speed Up Execution

1. **Reduce paper count**: Lower `max_papers` in config
2. **Disable geocoding**: Set `geocoding.enabled: false` in config
3. **Use cached data**: Re-running the script uses cached API responses

### Reduce Output Size

1. **Shorter abstracts**: Reduce `max_abstract_length` in config
2. **Fewer dimension details**: Comment out optional fields in code
3. **Sample data**: Add sampling logic to extract functions

## Testing

### Quick Test (Small Dataset)

Edit `config.yaml`:

```yaml
data_collection:
  min_papers: 100
  max_papers: 500
```

Run:

```bash
python extract_ai_research_data.py
```

Should complete in ~5 minutes.

### Verify Output

Check that all CSVs are generated:

```bash
ls -lh output/data/
```

You should see 5 CSV files.

Open the quality report:

```bash
# Linux
xdg-open output/logs/data_quality_report.html

# Mac
open output/logs/data_quality_report.html

# Windows
start output/logs/data_quality_report.html
```

## Advanced Usage

### Custom Filters

To focus on specific research areas, edit `config.yaml` → `core_concepts`:

```yaml
core_concepts:
  - "graph neural network"
  - "reinforcement learning"
  # Add your specific topics here
```

### Adding More APIs

The code structure supports multiple APIs. To enable Semantic Scholar:

1. Set `enabled: true` in `config.yaml`:

```yaml
apis:
  semantic_scholar:
    enabled: true
```

2. Implement enrichment logic in `extract_ai_research_data.py`

### Custom Metrics

To add your own metrics, modify the `MetricsCalculator` class:

```python
@staticmethod
def calculate_custom_metric(paper: Dict) -> float:
    # Your custom logic here
    return score
```

Then add it to the publications data in `extract_publications()`.

## System Requirements

**Minimum:**
- 2GB RAM
- 1 CPU core
- 500MB disk space

**Recommended:**
- 4GB+ RAM
- 2+ CPU cores
- 2GB disk space

**Network:**
- Stable internet connection
- ~100-500 MB data download (depending on paper count)

## Getting Help

If you encounter issues:

1. Check `output/logs/extraction_log.txt` for detailed errors
2. Review this guide's troubleshooting section
3. Verify your Python version: `python --version`
4. Check package versions: `pip list`

## Next Steps

After successful extraction:

1. ✅ Review `output/logs/data_quality_report.html`
2. ✅ Read `output/README.md` for dataset documentation
3. ✅ Import CSVs into Power BI
4. ✅ Build your visualizations!

---

**Happy extracting!** 🚀
