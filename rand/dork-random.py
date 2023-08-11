import platform,os,random
try:from googlesearch import search
except:os.system("pip install google-search")
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
o = input(f"""{g}
   #              #     
   #              #     
 ###   ##   ###   # #   
#  #  #  #  #  #  ##    
#  #  #  #  #     # #   
 ###   ##   #     #  #  

{lrd}[{lgn}1{lrd}] {lgn}Dork Sql injection\n\n{lrd}[{lgn}2{lrd}] {lgn}Dork Xss\n\n{lrd}[{lgn}3{lrd}] {lgn}Dork RCE

{lrd}[{lgn}+{lrd}] {cn}Enter Number : {k}""")
def dork_random(dork):
    clear()
    print (f"""{k}
                  .__                     __             
______   _______  |__| ___  __ _____    _/  |_    ____   
\____ \  \_  __ \ |  | \  \/ / \__  \   \   __\ _/ __ \  
|  |_> >  |  | \/ |  |  \   /   / __ \_  |  |   \  ___/  
|   __/   |__|    |__|   \_/   (____  /  |__|    \___> 
|__|                             
    \n""")
    try:
    	dork,page,time,save = dork,int(input(f"{lrd}[{lgn}+{lrd}] {lgn}Number Page{k} : {cn}")),int(input(f"{lrd}[{lgn}+{lrd}] {lgn}Timeout {k}: {cn}")),input(f"{lrd}[{lgn}+{lrd}] {lgn}save location : {k}")
    	nyx = 0
    	for i in search(dork, tld="com", lang="en", num=int(page), start=0, stop=None, pause=int(time)):
    		with open(save, 'a') as f:
    			f.write(f'{i}\n')
    		nyx += 1
    		print(f'\n{lrd}[{lgn}{nyx}{lrd}] {yw}=>> {lrd}[{k}{i}{lrd}]')
    		if nyx >= int(time):
    			break;
    	print(f'\n{yw}------------------------\n{lrd}[{lgn}+{lrd}] {gn}Saved : {lgn}{save}\n{lrd}[{lgn}+{lrd}] {gn}Number of sites found: {k}{nyx}')
    except ValueError:
    	exit(f'{lrd}[{rd}-{lrd}] {rd}Error Input')
    except KeyboardInterrupt:
    	exit(f'{lrd}[{rd}-{lrd}] {rd}Error')    	

if o == '1':
    with open("rand/sqli.txt",'r') as file:
        lines = file.readlines()
    random_line = random.choice(lines)
    dork_random(random_line)
    
elif o == '2':
    with open("rand/xss.txt",'r') as file:
        lines = file.readlines()
    random_line = random.choice(lines)
    dork_random(random_line)
    
elif o == '3':
    with open("rand/lfi.txt",'r') as file:
        lines = file.readlines()
    random_line = random.choice(lines)
    dork_random(random_line)
