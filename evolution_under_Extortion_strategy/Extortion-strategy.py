from numpy import *

def PAYOFFMAT():
    Pay1=array([3,0,5,1])
    Pay2=array([2,0,4,-1])
    Pay=array([Pay1,Pay2])
    return Pay

# x take extortion strategy at lamda=3,phai=1/26
p=tuple((11/13),(1/2),7/26,0)

# s=array([[0.5,0.5],[0.5,0.5]])
s=array([[0.8,0.2],[0.1,0.9]])
# s=array([[1,0],[0,1]])
# s=array([[0.2, 0.8], [0.9, 0.1]])

#environment Model (Model-based Rl)
def state_Transition_Matrix(s,p,q):
    r1 = array([p[0] * q[0] / 100, p[0] * (100 - q[0]) / 100, (1 - p[0]) * q[0] / 100, (1 - p[0]) * (100 - q[0]) / 100])
    r2 = array([p[1] * q[2] / 100, p[1] * (100 - q[2]) / 100, (1 - p[1]) * q[2] / 100, (1 - p[1]) * (100 - q[2]) / 100])
    r3 = array([p[2] * q[1] / 100, p[2] * (100 - q[1]) / 100, (1 - p[2]) * q[1] / 100, (1 - p[2]) * (100 - q[1]) / 100])
    r4 = array([p[3] * q[3] / 100, p[3] * (100 - q[3]) / 100, (1 - p[3]) * q[3] / 100, (1 - p[3]) * (100 - q[3]) / 100])
    A = array([r1, r2, r3, r4])
    r = s[0, 0] * A
    for k in range(1, 2):
        r = column_stack((r, s[0, k] * A))
    A = r
    for i in range(1, 2):
        r = s[i, 0] * A
        for j in range(1, 2):
            r = column_stack((r, s[i, j] * A))
        A = row_stack((A, r))
    print(A)
    return A

def dict_Xpay_type(Payoffmat):
    Pay_X=tuple(Payoffmat[0][3],Payoffmat[0][2],Payoffmat[0][1],Payoffmat[0][0],Payoffmat[1][3],Payoffmat[1][2],Payoffmat[1][1],Payoffmat[1][0])
    return Pay_X

def dict_Ypay_type(Payoffmat):
    Pay_Y=tuple(Payoffmat[0][3],Payoffmat[0][1],Payoffmat[0][2],Payoffmat[0][0],Payoffmat[1][2],Payoffmat[1][3],Payoffmat[1][1],Payoffmat[1][0])
    return Pay_Y

def x_p_cooperate(current_state,p):
    if current_state==0 or current_state==4:
        return p[3]
    if current_state==1 or current_state==5:
        return p[2]
    if current_state==2 or current_state==6:
        return p[1]
    if current_state==0 or current_state==4:
        return p[0]

def Extortion_Player_X(current_state):
    p_cooperate=x_p_cooperate(current_state,p)
    return random.uniform(0,1)<p_cooperate

def a_value_fn():
   pass

