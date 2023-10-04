import requests
from bs4 import BeautifulSoup
import re
import tldextract
import os

# We should give the link extensions by hand due to the web page standard

def get_links(url):
    r = requests.get(url)
    html_content = r.text
    soup = BeautifulSoup(html_content, features="html.parser")
    if soup:
        links = []
        for tag in soup.find_all('a', href=True):
            links.append(tag['href'])
    else:
        print("soup:" + soup)
    
    return links
        
def filter_links(links, start_url):
    ext = tldextract.extract(start_url)
    domain = ext.domain
    filtered_links = []
    for link in links:
        if domain in link:
            filtered_links.append(link)
    return filtered_links

def download_department_articles(departments):
    main_url = "https://dergipark.org.tr"
    for branch in departments:
        folder_path = './' + branch.replace('+', '') + '/'
        # Creating directory same with the name of department
        try:
            os.mkdir(folder_path)
        except OSError as error:
            print(error)  
            
        print("[*] STARTING DOWNLOAD "+ branch + " [*]")
        start_url = "https://dergipark.org.tr/tr/search/3?q=" + branch + "&section=articles&aggs%5BarticleType.id%5D%5B0%5D=55"
        links = get_links(start_url)

        filtered_links =filter_links(links, start_url)
        
        pdflinks = []
        
        if filtered_links:
            for line in filtered_links:
                if re.search("issue", line):
                    #print(line)
                    pdflinks.append(line)
                    
            #print(pdflinks)
            
            for dlink in pdflinks:
                links = get_links(dlink)
                #b = requests.get(dlink)
                # to see content to determine which element we will take
                #print(b.content)
                #print(pdflinks[0])

                download = []
                for link in links:
                    if "download" in link:
                        download.append(link)
                        
                if download[0]:            
                    print ("-------------")
                    print(main_url + download[0])
                    print ("-------------\n")
                    pdfurl = main_url + download[0]
                    r = requests.get(pdfurl, stream=True)
                    fname = str(download[0].split("/")[-1:])
                    #print(fname)
                    with open(folder_path + fname + ".pdf", 'wb') as fd:
                        for chunk in r.iter_content(2048):
                            fd.write(chunk)
                else:
                    print("There is no download link")
                    print("download[0]):" + download[0])
                    continue
                                         
        else:
           print("Not downloaded for links:" + ' '.join(filtered_links))
           continue            
