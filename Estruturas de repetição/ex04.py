pais1 = [80000, 0.03]
pais2 = [200000, 0.015]

anos = 0
while pais2 > pais1:
    anos += 1
    pais1[0] += pais1[0] * pais1[1] 
    pais2[0] += pais2[0] * pais2[1] 

print(f'Serão necessários {anos} anos para a população do pais A ultrapassar a população do pais B')
