ALNUM = 1
ALNUM_P = 2 
ALNUM_PU = 3 
ALNUM_PUC = 4
ALNUM_PUCP = 5
ALNUM_TEXT = 6
LATAM_TEXT = 7


#Alphabets
A = [None] * 11
A[1] = "a-z"
A[2] = "A-Z"
A[3] = "0-9"
A[4] = A[1] + "\-"
A[5] = A[2] + "_"
A[6] = A[3] +  "\'\""
A[7] = A[4] + "\.\,\!\?\:\;\(\)\[\]\{\}¡¿"
A[8] = A[5] + "\s"
A[9] = A[6] + "áéíóúÁÉÍÓÚñÑüÜ"

#Text Charsets
T = [None] * 4
T[1] = A[1] + A[2] + A[3]
T[2] = T[1] + A[4]
T[3] = T[2] + A[5] + A[6] + A[7] + A[8] + A[9]


def get_charset(number):
    if number in T:
     return f"^[{T[number]}]+$"

    return ""
