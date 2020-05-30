def crossOver(populasi, length):
    generasiBaru = []
    def dfs(cur, pos):
        if len(cur) == length:
            generasiBaru.append(cur)
        if pos == len(populasi):
            return
        if type(populasi) is list:
            for i in range(pos, len(populasi)):
                dfs(cur + [populasi[i]], i + 1)
        else:
            for i in range(pos, len(populasi)):
                dfs(cur + populasi[i], i + 1)
    if type(populasi) is list:        
        dfs([], 0)
    else:        
        dfs("", 0)
    return generasiBaru

def urutFitness(a,b) :
    if type(a) is list :  
        for i in range(0, len(a)):    
            for j in range(i+1, len(a)):
                #urutkan fitness    
                if(a[i] < a[j]):    
                    #urut untuk list fitness
                    temp = a[i]    
                    a[i] = a[j]    
                    a[j] = temp
                    #urutkan list kombinasi generasi 
                    temp2 = b[i]    
                    b[i] = b[j]    
                    b[j] = temp2
    return a,b
#membuat list untuk menampung jumlah koin dari setiap kemungkinan gabungan yang terjadi
#mengurutkan langsung list berdasarka jumlah fitness
def cekFitness(banyakAnak) :
    fitness = []
    buatFitness(banyakAnak,fitness)
    if type(banyakAnak) is list :
        for i in range(0, len(banyakAnak)):
            jumlah = 0
            for j in range(0, len(banyakAnak[0])):
                jumlah+=banyakAnak[i][j]
            fitness[i] = jumlah
    # memanggil fungsi urutFitness untuk mengurutkan dari yang terbesar
    fitness,banyakAnak = urutFitness(fitness,banyakAnak)        
    return fitness,banyakAnak
    
def buatFitness(banyakAnak,fitness):
    if type(fitness) is list :
        for i in range(0, len(banyakAnak)):
            fitness.append(0)
    return fitness

#mengubah isi kemungkinan koin dan fitnessnya menjadi nol
#ketika head tan tail tidak ada dalam kemungkinan gabungan koin
def cekIsi(fitness,banyakAnak,head,tail):
    if type(banyakAnak) is list :
        for i in range(0, len(banyakAnak)):
            tidakAda = True
            if(head in banyakAnak[i] or tail in banyakAnak[i] ):
                tidakAda = False
            else:
                fitness[i] = 0
                for j in range(0, len(banyakAnak[0])):
                    banyakAnak[i][j] = 0
                    
    fitness,banyakAnak = urutFitness(fitness,banyakAnak)            
    return fitness,banyakAnak  

selesai=False
while(selesai!=True):
    N=int(input("N : "))
    if(N%2 != 0 ):
        print(" masukan tidak berupa bilangan genap")
    else:
        pjgSolusi = int(N/2)
        print("\nMasukkan deretan nilai :")
        populasi = [int(input()) for i in range(N)]

        jlhMax = sum(populasi) #jumlah keseluruhan list
        
        #mulai algoritma genetika
        fitness = []
        banyakAnak = crossOver(populasi,pjgSolusi)
        fitness,banyakAnak = cekFitness(banyakAnak)
        
        mulai = int(input("pilih 1 untuk player mulai duluan 2 untuk Ai mulai duluan : "))
        j=0
        n=N
        x=0 #variabel untuk menampung list pilihan pemain
        y=0 #variabel untuk menampung list pilihan AI
        pemain=0
        collectAI = []
        collectPlayer = []
        for i in range(0,pjgSolusi):
            collectAI.append(0) #isi list koleksi AI
            collectPlayer.append(0) #isi list koleksi pemain

        head = 0
        tail = len(populasi)-1
        z=0
        tersedia = True #kondisi masukan pemain ada pada koin yang tersedia
        if(mulai==1):
            j+=1
            n+=1
            z+=1
            
        #MEMULAI PROGRAM
        for j in range(z,n):
            populasiBaru= [] # menyimpan populasi baru sementara
            print("\n\nKoin yang tersedia : ")
            for i in range(head,tail+1):
                print(populasi[i], end=" ")
                populasiBaru.append(populasi[i])
            if((j)%2 != 0):
                
                #membuat colection baru untuk digabung dengan populasi baru
                #ini dikarenakan colection player terkadang memiliki nilai '0'
                collectPlayerBaru = []
                collectPlayerBaru += collectPlayer
                while(0 in collectPlayerBaru):
                    collectPlayerBaru.remove(0)

                if(sum(collectPlayer) == 0):
                    print("")
                else:
                    populasiBaru = populasiBaru + collectPlayerBaru
                #---------------------------------------------------------------
                
                #tempat membuat solusi terbaik untuk pemain
                #menyatukan list yang sudah diambil oleh pemain dengan koin yang tersedia
                populasiBaru = crossOver(populasiBaru,pjgSolusi) #kombinasi yang kemungkinan terjadi pada populasi ini
                nilaiHead = populasi[head]
                nilaiTail = populasi[tail]
                ada = True
                fitness,banyakAnak = cekIsi(fitness,banyakAnak,nilaiHead,nilaiTail)

                print("\nKemungkinan Terbaik jika memilih : ",nilaiHead)
                for i in range(0,len(banyakAnak)):
                    if(banyakAnak[i] in populasiBaru and nilaiHead in banyakAnak[i]):
                        print(banyakAnak[i]," Fitness : ",fitness[i]) 
                        
                print("\nKemungkinan Terbaik jika memilih : ",nilaiTail)
                for i in range(0,len(banyakAnak)):
                    if(banyakAnak[i] in populasiBaru and nilaiTail in banyakAnak[i]):
                        print(banyakAnak[i]," Fitness : ",fitness[i]) 
                #---------------------------------------------------------------

                while(tersedia):
                    pemain = int(input("\nPlayer Pick : "))
                    if(pemain == populasi[head]):
                        tersedia = False
                    elif(pemain == populasi[tail]):
                        tersedia = False
                    else:
                        print("pilih harus antara ",populasi[head]," atau ",populasi[tail])
                    # kondisi jika pemain suda memilih koin yang benar
                tersedia = True
                if(pemain == populasi[head]):
                    head+=1
                    collectPlayer[x]=pemain
                    jlhMax-=pemain
                elif(pemain == populasi[tail]):
                    collectPlayer[x]=pemain
                    jlhMax-=pemain
                    tail-=1
                x+=1
                print("---------------------------------------------------------------")
            else:
                if(collectAI[y]+populasi[head]+jlhMax > collectAI[y]+populasi[tail]+jlhMax): #kondisi ketika nilai head lebih besar
                    collectAI[y]+=populasi[head]
                    print("\nAI Mengambil ",populasi[head])
                    jlhMax-=populasi[head]
                    head+=1
                elif(collectAI[y]+populasi[head]+jlhMax == collectAI[y]+populasi[tail]+jlhMax):
                    if(populasi[head] > populasi[tail]):
                        collectAI[y]+=populasi[head]
                        print("\nAI Mengambil ",populasi[head])
                        jlhMax-=populasi[head]
                        head+=1
                    else:
                        collectAI[y]+=populasi[tail]
                        print("\nAI Mengambil ",populasi[tail])
                        jlhMax-=populasi[tail]
                        tail-=1
                else:
                    collectAI[y]+=populasi[tail]
                    print("\nAI Mengambil ",populasi[tail])
                    jlhMax-=populasi[tail]
                    tail-=1
                y+=1
                print("---------------------------------------------------------------")
        #PROGRAM SELESAI
        #menampilkan koleksi pemain
        sumPemain=0
        sumAI=0
        print("\n\nPERMAINAN SELESAI !!! ")
        print("\nkoleksi koin Pemain : ")
        for i in range(0,x):
            print(collectPlayer[i],end=" ")
            sumPemain+=collectPlayer[i]
        print(" = ",sumPemain)
        print("\nkoleksi koin AI : ")
        for i in range(0,y):
            print(collectAI[i],end=" ")
            sumAI+=collectAI[i]
        print(" = ",sumAI)

        #cek jumlah terbanyak
        if(sumPemain>sumAI):
            print("\nPemain menang")
        elif(sumPemain == sumAI):
            print("\nPermainan imbang")
        else:
            print("\nAI Menang")

        mainLagi = input("\n\nmain Lagi(y/n) : ")
        if ( mainLagi == 'y' ):
            selesai = False
        else:
            selesai = True