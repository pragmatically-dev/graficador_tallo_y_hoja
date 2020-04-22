#AUTOR
#NIEVA SANTIAGO
#GMAIL:totonieva3@gmail.com
#GITHUB: github.com/pragmatically-dev/




def Ordenar(conj):
    conj.sort()
    l=conj
    frec=[]
    for i in range(len(l)):    
        t=l[i]
        frec.append(t)
    return frec




def obtenerTallos(c):
    tallos=[]
    conjunto=c
    for i in conjunto:
        d=str(i)
        if(len(d)>2):
            tallos.append(int(d[:2]))
        else:
            tallos.append(int(d[0]))
    print("Conjunto:",conjunto)
    tallos=list(set(tallos))
    print("Tallos:",tallos)
    return tallos



def resolverDiagrama(t,conj):
    talloYhoja=list()
    for i in t:
        for e in conj:
            d=str(e)
            if(len(d)>2):
               if(str(i)==d[:2]):
                    ax=[i,0]
                    aux=(int(d[1:3]))
                    ax[1]=aux
                    talloYhoja.append(ax)
            else:
                if(str(i)==d[0]):
                    ax=[i,0]
                    aux=(int(d[1]))
                    ax[1]=aux
                    talloYhoja.append(ax)


    return talloYhoja


def mostrarDiagrama(dataraw,tallos):
    aux=["" for i in range(len(tallos))]
    for x in range(len(tallos)):
        for i in dataraw:
            if(i[0]==tallos[x]):
                aux[x]+="  "+str(i[1])
            
    for c in range(len(tallos)):
        print(" "+str(tallos[c]) + "    |  " + aux[c] )
    
    
if __name__=="__main__":

    conj=[10, 10, 12, 12, 14, 15, 17, 20, 20, 20, 22, 22, 22, 24, 24, 25,25, 25, 28, 30, 30, 30, 32, 35, 35, 35, 40, 48, 50, 50, 50, 50, 50, 50, 60, 65, 65, 79, 120]
    conj= Ordenar(conj)
    tallos=obtenerTallos(conj)
    dataraw=resolverDiagrama(tallos,conj)

    mostrarDiagrama(dataraw,tallos)
    
    
            
