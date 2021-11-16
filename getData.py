import requests
import gzip
import os
import shutil

 
#Download the needed files from the Eurostat Database
url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tour_occ_nim.tsv.gz'
r = requests.get(url, allow_redirects=True)
open('Nights spent at tourist accommodation establishments_compressed','wb').write(r.content)
 
url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tour_occ_ninrmw.tsv.gz'
r = requests.get(url, allow_redirects=True)
open('Nights spent by non-residents at tourist accommodation establishments_compressed', 'wb').write(r.content)
 
 
url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tour_occ_arm.tsv.gz'
r = requests.get(url, allow_redirects=True)
open('Arrivals at tourist accommodation establishments_compressed', 'wb').write(r.content)
 
 
url = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tour_occ_arnrmw.tsv.gz'
r = requests.get(url, allow_redirects=True)
open('Arrivals of non-residents at tourist accommodation establishments_compressed', 'wb').write(r.content)
 
 
#Unpackage the files and convert them from .gz to tsv
with gzip.open('Nights spent at tourist accommodation establishments_compressed', 'rb') as f_in:
   with open('Nights spent at tourist accommodation establishments', 'wb') as f_out:
       shutil.copyfileobj(f_in, f_out)
with gzip.open('Nights spent by non-residents at tourist accommodation establishments_compressed', 'rb') as f_in:
   with open('Nights spent by non-residents at tourist accommodation establishments', 'wb') as f_out:
       shutil.copyfileobj(f_in, f_out)
 
with gzip.open('Arrivals at tourist accommodation establishments_compressed', 'rb') as f_in:
   with open('Arrivals at tourist accommodation establishments', 'wb') as f_out:
       shutil.copyfileobj(f_in, f_out)
 
with gzip.open('Arrivals of non-residents at tourist accommodation establishments_compressed', 'rb') as f_in:
   with open('Arrivals of non-residents at tourist accommodation establishments', 'wb') as f_out:
       shutil.copyfileobj(f_in, f_out)               
 
 
#Delete the .gz files
os.remove("Nights spent at tourist accommodation establishments_compressed")     
os.remove("Nights spent by non-residents at tourist accommodation establishments_compressed")   
os.remove("Arrivals at tourist accommodation establishments_compressed")   
os.remove("Arrivals of non-residents at tourist accommodation establishments_compressed")