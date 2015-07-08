#FILEHANDLING MODULES
import string
class filehandling():
    def __init__(self):
        self.a = 'C:\Users\DJ\Documents\pss.txt'
    def userinfo(self):
        f = open(self.a,'r')
        userinfo = [((l.split('\t'))[2],(l.split('\t'))[3]) for l in f if (l.split('\t'))[1] == 'Username' and (l.split('\t'))[0] == '#u' and len(l.split('\t')) >= 2]
        return userinfo
    
    def save_new_user(self,x,y):
        f = open(self.a,'a')
        s = '#u'+'\t'+"Username"+'\t'+str(x)+'\t'+str(y)+'\t'+'\n'
        #this will help in crypting decrypting
        f.write(str(s)) 
        f.close()
    
    def save_new_password(self,w,x,y,z):
        f = open(self.a,'a')
        s = str(w)+'\t'+str(x)+'\t'+str(y)+'\t'+str(z)+'\t'+'\n'
        f.write(str(s))
        f.close()
        
    def dropdown_options_in_rpass(self,user):
        f = open(self.a,'r')
        string = [str.split(str(l),'\t')[1] for l in f if str.split(str(l),'\t')[0] == str(user)]
        f.close()
        return string
        
    def show_saved_password(self,s,user):
        f = open(self.a,'r')
        t = [((l.split('\t'))[2],(l.split('\t'))[3]) for l in f if (l.split('\t'))[1] == str(s) and (l.split('\t'))[0] == str(user) and len(l.split('\t')) >= 3]
        f.close()
        return t

    def username_search(self,x,t):
        l = self.userinfo()
        f = [x for term in l if term[t] == x]
        if len(f)>0:
            return 1
        else: return 0
   
    def save_editted_password(self,user,x,old,new):
        f = open(self.a,'r')
        s= ""        
        for l in f:
            if  str(user) in l and str(x) in l and str(old) in l : 
                t = l.split("\t")
                t[t.index((old))] = str(new)
                s = s + "\t".join(t)
            else :
                s = s + str(l)
        f.close()
        f = open('C:\Users\DJ\Documents\pss.txt','w')
        f.write(s)
        f.close()
        return