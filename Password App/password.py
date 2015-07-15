#crypting not yet done 
#give a thought to login name change from saved data
#security question while saving password
#edit userid in main frame
#delete some saved password feature
# *************HIGHLY IMP FEATURE LEFT THAT AT A TIME ONLY ONE OF SAVE, EDIT , REVIEW FRAME SHUD BE ALLOWED TO OPEN ***************
import wx,filehandlingmod,pdb
       
#########################################################################################################################################################################
class filters():
    def newuser_filter(self,s,sb1,sb2,x):
        if sb1 == '' :
            dlg = wx.MessageDialog(s, 'Username cannot be kept blank', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        elif sb2 == '':
            dlg = wx.MessageDialog(s, 'Phone number cannot be kept blank', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        elif x.username_search(str(sb1),0):
            dlg = wx.MessageDialog(s, 'Username already exists in our database \nKindly select a new username', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        elif x.username_search(str(sb2),1):
            dlg = wx.MessageDialog(s, 'Phone number already registered in our database \nKindly enter another number', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else : 
            return True

    def save_new_password_filter(self,s,b):
        #NON BLANK ALIAS CHECKER 
        if b == '' or b == ' '*(len(b)):
            dlg = wx.MessageDialog(s, 'Alias cannot be kept blank\nIt wil help your retrieve your password\nSelect one such that you can remember', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else: return True

    def duplicate_alias_filter(self,s,user,sb1):
        x = filehandlingmod.filehandling()
        k = x.show_saved_data("",user,False)
        if (sb1) in k:
            dlg = wx.MessageDialog(s, 'Alias you gave already exists in our database\nIt wil help your retrieve your password\nSelect one such that you can remember it and is unique', 'Error', wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            return True
    def editpassword_filter(self,a,b,c,t):
        #new and old password cannot be the same
        if t==1 and a==b==c :
                dlg = wx.MessageDialog(self, "The old password and new password cannot be same.", 'Error', wx.OK|wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
        else:
            return True

#########################################################################################################################################################################

class authentication(wx.Frame):
    def __init__(self,parent,title,b):
        wx.Frame.__init__(self,parent,title = title,size = (400,275))
        panel = wx.Panel(self,-1)
        
        vsizer = wx.BoxSizer(wx.VERTICAL)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_b = wx.BoxSizer(wx.HORIZONTAL)
        
        st1 = wx.StaticText(panel,-1,"Enter your Name :\n(First + Last name) ")
        self.sb1 = wx.TextCtrl(panel,-1)
        hsizer1.Add(st1,1,wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,10)
        hsizer1.Add(self.sb1,2,0,0)
        
        st2 = wx.StaticText(panel,-1,"Enter the phone number : \n(with which u registered the account) ")
        self.sb2 = wx.TextCtrl(panel,-1)
        hsizer2.Add(st2,1,wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer2.Add(self.sb2,2,0,0)

        self.b1 = wx.Button(panel,1,"Login")
        self.b1.Bind(wx.EVT_BUTTON,self.login)
        self.b2 = wx.Button(panel,1,"Exit")
        self.b2.Bind(wx.EVT_BUTTON,self.quit)
        self.b3 = wx.Button(panel,1,"New User")
        self.b3.Bind(wx.EVT_BUTTON,self.user_reg)

        hsizer_b.Add(self.b1,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer_b.Add(self.b2,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer_b.Add(self.b3,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        
        vsizer.Add(hsizer1,2,wx.ALIGN_CENTER_HORIZONTAL|wx.UP,10)
        vsizer.Add(hsizer2,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        vsizer.Add(hsizer_b,2,wx.ALIGN_CENTER_HORIZONTAL|wx.UP,10)

        self.current_user_name = ''
        self.current_user = 0
        self.alluserinfo = []
        
        panel.SetSizer(vsizer)
        self.Centre()
        self.Show(b)
        
    def login(self,e):
        self.userinfo()
        if  self.user_match() :
            t = main(None,"Welcome " + self.alluserinfo[self.current_user][0],self.current_user_name,self.current_user)
            self.Destroy()
        else:
            self.st1 = wx.StaticText(self,-1,"Either of your credentials are wrong\n Kindly make changes and retry with login",(80,125),style = wx.ALIGN_CENTRE)
            
    def userinfo(self):
        x = filehandlingmod.filehandling()
        self.alluserinfo = x.userinfo()
        
    def user_match(self):
        t1,t2 = str(self.sb1.GetValue()),str(self.sb2.GetValue())
        for i,j in enumerate(self.alluserinfo):
            if t1 == str(j[0]) and t2 == str(j[1]):
                self.current_user = i
                self.current_user_name = str(j[0])
                return True
        return False
                
    def user_reg(self,e):
        a = user_regestration(None,"Register yourself user")
        
    def quit(self,e):
        dlg = wx.MessageDialog(self, 'Are you sure you want to exit?', 'Confirmation', wx.YES_NO|wx.NO_DEFAULT|wx.STAY_ON_TOP|wx.ICON_QUESTION)
        k = dlg.ShowModal()
        dlg.Destroy()
        if k  == wx.ID_YES:
            self.Destroy()
    
##########################################################################################################################################################################
class main(wx.Frame):

    def __init__(self,parent,title,user,identity):
        wx.Frame.__init__(self,parent,title = title,size= (466,100))
        self.panel = wx.Panel(self,-1)

        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.b1 = wx.Button(self.panel,1,"Save password")
        self.b2 = wx.Button(self.panel,1,"Retrieve password")
        self.b3 = wx.Button(self.panel,1,"Edit password")
        self.b4 = wx.Button(self.panel,1,"Exit")
        
        sizer1.Add(self.b1,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        sizer1.Add(self.b2,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        sizer1.Add(self.b3,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        sizer1.Add(self.b4,1,wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND,wx.ALL)
        
        self.b1.Bind(wx.EVT_BUTTON,self.savenewpassword)        
        self.b2.Bind(wx.EVT_BUTTON,self.reviewpassword)
        self.b3.Bind(wx.EVT_BUTTON,self.editpassword)
        self.b4.Bind(wx.EVT_BUTTON,self.quit)

        self.current_user_name = user
        self.current_user = identity 
        self.panel.SetSizer(sizer1)
        self.Centre()
        self.Show()

    def savenewpassword(self,e):
        self.panel.Disable()
        a = npass(None,"Save your password",self.current_user_name ,self.current_user + 1,self.panel)
    def reviewpassword(self,e):
        self.panel.Disable()
        a = rpass(None,"Review your saved passwords",self.current_user_name ,self.current_user + 1,self.panel)
    def editpassword(self,e):
        a = editpass(None,"Edit your credentials",self.current_user_name ,self.current_user + 1,self.panel)
        self.panel.Disable()
    def quit(self,e):
        dlg = wx.MessageDialog(self, 'Are you sure you want to exit?', 'Confirmation', wx.YES_NO|wx.NO_DEFAULT|wx.STAY_ON_TOP|wx.ICON_QUESTION)
        k = dlg.ShowModal()
        dlg.Destroy()
        if k  == wx.ID_YES:
            self.Destroy()

##########################################################################################################################################################################

##########################################################################################################################################################################

class user_regestration(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title = title)
        panel = wx.Panel(self,-1)
        vsizer = wx.BoxSizer(wx.VERTICAL)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_b = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel,-1,"Enter your Name \n(First + Last name) :")
        self.sb1 = wx.TextCtrl(panel,-1)
        hsizer1.Add(st1,1,wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,10)
        hsizer1.Add(self.sb1,2,0,0)

        st2 = wx.StaticText(panel,-1,"Enter the phone number \n(with which you want to register your account) :")
        self.sb2 = wx.TextCtrl(panel,-1)
        hsizer2.Add(st2,1,wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer2.Add(self.sb2,2,0,0)

        self.b1 = wx.Button(panel,1,"Save")
        self.b1.Bind(wx.EVT_BUTTON,self.save)
        self.b2 = wx.Button(panel,1,"Exit")
        self.b2.Bind(wx.EVT_BUTTON,self.quit)

        hsizer_b.Add(self.b1,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer_b.Add(self.b2,0,wx.ALIGN_CENTER_HORIZONTAL,0)
        
        vsizer.Add(hsizer1,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        vsizer.Add(hsizer2,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        vsizer.Add(hsizer_b,2,wx.ALIGN_CENTER_HORIZONTAL,0)
        #vsizer.Add(hsizer1,2,0,0)

        
        panel.SetSizer(vsizer)
        #vsizer.SetSizeHints(self)
        self.Centre()
        self.Show()

    def save(self,e):
        x = filehandlingmod.filehandling()
        y = filters()
        if (y.newuser_filter(self,self.sb1.GetValue(),self.sb2.GetValue(),x)) :
            x.save_new_entry(self.sb1.GetValue(),self.sb2.GetValue(),'','',True)
            self.Destroy()

    def quit(self,e):
        self.Destroy()

##########################################################################################################################################################################

class editpass(wx.Frame):
    def __init__(self,parent,title,user,identity,prev):
        wx.Frame.__init__(self,parent,title = title)
        panel = wx.Panel(self,-1)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.user = user
        self.identity = identity

        x=filehandlingmod.filehandling()
        string = x.show_saved_data("",self.user,False)

        self.cb = wx.ComboBox(panel,-1,'Select the alias with which you saved your data',size = (290,-1),choices = string, style = wx.CB_DROPDOWN)  
        self.cb.Bind(wx.EVT_COMBOBOX,self.show)
        self.stt2 = wx.StaticText(panel,-1,"Your username will appear here")
        
        st1 = wx.StaticText(panel,-1,"Enter the previous password :")
        self.sb1 = wx.TextCtrl(panel,-1)
        hsizer1.Add(st1,1,wx.ALIGN_LEFT,0)
        hsizer1.Add(self.sb1,2,0,0)

        st2 = wx.StaticText(panel,-1,"Enter the new password :")
        self.sb2 = wx.TextCtrl(panel,-1)
        hsizer2.Add(st2,1,wx.ALIGN_LEFT,0)
        hsizer2.Add(self.sb2,2,0,0)

        st3 = wx.StaticText(panel,-1,"Re-enter the new password :")
        self.sb3 = wx.TextCtrl(panel,-1)
        hsizer3.Add(st3,1,wx.ALIGN_LEFT,0)
        hsizer3.Add(self.sb3,2,0,0)
        
        self.b2= wx.Button(panel,1,"Update password")
        self.b3 = wx.Button(panel,1,"Exit")
        hsizer4.Add(self.b2,1,wx.ALIGN_CENTER_HORIZONTAL,0)
        hsizer4.Add(self.b3,1,wx.ALIGN_CENTER_HORIZONTAL,0)
        
        self.b2.Bind(wx.EVT_BUTTON,self.update)
        self.b3.Bind(wx.EVT_BUTTON,self.quit)
        
        vsizer1.Add(self.cb,0,wx.DOWN|wx.ALIGN_CENTER_HORIZONTAL,5)
        vsizer1.Add(self.stt2,0,wx.DOWN|wx.ALIGN_CENTER_HORIZONTAL,15)
        vsizer1.Add(hsizer1,0,wx.DOWN|wx.EXPAND,15)
        vsizer1.Add(hsizer2,0,wx.DOWN|wx.EXPAND,15)
        vsizer1.Add(hsizer3,0,wx.DOWN|wx.EXPAND,15)
        vsizer1.Add(hsizer4,0,wx.DOWN|wx.ALIGN_CENTER_HORIZONTAL,15)
        
        self.user = user
        self.identity = identity
        self.key = prev 

        self.x = filehandlingmod.filehandling() 

        panel.SetSizer(vsizer1)
        vsizer1.SetSizeHints(self)
        self.Centre()
        self.Show()
        
    def show(self,e):
        s = (self.cb.GetValue())
        t = self.x.show_saved_data(s,self.user,True)
        font = wx.Font(15,wx.ROMAN,wx.NORMAL,weight = wx.BOLD)
        self.stt2.SetLabel(str(t[0][0]))
        self.stt2.SetFont(font)
        
    def update(self,e):
        s = (self.cb.GetValue())
        if s!='Select the alias with which you saved your data':
            y = filters()
            if y.editpassword_filter(self.sb1.GetValue,self.sb2.GetValue,self.sb3.GetValue,1) and self.sb3.GetValue()==self.sb2.GetValue():
                temp = self.x.show_saved_data(s,self.user,True)
                if str(temp[0][1])== str(self.sb1.GetValue()) and len(temp)>=1:
                    self.x.save_editted_password(self.user,s,str(temp[0][1]),str(self.sb3.GetValue()))
                    self.key.Enable()
                    self.Destroy()
                else:
                    dlg = wx.MessageDialog(self, "The old password you entered does not match with the password saved in our database.\nPlease rectif!", 'Error', wx.OK|wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy() 
            else:
                dlg = wx.MessageDialog(self, "The new password you want to update is not same in above two places.\nPlease rectify!", 'Error', wx.OK|wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()        
   
    def quit(self,e):
        self.key.Enable()
        self.Destroy()

##########################################################################################################################################################################

class npass(wx.Frame):
    def __init__(self,parent,title,user,identity,prev):
        wx.Frame.__init__(self,parent,title = title)
        panel = wx.Panel(self,-1)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        
        st = wx.StaticText(panel,-1,"Enter the details properly to save into our database")
        font = wx.Font(15,wx.ROMAN,wx.NORMAL,weight = wx.BOLD)
        st.SetFont(font)
        st1 = wx.StaticText(panel,-1,"Enter the Alias :")
        self.sb1 = wx.TextCtrl(panel,-1)
        hsizer1.Add(st1,1,wx.ALIGN_LEFT,0)
        hsizer1.Add(self.sb1,2,wx.ALIGN_RIGHT,0)

        st2 = wx.StaticText(panel,-1,"Enter the Username :")
        self.sb2 = wx.TextCtrl(panel,-1)
        hsizer2.Add(st2,1,wx.ALIGN_LEFT,0)
        hsizer2.Add(self.sb2,2,wx.ALIGN_RIGHT,0)

        st3 = wx.StaticText(panel,-1,"Enter the password :")
        self.sb3 = wx.TextCtrl(panel,-1)
        hsizer3.Add(st3,1,wx.ALIGN_LEFT,0)
        hsizer3.Add(self.sb3,2,wx.ALIGN_RIGHT,0)
        
        self.b1 = wx.Button(panel,1,"Save Data")        
        self.b2 = wx.Button(panel,1,"Exit without saving")
        hsizer4.Add(self.b1,1,wx.RIGHT,10)
        hsizer4.Add(self.b2,1,wx.LEFT,10)
        
        self.b1.Bind(wx.EVT_BUTTON,self.save)
        self.b2.Bind(wx.EVT_BUTTON,self.quit)
        
        vsizer1.Add(st,0,wx.DOWN|wx.ALIGN_CENTER_HORIZONTAL,30)
        vsizer1.Add(hsizer1,0,wx.DOWN|wx.EXPAND,15)
        vsizer1.Add(hsizer2,0,wx.DOWN|wx.EXPAND,15)
        vsizer1.Add(hsizer3,0,wx.DOWN|wx.EXPAND,15)
        vsizer1.Add(hsizer4,0,wx.ALIGN_CENTER_HORIZONTAL,50)
        
        self.user = user
        self.identity = identity
        self.key = prev

        panel.SetSizer(vsizer1)
        vsizer1.SetSizeHints(self)
        self.Centre()
        self.Show()

    def save(self,e):
        x = filehandlingmod.filehandling()
        y = filters()
        if (y.save_new_password_filter(self,self.sb1.GetValue())):
            if y.duplicate_alias_filter(self,self.user,self.sb1.GetValue()) :
                x.save_new_entry(self.user,self.sb1.GetValue(),self.sb2.GetValue(),self.sb3.GetValue(),False)
                self.key.Enable()
                self.Destroy()

    def quit(self,e):
        self.key.Enable()
        self.Destroy()
    
##########################################################################################################################################################################

class rpass(wx.Frame):
    def __init__(self,parent,title,user,identity,prev):
        wx.Frame.__init__(self,parent,title = title)
        self.panel = wx.Panel(self,-1)

        self.user = user
        self.identity = identity
        self.key = prev

        x=filehandlingmod.filehandling()
        string = x.dropdown_options_in_rpass(self.user)

        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        
        self.cb = wx.ComboBox(self.panel,-1,'Select the alias with which you saved your data',size = (290,-1),choices = string, style = wx.CB_DROPDOWN)  

        self.st1 = wx.TextCtrl(self.panel, size = (-1,-1),style=wx.TE_READONLY|wx.BORDER_NONE|wx.EXPAND)
        self.st1.SetValue("Here is your userid")
        self.st1.SetBackgroundColour(wx.SystemSettings.GetColour(4))

        self.st2 = wx.TextCtrl(self.panel, size = (-1,-1), style=wx.TE_READONLY|wx.BORDER_NONE|wx.EXPAND)
        self.st2.SetValue("Here is your password")
        self.st2.SetBackgroundColour(wx.SystemSettings.GetColour(4))

        self.b1 = wx.Button(self.panel,-1,"Show")
        self.b1.Bind(wx.EVT_BUTTON,self.select)
        self.b2 = wx.Button(self.panel,-1,"Previous Window")
        self.b2.Bind(wx.EVT_BUTTON,self.close)

        self.st3 = wx.StaticText(self.panel,-1,"")

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self.b1,1,wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,0)
        hsizer1.Add(self.b2,1,wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,0)

                              
        self.vsizer.Add(self.cb,0,wx.DOWN|wx.UP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,15,25)
        self.vsizer.Add(self.st1,0,wx.UP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,25)
        self.vsizer.Add(self.st2,0,wx.UP|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL,25)
        self.vsizer.Add(hsizer1,0,wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.UP|wx.DOWN,40,20)
        self.vsizer.Add(self.st3,0,wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_BOTTOM,0)
        
        self.panel.SetSizer(self.vsizer)
        self.vsizer.SetSizeHints(self)
        self.Centre()
        self.Show()
    

    def select(self,e):
        s = (self.cb.GetValue())
        if s != 'Select the alias with which you saved your data':
            font = wx.Font(15,wx.ROMAN,wx.NORMAL,weight = wx.BOLD)
            x = filehandlingmod.filehandling()
            temp = x.show_saved_data(s,self.user,True)
            self.st1.SetLabel(str(temp[0][0]))
            self.st1.SetFont(font)
            self.st2.SetLabel(str(temp[0][1]))
            self.st2.SetFont(font)
            self.st3.SetLabel("You can simply select the userid and password and \n copy to which ever place you need if authentication.")
            self.vsizer.Layout()
            self.vsizer.Fit(self.panel)
            self.vsizer.SetSizeHints(self)
            self.Update()

    def close(self,e):
        self.key.Enable()
        self.Destroy()

##########################################################################################################################################################################
##########################################################################################################################################################################

app = wx.App()
aa = authentication(None,"Remeber your passwords with ease",True)
app.MainLoop()

