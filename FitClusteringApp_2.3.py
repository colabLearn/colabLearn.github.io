
# coding: utf-8

# In[1]:


import os
from os import path
import tkinter as tk
from tkinter import filedialog
from xlrd import open_workbook, XLRDError
from tkinter import *
import operator
from scipy import stats
import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter import filedialog
import copy
import xlwt 
from xlwt import Workbook


# In[2]:


if getattr(sys, 'frozen', False) :
    # running in a bundle
    chromedriver_path = os.path.join(sys._MEIPASS, 'chromedriver')


# In[3]:


class MyWindow:
    def __init__(self, window):
        self.Intro2 = Label(window, text="APPLICATION OF CUSTOMER PAIR-WISE MATRIX-BASED ALGORITHM FOR MASS CUSTOMIZATION OF GARMENTS").place(x = 30,y =50) 
        self.Intro3 = Label(window, text="Clustering Model by: Opaleye, Adepeju Abimbola, Adekunle Kolawole, and Oliver Ekepre Charles-owaba.").place(x = 30,y =80) 
        self.Intro4 = Label(window, text="Programmer: Adetunji Adeniran Copyright@2020 | Contact: tunji4physics@gmail.com").place(x = 30,y =110) 
        self.Intro4 = Label(window, text="fitClusterApp Version: 2.3").place(x = 225,y =140) 
        self.Intro5 = Label(window, text="======================================================================================================================").place(x = 30,y =170) 
        self.Intro6 = Label(window, text="\n")
        #self.title('fitClusterAlgo GUI')
        
        self.sbmitbtn = Button(window, text = "Please click to browse for measurement data", command=browsefunc)
        self.sbmitbtn.place(x = 250, y = 200)
        self.text1 = tk.StringVar()
        self.text1.set("")
        self.myLabel = Label(window, textvariable=self.text1, fg="blue", font='Helvetica 10 bold')
        self.myLabel.place(x=30, y=230)
        
        self.tolLabel=Label(window, text='Enter tolerance for data dimensions: ')
        self.tol = StringVar()
        self.cusDataEntry1 = Entry(window, textvariable=self.tol)
        self.tolLabel.place(x = 30, y = 290)
        self.cusDataEntry1.place(x = 250, y = 290, width=150, height=25) 
        self.sbmitbtn1 = Button(window, text = "Enter tolerance list", command=browsefunc1)
        self.sbmitbtn1.place(x = 410, y = 290)
        self.cusDataEntry1["state"] = DISABLED
        self.sbmitbtn1["state"] = DISABLED
        
               
        self.text2 = tk.StringVar()
        self.text2.set("")
        self.tolOutLabel = Label(window, textvariable=self.text2, fg="blue", font='Helvetica 10 bold')
        self.tolOutLabel.place(x=30, y=320)
        
        
        self.numCl=Label(window, text='Enter number of cluster: ')
        self.numC = StringVar()
        self.cusDataEntry2 = Entry(window, textvariable=self.numC)
        self.numCl.place(x = 30, y = 350)
        self.cusDataEntry2.place(x = 210, y = 350, width=50, height=25) 
        self.sbmitbtn2 = Button(window, text = "Enter number of cluster", command=ClusterNum)
        self.sbmitbtn2.place(x = 270, y = 350)
        
        self.cusDataEntry2["state"] = DISABLED
        self.sbmitbtn2["state"] = DISABLED
        
        self.text3 = tk.StringVar()
        self.text3.set("")
        self.numOfCluster = Label(window, textvariable=self.text3, fg="blue", font='Helvetica 10 bold')
        self.numOfCluster.place(x=30, y=380)
        
        self.extractData = Button(window, text = "Click to extract data", command=extractDataDictAndKeys)
        self.extractData.place(x = 200, y = 410)
        self.dataExt = tk.StringVar()
        self.dataExt.set("")
        self.myLabelExt = Label(window, textvariable=self.dataExt, fg="blue", font='Helvetica 10 bold')
        self.myLabelExt.place(x=30, y=440)
        self.extractData["state"] = DISABLED
        
        
        self.runCluster = Button(window, text = "Click to run clustering", command=runRecursive)
        self.runCluster.place(x = 200, y = 470)
        self.textRun = tk.StringVar()
        self.textRun.set("")
        self.myLabelRun = Label(window, textvariable=self.textRun, fg="blue", font='Helvetica 10 bold')
        self.myLabelRun.place(x=30, y=500)
        self.runCluster["state"]=DISABLED
        
        
        self.output = Button(window, text = "Select folder to store cluster output", command=getFolder)
        self.output.place(x = 250, y = 530)
        self.out = tk.StringVar()
        self.out.set("")
        self.myLabel = Label(window, textvariable=self.out, fg="blue", font='Helvetica 10 bold')
        self.myLabel.place(x=30, y=560)
        self.output["state"]=DISABLED
        
        self.fEntryLabel=Label(window, text='Enter valid excel filename with .xls extension: ')
        self.fText = StringVar()
        self.fText.set("")
        self.fEnteryBox = Entry(window, textvariable=self.fText)
        self.fEntryLabel.place(x = 30, y = 590)
        self.fEnteryBox.place(x = 280, y = 590, width=150, height=25) 
        self.fEnteryButton = Button(window, text = "Enter name", command=getOutputFilename)
        self.fEnteryButton.place(x = 440, y = 590)
        self.fEnteryBox["state"] = DISABLED
        self.fEnteryButton["state"] = DISABLED
        
        
        self.outButton = Button(window, text = "Save cluster output to file", command=getOutputToExcel)
        self.outButton.place(x = 210, y = 620)
        self.outButton["state"] = DISABLED
        
        self.outSave = StringVar()
        self.outSave.set("")
        self.outSaveLabel = Label(window, textvariable=self.outSave, fg="blue", font='Helvetica 10 bold')
        self.outSaveLabel.place(x=30, y=650)
        
        
        self.refresh = Button(window, text = "Run more clustering", command=self.refresh)
        self.refresh.place(x = 30, y = 680)
        self.refresh["state"] = DISABLED
        
        self.end = Button(window, text = "End program", command=end)
        self.end.place(x = 250, y = 680)
        self.end["state"] = DISABLED
        
    def refresh(self):
    
        self.text1.set("")
        self.tol.set("")
        self.cusDataEntry1["state"] = DISABLED
        self.cusDataEntry1.delete(0, END)
        self.sbmitbtn1["state"] = DISABLED
        self.text2.set("")
        self.numC.set("")
        self.dataExt.set("")
        self.text3.set("")
        self.extractData["state"] = DISABLED
        self.textRun.set("")
        self.runCluster["state"]=DISABLED
        self.out.set("")
        self.output["state"]=DISABLED
        self.fText.set("")
        self.fEnteryBox["state"] = DISABLED
        self.fEnteryButton["state"] = DISABLED
        self.fEnteryBox.delete(0,END)
        self.outButton["state"] = DISABLED
        self.outSave.set("")
        self.refresh["state"] = DISABLED
        self.end["state"] = DISABLED
        self.sbmitbtn["state"] = "normal"
        global cusData
        global custDict
        global start
        cusData =pd.DataFrame()
        custDict =None
        start = 1

        
    
   


# In[4]:


def test_book(filename):
        try:
            open_workbook(filename)
        except XLRDError:
            return False
        else:
            return True           


# In[5]:


def getCustomerDataFilePath(in_customerDataFilePath):
    #global cusData
    Data = pd.read_excel(in_customerDataFilePath)
    return Data


# In[6]:


def browsefunc():
    #global dataFile
    dataFile=filedialog.askopenfilename(initialdir = "/", title = "Select file")
    global cusData
    if (test_book(dataFile)):
        cusData=getCustomerDataFilePath(dataFile)
        mywin.text1.set("Input data path: "+ dataFile)
        mywin.myLabel.config(fg="blue")
            
        
        mywin.sbmitbtn["state"] = DISABLED
        mywin.cusDataEntry1["state"] = "normal"
        mywin.sbmitbtn1["state"] = "normal"
        #self.cusDataEntry1["state"] = "normal"
        #self.sbmitbtn1["state"] = "normal"
            
    else:
        mywin.text1.set(dataFile+ " is not a valide excel file")
        mywin.myLabel.config(fg="red")
        


# In[7]:


def toleranceToFloat(toleranceDimList):
        toleranceDimList=toleranceDimList.replace(" ", "")
        tol2 = toleranceDimList.split(",")
        #tollist=[float(x) for x in toleranceDimList]
        tolFloat=[]
        for val in tol2:
            tVal = float(val)
            tolFloat.append(tVal)
        
        return tolFloat


# In[8]:


def checkFloat(lst):
    result=True
    for x in lst:
        try:
            float(x)
        except ValueError:
            result =  False
            break
    
    return result


# In[9]:


def checkInt(myVal):
    result =  True
    try:
        int(myVal)
    except ValueError:
        result =  False
    
    return result  


# In[10]:


def browsefunc1():
    global cusData
    global toleranceList
    dataL = len(cusData.columns)
    temp = mywin.tol.get()
    temp=temp.replace(" ", "")
    tol2 = temp.split(",")
    if(checkFloat(tol2)!=True):
        messagebox.showerror("Input error", "Tolerance list must be numeric values seperate by commas \n e.g. 3,2,5.8. Please check and re-enter.")
        
        return
    tempList = toleranceToFloat(temp)
    if (len(tempList)==dataL):
        for x in tempList:
            toleranceList.append(x)
            mywin.text2.set("Tolenrace values/dimension : "+ temp)
            mywin.tolOutLabel.config(fg="blue")
            mywin.cusDataEntry1["state"] = DISABLED
            mywin.sbmitbtn1["state"] = DISABLED
            mywin.cusDataEntry2["state"] = "normal"
            mywin.sbmitbtn2["state"] = "normal"
    else:
        messagebox.showerror("Input error", "Number of tolerance value in list: " + str(len(tempList)) + " is not equal to data dimension: "+ str(dataL) + "\n Please insert correct tolenrace list.")
           
        return


# In[11]:


def ClusterNum(): 
    global numOfCluster
    temp = mywin.numC.get()
    if(checkInt(temp)!=True):
        messagebox.showerror("Input error", "Number of cluster must be integer.")
            
        return
    numOfCluster= int(temp)
    mywin.text3.set("Number of clusters : "+ temp)
    mywin.cusDataEntry2["state"] = DISABLED
    mywin.sbmitbtn2["state"] = DISABLED
    mywin.extractData["state"] = "normal"


# In[12]:


def extractDataDictAndKeys():
    #global dataFile
   
    #global numOfCluster
    global custDict
    global custDict2
    #getCustomerDataFilePath(dataFile)
    global cusData 
    #numberOfCustormer = len(cusData.column)
    numberOfCustormer = len(cusData)
    customerDataKey = []
    custDict = {}
    for a in range (0, numberOfCustormer):
        custDict[a] = []
    custormerDataList = cusData.values.tolist()
    customerDataKey = custDict.keys() 
    for i in customerDataKey:
        custDict[i]=custormerDataList[i]
    #l=len(custDict)
    
    custDict2= copy.deepcopy(custDict)
    #l = len(custDict2)
    #m = len(custDict)
    mywin.dataExt.set("Data extracted successfully ")
    mywin.extractData["state"]=DISABLED
    mywin.runCluster["state"]="normal"
    
    #return custDict, customerDataKey


# In[13]:


def compare_Xij_Xkj(xi, xk, in_tolerance):
    outpList=[]
    for xij, xkj, t in zip(xi, xk, in_tolerance):
        temp = abs(xij - xkj)
        if(temp<=t):
            outpList.append(1)
        else:
            outpList.append(0)
    return outpList


# In[14]:


def compute_wikj(in_inputData_Dict, in_tolerance):
    wikj_Dict ={}
    
    for key1, value1 in in_inputData_Dict.items():
        xij_xik={}
        for key2, value2 in in_inputData_Dict.items():
            temp = compare_Xij_Xkj(value1, value2, in_tolerance)
            xij_xik[key2]=temp
    
        wikj_Dict[key1]= xij_xik
    
    return wikj_Dict


# In[15]:


def compute_matrixTbymatrix(m1):
    sumN=0
    for e1 in m1:
        sumN+=e1*e1
    
    return sumN


# In[16]:


def compute_ir_Dict(in_B_ik):
    rik_All={}
    for key1, value1 in in_B_ik.items():
        rik={}
        for key2, value2 in value1.items():
            num = compute_matrixTbymatrix(value2)
            deNum=compute_matrixTbymatrix(value1[key1])
            rik_temp = float(float(num)/float(deNum))
            rik[key2]=rik_temp
        rik_All[key1]=rik
    return rik_All


# In[17]:


def computer_Ri_ForAll_i(in_r_ik_ForAll_i):
    R_i_Dic={}
    for key1, value1 in in_r_ik_ForAll_i.items():
    
        R_i_sum=0
        for key2, value2 in value1.items():
       
            if(key1!=key2):
                R_i_sum+=value1[key2]
        
        R_i_Dic[key1]=round(R_i_sum,3)
    
    return R_i_Dic  


# In[18]:


def compute_Ri_ideal(Dict):
    List=[]
    maxList=[]
    List=Dict.values()
    
    getMax=max(List)
    for key, value in Dict.items():
    #for j in range(len(Dict)):
        if(value==getMax):
            maxList.append(key) 
            break
    return maxList


# In[19]:


def returnCluster(in_rik_dict, in_R_i_Ideal):
    k_Dict={ }

    clusterList = []
    clusterList.append(in_R_i_Ideal[0])
    for key, value in in_rik_dict[in_R_i_Ideal[0]].items():
        if(key!=in_R_i_Ideal[0]):
            k_Dict[key]=value

    k_val_List=k_Dict.values()        

    maxRel = max(k_val_List)

    for key, value in k_Dict.items():
        if(value==maxRel):
            clusterList.append(key)
        
    return clusterList


# In[20]:


def cluster_ri_rel(in_rik_dict, in_cluster):
    cluster_Rel_Dict={}
    for key, value in in_rik_dict.items():
        r_i_rel = {}
        if(key in in_cluster):
            for key2, value2 in value.items():
                if(key2 in in_cluster):
                    r_i_rel[key2]=value2
            cluster_Rel_Dict[key]=r_i_rel       

    return cluster_Rel_Dict


# In[21]:


def getPercentageFit(in_ri_rel_cluster):
    sumNList=[]
    for key, value in in_ri_rel_cluster.items():
        temp = value.values()
        tempSum= round(sum(temp),2)
        sumNList.append(tempSum)
    netSum = sum(sumNList)

    l=len(sumNList)
    netSum = netSum-l
    perFit = 100*((netSum)/(l*(l-1)))

    return round(perFit,2)


# In[22]:


def getAggLoss(in_cluster, in_custDict, in_R_i_Ideal):
    netSumN = []
    for value in in_cluster:
        sumN = 0
        for v1, v2 in zip (in_custDict[in_R_i_Ideal[0]], in_custDict[value]):
            sumN+= (v1-v2)**2
    
        sumN =sumN**0.5
        netSumN.append(sumN)

    
    result =  (sum(netSumN))/len(netSumN)
    
    return round(result,3)


# In[23]:


def recordData(in_cluster,in_percentageFit,in_aggLoss):
    records=["ClusterKey", "DegreeFit", "AggLoss"]
    clusterDict = {}
    for a in records:
        clusterDict[a] = []

    clusterDict["ClusterKey"]=in_cluster
    clusterDict["DegreeFit"]=in_percentageFit
    clusterDict["AggLoss"]= in_aggLoss
    
    return clusterDict


# In[24]:


#def resetData(in_cluster, in_custDict):
 #   newDict = {}
  #  for key, value in in_custDict.items():
   #     if (key not in in_cluster):
            
    #        newDict[key]=value
            
            
    #return newDict 
def resetData(in_cluster, in_custDict):
    #global custDict
    
    for v in in_cluster:
        del in_custDict[v]
        


# In[25]:


def tryRun(in_toleranceList, in_custDict):
   
    result = {}
    #global custDict  
    Bik_dict = compute_wikj(in_custDict, in_toleranceList)
    rik_dict = compute_ir_Dict(Bik_dict)
    R_i_ForAll_i = computer_Ri_ForAll_i(rik_dict)
    R_i_Ideal = compute_Ri_ideal(R_i_ForAll_i)
    cluster = returnCluster(rik_dict, R_i_Ideal)
    ri_rel_cluster = cluster_ri_rel(rik_dict, cluster)
    percentageFit = getPercentageFit(ri_rel_cluster) 
    aggLoss = getAggLoss(cluster, in_custDict, R_i_Ideal)
    
    
    result = recordData(cluster,percentageFit,aggLoss)
    
    resetData(cluster, in_custDict)
    
   
    return result 
   


# In[26]:


def getLastCluster (in_R_i_ForAll_i):
    listLastCluster=[]
    for key, value in in_R_i_ForAll_i.items():
        listLastCluster.append(key)

    return listLastCluster


# In[27]:


def LastRun(in_toleranceList, in_custDict):
    result = {}
    #global custDict 
    Bik_dict = compute_wikj(in_custDict, in_toleranceList)
    rik_dict = compute_ir_Dict(Bik_dict)
    R_i_ForAll_i = computer_Ri_ForAll_i(rik_dict)
    R_i_Ideal = compute_Ri_ideal(R_i_ForAll_i)
    cluster = getLastCluster (R_i_ForAll_i)
    ri_rel_cluster = cluster_ri_rel(rik_dict, cluster)
    percentageFit = getPercentageFit(ri_rel_cluster)   
    aggLoss = getAggLoss(cluster, in_custDict, R_i_Ideal)
    
    result = recordData(cluster,percentageFit,aggLoss)
    
    
    return result


# In[28]:


def runRecursive():
    global custDict
    global toleranceList
    global numOfCluster
    global start
    global gResult
    
    
    if (start==numOfCluster):
        resultNow=LastRun(toleranceList,custDict)
        gResult[start]=resultNow
        
    else:
        resultNow = tryRun(toleranceList,custDict)
        gResult[start]=resultNow 
        start+=1
        runRecursive()
    
    mywin.textRun.set("Clustering successfull :)")
    #mywin.textRun.set(str(i)+ " "+str(j)+" "+ str(k)+" "+str(l))
    mywin.runCluster["state"]=DISABLED
    #return in_result
    mywin.output["state"]="normal"
    


# In[29]:


def getFolder():
    global outputFilename
    
    outputFilename = filedialog.askdirectory()
    
    
    mywin.out.set(outputFilename)
    mywin.output["state"]= DISABLED
    mywin.fEnteryBox["state"] = "normal"
    mywin.fEnteryButton["state"] = "normal"
    


# In[30]:


def getOutputFilename():
    temp = mywin.fText.get()
    global outputFilename
    
    filepaths = [temp]

    for fp in filepaths:
    
        ext = os.path.splitext(fp)[-1].lower()
        
        if ext != ".xls":
            messagebox.showerror("Input error", "Filename not ending with .xls. Please enter valide excel filename.")
            
            return
        else:
            outputFilename = outputFilename+ "/"+temp   
            mywin.out.set(outputFilename)
            mywin.fEnteryBox["state"] = DISABLED
            mywin.fEnteryButton["state"] = DISABLED
            mywin.outButton["state"] = "normal"


# In[31]:


def setResult():
    global gResult
    global custDict2

    global ClusterDict
    global keyDict
    global AggLossDict
    global DegreeFitDict
    for key, value in gResult.items():
        clusterList=[]
        
        for key2, value2 in value.items():
            if (key2=="ClusterKey"):
                keyDict[key] = value2
                for i in value2:
                    clusterList.append(custDict2[i])
                    keyDict
                    
    
            if (key2=="DegreeFit"):
                DegreeFitDict[key] = value2
            if (key2=="AggLoss"):
                AggLossDict[key]=value2
            
        ClusterDict[key]=clusterList
        


# In[32]:


def setSheet(sheet, in_dimLabel):
    for i in range(len(in_dimLabel)):
        sheet.write(0, i+1, in_dimLabel[i]) 
     
    sheet.write(0, len(in_dimLabel)+3, 'DegreeFit')
    sheet.write(0, len(in_dimLabel)+4, 'AggLoss')


# In[33]:


def getOutputToExcel():
    setResult()
    global ClusterDict
    OutputLabel=list(cusData)
    OutputLabel.insert(0,"DataKey")
    global outputFilename
    global keyDict
    wb = Workbook() 
    for key, value in ClusterDict.items():
        outputSheet = wb.add_sheet("sheet"+str(key))
        setSheet(outputSheet, OutputLabel)
        for j in range(len(value)):
            outputSheet.write(j+1, 0, j+1)
            outputSheet.write(j+1, 1, keyDict[key][j])
            for i in range(len(value[j])):
            #print j, "sheet"+str(key), value[j][i]
                outputSheet.write(j+1, i+2, value[j][i])
        outputSheet.write(1, len(OutputLabel)+3, DegreeFitDict[key])
        outputSheet.write(1, len(OutputLabel)+4, AggLossDict[key])
                

    wb.save(outputFilename)
    mywin.outSave.set("Cluster output successfully saved to file")
    mywin.outButton["state"] = DISABLED
    mywin.refresh["state"] = "normal"
    mywin.end["state"] = "normal"
    


# In[34]:


cusData =pd.DataFrame()
custDict =None
start = 1
gResult={}
toleranceList=[]
numOfCluster=None
#dataFile = None
outputFilename=None
custDict2 =None 
ClusterDict={}
AggLossDict={}
DegreeFitDict={}
keyDict = {}


# In[36]:


def end( ):
   global win
   win.destroy()


# In[37]:


if __name__ == "__main__":
    win=Tk()
    mywin=MyWindow(win)
    win.title('fitClusterAlgo GUI')
    win.geometry("700x750")
    win.mainloop()

