import requests 
from bs4 import BeautifulSoup
import json
import re 
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'
number = input(f"""{k}
 _____               _         _  _   
|  ___|             | |       (_)| |  
| |__  __  __ _ __  | |  ___   _ | |_ 
|  __| \ \/ /| '_ \ | | / _ \ | || __|     {lrd}searcher{k}
| |___  >  < | |_) || || (_) || || |_ 
\____/ /_/\_\| .__/ |_| \___/ |_| \__|
             | |                      
             |_|                   

{lrd}[{g}1{lrd}] {gn}Search on GitHub\n\n{lrd}[{g}2{lrd}] {gn}Search on packetstorm\n\n{lrd}[{lgn}+{lrd}] {gn}Enter Number : {cn}""")
NAME = input(f"\n\n{lrd}[{k}+{lrd}] {gn}Enter the name of what you are looking for : {cn}")
interesting = ['root', 'code execution', 'exploit', 'command','execute','malicious','payload',
                'remote','code','execution','arbitrary','information','leak', 
                'vulnerability', 'unrestricted', 'remotely',
                'remote-code-execution','PoC','poc','POC']
                
def PRINT(key_string, value_string,color='Kos?',end=True): 
    if end == True: 
        print(f"{gn}{(key_string)} : {gn}{(value_string)}")
        return
    print(f"{cn}{(key_string)} : {gn}{value_string}")    
def PACKETSTORM():
    text = requests.get(f"https://packetstormsecurity.com/search/?q={NAME}").text
    URLB = 'https://packetstormsecurity.com'
    n_pages = list(set(re.findall(r'href="/search/files/page(\d)/\?q=.*?"',text))) 
    n_pages_len = len(n_pages)
    all_page_urls = [f"https://packetstormsecurity.com/search/files/page{i}/?q={NAME}" for i in range(1,n_pages_len+1)]     
    for link in all_page_urls: 
        soup = BeautifulSoup(requests.get(link).content, 'html.parser')
        exploit_frames = soup.find('div', {'id':'m'}).find_all('dl')
        for frame in exploit_frames:             
            LINKS = frame.find('dt').a['href'] 
            TITLES = frame.find('dt').a.text 
            DATE = frame.find('dd', class_='datetime').a.text
            DEC = frame.find('dd', class_='detail').p.text
            TAGS = ''.join([str(a.text).replace('tags | ','') for a in frame.find_all('dd', class_='tags')]) 
            CVE = ''.join([str(dd.text).replace('advisories | ','') for dd in frame.find_all('dd', class_='cve') ]) 
            SYSTEM = ''.join([str(dd.text).replace('systems | ','') for dd in frame.find_all('dd', class_='os') ])             
            compare_interesting = [i.lower() for i in TITLES.split(' ')] 
            if  any(item in interesting for item in compare_interesting) : TITLES = (f'{TITLES}, {lgn}')            
            split_tags = [t.strip() for t in TAGS.split(',')]
            if any(item in interesting for item in split_tags): TAGS = (f'{TAGS}, {gn}')           
            DEC = DEC.split(' ')
            colored_description = []
            for word in DEC:                
                if word in interesting:colored_description.append((f'{word},{lgn}'))
                else: colored_description.append(word)            
            DEC = ' '.join(colored_description)
            print (f"{yw}=====================================")
            PRINT('\nTitle ', TITLES)
            PRINT('\nSummary ', DEC)
            if CVE: 
                PRINT(f'\n{lrd}Cve ', CVE)
            if SYSTEM: 
                PRINT('\nSystems ', SYSTEM)
            PRINT(f'\n{rd}Tags ', TAGS)     
            PRINT('\nDate ', DATE)
            PRINT('\nUrl ', f'{URLB+LINKS}')

def GITHUB():
	headers={'Accept':'application/vnd.github.v3+json'}
	jres = json.loads(requests.get(f'https://api.github.com/search/repositories?q={NAME}+PoC+&sort=stars&order=desc').text)
	for i in jres['items']: 
	    repo_name,description,html_link,create_date = i['full_name'],i['description'],i['html_url'],str(i['created_at'])[:10]
	    forks,language,ftags,last_updated = i['forks_count'],i['language'],i['topics'],str(i['updated_at'])[:10]                
	    tags = []
	    for i in ftags: 
	        if i in interesting: tags.append((f'{i}, {lrd}'))
	        else: tags.append(i)
	    tags = ', '.join(tags)
	    print (f"{yw}=====================================") 
	    PRINT('Title ', repo_name, end=True)
	    if description: PRINT('Summary ', description)
	    print(f"{gn}{('PUBLISHED')} : {rd}{create_date} {yw}| {cn}{('UPDATED')} : {k}{last_updated}")
	    if tags: PRINT('Tags ', tags)   
	    print(f"{gn}{('LANGUAGE')} : {rd}{language}{yw} | {cn}{('FORKS')} : {k}{forks}")
	    PRINT('Url ', html_link)        
	    
if number == '1': GITHUB()
elif number == '2': PACKETSTORM()
