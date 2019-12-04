from functions.validação import lerFloat
from functions.visual import arredondamento

tamanho = lerFloat('Digite o tamanho do arquivo em MB: ', pos=True, erro='Digite um tamanho válido')
velocidade = lerFloat('Digite a sua velocidade média de link com a internet em mbps: ', pos=True, erro='Digite uma velocidade válida')
temposeg = tamanho / velocidade
tempomin = arredondamento(temposeg / 60)

print(f'O tempo de download, em minutos, é de aproximadamente {tempomin} minutos.')