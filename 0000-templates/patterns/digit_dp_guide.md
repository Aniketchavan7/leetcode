# Algorithmic Pattern: Digit Dynamic Programming

## 1. Problem Formulation
Calculate the count of integers $X \in [L, R]$ satisfying predicate $P(X)$.
Using prefix subtraction: $f(L, R) = f(0, R) - f(0, L - 1)$.

## 2. Standard State Tuple
State: `(index, tight, leading_zeros, state_payload)`
- `index`: Current digit position from most significant to least significant.
- `tight`: Boolean flag indicating if current prefix matches prefix of upper bound $N$.
- `leading_zeros`: Boolean flag handling valid numbers of varying lengths.
