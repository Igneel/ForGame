import re
p1=re.compile("[\S ]*flag[\S ]*",re.IGNORECASE)
s="IGCADRPCDIETRNRYTTMOITSRRCCATOOASPHCWIHRPAOPTIHEYIPMYHLLERTEFLTOEPYEURAIRLIHFNTAISFNOAANAPTOSSEOSNNGDSA"
for a in range(2,len(s)):
    s1=""
    print(a)
    for x in range(0,a):
            s1=s1+s[x::a]
    print (s1)
    f=re.findall(p1,s1)
    if len(f) >0:
        print("Very Important Case!\n\n\n")
        print(s1)
    
#CWIHRPAOPTIHEYIPMYHLLERTEFLTOEPYEUR
#AIRLIHFNTAISFNOAANAPTOSSEOSNNGDSA


#I IMAGE OTCTIOARTODNSARRRSPYRPCTCHDTC

#INC GRACY TATODTORMAPO SCIPD THIS ERT RRC


#IGCADRPCDIETRNRYTTMOITSRRCCATOOASPH
#CWIHRPAOPTIHEYIPMYHLLERTEFLTOEPYEUR
# AIRLIHFNTAISFNOAANAPTOSSEOSNNGDSA


#INCRYPTOGRAPHYASCYTALEISATOOLUSEDTOPERFORMATRANSPOSITIONCIPHERANDTHEFLAGISCYLINDERWITHASTRIPOFPARCHMENT
