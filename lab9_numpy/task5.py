import numpy as np
from scipy.stats import multivariate_normal

def log_pdf_multivariate_normal(X, m, C):
    D = len(m)
    det_C = np.linalg.det(C)
    inv_C = np.linalg.inv(C)
    log_term = -0.5 * np.sum((X - m) @ inv_C * (X - m), axis=1)
    constant_term = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)
    return log_term + constant_term

X = np.random.randn(100, 2)
m = np.array([0, 0])
C = np.array([[1, 0.5], [0.5, 2]])
log_pdf_custom = log_pdf_multivariate_normal(X, m, C)
log_pdf_scipy = multivariate_normal(m, C).logpdf(X)

print(np.allclose(log_pdf_custom, log_pdf_scipy))
