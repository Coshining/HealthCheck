# URL
tokenURL = "https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode"
imageURL = "https://fangkong.hnu.edu.cn/imagevcode"
loginUrl = 'https://fangkong.hnu.edu.cn/api/v1/account/login'
commitUrl= 'https://fangkong.hnu.edu.cn/api/v1/clockinlog/add' 

# path
dirPath  = './data/.img/'
dataPath = './data/user.csv'

# 邮箱配置
senderEmail = '×××'		# 代发邮箱（使用此邮箱给打卡用户发送邮件）
sender = "×××"			# 代发邮箱昵称，任意
devEmail = '×××'		# 开发者邮箱（如出现打卡失败的情况，代发邮箱给此邮箱发送打卡失败用户列表）
AuthCode = '×××'		# 开启`POP3/SMTP`服务时的授权码

sucessMsg = '   今日打卡成功，打卡时间：'
failMsg = '     我们对您的账户进行了3次打卡尝试，由于某些原因导致打卡失败，请于今日手动完成打卡。\
您可以尝试联系此邮箱以解决打卡失败的问题。祝您生活愉快！\n发件人： '+senderEmail

# http://fast.95man.com/注册使用
k95Username = '×××'		# 快识别帐号
k95Passwd = "×××"		# 快识别密码

# 打卡时间设置 0:20
checkHour = '0'			# 时间设置 任意
checkMin  = '20'