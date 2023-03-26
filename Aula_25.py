'''
CONSTANTES = " Variaveis" queão vão mudar
muitas condições no mesmo if(ruim)
     <- Contagem de complexixade (ruim)
'''
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocide maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGER = 1 # A distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
multar_carro_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGER) and \
    local_carro <= (LOCAL_1 + RADAR_RANGER)



if vel_carro_pass_radar_1:
    print('Voce passou a velocidade e multado')

if multar_carro_radar_1 and vel_carro_pass_radar_1:
    print('carro multado em radar')
