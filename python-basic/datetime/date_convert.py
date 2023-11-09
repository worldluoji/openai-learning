import datetime  
  
date_string = "2023-07-07"  
  
date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")  
  
print("字符串转转化为date:", date_object)


d = date_object + datetime.timedelta(days=5)   
  
date_string = d.strftime("%Y-%m-%d")  
  
print("date转化为字符串", date_string)