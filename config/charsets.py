ALNUM = 1
ALNUMSPHU = 8
LATAM_TEXT = 5


#Basic Charsets
A = [None] * 11
A[1] = "abcdefghijklmnopqrstuvwxyz"
A[2] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A[3] = "0123456789"
A[4] = A[3] + "\\-"
A[5] = A[4] + "_"
A[6] = A[3] +  ","
A[7] = A[4] + "\\.\\,\\!\\?\\:\\;\\(\\)\\[\\]\\{\\}¡¿"
A[8] = A[5] + "\\s"
A[9] = A[6] + "áéíóúÁÉÍÓÚñÑüÜ"
A[10] = "#@&*'%\\/"

#Text Charsets
T = [None] * 9
T[1] = A[1] + A[2] + A[3] #charset alfanumérico
T[2] = T[1] + A[4] #charset alfanumérico con guión medio (hyphen)
T[2] = T[1] + A[4] #charset alfanumérico con guion bajo (underscore)
T[4] = T[1] + A[8] + A[9] #charset alfanumérico Latino con espacios
T[5] = T[4] + A[7] #charset texto latino
T[6] = A[4] + A[5] # guiones
T[7] = T[5] + T[6] #charset texto latino con guiones 
T[8] = T[1] + T[6] #charset alfanumérico con guiones
