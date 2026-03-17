item = ["arroz","feijão","macarrão","leite"]
numeros = [1,2,3,4,5]


print("Primeiro item:", item [0])   # "arroz"
print("Último item:", item[-1])      # "leite"


item[1] = "farinha"
print("após alterar:", item)

item.append("ovos")  
item.insert(1, "acucar")
print("após adicionar:", item)

item.remove("leite")
ultima = item.pop()
print("após remover 'leite' e pop():", item, "(última removida:", ultima)