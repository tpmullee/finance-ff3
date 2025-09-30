import sys, pandas as pd, numpy as np
from datetime import datetime
# Minimal placeholder: prints a fake "alpha/betas" table so the project runs instantly.
ticker = sys.argv[1] if len(sys.argv) > 1 else "SPY"
np.random.seed(0)
coefs = pd.DataFrame({"coef":["alpha","Mkt-RF","SMB","HML"], "value":np.round(np.random.randn(4)/10,3)})
print(f"[FF3 demo] Ticker={ticker}  As-of={datetime.utcnow().date()}")
print(coefs)
