import re
import requests


ff=open("endless","a")

def linkedlist(nothing_data):
	url="http://www.pythonchallenge.com/pc/def/linkedlist.php"
	data={'nothing':nothing_data}
	response = requests.get(url,params=data)
	numbers = re.findall(r"\d",response.text)
	responsetext =response.text

	con=""
	for x in numbers:
		con = con+x
	return con,responsetext

def finding(yy):
	print linkedlist(yy)[1]
	return finding(linkedlist(yy)[0])



if __name__ == '__main__':
	finding(63579)