fobj=open('output.txt','r')
data=fobj.read()
fobj.close()
'''
print(data.split('####################'))

i=0
for d in data.split('####################'):
    if 'E.Mai' not in d and 'E.mail' not in d and 'Email' not in d and 'Mail' not in d and 'E.Mal' not in d:
        i+=1
        print(d)
        print('############################################')
        if i==50:
            #print('Breaked...............')
            break
'''
fobj=open('Univ_Data.csv','a')
finaldata=''
for d in data.split('####################'):
    try:
        lines = d.strip().splitlines()
        univ_name = lines[0].strip().split('(')[0].strip()
    except:
        pass
    for line in lines:
        if '@' in line:
            for email in line.split():
                if '@' in email:
                    info = ','.join([univ_name]+email.strip('E.Mail').split('/'))
                    fobj.write(info+'\n')

fobj.close()











