# <img src="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=69948112,3892466283&fm=26&gp=0.jpg" alt="hnu" style="zoom:15%;" /> HNU 自动打卡 HealthCheck

- 简介 :bulb:

> HealthCheck基于**python**搭建，它每天尝试三次打卡，成功后会**邮箱提醒**你打卡成功; 如果3次尝试还没有成功，它会邮件提醒您手动打卡，并将**错误日志**发送给开发者（yourself）.
>
> HealthCheck分离代码和配置文件，你可以很方便地通过修改配置文件来达到**切换运行**环境的目的。同时你也可以通过向用户列表文件中添加新的打卡用户信息来进行**批量打卡**。同时mapper文件夹下的接口分离主程序，可以随时**测试接口**。
>
> HealthCheck通过ASP定时框架来实现定点打卡，一旦你将HealthCheck部署到服务器，即可解放双手，高效生活。

- **声明** :triangular_flag_on_post:
> **使用此项目完成打卡的同学有义务保证信息的准确性！如若出现身体异常，请务必配合疫情防控工作，完成异常信息上报！**

- **目录结构 :trident:**

>  目录结构

```zsh
.
├── config						
│   └── appConfig.py            # 配置文件
├── data						
│   ├── .img                    # 验证码图片缓存
│   └── user.csv                # 打卡用户信息 
├── main.py                     # 程序入口
├── mapper                      # 方法接口
│   ├── commit.py               # 提交打卡信息表单
│   ├── getImage.py             # 下载保存验证码图片
│   ├── ksdemo.py               # 验证码图像识别
│   ├── login.py                # 登陆
│   ├── readData.py             # 数据读取
│   └── sendEmail.py            # 邮件发送
└── README.md                   # README
```



## Quick Start

>  使用此程序需要简单三步，在开始之前你应该使用**git clone** 或下载 **zip** 包以获取程序

### （1）环境搭建

- 解释器

```zsh
python 3.x
```

- 第三方包：你可以使用pip install `packageName`下载它们

```zsh
$ pip install numpy                 # 这里用于处理numpy数组 
$ pip install apscheduler			# APS定时框架
$ pip install requests				# HTTP for Humans.
$ pip install pandas				# 这里用作数据读取
```

- 代发邮箱开启`POP3/SMTP`服务：

此程序包含邮箱提醒功能，如果你想要使用此功能，请将代发邮箱开启`POP3/SMTP`服务。参考教程：https://jingyan.baidu.com/article/6079ad0eb14aaa28fe86db5a.html，注意开启服务后将会获取一段**授权码**，请保留。

- 注册**快识别**帐号：

由于采用了验证码的验证方式，所以我们要识别验证码图片，最简单的方法是用第三方API。**快识别** 免费提供了这样的服务。我们需要注册快识别的帐号来支持验证码图片识别功能，快识别官网：http://fast.95man.com/（建议不要滥用）



### （2）填写配置文件

配置文件包含程序运行所需要的所有信息，路径为`HealthCheck/config/appConfig.py`，下面是`appConfig`的一个配置样例，你需要根据自己的使用请情况修改以下`×××`的部分：

```python
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
```



### （3）填写打卡用户信息

程序已配置完毕，接下来填写打卡用户信息。你需要修改路径`HealthCheck/data/user.csv` 文件，参考以下实例：

```python
username,passwd,email,RealAddress,RealCity,RealCounty,RealProvince
802180010599,mima123456,3214566@qq.com,密西西比村,岳阳市,岳阳县,湖南省
802180010598,mima654321,1245678@qq.com,八里屯小区,武威市,凉州区,甘肃省
.....继续添加
```

> 注意：username,passwd分别代表Grmh的帐号和密码。



## 运行实例

- 最后，你可以简单的使用命令执行`main.py`

```zsh
$ python main.py
```

- 终端日志

<img src="https://i.loli.net/2021/02/12/KZtjcHnwiTlva9W.png" alt="image-20210212142308263" style="zoom: 51%;" /> 

- 邮箱提醒

<img src="https://i.loli.net/2021/02/12/ClmSj6RqrnO9JeB.png" alt="image-20210212142621554" style="zoom:50%;" /> <img src="https://i.loli.net/2021/02/12/mzMoVOyfSdWlH48.png" alt="image-20210212142659234" style="zoom:50%;" />



## 部署服务器（非必须）

如果将HealthCheck部署到服务器，你就能完全解放双手了，部署方法见：

```python
# 在服务器上克隆项目
git clone git@github.com:LinXiaoDe/HealthCheck.git
# 修改配置文件和用户列表
见quickSatart
# 开启一个screen会话
screen -S HealthCheck
# 进入根目录
cd HealthCheck
# 执行
python main
```
