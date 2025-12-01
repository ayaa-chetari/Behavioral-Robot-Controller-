from controller import Robot, Keyboard

TIMESTAMP = 64 #temps d'echntillonnage 
CRUISING_SPEED = 2.8 #vitesse des moteurs
TURN_SPEED = CRUISING_SPEED / 2 #vitesse de rotation

Limit1 = 1000 #limite pour laquelle l'objet est considéré detecté
Limit2 = 4000 # limite a respecter pour avoir une certaine distance entre le robot et un objet

# instanciation du robot
robot = Robot()



# recuperer les moteurs
motor_left = robot.getMotor('motor.left')
motor_right = robot.getMotor('motor.right')

# initialisation des positions des moteurs

motor_left.setPosition(float("inf"))
motor_right.setPosition(float("inf"))

# initialisation des vitesses des moteurs
motor_left.setVelocity(0.0)
motor_right.setVelocity(0.0)

# Lecture des capteurs

distanceSensors = []
for i in range(7):
    distanceSensors.append(robot.getDistanceSensor('prox.horizontal.' + str(i)))
    distanceSensors[i].enable(TIMESTAMP) # synchroniser avec la frequence d'echantillonnage
distanceVal = [0.0] * 7

# instanciation du clavier

keyboard = Keyboard()
keyboard.enable(TIMESTAMP)# synchroniser avec la frequence d'echantillonnage 

# dictionnaire pour les touches du clavier 
motor_cmd = {

# première partie gère les commandes de bases 

    ord('A'): (CRUISING_SPEED, CRUISING_SPEED),# avancer
    ord('G'): (-TURN_SPEED, TURN_SPEED),#tourner à gauche
    ord('D'): (TURN_SPEED, -TURN_SPEED),#tourner à droite
    ord('R'): (-TURN_SPEED, -TURN_SPEED),# reculer
    ord('S'): (0.0, 0.0),# s'arreter
    
# la deuxième partie gère les personnalités choisis
    
    ord('T'): "Timide",
    ord('P'): "ParanoiaqueB",
    ord('O'): "obstine B",
    ord('N'): "obstine A"
}


# fonctions de base

def commande_moteurs(cmd):

    motor_left.setVelocity(cmd[0])
    motor_right.setVelocity(cmd[1])
    
def avancer():
    commande_moteurs(motor_cmd[ord('A')])


def reculer():
    commande_moteurs(motor_cmd[ord('R')])


def sarreter():
    commande_moteurs(motor_cmd[ord('S')])


def tourner_G():
    commande_moteurs(motor_cmd[ord('G')])


def tourner_D():
    commande_moteurs(motor_cmd[ord('D')])


# Fonctions de personnalités
def Timide(distance):
    
    
    if (distance[2] == 0.0):
        print(f"distance is {distance[2]}")
        avancer()
        
    elif (distance [2] > Limit2):
        print(f"distance is {distance[2]}")
        sarreter()


def Paranoiaque_B(distance):

    
    
    if ((distance[2] > Limit1) and (distance[2] < Limit2)):
        print(f"distance is {distance[2]}")
        avancer()
    elif (distance[4]!=0):
        
        tourner_D()
        
    elif (distance[0]!=0) :
    
        tourner_G()
        
    elif ((distance[2] < Limit1) or (distance [2] > Limit2)):
        sarreter()


def obstine_B(distance):

    if ((distance[2] > Limit1) and (distance[2] < Limit2)):
        avancer()
    elif ((distance[5] > Limit1) and (distance[5] < Limit2)):
        reculer()
    elif ((distance[5] <Limit1 ) and (distance[2] <Limit1)):

        sarreter()


print("start")

while robot.step(TIMESTAMP) != -1:
    #key = keyboard.getKey()

    for i in range(7):
        distanceVal[i] = distanceSensors[i].getValue()

    Paranoiaque_B(distanceVal)#imposer le caractere paranoiaqueB pour ce robot
    
    pass