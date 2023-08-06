from BayesianNetwork import BayesianNetwork
from node import Node

rain = Node(
    cpt = {
        'none': 0.7,
        'light': 0.2,
        'heavy': 0.1
    },
    name = 'Rain',
    distribution='discrete'
)

maintenance = Node(
    cpt = [
        ['none', 'yes', 0.4],
        ['none', 'no', 0.6],
        ['light', 'yes', 0.2],
        ['light', 'no', 0.8],
        ['heavy', 'yes', 0.1],
        ['heavy', 'no', 0.9]
    ],
    name = 'Maintanance',
    distribution='conditional'
)

train = Node(
    cpt = [
    ["none", "yes", "on time", 0.8],
    ["none", "yes", "delayed", 0.2],
    ["none", "no", "on time", 0.9],
    ["none", "no", "delayed", 0.1],
    ["light", "yes", "on time", 0.6],
    ["light", "yes", "delayed", 0.4],
    ["light", "no", "on time", 0.7],
    ["light", "no", "delayed", 0.3],
    ["heavy", "yes", "on time", 0.4],
    ["heavy", "yes", "delayed", 0.6],
    ["heavy", "no", "on time", 0.5],
    ["heavy", "no", "delayed", 0.5]
    ], 
    name="Train",
    distribution='conditional'
    )

appointment = Node(
    cpt = [
    ["on time", "attend", 0.9],
    ["on time", "miss", 0.1],
    ["delayed", "attend", 0.6],
    ["delayed", "miss", 0.4]
    ],
    name="Appointment",
    distribution='conditional'
)

model = BayesianNetwork()
model.add_states(rain, maintenance, train, appointment)

model.add_edge(rain, maintenance)
model.add_edge(rain, train)
model.add_edge(maintenance, train)
model.add_edge(train, appointment)

probability = model.probability({
    'Rain': 'heavy',
    'Train': 'on time',
    'Maintanance': 'yes',
    'Appointment': 'miss'
})