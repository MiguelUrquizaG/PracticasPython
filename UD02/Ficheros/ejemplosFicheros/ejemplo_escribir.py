f = open('canary_iata.txt','w')

canary_iata =('TFN'
,'TFS'
,'LPA'
,'GMZ'
,'VDE'
,'SPC'
,'ACE'
,'FUE')

'''for code in canary_iata:
    f.write(code+'\n')
'''

#f.write('\n'.join(canary_iata))

f.writelines('\n',canary_iata)

f.close()