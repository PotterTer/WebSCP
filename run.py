import requests as req
import time, os, sys

w = "\033[1;0m"
r = "\033[31m"    # Red
g = "\033[32m"    # Green

url = ""
if len(sys.argv)==2:
	url = sys.argv[1]
else:
	sys.exit()
	print()
	
def re():
	try:
		print()
		web_data = req.get(url)
		text_data = (web_data.text) 
		file = open('data.txt', 'w')
		file.write(f'{text_data}')
		file.close()
		print(f"[{r}+{w}]{r}> {w}Web Scraping \n{w}[{r}={w}] States{r} : {w}({g}✓{w})")
		print(f"{w}[{r}#{w}]{r}> {w}Save File : {g}data{w}.txt")
		print()
	except:
		print(f"[{r}-{w}]{r}> {w}Web Scraping \n{w}[{r}={w}] States{r} : {w}({r}X{w})")
		print()

def banner_web_scap():
	print()
	print(f"""Web {r}Scraping{w}
██╗    ██╗███████╗██████╗  {r} ███████╗ █████╗ ██████╗ {w}
██║    ██║██╔════╝██╔══██╗  {r}██╔════╝██╔════╝██╔══██╗{w}
██║ █╗ ██║█████╗  ██████╔╝  {r}███████╗██║     ██████╔╝{w}
██║███╗██║██╔══╝  ██╔══██╗  {r}╚════██║██║     ██╔═══╝ {w}
╚███╔███╔╝███████╗██████╔╝  {r}███████║╚██████╗██║{w}
 ╚══╝╚══╝ ╚══════╝╚═════╝   {r}╚══════╝ ╚═════╝╚═╝{w} """)
					 	            
def about():
	print(f"{r}+--------------------------------------------------------+")
	print(f"{r}| About       : Web Scraping                             |{w}")
	print(f"{r}| YouTube     : Potter                                   |{w}")
	print(f"{r}| Github URL  : https://github.com/PotterTer             |{w}")
	print(f"{r}+--------------------------------------------------------+{w}")

banner_web_scap()
about()
re()
      						
