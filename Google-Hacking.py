import requests,platform,os
from bs4 import BeautifulSoup
try:from googlesearch import search
except:os.system("pip install google-search")
from urllib.parse import urljoin
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'
def clear():
	if 'Windows' in platform.uname():
		from colorama import init
		init()
		os.system("cls")
	elif 'Windows' not in platform.uname():
		os.system("clear")
clear()
o = input(f"""{k}
 .d8888b.                             888          
d88P  Y88b                            888          
888    888                            888          
888         .d88b.   .d88b.   .d88b.  888  .d88b.  
888  88888 d88""88b d88""88b d88P"88b 888 d8P  Y8b 
888    888 888  888 888  888 888  888 888 88888888   {lrd}Hacking{k}
Y88b  d88P Y88..88P Y88..88P Y88b 888 888 Y8b.     
 "Y8888P88  "Y88P"   "Y88P"   "Y88888 888  "Y8888  
                                  888              
                             Y8b d88P              
                              "Y88P"               

          {gn}Channel : {rd}@esfelurm

{lrd}[{lgn}1{lrd}] {gn}Getting a list of sites with Dork {rd}[Singel]\n\n{lrd}[{lgn}2{lrd}] {gn}Getting a list of sites with Dork {rd}[file.txt]\n\n{lrd}[{lgn}3{lrd}] {gn}Find site directories\n\n{lrd}[{lgn}4{lrd}] {gn}Find subdomains \n\n{lrd}[{lgn}5{lrd}] {gn}Find the admin panel\n\n{lrd}[{lgn}+{lrd}] {g}Enter Number : {cn}""")
def dork_Singel():
    clear()
    print (f"""{k}
                  _,.---._                    ,--.-.,-.  
  _,..---._     ,-.' , -  `.     .-.,.---.   /==/- |\  \ 
/==/,   -  \   /==/_,  ,  - \   /==/  `   \  |==|_ `/_ / 
|==|   _   _\ |==|   .=.     | |==|-, .=., | |==| ,   /  
|==|  .=.   | |==|_ : ;=:  - | |==|   '='  / |==|-  .|   {rd}Single{k}
|==|,|   | -| |==| , '='     | |==|- ,   .'  |==| _ , \  
|==|  '='   /  \==\ -    ,_ /  |==|_  . ,'.  /==/  '\  | 
|==|-,   _`/    '.='. -   .'   /==/  /\ ,  ) \==\ /\=\.' 
`-.`.____.'       `--`--''     `--`-`--`--'   `--`           
    \n""")
    try:
    	dork,page,time,save = input(f"{lrd}[{lgn}+{lrd}] {lgn}Dork File List{k}: {cn}"),int(input(f"{lrd}[{lgn}+{lrd}] {lgn}Number Page{k} : {cn}")),int(input(f"{lrd}[{lgn}+{lrd}] {lgn}Timeout {k}: {cn}")),input(f"{lrd}[{lgn}+{lrd}] {lgn}save location : {k}")
    	nyx = 0
    	for i in search(dork, tld="com", lang="en", num=int(page), start=0, stop=None, pause=int(time)):
    		with open(save, 'a') as f:
    			f.write(f'{i}\n')
    		nyx += 1
    		print(f'\n{lrd}[{lgn}{nyx}{lrd}] {yw}=>> [{k}{i}{lrd}]')
    		if nyx >= int(time):
    			break;
    	print(f'\n{yw}------------------------\n{lrd}[{lgn}+{lrd}] {gn}Saved : {lgn}{save}\n{lrd}[{lgn}+{lrd}] {gn}Number of sites found: {k}{nyx}')
    except ValueError:
    	exit(f'{lrd}[{rd}-{lrd}] {rd}Error Input')
    except KeyboardInterrupt:
    	exit(f'{lrd}[{rd}-{lrd}] {rd}Error')
    	
def dork_List():
    clear()
    print (f"""{k}
 ;                                            
 ED.               :                          
 E#Wi             t#,                 G:      
 E###G.          ;##W.    j.          E#,    :
 E#fD#W;        :#L:WE    EW,         E#t  .GE
 E#t t##L      .KG  ,#D   E##j        E#t j#K;
 E#t  .E#K,    EE    ;#f  E###D.      E#GK#f  
 E#t    j##f  f#.     t#i E#jG#W;     E##D. {rd}file{k}  
 E#t    :E#K: :#G     GK  E#t t##f    E##Wi {rd}mod{k}  
 E#t   t##L    ;#L   LW.  E#t  :K#E:  E#jL#D: 
 E#t .D#W;      t#f f#:   E#KDDDD###i E#t ,K#j
 E#tiW#G.        f#D#;    E#f,t#Wi,,, E#t   jD
 E#K##i           G#t     E#t  ;#W:   j#t     
 E##D.             t      DWi   ,KK:   ,;     
 E#t                                          
 L:                                               
    \n""")
    try:
    	dork,page,time,save = input(f"{lrd}[{lgn}+{lrd}] {lgn}Dork File List{k}: {cn}"),int(input(f"{lrd}[{lgn}+{lrd}] {lgn}Number Page{k} : {cn}")),int(input(f"{lrd}[{lgn}+{lrd}] {lgn}Timeout {k}: {cn}")),input(f"{lrd}[{lgn}+{lrd}] {lgn}save location : {k}")
    	f = open(dork,'r')
    	nyx = 0
    	for file in f:
    	    for i in search(file, tld="com", lang="en", num=page, start=0, stop=None, pause=int(time)):
    		    with open(save, 'a') as f:
    		    	f.write(f'{i}\n')
    		    	nyx += 1
    		    	print(f'\n{lrd}[{lgn}{nyx}{lrd}] {yw}=>> [{k}{i}{lrd}]')
    		    if nyx >= int(page):
    		    	break
    		    print(f'\n{yw}------------------------\n{lrd}[{lgn}+{lrd}] {gn}Saved : {lgn}{save}\n{lrd}[{lgn}+{lrd}] {gn}Number of sites found: {k}{nyx}')
    except ValueError:
    	exit(f'{lrd}[{rd}-{lrd}] {rd}Error Input')
    except KeyboardInterrupt:
    	exit(f'{lrd}[{rd}-{lrd}] {rd}Error')	

def dir(url, visited_urls=None, depth=0):    
    if visited_urls is None:
        visited_urls = set()   
    if depth > 3: 
        return    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            for link in soup.find_all('a', href=True):
                href = link['href']
                absolute_url = urljoin(url, href)                 
                if absolute_url not in visited_urls:
                    print(f"\n{lrd}[{lgn}+{lrd}] {cn}directory was found :{lgn} {absolute_url}")                            	
                    visited_urls.add(absolute_url)
                    dir(absolute_url, visited_urls, depth + 1) 
    except requests.exceptions.RequestException as e:
        print(f'{lrd}Request error: {rd}{e}')
def sub():
    target = input(f"""
    
{lrd}+-++-++-++-++-++-++-++-++-++-+
{rd}|{lgn}s{k}||{lgn}u{k}||{lgn}b{k}||{lgn}d{k}||{lgn}o{k}||{lgn}m{k}||{lgn}a{k}||{lgn}i{k}||{lgn}n{k}||{lgn}s{rd}|
{lrd}+-++-++-++-++-++-++-++-++-++-+

{lrd}[{lgn}+{lrd}] {gn}Enter URL Target {cn}[Ex : https://google.com] {gn}: {k}""")     
    link_list = open('/file/sub.txt', 'r').read().split()
    for List in link_list:
    	f = target+'/'+List
    	req = requests.get(f)
    	if '404' in req.text: print (f'\n{lrd}[{yw}NO{lrd}] {lrd}Page not found : {lrd}[ {lrd}{target}/{cn}\033[41m{List}\033[0m{lrd} ]')
    	else: print (f'\n{lrd}[{lgn}OK{lrd}]{lgn} Page found : {lrd}[ \033[42m{target}/{List}\033[0m{lrd} ]')

def admin():
    target = input(f"""{k}
 _______  ______   _______ _________ _       
(  ___  )(  __  \ (       )\__   __/( (    /|
| (   ) || (  \  )| () () |   ) (   |  \  ( |
| (___) || |   ) || || || |   | |   |   \ | |
|  ___  || |   | || |(_)| |   | |   | (\ \) |
| (   ) || |   ) || |   | |   | |   | | \   |
| )   ( || (__/  )| )   ( |___) (___| )  \  |
|/     \|(______/ |/     \|\_______/|/    )_)

{lrd}[{lgn}+{lrd}] {gn}Enter URL Target {cn}[Ex : https://google.com] {gn}: {k}""")     
    link_list = open('/file/admin.txt', 'r').read().split()    
    for List in link_list:
		    s = target+'/'+List
		    req = requests.get(s)
		    if '404' in req.text: print (f'\n{lrd}[{yw}NO{lrd}] {lrd}Page not found : {lrd}[ {lrd}{target}/{cn}\033[41m{List}\033[0m{lrd} ]')
		    else: print (f'\n{lrd}[{lgn}OK{lrd}]{lgn} Page found : {lrd}[ \033[42m{target}/{List}\033[0m{lrd} ]')
		        	     	 
if o == '1':
	dork_Singel()
elif o == '2':
	dork_List()
elif o == '3':
	clear()
	print (f"""{k}
 .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. |
| |  ________    | || |     _____    | || |  _______     | |
| | |_   ___ `.  | || |    |_   _|   | || | |_   __ \    | |
| |   | |   `. \ | || |      | |     | || |   | |__) |   | |
| |   | |    | | | || |      | |     | || |   |  __ /    | |
| |  _| |___.' / | || |     _| |_    | || |  _| |  \ \_  | |
| | |________.'  | || |    |_____|   | || | |____| |___| | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'
    
    """)
	site_url = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter the site address : {k}")
	dir(site_url)
elif o == '4':
	clear()
	sub()
elif o == '5':
	clear()
	admin()
else:
	print (f"{lrd}Enter the appropriate option ")