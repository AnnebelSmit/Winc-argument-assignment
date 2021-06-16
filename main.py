# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greetingtemplate = "Hello, <name>!"):
    result = greetingtemplate.replace('<name>', name)
    return result

result = greet('Bob', "What's up, <name>!")
print(result)

def force(mass, body = 'earth'):
    bodies = {"earth" : 9.798,
        "sun": 274.0,
        "jupiter": 24.92,
        "neptune": 11.15, 
        "saturn": 10.44, 
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury":3.7,
        "moon": 1.62,
        "pluto":0.58
        }
    gravity = bodies[body]
    force_formula = mass* round(gravity,1)
    return force_formula

mass = 2.653

result = force(mass)
print(result)

def pull(m1, m2, d):
    G = 6.674e-11
    gravitional_pull = G * (((m1*m2) / d**2))
    return gravitional_pull

result = pull(1,1,1)
print(result)