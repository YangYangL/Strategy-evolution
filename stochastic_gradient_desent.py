def U1(p,q):
    return p[2]*(1-p[1])*q[1]+p[2]*p[1]*q[2]
def U2(p,q):
    return p[0]*p[2]*q[0]+p[2]*(1-p[0])*q[1]-p[2]
def U3(p,q):
    return p[0]*(p[1]-1)*q[0]+p[1]*(1-p[0])*q[2]+(1-p[1])

def Gy_fn(p,q,payoff_mat):
    return -payoff_mat[0]*q[3]*U1(p,q)+ payoff_mat[2]*q[3]*U2(p,q)-payoff_mat[1]*q[3]*U3(p,q)+payoff_mat[3]*[(-1+q[0]-(p[0]*q[0]-1)/p[1])*U1(p,q)+(-1+q[1]-(p[2]*q[1])/p[1])*U3(p,q)]

def Gy_gradient(p,q,payoff_mat):
    return [[payoff_mat[2]*p[0]*p[2]*q[3]+payoff_mat[1]*p[0]*(1-p[1])*q[3]+payoff_mat[3]*[(1-p[0]/p[1])*U1(p,q)+(-1+q[1]-(p[2]*q[1])/p[1])*p[0]*(p[1]-1)]],
            [-payoff_mat[0]*q[3]*p[2](1-p[1])+payoff_mat[2]*q[3]*p[2](1-p[0])+payoff_mat[3]*[(-1+q[0]-(p[0]*q[0]-1)/p[1])*p[2]*(1-p[1])+(1-p[2]/p[1])*U2(p,q)]],
            [-payoff_mat[0]*q[3]*p[1]*p[2]-payoff_mat[1]*q[3]*p[1]*(1-p[0])+payoff_mat[3]*[(-1+q[0]-(p[0]*q[0]-1)/p[1])]*p[2]*p[1]+(-1+q[1]-(p[2]*q[1])/p[1])*p[1]*(1-p[0])],
            [-payoff_mat[0]*U1(p,q)+payoff_mat[2]*U2(p,q)-payoff_mat[1]*U3(p,q)]]

def Gx_fn(p,q,payoff_mat):
    return -payoff_mat[0] * q[3] * U1(p, q) + payoff_mat[1] * q[3] * U2(p, q) - payoff_mat[2] * q[3] * U3(p, q) + payoff_mat[3] * [
               (-1 + q[0] - (p[0] * q[0] - 1) / p[1]) * U1(p, q) + (-1 + q[1] - (p[2] * q[1]) / p[1]) * U3(p, q)]

