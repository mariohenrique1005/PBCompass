import hashlib #Importação da biblioteca

while True: #Colocar o script sempre em execução
    string=input("Digite: ") #Ler uma entrada e armazenar em uma variável
    hashed_string=hashlib.sha256(string.encode('utf-8')).hexdigest() #Atribuir uma hash para a string de entrada por meio do algoritmo SHA-1
    print("Hash:", hashed_string) #Imprimir a hash para a string