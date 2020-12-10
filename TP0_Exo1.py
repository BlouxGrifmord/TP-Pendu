def AnneeBissextile(pA):
    
    pAt = str(pA)
    pAn = int(pA)
    ans = False
    if (pAt[-1]!=0  and pAt[-2]!=0):
        if pAn%4 == 0:
            ans = True
    elif pAn%400 == 0:
        ans = True
        
    return ans


def NbJours(pM,pA):
    
    M31 = [1,3,5,7,8,10,12]
    M30 = [4,6,9,11]
    if type(pM) != int or type(pA) != int or pM>12:
        ans = -1
    if pM in M30:
        ans = 30
    if pM in M31:
        ans=31
    if pM == 2:
        if AnneeBissextile(pA)==True :
            ans = 29
        else:
            ans = 28
    return(ans)
        
        
    
def DateValide(pJ,pM,pA):
    
    ans = True
    if type(pJ)!= int or pJ >NbJours(pM,pA) or pJ<0 or pM<0 :
        ans = False
    return(ans)
   
def SaisieDate():

    D = input("Saisir la date (JJ/MM/AAAA) :")
    J = int(D[:2])
    M = int(D[3:5])
    A = int(D[6:])

    if DateValide(J,M,A):
        print("Date valide")
    else:
        print("Date non valide")
        



def mesImpots(pR):
    
    Tranche = [0,9964,27519,737779,156244]
    Taux = [0,0.14,0.3,0.41,0.45]
    Impots = 0
    
    n=0
    for i in Tranche:
        if pR > i:
            n+=1       
    Impots = (pR-Tranche[n-1])*Taux[n-1]
    k=n-1
    while k>0:
        Impots += (Tranche[k]-Tranche[k-1])*Taux[k-1]
        k-=1
    return(Impots)
            


A = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]
B = [[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]]
def ProduitMatriciel(A,B):
    
    
    C=[]
    for n in range(0,len(A)):
        coeff = 0
n        for k in range(0,len(A)):
            coeff +=A[n][k]*B[k][n]
    
    
    

