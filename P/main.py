from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import random
def edit_image(Studentname, Teachername, Starttime, CloseTime,ApplicationTime,PassTime,StatusBarTime,TimeRemaining,base_image_path, font_path_time, font_path_name,font_path_chinese_bold,EmergencyContacts,Reasonforleave,output_path,destination,Leavingschool):
    # 打开基础图片
    image = Image.open(base_image_path)
    draw = ImageDraw.Draw(image)
    # draw = ImageDraw.Draw(Image.open("img/kefu.png"))

    font_time = ImageFont.truetype(font_path_time, size=40)   #设置粗时间字体
    font_name = ImageFont.truetype(font_path_name, size=38)   #设置名称字体
    font_Chinese_Blod = ImageFont.truetype(font_path_chinese_bold,size=45) #设置剩余时间字体

    draw.text((267, 1183), Starttime, font=font_time, fill="#6c6e72")       #开始时间
    draw.text((267, 1183 + 67), CloseTime, font=font_time, fill="#6c6e72")  #结束时间
    draw.text((160, 2080 - 5), Studentname, font=font_name, fill="#706f7f") #申请学生名称
    draw.text((250 + 30, 2180 +10), Teachername, font=font_name, fill="#706f7f") #审批老师名称
    draw.text((932, 2080 - 5), ApplicationTime, font=font_name, fill="#acacac")    #申请时间
    draw.text((932, 2180 +10), ApplicationTime, font=font_name, fill="#acacac")    #审批时间
    draw.text((81, 45), StatusBarTime, font=ImageFont.truetype(font_path_name, size=42), fill="#706f7f") #状态栏时间
    draw.text((748, 1200 -3), TimeRemaining, font=font_Chinese_Blod, fill="#4e99ff")#剩余时间
    draw.text((315, 1375), EmergencyContacts, font=font_name, fill="#706f7f")       #紧急联系人
    draw.text((277, 1440), Reasonforleave, font=font_name, fill="#706f7f")          #请假原因
    draw.text((277, 1640), destination, font=font_name, fill="#706f7f")             #目的地
    draw.text((795, 808), Leavingschool, font=font_name, fill="#706f7f")            #是否离校
    #审批通过图片处理
    shenpitongguo = Image.open('img/shenpi.png')
    mask = shenpitongguo.convert("RGBA").split()[3]
    if(len(Teachername) == 3):
        x, y = 0, 0
        image.paste(shenpitongguo, (x, y), mask)
    elif(len(Teachername) == 2):
        x,y = -27,0
        image.paste(shenpitongguo, (x, y), mask)

    #客服图片处理
    kefu = Image.open('img/kefu.png')
    mask = kefu.convert("RGBA").split()[3]
    x, y = 0, 0
    image.paste(kefu, (x, y), mask)

    # 保存编辑后的图像
    image.save(output_path)
if __name__ == "__main__":
    # 替换成您的图片路径
    base_image_path = "img/b.png"
    # 替换成您的字体文件路径，确保字体文件存在
    font_path_time = "Fonts/kaglia-kaglia-sans-400.ttf"   #申请时间字体（粗）
    font_path_name = "Fonts/MiSans-Medium.ttf"       #普通字体
    font_path_chinese_bold = "Fonts/msyhbd.ttc" #剩余时间字体
    # 指定输出图片的路径
    output_path = "img/edited_image.png"
    # 要插入到图片中的时间和名称
    Studentname = "赵登亮 - 发起申请" #申请学生名称

    Teachername = "张冰晓"  #导员名称
    Starttime = "04-22 12:00" #请假开始时间
    CloseTime = "04-22 20:00" #请假结束时间

    # 定义时间字符串格式
    time_format = "%m-%d %H:%M"
    # 转换字符串为 datetime 对象
    start_time_obj = datetime.strptime(Starttime, time_format)
    close_time_obj = datetime.strptime(CloseTime, time_format)
    # 计算剩余时间
    remaining_time = close_time_obj - start_time_obj
    # 获取剩余的天数、秒数
    remaining_days = remaining_time.days
    remaining_seconds = remaining_time.seconds
    # 将剩余的秒数转换为小时和分钟
    remaining_hours = remaining_seconds // 3600  # 计算整小时
    remaining_minutes = (remaining_seconds % 3600) // 60  # 计算剩余分钟
    # 将剩余时间转换为字符串（例如："2天 3小时 45分钟"）
    remaining_time_str = f"{remaining_days}天 {remaining_hours}小时 {remaining_minutes}分钟"

    ApplicationTime = "04-22 12:00" #申请时间
    PassTime = "04-22 12:09" #审批时间
    StatusBarTime = "12:10" #截图时状态栏的时间
    TimeRemaining = remaining_time_str #剩余时间
    EmergencyContacts=Reasonforleave=destination = None     #初始化
    if(EmergencyContacts is None):
        #如果电话参数为空，即随机生成一个电话
        random_number = random.randint(1000000000, 9999999999)
        EmergencyContacts = "1"+str(random_number)
    else:
        EmergencyContacts = ""    
    Reasonforleave = None
    
    if(Reasonforleave is None):
        #如果请假原因为空使用默认参数
        Reasonforleave = "出去买衣服"
    else:
        Reasonforleave = ""
    if(destination is None):
        #如果目的地为空使用默认参数
        destination = "河南省/郑州市/金水区"
    else:
        destination =""
    Leavingschool =  True
    if(Leavingschool is True):
        #是否离校
        Leavingschool = "离校"
    else:
        Leavingschool = "否"
    # 调用函数
    edit_image(Studentname,Teachername, Starttime, CloseTime,ApplicationTime,PassTime,StatusBarTime,TimeRemaining, base_image_path, font_path_time, font_path_name,font_path_chinese_bold, EmergencyContacts,Reasonforleave,output_path,destination,Leavingschool)
    print("图片编辑完成，保存路径：", output_path)

