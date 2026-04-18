# POIS Project — Raj's Assignment

**Student:** Raj  
**Role:** Cryptographic Foundations — OWF, PRG, PRF, and Primality Testing  
**Assigned PAs:** PA#1, PA#2, PA#13  

## Overview

You are responsible for implementing the **cryptographic foundation** of the project. Your work forms the base of the entire reduction chain:

```
PA#13 (Miller-Rabin) → PA#1 (OWF, PRG) → PA#2 (PRF/GGM Tree) → Rest of Project
```

## Your Deliverables

### Week 1 (Foundations & Shared Utilities)
**CRITICAL DEADLINE:** These must be delivered for other team members to proceed.

- ✅ **`src/utils/random_utils.py`** — `generate(n)` for os.urandom
- ✅ **`src/utils/mod_exp.py`** — `square_and_multiply(base, exp, mod)` 
- ✅ **`src/utils/ext_gcd.py`** — Extended GCD and modular inverse
- ✅ **`src/utils/int_root.py`** — Integer root for PA#14
- ✅ **`src/primality/miller_rabin.py`** — Miller-Rabin test + `gen_prime(bits)`
- ✅ **`interfaces/owf.py`** — OWF abstract base class
- ✅ **`interfaces/prg.py`** — PRG abstract base class
- ✅ **`interfaces/prf.py`** — PRF abstract base class

### Week 2-3 (Core Implementations)

#### PA#1: One-Way Functions & Pseudorandom Generators
- **File:** `src/foundations/owf.py`
- **What to implement:**
  - `DLP_OWF` — Discrete Logarithm based: $f(x) = g^x \bmod p$
  - `FactorOWF` — Factoring-based: $f(p,q) = p \cdot q$
  - `HILL_PRG` — Haastad-Impagliazzo-Levin-Luby construction
    - Goldreich-Levin hard-core predicate: $b(x) = \langle x, r \rangle$
    - Iterative expansion: $G(x_0) = b(x_0) \| b(x_1) \| \ldots \| b(x_\ell)$

- **Bidirectional Reductions** (BOTH directions required):
  - Forward: OWF ⇒ PRG via HILL construction ✅
  - Backward: PRG ⇒ OWF (show that $f(s) = G(s)$ is one-way)

- **Tests:** `tests/test_pa1.py`

#### PA#2: Pseudorandom Function via GGM Tree
- **File:** `src/prf/ggm_prf.py`
- **What to implement:**
  - `GGM_PRF` — Binary tree traversal construction
  - Algorithm: 
    $$F_k(b_1 b_2 \ldots b_n) = G_{b_n}(\ldots G_{b_2}(G_{b_1}(k))\ldots)$$
  - Each node expands via PRG: $G(s) = G_0(s) \| G_1(s)$ (left/right children)
  - Tree depth = input bit length
  
- **Bidirectional Reductions** (BOTH directions required):
  - Forward: PRG ⇒ PRF via GGM construction ✅
  - Backward: PRF ⇒ PRG via $G(s) = F_s(0^n) \| F_s(1^n)$ ✅

- **PRF Distinguishing Game** (Security Test):
  - Adversary makes $q$ queries to either real PRF or random function
  - Advantage should be negligible
  - See `distinguishing_game()` in `ggm_prf.py`

- **Tests:** `tests/test_pa2.py`

#### PA#13: Miller-Rabin Primality Testing
- **File:** `src/primality/miller_rabin.py`
- **What to implement:**
  - `is_prime(n, k)` — Miller-Rabin test (error probability ≤ $4^{-k}$)
  - `gen_prime(bits)` — Generate $b$-bit probable prime
  - `gen_prime_safe(bits)` — Generate safe prime $p = 2q+1$ (for DH/DLP)

- **Algorithm (Miller-Rabin):**
  1. Write $n - 1 = 2^s \cdot d$ where $d$ is odd
  2. For $k$ rounds:
     - Choose random witness $a \in [2, n-2]$
     - Compute $x = a^d \bmod n$
     - If $x = 1$ or $x = n-1$: continue
     - Square $x$ repeatedly $s-1$ times, checking for $n-1$ each time
     - If never found: return COMPOSITE
  3. Return PROBABLY_PRIME

- **Tests:** `tests/test_pa13.py`
  - Small primes: 2, 3, 5, 7, 11, ...
  - Small composites: 4, 6, 8, 9, 10, ...
  - Carmichael numbers (561 = 3 × 11 × 17) — must reject
  - Large primes (e.g., $2^{31} - 1$)

## Technical Notes

### One-Way Functions
A function $f$ is one-way if:
- **Easy:** $f(x)$ computable in polynomial time
- **Hard:** For random $x$, no PPT adversary can find $x'$ with $f(x') = f(x)$

Three instantiations:
1. **DLP:** $f(x) = g^x \bmod p$ (hard due to discrete log)
2. **Factoring:** $f(p,q) = N = p \cdot q$ (hard due to factorization)
3. **AES:** $f(k) = \text{AES}_k(0^{128}) \oplus k$ (Davies-Meyer)

### Hard-Core Predicates
The Goldreich-Levin hard-core predicate for OWF $f$ is:
$$b(x) = \langle x, r \rangle = \sum_i x_i \cdot r_i \pmod 2$$

This is hard to compute given $f(x)$ even if $f$ is easy to compute.

### GGM Tree Details
- **Tree structure:** Binary tree of depth = input bit length
- **Path:** For input $x = b_1 b_2 \ldots b_n$, traverse from root to leaf
- **At each node:** Expand current node via PRG: $\text{left} \| \text{right} = G(\text{node})$
- **Time complexity:** $O(n)$ where $n$ = input length
- **Space complexity:** $O(n)$ for recursion (can be made $O(1)$ iteratively)

## Project Structure

```
POIS_PROJECT/
├── src/
│   ├── foundations/
│   │   └── owf.py                 # PA#1: OWF and PRG implementations
│   ├── prf/
│   │   └── ggm_prf.py             # PA#2: GGM-based PRF
│   ├── primality/
│   │   └── miller_rabin.py         # PA#13: Primality testing
│   └── utils/
│       ├── random_utils.py         # Random byte generation
│       ├── mod_exp.py              # Square-and-multiply
│       ├── ext_gcd.py              # Extended GCD + modular inverse
│       └── int_root.py             # Integer root computation
├── interfaces/
│   ├── owf.py                      # OWF abstract base class
│   ├── prg.py                      # PRG abstract base class
│   └── prf.py                      # PRF abstract base class
├── tests/
│   ├── test_pa1.py                 # Tests for PA#1
│   ├── test_pa2.py                 # Tests for PA#2
│   └── test_pa13.py                # Tests for PA#13
├── requirements.txt                # pytest (only testing dependency)
└── README.md                        # This file

Folders created but not yet filled:  (Others will implement these)
├── src/enc/                        # PA#3-4, PA#6 (Kanishk)
├── src/mac/                        # PA#5, PA#10 (Shubham)
├── src/hash/                       # PA#7-10 (Shubham)
├── src/dh/                         # PA#11 (Shobhan)
├── src/rsa/                        # PA#12, PA#14 (Shobhan)
├── src/elgamal/                    # PA#16 (Shobhan)
├── src/sig/                        # PA#15 (Shobhan)
├── src/pke/                        # PA#17 (Shobhan)
└── src/mpc/                        # PA#18-20 (Swaraj)
```

## Running Tests

```bash
# Create and activate environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
python3 -m pip install -r requirements.txt

# Run all your tests
python3 -m pytest tests/test_pa1.py tests/test_pa2.py tests/test_pa13.py -v

# Run specific test
python3 -m pytest tests/test_pa1.py::TestDLP_OWF -v

# Run with coverage
python3 -m pytest tests/ --cov=src --cov-report=html
```

## Bug Fixes Applied

1. `src/primality/miller_rabin.py`
  - Fixed `gen_prime(bits)` candidate construction to avoid `ValueError: negative shift count`.
  - Candidate is now masked to `bits`, then highest bit and odd parity bits are explicitly set.

2. `src/foundations/owf.py`
  - Updated imports from `src.interfaces.*` to `interfaces.*`.

3. `src/prf/ggm_prf.py`
  - Updated import from `src.interfaces.prf` to `interfaces.prf`.

4. Execution guidance
  - Standardized all test commands to use `python3 -m pytest` in `venv`.

## Key Implementation Checklist

### PA#1: OWF & PRG
- [ ] DLP_OWF class with safe prime generation
- [ ] HILL_PRG with Goldreich-Levin predicate
- [ ] PRG from PRF (backward reduction)
- [ ] Test DLP hardness demo
- [ ] Test PRG expansion and determinism

### PA#2: GGM PRF
- [ ] GGM_PRF binary tree traversal
- [ ] Bit-by-bit LEFT/RIGHT child selection
- [ ] PRG from PRF backward direction
- [ ] PRF distinguishing game test
- [ ] Verify consistency (same key + input = same output)

### PA#13: Miller-Rabin
- [ ] Miller-Rabin primality test (k=40 rounds)
- [ ] gen_prime(bits) — random bit generation + Miller-Rabin loop
- [ ] gen_prime_safe(bits) — Safe prime p=2q+1
- [ ] Test on small primes, composites, Carmichael numbers
- [ ] Carmichael 561 rejection (critical!)

## Dependency Notes

### Your code may depend on:
- `os.urandom()` — Python built-in (permitted)
- Python `int` (arbitrary precision) — permitted
- No external crypto libraries

### Who depends on you:
- **Shobhan (PA#11, PA#12)** needs `gen_prime()` for DH/RSA
- **Kanishk (PA#3, PA#4)** needs PRF from you for encryption
- **Shubham (PA#5)** uses PRF for MAC
- **Entire team** depends on shared utilities

## Timeline

- **Week 1, Days 1-2:** Complete all shared utilities + interfaces → Review with team
- **Week 1, Days 3-5:** Implement PA#13 (Miller-Rabin) → Deliver to Shobhan by EOD
- **Week 2:** Implement PA#1 (OWF + PRG) → Deliver to Kanishk/Shubham
- **Week 2-3:** Implement PA#2 (GGM PRF) + tests → Full delivery EOW3
- **Week 3:** Web app panels (GGM visualizer + PRG live output)

## Important Reminders

1. **No external crypto libraries:** All crypto code is from scratch
2. **Bidirectional reductions:** Both A ⇒ B and B ⇒ A must be implemented
3. **Test coverage:** Each PA needs comprehensive pytest suite
4. **Code review:** Share interim work with team by Friday of each week
5. **Comments:** Explain reduction logic and security properties in code

## Questions?

- Cryptography concepts: See course slides and Minicrypt paper
- Python implementation details: Use StackOverflow/Python docs
- Integration with team: Coordinate via shared interfaces (see `interfaces/`)
- Security properties: Reference attached spec PDFs

**Good luck, Raj! You're building the foundation that makes everything else possible.** 🎯

---

**Status:**
- ✅ Shared utilities (Week 1)
- ✅ Miller-Rabin primality (Week 1)
- ⏳ PA#1: OWF & PRG (Week 2)
- ⏳ PA#2: GGM PRF (Week 2-3)
- ⏳ Web app panels (Week 3)
