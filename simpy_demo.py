import simpy

def normal_device(env):
    while True:
        print(f"Time {env.now}: Device sends packet")
        yield env.timeout(2)

def attacker(env):
    while True:
        print(f"Time {env.now}: Attacker sends fake packet")
        yield env.timeout(5)

env = simpy.Environment()

env.process(normal_device(env))
env.process(attacker(env))
env.run(until=20)
