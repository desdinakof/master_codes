##################### SCRAPING WEBSITE ######################
# Import Libraries
##from bs4 import BeautifulSoup
from os.path import dirname, abspath, basename
##import requests
### Declare base information 
##base_url = 'http://www.cde.ca.gov/ds/sp/ai/'
basedir = dirname(dirname(abspath(__file__))) + '/california/'
### start scraping the main page
##page = requests.get(base_url).text
##soup = BeautifulSoup(page, 'lxml') # read the content with BeautifulSoup
##hrefs = [a['href'] for a in soup.findAll('a', href = True)] # scrape all urls
##xls = [href for href in hrefs if 'xls' in href] # extract all urls wnding with 'xls'
##for url in xls:
##    filename = basedir+ basename(url)
##    with open(filename, 'wb+') as f:
##        print(url)
##        try: # in some cases, the initial url works
##            data = requests.get(url).content
##            f.write(data)
##        except: # in some other cases, only the final path is supplied, and we have to add the base_url
##            url = base_url + url
##            data = requests.get(url).content
##            f.write(data)
##        f.close()


######################### ANALYSIS ############################
# Import Libraries
import glob # we use this library to manage files and upload them - alternative code
import pandas as pd # we use this library to manage xls files once uploaded
import numpy as np # we use this library to run statistical analyses

# Read .xls files: 14-16 first
sat_data = pd.DataFrame()
act_data = pd.DataFrame()
ap_data = pd.DataFrame()

##years = [14,15,16]
##types = ['sat','act','ap']
years = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','99','00']
types = ['sat','act']

foo = {t : pd.DataFrame() for t in types} # generate a dictionary with a key for each type
for t in types: #for each data type
    for y in years: # for each year
        filedir = basedir + t + y + '.xls'
        print(int(y))
        if (int(y) >= 0 and int(y) <= 8) or int(y) == 99:
            df = pd.read_excel(filedir, header = 1, skiprows = 1)
            df['cds'] = df['County\nNumber'].astype(str) + df['District\nNumber'].astype(str) + df['School\nNumber'].astype(str) # generate the CDS variable from the county/district/school variables
            df['cds'] = pd.to_numeric(df['cds'])
        elif int(y) == 10 and t == 'sat':
            df = pd.read_excel(filedir, header = 1, skiprows = 3)
        elif int(y) >= 9 and int(y) <= 13:
            df = pd.read_excel(filedir, header = 1, skiprows = 2)
        else:
            df = pd.read_excel(filedir, header = 0)
        

##        print(filedir)
##        df = pd.read_excel(filedir, header = 1, skiprows = 1)
##        print(df.head())
        df.rename(columns = lambda x: x.replace('\n',' ').replace('\n',' ').replace('\n',' '), inplace = True) # rename columns
        #print(df['year'])
        #print(df.cds.head())
        #print(df.head())
        foo[t] = foo[t].append(df,ignore_index = True)

##print(foo['sat'].columns)
##print(foo['sat'].describe())
##foo['act'].describe()

df = foo['sat']
data = df.loc[df['rtype'] == 'S']
print(data)

##y = '06'
##types = ['sat','act']
##for t in types: #for each data type
##    filedir = basedir + t + y + '.xls'
##    df = pd.read_excel(filedir, header = 2)
##    #print(df['year'])
##    #print(df.cds.head())
##    df.rename(columns = lambda x: x.replace('\n',' ').replace('\n',' ').replace('\n',' '), inplace = True) # rename columns
##    print(df.columns)
