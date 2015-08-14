#FILEHANDLING MODULES
import getpass,os,platform
class filehandling():
    def __init__(self):
	if platform.system()=='Linux':
		x=getpass.getuser()
		path="/home/"+str(x)+"/Password_Database"
		if not os.path.isdir(path):		
			os.mkdir(path)
        	self.a = path+'/pss.txt'
		if not os.path.exists(self.a):		
			f = open(self.a,'a')
			f.close()
	if platform.system()=='Windows':
		x=getpass.getuser()
		path="C:\Users"+str(\)+str(x)+"\Documents\Password_Database"
		if not os.path.isdir(path):		
			os.mkdir(path)
        	self.a = path+'\pss.txt'
		if not os.path.exists(self.a):		
			f = open(self.a,'a')
			f.close()
        #self.element = cryptingmod.cryptography()
    
    def userinfo(self):
        f = open(self.a,'r')
        userinfo = []
        for l in f:
            t = (l.split('\t'))
            if len(t)>=2 and "#u" in l and "Username" in l:
                userinfo.append((t[2],t[3]))
        return userinfo
        
    def save_new_entry(self,w,x,y,z,switch):
        f = open(self.a,'a')
        if switch:
            s = ['#u',"Username",str(w),str(x),'\n']
            x = [str(item) for item in s]
        else:        
            s = [w,x,y,z,'\n']
            x = [str(item) for item in s]
        f.write("\t".join(x))
        f.close()
            
    def show_saved_data(self,s,user,switch):
        f = open(self.a,'r')
        t = []
        for l in f:
            temp = l.split('\t')
            if switch :
                if len(temp)>=2 and str(temp[1])==str(s) and str(temp[0]== str(user)):
                    t.append((temp[2],temp[3]))
            else:
                if len(temp)>=2 and str(temp[0])==str(user):
                    t.append((temp[1]))
        f.close()
        return t

    def username_search(self,x,t):
        l = self.userinfo()
        f = [x for term in l if term[t] == x]
        if len(f)>0:
            return True
        else: return False
   
    def save_editted_password(self,user,x,old,new):
        f = open(self.a,'r')
        s = ''
        for l in f:
            t = l.split("\t")
            if str(user)==str(t[0]) and str(x)==str(t[1])and str(old)== str(t[3]) : 
                t[3] = str(new)
                s = s + "\t".join(t)
            else :
                s = s + str(l)
        f.close()
        f = open('C:\Users\DJ\Documents\pss.txt','w')
        f.write(s)    
        f.close()
        return
