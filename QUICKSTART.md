# Raj's POIS Project — Quick Start Guide

## ✅ What's Been Set Up For You

### Core Implementations (PA#13, PA#1, PA#2)
1. **PA#13: Miller-Rabin Primality** → `src/primality/miller_rabin.py`
   - ✅ `is_prime(n, k)` — Miller-Rabin test with k rounds
   - ✅ `gen_prime(bits)` — Generate b-bit probable primes
   - ✅ `gen_prime_safe(bits)` — Generate safe primes p=2q+1
   - ✅ Tests in `tests/test_pa13.py`

2. **PA#1: OWF & PRG** → `src/foundations/owf.py`
   - ✅ `DLP_OWF` — Discrete Log based one-way function
   - ✅ `HILL_PRG` — Haastad-Impagliazzo-Levin-Luby generator
   - ✅ Goldreich-Levin hard-core predicate implementation
   - ✅ Tests in `tests/test_pa1.py`

3. **PA#2: GGM PRF** → `src/prf/ggm_prf.py`
   - ✅ `GGM_PRF` — Pseudorandom function via GGM tree
   - ✅ Binary tree traversal for PRF evaluation
   - ✅ Backward direction: PRG from PRF
   - ✅ Tests in `tests/test_pa2.py`

### Shared Utilities (Week 1 Deliverables)
- ✅ `src/utils/random_utils.py` — `generate(n)` using os.urandom
- ✅ `src/utils/mod_exp.py` — `square_and_multiply(base, exp, mod)`
- ✅ `src/utils/ext_gcd.py` — Extended GCD and modular inverse
- ✅ `src/utils/int_root.py` — Integer root computation

### Interfaces (Shared with Team)
- ✅ `interfaces/owf.py` — OWF abstract base class
- ✅ `interfaces/prg.py` — PRG abstract base class
- ✅ `interfaces/prf.py` — PRF abstract base class

## 🚀 Getting Started

### 1. Set Up Python Environment
```bash
cd /home/rajkjain/Downloads/POIS_PROJECT
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

### 2. Run Your Tests
```bash
# Test all your implementations
python3 -m pytest tests/test_pa1.py tests/test_pa2.py tests/test_pa13.py -v

# Or run specific tests
python3 -m pytest tests/test_pa13.py -v  # Test Miller-Rabin
python3 -m pytest tests/test_pa1.py -v   # Test OWF & PRG
python3 -m pytest tests/test_pa2.py -v   # Test GGM PRF
```

### 3. Test Individual Components
```python
# In Python terminal:
from src.primality.miller_rabin import is_prime, gen_prime
from src.foundations.owf import DLP_OWF, HILL_PRG
from src.prf.ggm_prf import GGM_PRF

# Test primality
print(is_prime(17, k=20))  # True
print(is_prime(561, k=20))  # False (Carmichael number)

# Generate a 128-bit prime
p = gen_prime(128)
print(f"Generated prime: {p}")

# Create OWF and PRG
owf = DLP_OWF(bits=128)
prg = HILL_PRG(owf)
seed = b'\x00' * 16
output = prg.expand(seed, 32)
print(f"PRG output: {output.hex()}")

# Create and use GGM PRF
prf = GGM_PRF()
key = b'\x00' * 16
x = b'\x01' * 16
y = prf.evaluate(key, x)
print(f"PRF output: {y.hex()}")
```

## 📋 Status

| Component | Status | Location | Tests |
|-----------|--------|----------|-------|
| PA#13 Miller-Rabin | ✅ Complete | `src/primality/miller_rabin.py` | `tests/test_pa13.py` |
| PA#1 OWF & PRG | ✅ Complete | `src/foundations/owf.py` | `tests/test_pa1.py` |
| PA#2 GGM PRF | ✅ Complete | `src/prf/ggm_prf.py` | `tests/test_pa2.py` |
| Shared Utils | ✅ Complete | `src/utils/` | - |
| Interfaces | ✅ Complete | `interfaces/` | - |

## 🔍 What Each Implementation Does

### Miller-Rabin (`src/primality/miller_rabin.py`)
- **Inputs:** Integer n, number of rounds k
- **Outputs:** True (probably prime) or False (definitely composite)
- **Error probability:** ≤ 4^(-k)
- **Usage:** Used by Shobhan (PA#12 RSA key generation)

### OWF & PRG (`src/foundations/owf.py`)
- **DLP_OWF:** One-way function using discrete log
- **HILL_PRG:** Expands short seed to long pseudorandom stream
- **Used by:** Kanishk (encryption), Shubham (MACs), everyone (foundation)

### GGM PRF (`src/prf/ggm_prf.py`)
- **Input:** Key and n-bit input
- **Output:** Pseudorandom n-bit output
- **Method:** Binary tree traversal with PRG at each node
- **Used by:** Kanishk (CPA encryption), Shubham (MACs)

## 📚 Files Created for You

```
Your Project:
POIS_PROJECT/
├── src/
│   ├── foundations/
│   │   └── owf.py                      # PA#1: OWF & PRG
│   ├── prf/
│   │   └── ggm_prf.py                  # PA#2: GGM PRF
│   ├── primality/
│   │   └── miller_rabin.py             # PA#13: Primality
│   └── utils/
│       ├── random_utils.py             # Random generation
│       ├── mod_exp.py                  # Square-and-multiply
│       ├── ext_gcd.py                  # Extended GCD
│       └── int_root.py                 # Integer roots
├── interfaces/
│   ├── owf.py                          # OWF interface
│   ├── prg.py                          # PRG interface
│   └── prf.py                          # PRF interface
├── tests/
│   ├── test_pa1.py                     # PA#1 tests
│   ├── test_pa2.py                     # PA#2 tests
│   └── test_pa13.py                    # PA#13 tests
└── RAJ_README.md                       # Detailed assignment guide

(Plus __init__.py files for Python packages)
```

## ⚠️ Important Notes

1. **No External Crypto:** All code uses only os.urandom + Python int
2. **Bidirectional Reductions:** Both directions of each reduction are implemented
3. **Safe Primes:** Always use `gen_prime_safe()` for DH/DLP protocols
4. **Tests Must Pass:** Run tests before committing code to team

## 🎯 Next Steps

1. ✅ Review code in each module
2. ✅ Run tests to verify everything works
3. ✅ Share with team for Week 1 review (Friday EOD)
4. ⏳ Add web app panels (GGM visualizer + PRG viewer)
5. ⏳ Integrate with other team members' work

## 📞 Support

If you hit any issues:
1. Check test error messages: `python3 -m pytest -v` shows line numbers
2. Review comments in each `.py` file for implementation details
3. See `RAJ_README.md` for detailed cryptographic explanations
4. Check project spec PDF for security definitions

### Common Fixes Applied
1. If `python` is not found, use `python3`.
2. If `No module named pytest`, activate `venv` and install requirements.
3. If `ModuleNotFoundError: src.interfaces`, make sure source uses `interfaces.*` imports.
4. If prime generation fails with `negative shift count`, update to the fixed `gen_prime()` implementation in `src/primality/miller_rabin.py`.

---

**You're all set! Run the tests first to verify everything, then reach out to your team for integration.** 🚀
