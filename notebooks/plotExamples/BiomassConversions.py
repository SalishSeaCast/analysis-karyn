import numpy as np
import pandas as pd


def PugetSound1(SoGlength,c1,c2,c3,c4):
    biomass = (c1*SoGlength**c2)*c3*c4
    return biomass

def PugetSound2(SoGlength,c1,c2,c3,c4):
    biomass = 10**(c1*np.log10(SoGlength)-c2)*c3*c4
    return biomass

def PugetSound3(SoGlength,c1,c2,c3,c4):
    biomass = (np.exp(c1*np.log((SoGlength)*c2)-c3))*c4
    return biomass

def PugetSound4(SoGlength,c1,c2,c3,c4):
    biomass = c1*SoGlength+c2
    return biomass

def PugetSound5(SoGlength,c1,c2,c3,c4):
    biomass = (10**(c1*SoGlength + c2))*c3
    return biomass

def PugetSound6(SoGlength,c1,c2,c3,c4):
    biomass = (c1/c2)*SoGlength*c3*c4
    return biomass

def PugetSound7(SoGlength,c1,c2,c3,c4):
    biomass = 10**(c1*(np.log10(SoGlength*c2))-c3)
    return biomass


def BiomassConversion(SoGlength,c1,c2,c3,c4,FunctionName):
    if FunctionName=='PugetSound1':
        Biomass=PugetSound1(SoGlength,c1,c2,c3,c4)
    elif FunctionName=='PugetSound2':
        Biomass=PugetSound2(SoGlength,c1,c2,c3,c4)
    elif FunctionName=='PugetSound3':
        Biomass=PugetSound3(SoGlength,c1,c2,c3,c4)
    elif FunctionName=='PugetSound4':
        Biomass=PugetSound4(SoGlength,c1,c2,c3,c4)
    elif FunctionName=='PugetSound5':
        Biomass=PugetSound5(SoGlength,c1,c2,c3,c4)
    elif FunctionName=='PugetSound6':
        Biomass=PugetSound6(SoGlength,c1,c2,c3,c4)
    elif FunctionName=='PugetSound7':
        Biomass=PugetSound7(SoGlength,c1,c2,c3,c4)
   
    else:
        raise Exception(f'Function Name unknown: {FunctionName}')
    Biomass=Biomass/1000 #to convert from ug to mg C
    return Biomass

def LoadConversions(filename='/ocean/ksuchy/MOAD/observe/SoGNewBiomassConversions.xlsx'):
    df=pd.read_excel(filename,engine='openpyxl')
    df.dropna(how='all',inplace=True)


    df['BiomassPerIndividual']=np.nan
    for i,row in df.iterrows():
        biomass=BiomassConversion(row['SoGLength'],row['c1'],row['c2'],row['c3'],row['c4'],row['Function Name'])
        df.at[i,'BiomassPerIndividual']=biomass
    
    return df