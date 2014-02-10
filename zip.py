import re



def linkedlist(nothing_data):
    
    ff=open("Downloads/channel/"+str(nothing_data)+".txt")
    # import pdb;pdb.set_trace()
    g=ff.read()
    numbers = re.findall(r"\d",g)
    responsetext =g

    con=""
    for x in numbers:
        con = con+x
    return con,responsetext

def finding(yy):

    if linkedlist(yy)[0]:
        with zipfile.ZipFile("Downloads/channel.zip", "r") as f:
            zipInfo = f.getinfo(str(linkedlist(yy)[0])+".txt")
            print zipInfo.comment,
        return finding(linkedlist(yy)[0])

    else:
        print linkedlist(yy)



if __name__ == '__main__':
    import zipfile
    finding(90052)

