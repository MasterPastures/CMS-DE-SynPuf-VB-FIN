This folder contains a Python script to download the synthetic Medicare data (DE-SynPUF) from CMS and Jupyter notebooks to perform exploratory data analysis on it.


## downloads
#### beneficiary_summaries
The Excel files containing the beneficiary summary data dating from 2008 to 2010 live here.

#### inpatient_claims
The Excel files containing the inpatient claim data dating from 2008 to 2010 live here.

## notebooks
The EDA of the beneficiary summary and inpatient claims data lives here. The notebook for the beneficiary summary EDA should be ran first, as it provides the DataFrame to join the inpatient claims data with. `NOTE: The beneficiary summary notebook will recursively search for all of the downloaded files using glob() to construct the DataFrames. Please allocate appropriate compute to your Jupyter instance.`

## scripts
The script lives at `CMS-DE-SynPuf-VB/scripts/download_cms_data.py`. You can execute it by running `python download_cms_data.py` from the command line or a terminal. `NOTE:` the 2010 beneficiary summary data for sample 1 is missing because the associated hyperlink is broken; the script will therefore only download 19 files instead of 20 within the `CMS-DE-SynPuf-VB/downloads/beneficiary_summaries/2010` directory.
