#-------------------Importing Liberaries---------------------#

try:
  from bs4 import BeautifulSoup # extracting data and parsing!
  from numpy import * # img number generation!
  import pandas as pd # data manipulating!
  import urllib.request # url requesting and opening!
  import os # creating dirs!
  import re # compiling https requests!

except Exception as e: # if not found print the error!
  print('Missing Packages! \n\n {}'.format(e))
  
#--------------------Request and Declaration--------------------------#

page = urllib.request.urlopen('https://zaak.azurewebsites.net/work.html') # requesting and opening!
soup = BeautifulSoup(page, features='html.parser') # declaring bs4!
links = [] # array of links with https!
images = [] # array of images links!
category = [] # array of alts categories!
source = [] # arry of sources!

#--------------------Extraction Data--------------------------#

for extract_links_source in soup.findAll('a', attrs={'href': re.compile("^https://")}): # finding all links in https
    links.append(extract_links_source.get('href')) # adding founded links to the links[] array!
    source.append(extract_links_source.get('i')) # adding extracted sources!

for extract_img_cate in soup.findAll('img'): # finding all images and alternatives!
    images.append('https://zaak.azurewebsites.net/'+extract_img_cate.get('src')) # concating pageLink+imgName
    category.append(extract_img_cate.get('alt')) # adding extracted image category!
    
#---------------------Checking Extracted Data-------------------------#

#print('Urls Links: {} \n\nImages Links: {} \n\nImg Category: {}'.format(links,images,category)) # printing extracted data!

#-----------------Creating Directories-----------------------------#

if not os.path.exists('data'): # checking if the dirs are exists, if not create new!
    os.mkdir('data') # creating parent folder dir!
    os.mkdir('data/scraped_data') # creating child folder dir(testing)!
    os.mkdir('data/dataset') # creating child folder dir(dataset)!
    
#--------------------Writing Extracted Data To .txt File--------------------------#

with open(f'data/scraped_data/{random.randint(100)}.txt', 'w') as extract: # creating .txt file data!
    extract.write(str(links)) # writing links collected to the txt file!
    extract.write('\n\n') # making space between lines!
    extract.write(str(images)) # writing images collected to the txt file!
    extract.write('\n\n') # making space between lines!
    extract.write(str(category)) # writing collected image categories to the txt file!
    extract.write('\n\n') # making space between lines!
    extract.write(str(source)) # writing collected project source to the txt file!
    
#-----------------Merge and Saving Data To .csv File-----------------------------#

zipList = list(zip(links,images,category,source)) # merging all arrays in one list!
#print(zipList) # printing it to check if it got merged and converted to a list!
df = pd.DataFrame(zipList, columns=['Links','Images','Category','Source']) # converting merged data to DataFrame and given it columns names!
df.fillna('GitHub', inplace=True)
print(df) # printing the DataFrame!
df.to_csv('data/dataset/dataset.csv', index=False) # converting it to a csv file.

#----------------------------------------------#

