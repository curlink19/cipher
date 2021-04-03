import random


module = 0x10FFFF + 1
xorModule = 2**20
decodeModule = module

seqCounter = dict()

def precalc():
    seqCounter['th'] = 330
    seqCounter['he'] = 302
    seqCounter['an'] = 181 
    seqCounter['in'] = 179
    seqCounter['er'] = 169
    seqCounter['nd'] = 146
    seqCounter['re'] = 133
    seqCounter['ed'] = 126
    seqCounter['es'] = 115
    seqCounter['ou'] = 115
    seqCounter['to'] = 115
    seqCounter['ha'] = 114
    seqCounter['en'] = 111
    seqCounter['ea'] = 110
    seqCounter['st'] = 109
    seqCounter['nt'] = 106
    seqCounter['on'] = 106
    seqCounter['at'] = 104
    seqCounter['hi'] = 97
    seqCounter['as'] = 95
    seqCounter['it'] = 93
    seqCounter['ng'] = 92
    seqCounter['is'] = 86
    seqCounter['or'] = 84
    seqCounter['et'] = 83
    seqCounter['of'] = 80
    seqCounter['ti'] = 76
    seqCounter['ar'] = 75
    seqCounter['te'] = 75
    seqCounter['se'] = 74
    seqCounter['me'] = 68
    seqCounter['sa'] = 67
    seqCounter['ne'] = 66
    seqCounter['wa'] = 66
    seqCounter['ve'] = 65
    seqCounter['le'] = 64
    seqCounter['no'] = 60
    seqCounter['ta'] = 59
    seqCounter['al'] = 57
    seqCounter['de'] = 57
    seqCounter['ot'] = 57
    seqCounter['so'] = 57
    seqCounter['dt'] = 56
    seqCounter['ll'] = 56
    seqCounter['tt'] = 56
    seqCounter['el'] = 55
    seqCounter['ro'] = 55
    seqCounter['ad'] = 52
    seqCounter['di'] = 50
    seqCounter['ew'] = 50
    seqCounter['ra'] = 50
    seqCounter['ri'] = 50
    seqCounter['sh'] = 50

class CaesarCipher:
    base = str()
    key = int()

    def __init__(self, info):
        global module
        self.base = info
        self.key = int(random.randint(0, module - 1) * module + module / 2) % module

    def changeKey(self, newKey):
        self.key = int(newKey)

    def encode(self):
        global module
        old = self.base
        self.base = ''
        for c in old:
            self.base += chr((ord(c) + self.key) % module)

    def decode(self):
        global module
        old = self.base
        self.base = ''
        for c in old:
            self.base += chr((ord(c) - self.key + module) % module)

class VigCipher:
    base = str()
    key = str()

    def __init__(self, info):
        self.base = info
        self.key = 'math'

    def changeKey(self, newKey):
        self.key = newKey

    def encode(self):
        global module
        old = self.base
        self.base = ''
        counter = 0
        for c in old:
            counter = (counter + 1) % len(self.key)
            self.base += chr((ord(c) + ord(self.key[counter])) % module)

    def decode(self):
        global module
        old = self.base
        self.base = ''
        counter = 0
        for c in old:
            counter = (counter + 1) % len(self.key)
            self.base += chr((ord(c) - ord(self.key[counter])) % module)

class VerCipher:
    base = str()
    key = str()

    def __init__(self, info):
        self.base = info
        self.key = 'math'

    def changeKey(self, newKey):
        self.key = newKey

    def encode(self):
        global module
        old = self.base
        self.base = ''
        counter = 0
        for c in old:
            counter = (counter + 1) % len(self.key)
            self.base += chr((ord(c) % xorModule) ^ (ord(self.key[counter]) % xorModule))

    def decode(self):
        self.encode()

def value(base):
    result = 0
    for i in range(len(base) - 1):
        if base[i:i+2] in seqCounter.keys(): 
            result += seqCounter[base[i:i+2]]
    return result

def decodeCaesar(base):
    result = base
    resultValue = -1
    for x in range(decodeModule):
        cipher = CaesarCipher(base)
        cipher.changeKey(x)
        cipher.decode()
        currentValue = value(cipher.base)
        if currentValue > resultValue:
            resultValue = currentValue
            result = cipher.base
    return result

def main():
    precalc()
    print("Enter path to file")
    path = input()
    f = open(path, encoding='utf-8')
    print("Choose the encryption type from:\n1) Caesar\n2) Vigenère\n3) Vernam")
    print("\nOr you can decode without key, press for what '4'")
    number = int(input())
    if number == 4:
        base = f.read()
        os = open(path, 'w', encoding='utf-8')
        os.write(decodeCaesar(base))
        f.close()
        os.close()
        return;
    cipher = None
    if number == 1:
        cipher = CaesarCipher(f.read())
    elif number == 2:
        cipher = VigCipher(f.read())
    elif number == 3:
        cipher = VerCipher(f.read())
    print("Enter key")
    word = input()
    cipher.changeKey(word)
    print("Enter 'e' to encode or 'd' to decode")
    way = input()
    if way == 'e':
        cipher.encode()
    else:
        cipher.decode()
    os = open(path, 'w')
    os.write(cipher.base)
    f.close()
    os.close()


import tkinter as tk

class Gui:
    def caesarDoEncode(self):
        f = open(self.path.get(), encoding = 'utf-8')
        cipher = CaesarCipher(f.read())
        cipher.changeKey(self.key.get())
        cipher.encode()
        os = open(self.path.get(), 'w', encoding = 'utf-8')
        os.write(cipher.base)
        f.close()
        os.close()
    
    def caesarDoDecode(self):
        f = open(self.path.get(), encoding = 'utf-8')
        cipher = CaesarCipher(f.read())
        cipher.changeKey(self.key.get())
        cipher.decode()
        os = open(self.path.get(), 'w', encoding = 'utf-8')
        os.write(cipher.base)
        f.close()
        os.close()

    def vigDoEncode(self):
        f = open(self.path.get(), encoding = 'utf-8')
        cipher = VigCipher(f.read())
        cipher.changeKey(self.key.get())
        cipher.encode()
        os = open(self.path.get(), 'w', encoding = 'utf-8')
        os.write(cipher.base)
        f.close()
        os.close()

    def vigDoDecode(self):
        f = open(self.path.get(), encoding = 'utf-8')
        cipher = VigCipher(f.read())
        cipher.changeKey(self.key.get())
        cipher.decode()
        os = open(self.path.get(), 'w', encoding = 'utf-8')
        os.write(cipher.base)
        f.close()
        os.close()

    def verDoEncode(self):
        f = open(self.path.get(), encoding = 'utf-8')
        cipher = VerCipher(f.read())
        cipher.changeKey(self.key.get())
        cipher.encode()
        os = open(self.path.get(), 'w', encoding = 'utf-8')
        os.write(cipher.base)
        f.close()
        os.close()

    def verDoDecode(self):
        f = open(self.path.get(), encoding = 'utf-8')
        cipher = VerCipher(f.read())
        cipher.changeKey(self.key.get())
        cipher.decode()
        os = open(self.path.get(), 'w', encoding = 'utf-8')
        os.write(cipher.base)
        f.close()
        os.close()

    def doUniversalDecode(self):
        f = open(self.path.get(), encoding = 'utf-8')
        base = f.read()
        os = open(self.path.get(), 'w', encoding = 'utf-8')
        os.write(decodeCaesar(base))
        f.close()
        os.close()
      
    def __init__(self):
        self.window = tk.Tk()
        self.infoPath = tk.Label(text = 'Enter the path', font = ("curlink", 19))
        self.path = tk.Entry(font = ("curlink", 19))
        self.infoKey = tk.Label(text = 'Enter the key', font = ("curlink", 19))
        self.key = tk.Entry(font = ("curlink", 19))
        self.infoChoose = tk.Label(text = 'Choose an option', font = ("curlink", 19))
        self.caesarEncode = tk.Button(text = 'Caesar encode', font = ("curlink", 19), command = self.caesarDoEncode)
        self.caesarDecode = tk.Button(text = 'Caesar decode', font = ("curlink", 19), command = self.caesarDoDecode)
        self.vigEncode = tk.Button(text = 'Vigenère encode', font = ("curlink", 19), command = self.vigDoEncode)
        self.vigDecode = tk.Button(text = 'Vigenère decode', font = ("curlink", 19), command = self.vigDoDecode)
        self.verEncode = tk.Button(text = 'Vernam encode', font = ("curlink", 19), command = self.verDoEncode)
        self.verDecode = tk.Button(text = 'Vernam decode', font = ("curlink", 19), command = self.verDoDecode)
        self.universalDecode = tk.Button(text = 'Decode without key', font = ("curlink", 19), command = self.doUniversalDecode)
        self.window.geometry("640x480")
        self.infoPath.pack()
        self.path.pack()
        self.infoKey.pack()
        self.key.pack()
        self.infoChoose.pack()
        self.caesarEncode.place(x = 35, y = 200)
        self.vigEncode.place(x = 35, y = 250)
        self.verEncode.place(x = 35, y = 300)
        self.caesarDecode.place(x = 360, y = 200)
        self.vigDecode.place(x = 360, y = 250)
        self.verDecode.place(x = 360, y = 300)
        self.universalDecode.place(x = 170, y = 400)
   
#main()
precalc()
cipher = Gui()
cipher.window.mainloop()





