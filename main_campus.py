import numpy as np
from mapper.getImage import getToken,getPic
from mapper.ksdemo import KSClient
from mapper.login import login
from mapper.sendEmail import sendEmail
from mapper.readData import readData_campus
from mapper.commit import commit_campus
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from config.appConfig import *

# 打卡
def check(username,passwd,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp):
    imageName = username+".jpeg"
    # 获取&下载图片
    token = getToken(tokenURL)
    print("获取token:",token)
    if(token != "error"):
        url = imageURL + "?token=" + token
        getPic(url,dirPath,imageName)
    # 获取验证码
    Ks95man = KSClient()	
    verCode = ""
    if Ks95man.GetTaken(k95Username,k95Passwd):   								
        verCode = Ks95man.PostPic(dirPath+imageName,2)
        print('识别结果：'+verCode)
    # 登陆
    response,cookie= login(loginUrl,username,passwd,token,verCode)
    if response['code'] != 0:   # 登陆失败
        return -1
    print("登陆成功")
    # 提交信息
    response = commit_campus(commitUrl,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp,cookie)
    print(response)
    return response['code']

# 循环打卡作业
def check_Job():
    cur = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    print("----------[log] : "+cur)
    # 读取用户信息
    users = readData_campus(dataPathCampus)
    # 最多进行3次打卡尝试 / day
    for t in range(3):
        # 保存打卡成功的用户下标 用于用户列表信息清除
        sucessList = []
        # 遍历用户列表
        for i in range(1,len(users)):
            username,passwd,email,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp = users[i]
            try:
                res = check(username,passwd,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp)
            except:
                res = -1
            cur = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            # 打卡成功
            if(res == 0):
                sucessList.append(i)
                sendEmail(senderEmail,email,AuthCode,sender,username,
                "打卡成功提醒","Hi "+username+" :\n"+sucessMsg+cur+"，祝您生活愉快！\n发件人： "+senderEmail)
            # 重复打卡
            elif(res == 1):
                sucessList.append(i)
        # 清理用户列表
        users = np.delete(users,sucessList,0)

    # 未成功打卡的用户发送邮箱提醒手动打卡
    unCheck = ""
    for i in range(1,len(users)):
        username,passwd,email,RealAddress,RealCity,RealCounty,RealProvince,BackState,MorningTemp,NightTemp = users[i]
        cur = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        print("错误",i)
        sendEmail(senderEmail,email,AuthCode,
        sender,username,"打卡失败提醒","Hi "+username+" ：\n"+failMsg)
        unCheck +=(username + '\n')
    
    # 开发者邮件
    if unCheck!="":    
        sendEmail(senderEmail,devEmail,AuthCode,sender,'Developer',
        "打卡失败提醒(dev)","打卡出现问题，下列用户未打卡"+unCheck)
    
if __name__ == '__main__':
    定点任务
    sched = BlockingScheduler()
    sched.add_job(check_Job,'cron',hour=checkHour,minute=checkMin)
    sched.start()