## 传入日志文件
def getNum(fileName):
    ##定义一个计数器
    sumNum = 0
    with open(fileName)as file:
        for info in file:
            ## listInfo 的值其中一个为  ['47.29.201.179', '-', '-', '[28/Feb/2019:13:17:10', '+0000]', '"GET', '/?p=1', 'HTTP/2.0"', '200', '5316', '"https://domain1.com/?p=1"', '"Mozilla/5.0', '(Windows', 'NT', '6.1)', 'AppleWebKit/537.36', '(KHTML,', 'like', 'Gecko)', 'Chrome/72.0.3626.119', 'Safari/537.36"', '"2.75"']
            listInfo=info.replace("\n","").replace("\t"," ").split(" ")
            for value in listInfo:
                if  "domain1.com" in value:
                    sumNum+=1
                    break
    return sumNum

print(getNum("1.txt"))

##传入一个时间  形如 28/Feb/2019
def getRatio(curData,fileName):
    ##当前时间全部的记录
    curDataAll=0
    ##当前时间成功的记录
    curDataSuccess=0
    with open(fileName)as file:
        for info in file:
            listInfo=info.replace("\n","").replace("\t"," ").split(" ")
            ##这里默认为所有日志中的格式均与第一行类似 则分割后的列表索引3表示日期 索引8表示状态码
            if curData in listInfo[3]:
                curDataAll+=1
            if listInfo[8]=="200":
                curDataSuccess+=1

    return curDataSuccess/curDataAll

print(getRatio("28/Feb/2019","1.txt"))








