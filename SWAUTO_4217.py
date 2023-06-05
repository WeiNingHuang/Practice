import Common_Libs
import xml.etree.ElementTree as ET
  
def Get_XML_Item_Number(f_path, f_name, x_path):
  file = Common_Libs.Get_File(f_path, f_name)
  tree = ET.parse(file)
  item = tree.findall(x_path)
  number_of_item = len(item)
  return number_of_item
  
  
def Get_XML_Item_Value(f_path, f_name, x_path, attrib):
  values = []
  file = Common_Libs.Get_File(f_path, f_name)
  tree = ET.parse(file)
  items = tree.findall(x_path)
  for item in items:
    values.append(item.attrib[attrib])
      
  return values
  
  
def Get_ICUConfig_Item_Number():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"ICUConfig_eP5.xml"
  x_path = ".//ICUPresetsPerLEMode"
  number_of_item = Get_XML_Item_Number(f_path, f_name, x_path)
  Log.Message(number_of_item)
  
  return number_of_item
  
  
def Get_SystemSpec_Item_Number():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"SystemSpecV2.xml"
  x_path = ".//ToolSpecLevel2[@key='LEMode']"
  number_of_item = Get_XML_Item_Number(f_path, f_name, x_path)
  Log.Message(number_of_item)
  
  return number_of_item
  

def Get_License_Item_Number():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"LicenseV2.xml"
  x_path = ".//ToolLicenseLevel2[@key='LEMode']"
  number_of_item = Get_XML_Item_Number(f_path, f_name, x_path)
  Log.Message(number_of_item)
  
  return number_of_item  
  

def Get_LEModeConfig_Item_Number():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"LEModeConfig_eP5.xml"
  x_path = r".//LEMode"
  number_of_item = Get_XML_Item_Number(f_path, f_name, x_path)
  Log.Message(number_of_item)
  
  return number_of_item
    
  
def Get_LEModeConfig_Name_Value():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"LEModeConfig_eP5.xml"
  x_path = r".//LEMode"
  attrib = 'Name'
  values = Get_XML_Item_Value(f_path, f_name, x_path, attrib)
  
  return values
  
  
def Get_SystemSpec_LEMode_Min_Value():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"SystemSpecV2.xml"
  x_path = r".//ToolSpecLevel3[@key='LE']"
  attrib = "min"
  values = Get_XML_Item_Value(f_path, f_name, x_path, attrib)
  
  return values
  

def Get_SystemSpec_LEMode_Max_Value():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"SystemSpecV2.xml"
  x_path = r".//ToolSpecLevel3[@key='LE']"
  attrib = "max"
  values = Get_XML_Item_Value(f_path, f_name, x_path, attrib)
  
  return values
  

def Get_License_LEMode_Min_Value():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"LicenseV2.xml"
  x_path = r".//ToolLicenseLevel3[@key='LE']"
  attrib = "min"
  values = Get_XML_Item_Value(f_path, f_name, x_path, attrib)
  
  return values
  

def Get_License_LEMode_Max_Value():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"SystemSpecV2.xml"
  x_path = r".//ToolLicenseLevel3[@key='LE']"
  attrib = "max"
  values = Get_XML_Item_Value(f_path, f_name, x_path, attrib)
  
  return values
  
  
def Get_License_LE_Index():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"SystemSpecV2.xml"
  x_path = r".//ToolLicenseLevel2[@key='LEMode']"
  attrib = "value"
  values = Get_XML_Item_Value(f_path, f_name, x_path, attrib)
  
  return values
  
  
def Get_SystemSpec_LE_Index():
  f_path = r"D:\hmi2010\Config\System"
  f_name = r"SystemSpecV2.xml"
  x_path = r".//ToolSpecLevel2[@key='LEMode']"
  attrib = "value"
  values = Get_XML_Item_Value(f_path, f_name, x_path, attrib)
  
  return values
  

def Intersection(lst1, lst2):

  
def Generate_UI_Text_From_XML():
  systemspec_index = Get_SystemSpec_LE_Index()
  license_index = Get_License_LE_Index()
  
  
  

def Get_UI_Text():
  UI_text = []
  eliteGUI = Aliases.EliteGUI
  SysCalibratedConditions = eliteGUI.EliteMainForm.ToolBarDockArea.ToolBar_Mid.zpanel.Optics.SysCalibratedConditions
  SysCalibratedConditions.ClickButton()
  comboBox = Aliases.EliteGUI.ConditionForm.comboBox_LE_Mode_Switch
  for item in comboBox.Items.Item:
    UI_text.append(item.OleValue)
    Log.Message(item.OleValue)

  return UI_text

  
def Get_Expected_UI_Text():
  pass