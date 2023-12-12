import urllib.request
import zipfile
from io import BytesIO

def download_and_unzip(url, extract_to='.'):
    # Download the zip file
    response = urllib.request.urlopen(url)
    zip_content = response.read()
    
    # Unzip the file in memory
    with zipfile.ZipFile(BytesIO(zip_content)) as zf:
        zf.extractall(path=extract_to)

def main():
    cms_url = "https://www.cms.gov/research-statistics-data-and-systems/downloadable-public-use-files/synpufs/downloads/"
    mbsf_2008_prefix = "de1_0_2008_beneficiary_summary_file_"
    mbsf_2009_prefix = "de1_0_2009_beneficiary_summary_file_"
    mbsf_2010_prefix = "de1_0_2010_beneficiary_summary_file_"
    inpatient_prefix = "de1_0_2008_to_2010_inpatient_claims_"

    partition_id_list = [f"Sample_{i}" for i in list(range(1,21))]

    # There is an error in the url path for 2010 mbsf sample 1 data, so the 2010 folder only has 19 files

    for partition_id in partition_id_list:
        #download mbsf data
        mbsf_2008_url = cms_url + mbsf_2008_prefix + partition_id + ".zip"
        download_and_unzip(mbsf_2008_url, extract_to="../downloads/beneficiary_summaries/2008/")
        
        mbsf_2009_url = cms_url + mbsf_2009_prefix + partition_id + ".zip"
        download_and_unzip(mbsf_2009_url, extract_to="../downloads/beneficiary_summaries/2009")
        
        mbsf_2010_url = cms_url + mbsf_2010_prefix + partition_id + ".zip"
        if partition_id != 'Sample_1': #there is an error in source data
            download_and_unzip(mbsf_2010_url, extract_to="../downloads/beneficiary_summaries/2010")
        
        #download inpatient data 
        inpatient_url = cms_url + inpatient_prefix + partition_id + ".zip"
        download_and_unzip(inpatient_url, extract_to="../downloads/inpatient_claims/")


if __name__ == "__main__":
    main()