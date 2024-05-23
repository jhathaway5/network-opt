### Example Problem: Supply Chain Network Optimization for Aerospace MRO Parts

**Problem Statement:**

You are the supply chain manager for an aerospace company responsible for distributing MRO parts from multiple suppliers to several service centers and then to various aircraft maintenance sites. The goal is to optimize the supply chain network to minimize the total cost while ensuring that the demand for MRO parts at the maintenance sites is met.

### Network Structure

- **Suppliers (S)**: S1, S2
- **Service Centers (C)**: C1, C2, C3
- **Maintenance Sites (M)**: M1, M2, M3, M4

### Data

1. **Supplier Production Costs**:
   - S1: $100 per unit
   - S2: $120 per unit

2. **Transportation Costs (per unit)**:
   - From Suppliers to Service Centers:
     - S1 to C1: $15, S1 to C2: $20, S1 to C3: $25
     - S2 to C1: $18, S2 to C2: $16, S2 to C3: $22
   - From Service Centers to Maintenance Sites:
     - C1 to M1: $10, C1 to M2: $12, C1 to M3: $15, C1 to M4: $18
     - C2 to M1: $14, C2 to M2: $11, C2 to M3: $16, C2 to M4: $13
     - C3 to M1: $20, C3 to M2: $18, C3 to M3: $14, C3 to M4: $10

3. **Holding Costs (per unit per period)**:
   - C1: $2
   - C2: $1.5
   - C3: $2.5

4. **Demand at Maintenance Sites (units)**:
   - M1: 50
   - M2: 60
   - M3: 70
   - M4: 80

### Objective

Minimize the total cost, which includes:
- Production costs at suppliers
- Transportation costs from suppliers to service centers
- Transportation costs from service centers to maintenance sites
- Holding costs at service centers

### Constraints

1. Production capacity constraints at suppliers.
2. Demand fulfillment constraints at maintenance sites.
3. Flow conservation constraints at service centers (inflow must equal outflow plus holding).

### Linear Programming Formulation

**Variables:**
- \( x_{ij} \): Units shipped from supplier \( i \) to service center \( j \)
- \( y_{jk} \): Units shipped from service center \( j \) to maintenance site \( k \)
- \( h_j \): Units held in service center \( j \)

**Objective Function:**
\[
\text{Minimize} \quad Z = \sum_{i} \sum_{j} C_{ij} x_{ij} + \sum_{j} \sum_{k} T_{jk} y_{jk} + \sum_{j} H_j h_j + \sum_{i} P_i \sum_{j} x_{ij}
\]
where \( C_{ij} \) is the transportation cost from supplier \( i \) to service center \( j \), \( T_{jk} \) is the transportation cost from service center \( j \) to maintenance site \( k \), \( H_j \) is the holding cost at service center \( j \), and \( P_i \) is the production cost at supplier \( i \).

**Constraints:**
1. **Demand constraints at maintenance sites**:
   \[
   \sum_{j} y_{jk} \geq D_k \quad \forall k
   \]
   where \( D_k \) is the demand at maintenance site \( k \).

2. **Flow conservation constraints at service centers**:
   \[
   \sum_{i} x_{ij} + h_j = \sum_{k} y_{jk} + h_j \quad \forall j
   \]

3. **Non-negativity constraints**:
   \[
   x_{ij}, y_{jk}, h_j \geq 0 \quad \forall i, j, k
   \]

### Explanation

1. **Data**: Define the costs, demand, and other parameters specific to the aerospace MRO parts network.
2. **Problem Definition**: Create a `LpProblem` instance to minimize the total cost.
3. **Variables**: Define variables for shipments and holdings.
4. **Objective Function**: Sum the production, transportation, and holding costs.
5. **Constraints**:
   - Ensure that the demand at each maintenance site is met.
   - Maintain flow conservation at each service center.
6. **Solving**: Use the solver to find the optimal solution.
7. **Results**: Print the status, total cost, and shipment and holding decisions.
