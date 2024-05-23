import pulp

# Data
suppliers = ['S1', 'S2']
service_centers = ['C1', 'C2', 'C3']
maintenance_sites = ['M1', 'M2', 'M3', 'M4']

production_costs = {'S1': 100, 'S2': 120}
transport_cost_sc = {
    ('S1', 'C1'): 15, ('S1', 'C2'): 20, ('S1', 'C3'): 25,
    ('S2', 'C1'): 18, ('S2', 'C2'): 16, ('S2', 'C3'): 22
}
transport_cost_cm = {
    ('C1', 'M1'): 10, ('C1', 'M2'): 12, ('C1', 'M3'): 15, ('C1', 'M4'): 18,
    ('C2', 'M1'): 14, ('C2', 'M2'): 11, ('C2', 'M3'): 16, ('C2', 'M4'): 13,
    ('C3', 'M1'): 20, ('C3', 'M2'): 18, ('C3', 'M3'): 14, ('C3', 'M4'): 10
}
holding_costs = {'C1': 2, 'C2': 1.5, 'C3': 2.5}
demand = {'M1': 50, 'M2': 60, 'M3': 70, 'M4': 80}

# Define the LP problem
prob = pulp.LpProblem("Aerospace_MRO_Inventory_Optimization", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("Shipment_SC", [(s, c) for s in suppliers for c in service_centers], lowBound=0, cat='Continuous')
y = pulp.LpVariable.dicts("Shipment_CM", [(c, m) for c in service_centers for m in maintenance_sites], lowBound=0, cat='Continuous')
h = pulp.LpVariable.dicts("Holding", service_centers, lowBound=0, cat='Continuous')

# Objective function
prob += (
    pulp.lpSum(production_costs[s] * pulp.lpSum(x[(s, c)] for c in service_centers) for s in suppliers) +
    pulp.lpSum(transport_cost_sc[(s, c)] * x[(s, c)] for s in suppliers for c in service_centers) +
    pulp.lpSum(transport_cost_cm[(c, m)] * y[(c, m)] for c in service_centers for m in maintenance_sites) +
    pulp.lpSum(holding_costs[c] * h[c] for c in service_centers)
)

# Demand constraints at maintenance sites
for m in maintenance_sites:
    prob += pulp.lpSum(y[(c, m)] for c in service_centers) >= demand[m]

# Flow conservation constraints at service centers
for c in service_centers:
    prob += pulp.lpSum(x[(s, c)] for s in suppliers) + h[c] == pulp.lpSum(y[(c, m)] for m in maintenance_sites) + h[c]

# Solve the problem
prob.solve()

# Print the results
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Total Cost: {pulp.value(prob.objective)}")

for s in suppliers:
    for c in service_centers:
        if x[(s, c)].varValue > 0:
            print(f"Units shipped from {s} to {c}: {x[(s, c)].varValue}")

for c in service_centers:
    for m in maintenance_sites:
        if y[(c, m)].varValue > 0:
            print(f"Units shipped from {c} to {m}: {y[(c, m)].varValue}")

for c in service_centers:
    if h[c].varValue > 0:
        print(f"Units held in {c}: {h[c].varValue}")