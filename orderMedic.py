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


Betaferon                                     1 boîte
Sirdalud Retard 6 mg                 {0} boîte(s)
Lioresal 25 mg                            {1} boîte(s)
{2}{3}{4}

Avec mes remerciements et mes cordiales salutations,
Jean-Pierre Schnyder\n"""
valverdeLine ="Valverde Forte                             {0} boîte(s)\n"
zincGlukoLine="Zinc Glukonat 30mg                   {0} boîte(s)\n"
magnesiumLine="Magnesium Compl 100 caps    {0} boîte(s)\n"

pattern = r"(\d?)\W*(\d)\W*(\d)\W*(\d)\W*(\d)"

droid.dialogCreateInput(TITLE,"Nombre de boîtes (Lioresal, Sirdalud, Valverde F, Zinc G, Magnesium)","1, 2, 0, 0, 0")
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
zincQt=parms[3]
magnQt=parms[4]

if int(valvQt) > 0:
    valverdeLine = valverdeLine.format(valvQt)
else:
    valverdeLine = ""
    
if int(zincQt) > 0:
    zincGlukoLine = zincGlukoLine.format(zincQt)
else:
    zincGlukoLine = ""

if int(magnQt) > 0:
    magnesiumLine = magnesiumLine.format(magnQt)
else:
    magnesiumLine = ""

commande=commande.format(sirdaQt,lioQt,valverdeLine,zincGlukoLine,magnesiumLine)
    	
sm.sendMailWithBodyTo(commande, EMAIL_ADDRESS, EMAIL_BCC, EMAIL_TITLE,'JP Schnyder')
msg="Commande de médicaments ({0} Lio, {1} Sirda, {2} Valv, {3} Zinc, {4} Magn) envoyée à {5}".format(lioQt,sirdaQt,valvQt,zincQt,magnQt,EMAIL_ADDRESS)
    
droid.dialogCreateAlert('',msg)
droid.dialogSetPositiveButtonText('OK') 
droid.dialogShow() 
response = droid.dialogGetResponse()
