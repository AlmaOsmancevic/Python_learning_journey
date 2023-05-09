#global variables defined
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#FUNCTIONS

#this function takes in a fahrenheit temperature and converts it to celsius. 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#this function takes in a celsius temperature and converts it to fahrenheit.
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) +32
  return f_temp

#this function multiplies the mass with the acceleration
def get_force(mass, acceleration):
  return mass * acceleration

#this functions returns the mass multiplied c squared. C is a constant in this case.
def get_energy(mass, c=3*10**8):
  return mass * c**2

#this function calls the get_force function and thereby force is multiplied by distance.
def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work


#calling functions and calculations
f100_in_celcius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " X Joules.")

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")