import os  
from time import time
import binascii
import math
import os.path

enter_name_of_file = input("New computer code: c and old computer code: e: ")

#@Author Jurijus pacalovas

class compression:

    def cryptograpy_compression(self):

                self.name = "Created: Jurijus pacalovas price Software 1000 000 Euro cost"

                if enter_name_of_file=="c":
                    counts_times=0


                    corridors=0


                    corridors_2=7


                    name = input("What is name of file? ")


                    name_new="file.Secret"

                    name_2=""

                    name_2_clear="?"

                    e5=0


                    e1=""


                    e6=0


                    e7=255

                    INFO3=""

                    INFO4=""

                    INFO5=""

                    reverse_bin=0

                    block_2=5

                    block_21=4

                    name_1=name

                    name_of_file=len(name_1)

                    name_1=name+".bin"

                    name_of_file=len(name_1)

                    count_numbers=0

                    counts_1=2


                    counts_11=0





                    s=""





                    e2=0





                    e3=2





                    e4=""





                    c=2





                    select_words=2





                    elements_words=0





                 





                    INFO3=""





                    INFO_OR_DATA_TO_BINARY=""











                    size_of_size_cosscounts_1=0





                    





                    binary_to_data=0











                    block=1





                    r=""











                    x=0





                    x1=0





                    x2=0





                    x = time()











                    with open(name_1, "w") as f4:





                            f4.write(s)





                    with open(name_1, "a") as f3:





                            f3.write(s)





                    with open(name, "rb") as binary_file:



                       # Read the whole file at once

                   
                        data = binary_file.read()
                     
                      


                        s=str(data)



                        long1=len(data)





                        long5=len(data)


                        times_numbers_reapits=0


                        binary_to_data_1=0




                        while times_numbers_reapits<10:





                            aas1=0


                            a1=0


                            counts_1=counts_1+1



                            count_numbers=count_numbers+1



                            with open(name_1, "ab") as f2:





                                if count_numbers==1:





                                    INFO=bin(int(binascii.hexlify(data),16))[2:]





                                    long=len(INFO)





                                    long1=len(data)




                                    times_7=(long1*8)-long





                                    z=0





                                    if times_7!=0:





                                        while z<times_7:



                                            if counts_11==0:

                                                INFO="0"+INFO





                                            z=z+1



                                    INFO=INFO


                                    if count_numbers==1:

                                     INFO_OR_DATA_TO_BINARY=INFO
                                     c=1
                                     counts_12=0
                                     counts_14=0
                                     if c==1:
                                         
                                         while counts_11!=1:
                                             L=0
                                             long2=len(INFO_OR_DATA_TO_BINARY)
                                             block=0
                                             X=0
                                             X1=0
                                             INFOS=""
                                             Er="0"
                                             
                                             while block<long2:
                                                xyz1=INFO_OR_DATA_TO_BINARY[block:block+5]
                                                xyz=xyz1[0:4]
                                                xyzg1=xyz1[0:2]
                                                xyzg2=xyz1[2:4]
                                                if len(xyz1)==5:
                                                    
                                                    A=int(xyz1[0:2],2)
                                                    B=int(xyz1[2:4],2)
                                                    B1=int(xyz1[2:4],2)
                                                    B2=xyz1[2:4]
                                                    B3=int(xyz1[2:3],2)
                                                #print(X1)
                                                if     len(xyz1)!=5:
                                                        X1=1
                                                else:
                                                     AB=int(xyz,2)
                                                X+=1
                                                if X>1:
                                                    X=0
                                                #print(X)


                                                if A==X and B==X and X==1 and xyz1[4:5]=="0":
                                                    C="00"+"1"+xyz1[3:4]
                                                    #print(C)
                                                                                                                   
                                                elif A==X and B3==X and X==0:
                                                    
                                                    C="01"+"1"+xyz1[3:4]
                                                    #print(xyz1)
                                                    #print(C)                                           
                                                
                                                elif A==X and B3==X and X==1:
                                                    
                                                    C="00"+"0"+xyz1[3:4]
                                                    #print(xyz1)
                                                    #print(C)   
                                                
                                                elif A==X and B==X and X==1 and len(xyz1)==5:
                                                    if xyz1[4:5]=="1":
                                                    
                                                        C=xyzg1+"0"
                                                    
                                                        
                                                                                                                                          
                                                    #print(xyz1)
                                                    #print(C)   
                                                    
                                                elif A==X and B==X and X==0:
                                                    Er="1"
                                                    


                                                    #print(xyz1)
                                                    #print(C)   
                                                    

                                             
                                                else:
                               
                                                         

                                                         
                                                         

                                                 
                                                         #print(X)
                                                         C=xyz1[:4]
                                                         if len(xyz1)<4:
                                                             Er="1"
                                                         
                                                         
                                                       
                                                         #print(C)
                                                         
                                                                                                             
                                                 
                                                 
                                                if A==X and B=="00" and X==1 and  len(xyz1)==5:
                                                    if xyz1[4:5]=="0":
                                                        Er="1"
                                                    #print(xyz1)
                                                    #print(C)   
                                                if A=="00" and B=="11" and X==1:
                                                     if xyz1[4:5]=="0":
                                                         Er="1"                                                                                                                                                                                                
                                                 
       
                                                   
                                                #print(C)
                                                INFOS=INFOS+C
                                                
                                                
                                                block+=4
                                                #print(block)
                                          
                                            
                                             L=len(xyz1)
                                             L-=1
                                           
                                             C=format(L,'02b')
                                             if Er=="0":
                                                 INFOS=INFOS+C+Er
                                             else:
                                                  INFOS=INFO_OR_DATA_TO_BINARY+Er
                                                  
                                             INFO_OR_DATA_TO_BINARY=INFOS
                                             After_long=len(INFOS)
                                             counts_12+=1
                                             if After_long>long2 or counts_12==(2**24)-1:
                                                 counts_14+=1
                                                 INFO_OR_DATA_TO_BINARY
                                                 #print(long2)
                                                 #print(counts_14)
                                                 
                                                 
                                             if counts_14==52 or counts_12==(2**24)-1:
                                                 counts_11=1
                                                 
                                                 
                                              
                                             #print(INFOS)
                                             
                                         if counts_11==1:
                                                             
                                         
                                    

                                              
                                              add_times=format(counts_12,'024b')
                                              INFOS=add_times+INFOS
                                             
                                              INFO_OR_DATA_TO_BINARY="1"+INFOS

                                    long=len(INFO_OR_DATA_TO_BINARY)
                                long1=len(INFO_OR_DATA_TO_BINARY)
                                times_7=8-long%8
                                z=0
                               
                                if times_7!=0:





                                        while z<times_7:





                                            INFO_OR_DATA_TO_BINARY="0"+INFO_OR_DATA_TO_BINARY





                                            z=z+1                                        
                                    
                                        
                                        n = int(INFO_OR_DATA_TO_BINARY, 2)
                                        #print(n)


                                        binary_data=len(INFO_OR_DATA_TO_BINARY)
                                        #print(binary_data)





                                        binary_data=(binary_data/8)*2





                                        binary_data=str(binary_data)





                                        binary_data="%0"+binary_data+"x"


                                        jl=binascii.unhexlify(binary_data % n)

                                        binary_to_data_2=len(jl)

                                        data=jl

                                        binary_to_data_1=binary_to_data_1+1



                                        binary_to_data_3=""


                                        size_x=""



                                        reverse_bin=reverse_bin+1
                                        if reverse_bin==1:

                                                times_numbers_reapits=10
                                             
                                                if times_numbers_reapits==10:
                                                      

                                                            f2.write(jl)
                                                            x2 = time()
                                                            x3=x2-x
                                                            return print(x3)







    def cryptograpy_unpack(self):                                 





                 if enter_name_of_file=="e":





                    corridors=0





                    corridors_2=7





                    name=input("What is name of file? ")





                    name_new="file.Secret"





                    name_2=""





                    name_2_clear="?"





                    e1=""











                    e5=0





                    e6=0





                    e7=255











                    INFO3=""





                    INFO4=""





                    INFO5=""





                    INFO8=""











                 





                    reverse_bin=0





                    block_2=5





                    block_21=4





                    name_1=name





                    name_of_file=len(name_1)





                    name_1=name[:name_of_file-4]





                    name_of_file=len(name_1)





                    





                    count_numbers=0





                    counts_1=2





                    counts_11=0





                    s=""





                    e2=0





                    e3=2





                    e4=""





                    c=2





                    select_words=2





                    elements_words=0





                    cr=0





                 





                    INFO3=""





                    INFO_OR_DATA_TO_BINARY=""











                    size_of_size_cosscounts_1=0





                    





                    binary_to_data=0











                    block=1





                    counts_11=0











                    x=0





                    x1=0





                    x2=0





                    x = time()











                    with open(name_1, "w") as f4:





                            f4.write(s)





                    with open(name_1, "a") as f3:





                            f3.write(s)





                    with open(name, "rb") as binary_file:











                        # Read the whole file at once





                        data = binary_file.read()





                        s=str(data)





                        





                        long1=len(data)





                        long5=len(data)





                        





                        times_numbers_reapits=0





                        binary_to_data_1=0





                       





                        while times_numbers_reapits<10:





                       





                            aas1=0





                            a1=0











                            counts_1=counts_1+1





                            





                            count_numbers=count_numbers+1











                            with open(name_1, "ab") as f2:





                                if count_numbers==1:





                                    INFO=bin(int(binascii.hexlify(data),16))[2:]





                                    long=len(INFO)





                                    long1=len(data)





                                





                                    times_7=(long1*8)-long





                                    z=0





                                    if times_7!=0:





                                        while z<times_7:





                                            INFO="0"+INFO





                                            z=z+1





                                            





                                    INFO=INFO











                                    if count_numbers==1:




                                        c=1                                   
                                        counts_12=0
                                        counts_14=0
                                        INFO_OR_DATA_TO_BINARY=INFO
                                        size_data3=INFO_OR_DATA_TO_BINARY
                                        if counts_12==0:
                                            
                                            if size_data3[0:9]=="000000001":
                                                size_data3=size_data3[9:]
                                            elif size_data3[0:8]=="00000001":
                                                size_data3=size_data3[8:]
                                            elif size_data3[0:7]=="0000001":
                                                size_data3=size_data3[7:]
                                            elif size_data3[0:6]=="000001":
                                                size_data3=size_data3[6:]
                                            elif size_data3[0:5]=="00001":
                                                size_data3=size_data3[5:]
                                            elif size_data3[0:4]=="0001":
                                                size_data3=size_data3[4:]
                                            elif size_data3[0:3]=="001":
                                                size_data3=size_data3[3:]
                                            elif size_data3[0:2]=="01":
                                                size_data3=size_data3[2:]
                                            elif size_data3[0:1]=="1":
                                                size_data3=size_data3[1:]
                                            
                                            size_data3=size_data3
                                            
                                    if c==1:
                                         times_1=int(size_data3[:24],2)
                                         size_data3=size_data3[24:]
                                         INFO_OR_DATA_TO_BINARY=size_data3
                                         
                                         while counts_11!=1:
                                             L=0
                                             long2=len(INFO_OR_DATA_TO_BINARY)
                                             Er=INFO_OR_DATA_TO_BINARY[long2-1:]
                                             INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY[:long2-3]
                                             long2=len(INFO_OR_DATA_TO_BINARY)
                                             block=0
                                             X=0
                                             X1=0
                                             INFOS=""
                                             Er="0"
                                             while block<long2:
                                                xyz1=INFO_OR_DATA_TO_BINARY[block:block+5]
                                                xyz=xyz1[0:4]
                                                xyzg1=xyz1[0:2]
                                                xyzg2=xyz1[2:4]
                                                if len(xyz1)==5:
                                                    
                                                    A=int(xyz1[0:2],2)
                                                    B=int(xyz1[2:4],2)
                                                    B1=int(xyz1[2:4],2)
                                                    B2=xyz1[2:4]
                                                    B3=int(xyz1[2:3],2)
                                                #print(X1)
                                                if     len(xyz1)!=5:
                                                        X1=1
                                                else:
                                                     AB=int(xyz,2)
                                                X+=1
                                                if X>1:
                                                    X=0
                                                #print(X)


                                                if A=="00" and B=="11" and X==1 and len(xyz1)==5: 
                                                    if xyz1[4:5]=="0":
                                                        C="01"+"01"
                                                    else:
                                                        C=xyz
                                                    block+=4
                                                    #print(C)
                                                                                                                   
                                                elif A==X and B3==X and X==0:
                                                    
                                                    C="01"+"1"+xyz1[3:4]
                                                    block+=4
                                                    #print(xyz1)
                                                    #print(C)                                           
                                                
                                                elif A==X and B3==X and X==1:
                                                    
                                                    C="00"+"0"+xyz1[3:4]
                                                    block+=4
                                                    #print(xyz1)
                                                    #print(C)   
                                                
                                                elif A==X and B==X and X==1:
                                                    
                                                    
                                                        C=xyzg1+"01"
                                                        block+=3
                                                    
                                                        
                                                                                                                                          
                                                    #print(xyz1)
                                                    #print(C)   
                                                    
 
                                                    #print(xyz1)
                                                    #print(C)   
                                                    

                                             
                                                else:
                               
                                                         

                                                         
                                                         

                                                 
                                                         #print(X)
                                                         C=xyz1[:4]
                                                         block+=4
                                                       
                                                         
                                                         
                                                       
                                                         #print(C)
                                                         
                                                                                                             
                                                 
                                                                                                                                                                                                                             
                                                 
       
                                                   
                                                #print(C)
                                                INFOS=INFOS+C
                                                
                                                
                                               
                                                #print(block)
                                          
                                            
                                             if Er=="0":
                                                 INFOS=INFOS
                                             else:
                                                  INFOS=INFO_OR_DATA_TO_BINARY
                                                  
                                             INFO_OR_DATA_TO_BINARY=INFOS
                                             After_long=len(INFOS)
                                             counts_12+=1
                                   
                                                 #print(long2)
                                                 #print(counts_14)
                                                 
                                                 
                                             if counts_12==times_1:
                                                 counts_11=1
                                                 
                                                 
                                              
                                             #print(INFOS)
                                             
                                         if counts_11==1:
                                                             
                                             long=len(INFO_OR_DATA_TO_BINARY)
                                long1=len(INFO_OR_DATA_TO_BINARY)
                                times_7=8-long%8
                                z=0
                               
                                if times_7!=0:





                                        while z<times_7:





                                            INFO_OR_DATA_TO_BINARY="0"+INFO_OR_DATA_TO_BINARY





                                            z=z+1                                        
                                    
                                        
                                        n = int(INFO_OR_DATA_TO_BINARY, 2)
                                        #print(n)


                                        binary_data=len(INFO_OR_DATA_TO_BINARY)
                                        #print(binary_data)





                                        binary_data=(binary_data/8)*2





                                        binary_data=str(binary_data)





                                        binary_data="%0"+binary_data+"x"


                                        jl=binascii.unhexlify(binary_data % n)

                                        binary_to_data_2=len(jl)

                                        data=jl

                                        binary_to_data_1=binary_to_data_1+1



                                        binary_to_data_3=""


                                        size_x=""



                                        reverse_bin=reverse_bin+1
                                        if reverse_bin==1:

                                                times_numbers_reapits=10
                                             
                                                if times_numbers_reapits==10:
                                                      

                                                            f2.write(jl)
                                                            x2 = time()
                                                            x3=x2-x
                                                            return print(x3)




d=compression()











xw=d.cryptograpy_compression()





print(xw)











xw1=d.cryptograpy_unpack()





print(xw1)