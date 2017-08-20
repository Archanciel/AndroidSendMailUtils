import sendmail.sendmail as sm
import android
import re
from io import StringIO

TITLE='Commande de médicaments'
EMAIL_ADDRESS='baccaph@planet.ch'
#EMAIL_ADDRESS='katchenjunga@gmail.com'
EMAIL_TITLE="Commande de médicaments pour Jean-Pierre Schnyder"
EMAIL_BCC='jp.schnyder@gmail.com'

def toHtmlTable(buf, lol):
  buf.write('<table border="0">\n')
  for sublist in lol:
    buf.write('  <tr>\n')
    buf.write('  <td>' + '</td><td>'.join(sublist) + '<td>\n')
    buf.write('  </tr>\n')
  buf.write('</table>')
  
droid=android.Android()
commandeTxt="""
Bonjour,

Je souhaite vous commander les médicaments suivants. Avec mes remerciwnment et mes salutations. JP Schnyder.

"""

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

commande = [['Betaferon', '1', 'bo&icirc;te'],
            ['Sirdalud Retard 6 mg', str(sirdaQt), 'bo&icirc;te(s)'],
            ['Lioresal 25 mg', str(lioQt), 'bo&icirc;te(s)']]

if int(valvQt) > 0:
    commande.append(['Valverde Forte', str(valvQt), 'bo&icirc;te(s)'])

if int(zincQt) > 0:
    commande.append(['Zinc Glukonat 30mg', str(zincQt), 'bo&icirc;te(s)'])

if int(magnQt) > 0:
    commande.append(['Magnesium Compl 100 caps', str(magnQt), 'bo&icirc;te(s)'])

buf = StringIO()

toHtmlTable(buf, commande)
commandeHTML = buf.getvalue()

sm.sendMailWithTxtAndHtmlBodyTo(commandeTxt, commandeHTML, EMAIL_ADDRESS, EMAIL_BCC, EMAIL_TITLE,'JP Schnyder')
msg="Commande de médicaments ({0} Lio, {1} Sirda, {2} Valv, {3} Zinc, {4} Magn) envoyée à {5}".format(lioQt,sirdaQt,valvQt,zincQt,magnQt,EMAIL_ADDRESS)
    
droid.dialogCreateAlert('',msg)
droid.dialogSetPositiveButtonText('OK') 
droid.dialogShow() 
response = droid.dialogGetResponse()
