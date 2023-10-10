import random

#Exercicio 1

nomes = 
['Maria','João','Ana','Pedro','Sofia','Lucas','Clara','Matheus','Laura','Gustavo','Camila','Felipe','Beatriz','Rafael','Isabela','Thiago','Mariana','Leonardo','Julia','Gabriel'] 
sobrenomes = ['Silva','Santos','Oliveira','Souza','Pereira','Costa','Rodrigues','Almeida','Fernandes','Carvalho','Gomes','Martins','Lima','Ferreira','Ribeiro','Barbosa','Nunes','Cardoso','Pereira','Castro']

def geracao1(numero,arquivo):
    arquivo = open(arquivo,'w')
    for i in range(numero):
        aleatorios = random.choice(nomes)
        aleatorioss = random.choice(sobrenomes)
        arquivo.write("Nome: ")
        arquivo.write(aleatorios)
        arquivo.write(' ')
        arquivo.write(aleatorioss)
        arquivo.write(' Idade: ')
        idade = str(random.randint(0,100))
        arquivo.write(idade)
        arquivo.write('\n')
pergunta = int(input("Digite quantos nomes, sobrenomes e idades aleatórios quer gerar: "))
geracao1(pergunta,'atividade1.txt')


#Exercicio 2

def geracao(numero,arquivo):
    arquivo = open(arquivo,'w')
    for i in range(numero):
        aleatorios = random.choice(nomes)
        aleatorioss = random.choice(sobrenomes)
        arquivo.write("Nome: ")
        arquivo.write(aleatorios)
        arquivo.write(' ')
        arquivo.write(aleatorioss)
        arquivo.write(' Idade: ')
        idade = str(random.randint(0,100))
        arquivo.write(idade)
        arquivo.write(' Altura: ')
        altura = (random.uniform(1.0,2.2))
        tamanho = round(altura,2)
        stringuers = str(tamanho)
        arquivo.write(stringuers)
        arquivo.write('\n')
pergunta2 = int(input("Quantos nomes,sobrenomes,idades e alturas aleatorios deseja gerar?: "))
geracao(pergunta2,'atividade2.txt')

#Exercicio 3

def copia(livro,livro2):
    c1 = open(livro,'w')
    c1.write("A vida é cheia de surpresas e desafios que nos ajudam a crescer como indivíduos.")
    c1.close()
    c1 = open(livro,'r')
    c2 = open(livro2,'w')
    for texto in c1:
        c2.write(texto)
    c1.close()
    c2.close()

copia('livro.txt','livro2.txt')

#Exercicio 4

alunoss = ['Carlos','Kauan','Marcos ','Maicon','Victoria ','Thiago']
notass = ['70','75','60','82','98','78']

alunoss = str(alunoss)
alunoss = str(alunoss).replace('[','')
alunoss = str(alunoss).replace(',','\n')
alunoss = str(alunoss).replace("'",'')
alunoss = str(alunoss).replace(']','')
alunoss = str(alunoss).replace(' ','')

anotass = str(notass)
notass= str(notass).replace('[','')
notass = str(notass).replace(',','\n')
notass = str(notass).replace("'",'')
notass= str(notass).replace(']','')
notass= str(notass).replace(' ','')

def notas(aluno,nota):
    n1 = open(aluno,'w')
    n2 = open(nota,'w')
    
    n1 = n1.write(str(alunoss))
    n2 = n2.write(str(notass))
    
    n1 = open(aluno,'r')
    n2 = open(nota,'r')
    result = ('resultado.txt')
    n3 = open(result,'w')
    
    for palavras,texto in zip(n1,n2):
        aluno = palavras.strip()
        nota = texto.strip()
        
        n3.write(f"{aluno}: {nota}\n")

    n1.close()
    n2.close()
    n3.close()




notas('aluno.txt','nota.txt')

#Exercicio 5

def mudarnota(aluno, notavel, notanov):
    alunoar = 'aluno.txt'
    notaar = 'nota.txt'
    tempaluno = 'tempAluno.txt'
    tempnota = 'tempNota.txt'
    
    p1 = open(alunoar, 'r')
    p2 = open(notaar, 'r')
    t1 = open(tempaluno, 'w')
    t2 = open(tempnota, 'w')
    
    encontrado = False
    
    for nome, nota in zip(p1, p2):
        nome = nome.strip()
        nota = nota.strip()
        
        if nome == aluno and nota == notavel:
            t1.write(nome + '\n')
            t2.write(notanov + '\n')
            encontrado = True
        else:
            t1.write(nome + '\n')
            t2.write(nota + '\n')
    p1.close()
    p2.close()
    t1.close()
    t2.close()
    
    if encontrado:
        import os
        os.remove(alunoar)
        os.remove(notaar)
        os.rename(tempaluno, alunoar)
        os.rename(tempnota, notaar)

        r1 = open(alunoar, 'r') 
        r2 = open(notaar, 'r') 
        r3 = open('resultado.txt', 'w')
    
        for nome, nota in zip(r1, r2):
            nome = nome.strip()
            nota = nota.strip()
            r3.write(f"{nome}: {nota}\n")

        r1.close()
        r2.close()
        r3.close()

        print(f"A nota de {aluno} foi alterada para {notanov}.")
    else:
        print(f"Aluno não encontrado ou nota não alterada.")



mudarnota('Kauan', '75', '80')