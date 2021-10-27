import math

class CesarEncoding():
    
    def coding(self,filename, result, key, type):
        if(type<0):
            key*=-1
        hookah = "0123456789абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        hookah = list(hookah)
        file = open(filename, encoding="ISO-8859-1")
        data = file.read()
        file.close()
        encrypted = []
        for letter in data:
            code = letter
            for i in range(0, len(hookah), 1):
                if(letter==hookah[i]):
                    code = i
            if(code != letter):
                mem = key
                if(code >= 0 and code <= 9 and math.fabs(key) >= 10):
                    key %= 10
                elif(code >= 76 and code <= 127 and math.fabs(key) >= 26):
                    key = math.fabs(key) % 26 * key/math.fabs(key)
                    key = int(key)
                else:
                    key = math.fabs(key) % 33 * key/math.fabs(key)
                    key = int(key)
                # A > Z
                if(code >= 102 and code <= 127):
                    if(code+key > 127):
                        code = key - (127 - code) + 102 - 1
                    elif(code+key < 102):
                        code += key + 26
                    else:
                        code += key
                # a > z
                if(code >= 76 and code <= 101):
                    if(code+key > 101):
                        code = key - (101 - code) + 76 - 1
                    elif(code+key < 76):
                        code += key + 26
                    else:
                        code += key
                # 0 > 9
                if(code >= 0 and code <= 9):
                    if(code+key > 9):
                        code = key - (9 - code) + 0 - 1
                    elif(code+key < 0):
                        code += key + 10
                    else:
                        code += key
                # а > я
                if(code >= 10 and code <= 42):
                    if(code+key > 42):
                        code = key - (42 - code) + 10 - 1
                    elif(code+key < 10):
                        code += key + 33
                    else:
                        code += key
                # A > Я
                if(code >= 43 and code <= 75):
                    if(code+key > 75):
                        code = key - (75 - code) + 43 - 1
                    elif(code+key < 43):
                        code += key + 33
                    else:
                        code += key
                encrypted.append(hookah[code])
                key = mem
            else:
                encrypted.append(code)
        encrypted = ''.join(encrypted)
        file = open(result, 'w', encoding="ISO-8859-1")
        for index in encrypted:
            file.write(index)
        file.close()