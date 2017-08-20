#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import sendmail.sendmail as sm
import android

TITLE='Liste de courses'
EMAIL_ADDRESS='katchenjunga@gmail.com'
#EMAIL_ADDRESS='planif.gde@avasad.ch'
EMAIL_BCC='jp.schnyder@gmail.com'
EMAIL_TITLE="Liste d'achats pour Jean-Pierre Schnyder, le vendredi à 13.30 H"
LISTTOKEN="Fivefly La liste d'achat."
LIST_HEADER="""
M = grande Migros Aigle
D = Denner au même endroit
L = Lidl Aigle\n
Code porte entrée: 3710 + A\n
Mon natel: 076 822 49 87
Avec mes remerciements !\n"""
EOL_REPLACEMENT='.'
MAIL_EOL_REPLACEMENT='. |'
#SMS_PHONE='0768224987' #JPS
SMS_PHONE='0765920604' #Papa

def replEol(listC,repl):
    listC=listC.replace(' (-)',repl)
    listC=listC.replace(' (+)',repl)
    return listC

droid=android.Android()
listC=droid.getClipboard().result

if listC.find(LISTTOKEN) == -1:
    droid.dialogCreateAlert("ERREUR",'Aucune liste dans le clipboard !')
    droid.dialogSetPositiveButtonText('OK') 
    droid.dialogShow() 
    quit()

listC=listC.replace(LISTTOKEN,LIST_HEADER)

#input=droid.dialogGetInput('CHOISIR','C-clipboard, S-SMS, M-mail').result
#input=input.upper()

droid.dialogCreateAlert("Mode d'envoi")
droid.dialogSetSingleChoiceItems(['Clipboard','SMS','Mail'])
droid.dialogSetPositiveButtonText("OK") 
droid.dialogShow() 
response = droid.dialogGetResponse()

if response.result["which"] == "positive":
    selected = droid.dialogGetSelectedItems()

sendType = selected[1][0]

msg=''

if sendType == 0:
    listC=replEol(listC,EOL_REPLACEMENT)
    droid.setClipboard(listC)
    msg="Liste d'achat copiée dans clipboard !"
elif sendType == 2:
    listC=replEol(listC,MAIL_EOL_REPLACEMENT)
    sm.sendMailWithTextBodyTo(listC, EMAIL_ADDRESS, EMAIL_BCC, EMAIL_TITLE, 'JP Schnyder')
    msg="Liste d'achat envoyée à {0}".format(EMAIL_ADDRESS)
else: #send per sms
    listC=replEol(listC,EOL_REPLACEMENT)
    droid.smsSend(SMS_PHONE,listC)
    msg="Liste d'achat envoyée à {0}".format(SMS_PHONE)
    
droid.dialogCreateAlert('',msg)
droid.dialogSetPositiveButtonText('OK') 
droid.dialogShow() 
response = droid.dialogGetResponse()
