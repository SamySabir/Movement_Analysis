question_1= input('Bonjour!' + '\n' + 'Combien de pas peut effectuer votre robot?')

a=int(question_1) #c'est le nombre de pas possibles

question_2= input("C'est noté!"+'\n'+ "Quelle sera une des dimensions de la région carrée où vous voulez que le robot se déplace ?") #formulation de la question??

b=int(question_2) #C'est la longueur d'un coté du carré d'incertitude

x= var("x")
f=1/(1-x-x^2-x^3)
f_1=(1)/(1-2*x-2*x^2-2*x^3)
d=f.taylor(x,0,a)      #fcts taylor 1 direction
d_1=d.coefficients()   #coefficients=nbr de chemins possibles 1 direction
e=f_1.taylor(x,0,a)    #fcts taylor 2 directions
e_1=e.coefficients()   #coefficients= nmbr chemins possibles 2 directions

K = 0

# Nombre de chemins avec des pas perdus
for i in range ((a/2)-(b/2), (a/2)+(b/2)+1):
    for n in range (2, (b/2)+1):
        for m in range (1, n):
            if ((a/2)-(b/2)) <=a-2*n-i<=  ((a/2)+(b/2)):
                K+= int(d_1[i][0])*int(d_1[m][0])^2* int(d_1[n-m][0])^2 * int(d_1[a-2*n-i][0])


# Nombre de chemins sans pas perdus
C = 0
for i in range ((a/2)-(b/2), (a/2)+(b/2)+1):
    C += int(d_1[i][0])*int(d_1[a-i][0])


M = K+C   # nombre total de chemin dans la boite

L = int(e_1[a][0])

P = float( M/L)*100

show(f'Probabilité que le robot arrive dans la boite:   {P}  % ')
