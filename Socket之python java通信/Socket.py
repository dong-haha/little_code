# -*- coding: UTF-8 -*-
# 作者：东
# 时间：2021.11.29
# 服务端代码
import cv2
import plantid
import json
import socket



plant_identifier = plantid.PlantIdentifier()
# 注意，经测试，使用localhost时，socket仅能在本机进程通信，使用内网ip能远程访问。
#address = ('localhost', 19999) 
address = ('10.0.4.3', 19999)


# 创建socket对象，同时设置通信模式，AF_INET代表IPv4，SOCK_STREAM代表流式socket，使用的是tcp协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定到我们刚刚设置的ip和端口元组，代表我们的服务运行在本机的19999端口上
server.bind(address)
# 开始监听，5位最大挂起的连接数
server.listen(5)

# 无限循环，实现反复接收请求
while True:
    try:
        client, addr = server.accept()
        data = client.recv(1024)
        image_filename=str(data,encoding='utf-8')
        image = cv2.imread(image_filename.strip()) # 每次recv后面带了\n
        outputs = plant_identifier.identify(image, topk=5)
        if outputs['status'] == 0:
            result=json.dumps(outputs,ensure_ascii=False)
            client.sendall(bytes(result,encoding='utf8')) # 发送消息给客户端，发送的消息必须是byte类型
        client.close()        # 关闭连接
    except:
        print("出错")
        client.close()
server.close()




