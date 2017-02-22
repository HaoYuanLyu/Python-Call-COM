'''
Created on 2017/02/17

@author: haoyuanlyu
'''

# GUI component
import Tkinter
from Tkinter import*
import ttk

# COM component
import comtypes
import comtypes.client
from comtypes import BSTR

# Load the typelibrary registered with the Windows registry
tlb_id = comtypes.GUID("{55F15B5C-F5EB-4f78-8485-7D57F00F2B98}")
GM = comtypes.client.GetModule((tlb_id,1,0)) 
print GM

import comtypes.gen._55F15B5C_F5EB_4F78_8485_7D57F00F2B98_0_1_0 as DJTRADEOBJLibTCST

class App(Tkinter.Tk):
    # contractor
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    
    #defoult init
    def initialize(self):
        self.TradeObject = comtypes.client.CreateObject("DJTradeObj.TradeApp")
        print self.TradeObject
        self.TradeApp = self.TradeObject.QueryInterface(DJTRADEOBJLibTCST.ITradeApp)
        print self.TradeApp
        strDas = ''
        rtn = self.TradeApp.Init(strDas)
        print rtn
        
        self.strLoginID = Tkinter.StringVar(self)
        self.strLoginPwd = Tkinter.StringVar(self)
        self.strLoginInfo = Tkinter.StringVar()
        
        # init GUI component
        UIDLB = Tkinter.Label(self,text='UID')
        PwdLB = Tkinter.Label(self,text='PWD')
        
        LoginIdED = Tkinter.Entry(self, textvariable=self.strLoginID)
        LoginPwdED = Tkinter.Entry(self, textvariable=self.strLoginPwd)
        LoginInfoLB = Tkinter.Label(self,textvariable=self.strLoginInfo)
        ACCLB = Tkinter.Label(self,text = 'ACC')
        self.AccountCB = ttk.Combobox(self) 
        LoginButton = Button(self, text="Login", command=self.OnLoginButtonClick)
        LogoutButton = Button(self, text="Logout", command=self.OnLogoutButtonClick)       
        
        # init Layout component
        
        self.grid()
        UIDLB.grid(column=0,row=0)
        PwdLB.grid(column=0,row=1)
        LoginIdED.grid(column=1,row=0)
        LoginPwdED.grid(column=1,row=1)
        ACCLB.grid(column=2,row=0)
        self.AccountCB.grid(column=3,row=0)
        LoginInfoLB.grid(column=3,row=1)
        LoginButton.grid(column=4,row=0)
        LogoutButton.grid(column=4,row=1)
        
        self.resizable(False,False)
    
    def OnLoginButtonClick(self):
        self.strLoginInfo.set("Logining...")
        rtn = self.TradeApp.Login(self.strLoginID.get(), self.strLoginPwd.get())
        print rtn
        rtn = self.TradeApp.GetAccountList()
        print rtn
        self.AccountCB.set(rtn)
        self.strLoginInfo.set("")

    def OnLogoutButtonClick(self):
        self.strLoginInfo.set("Logouting...")
        rtn = self.TradeApp.Logout(self.strLoginID.get())
        print rtn
        self.AccountCB.set("")
        self.strLoginInfo.set(rtn)
if __name__ == "__main__":
    
    app = App(None)
    app.title('TCST API DEMO')
    
    #run main loop
    app.mainloop()
    