#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import sendmail.sendmail as sm
import android
import re

TITLE='Commande de médicaments'
#EMAIL_ADDRESS='katchenjunga@gmail.com'
EMAIL_ADDRESS='baccaph@planet.ch'
EMAIL_TITLE="Commande de médicaments pour Jean-Pierre Schnyder"
EMAIL_BCC='jp.schnyder@gmail.com'

droid=android.Android()
commande="""
Bonjour,

Je souhaite vous commander les médicaments  suivants:

Betaferon                     1 boîte
Sirdalud Retard 6 mg {0} boîte(s)
Lioresal 25 mg            {1} boîte(s)
{2}
Avec mes remerciements et mes cordiales salutations,
Jean-Pierre Schnyder\n"""
valverdeLine="Valverde Forte             {0} boîte(s)\n"

pattern = r"(\d?)\W*(\d)\W*(\d)"

droid.dialogCreateInput(TITLE,"Nombre de boîtes (Lioresal, Sirdalud, Valverde F)","1, 2, 0")
droid.dialogSetPositiveButtonText('OK')
droid.dialogSetNegativeButtonText('Cancel') 
droid.dialogShow() 
answer = droid.dialogGetResponse().result

if answer['which'] == 'negative':
    quit(0)
    
parms=re.search(pattern,answer['value']).groups()
lioQt=parms[0]
sirdaQt=parms[1]
valvQt=parms[2]

if int(valvQt) > 0:
    valverdeLine = valverdeLine.format(valvQt)
    commande=commande.format(sirdaQt,lioQt,valverdeLine)
else:
    commande=commande.format(sirdaQt,lioQt,"")

sm.sendMailWithBodyTo(commande, EMAIL_ADDRESS, EMAIL_BCC, EMAIL_TITLE,'JP Schnyder')
msg="Commande de médicaments ({0} Lio, {1} Sirda, {2} Valv) envoyée à {3}".format(lioQt,sirdaQt,valvQt,EMAIL_ADDRESS)
    
droid.dialogCreateAlert('',msg)
droid.dialogSetPositiveButtonText('OK') 
droid.dialogShow() 
response = droid.dialogGetResponse()
