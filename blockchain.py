import datetime
import hashlib
import json
from flask import Flask, jsonify

# Parte 1 - Criando um blockchain

class Blockchain:
    #Inicializar uma class, o self representa as variaveis da propria class
    def __init__(self):
        self.chain = [] #Declarando uma variavel do tipo array
        self.create_block(proof = 1, previous_hash='0') 
    
    def create_block(self, proof, previous_hash):
        #Criar o dicionário com 4 chaves
        #1 - indice do block, 2- Data de criação, proof e previous_hash
        # len(array) == array.length
        block = {'index': len(self.chain) + 1, 'timestamp': str(datetime.datetime.now()), 'proof': proof, 'previous_hash': previous_hash}
        self.chain.append(block) #array.append == array.push
        return block
    
    def get_previous_block(self):
        return self.chain[-1] #Retorna o ultimo elemento do array
    
    #Metodo para achar a prova anterior
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof +=1
        return new_proof