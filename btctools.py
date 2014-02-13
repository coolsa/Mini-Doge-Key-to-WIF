import hashlib, binascii, os

t='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

"""The initial version of the 'minwif' function
was contributed by JeromeS at BitcoinTalk.org
https://bitcointalk.org/index.php?topic=84238.0
The version used is contributed by ConceptPending at github
https://github.com/ConceptPending/PythonBTCTools
"""

def minwif(numpriv):
    step0 = hashlib.sha256(numpriv).hexdigest()
    step1 = '9e'+step0[0:].strip('L').zfill(64)
    step2 = hashlib.sha256(binascii.unhexlify(step1)).hexdigest()
    step3 = hashlib.sha256(binascii.unhexlify(step2)).hexdigest()
    step4 = int(step1 + step3[:8] , 16)
    return ''.join([t[step4/(58**l)%58] for l in range(100)])[::-1].lstrip('1')

