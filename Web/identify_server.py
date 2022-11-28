import Web.Modules.safeserver as safeserver
import Web.Modules.database_operate as database_operate
import Web.Modules.send_email as send_email
import time

email_sent = {}
user_list = []  # {"username" : address}


class IdentifyServer:
    def __init__(self, ip: str, port: int, heart_time: int = -1, debug: bool = False):
        """注册服务器初始化
        :参数: ip: 服务器ip， port: 端口， heart_time: 心跳时间（默认-1），debug: 调试模式
        :返回: 无返回
        """
        self.server = safeserver.SocketSever(ip, port, heart_time, debug)
        self.all_reg_acc = database_operate.get_all_reg_acc() # 服务器对象内置所有账户的字典
        self.server.start()

    def opt1(self, username: str, email: str, addr: tuple):
        """发送验证码操作
        :参数: username：用户名，email：邮箱，addr：地址元组
        :返回: 无返回
        """
        email_sent[(username, email)] = True
        id_code = send_email.generate_id_code()
        send_email.send_email(username, email, id_code)
        self.server.send(addr, id_code)

    def opt2(self, username: str, email: str, rmessage: dict, addr: tuple):
        """接受并写入数据库操作
        :参数: username：用户名，email：邮箱，rmessage：传入的各种信息字典，addr：地址元组
        :返回: 无返回
        """
        if (username, email) in email_sent:
            password = rmessage["password"]
            time_n = time.ctime()
            database_operate.insert_acc_data([username, password, time_n, email])
            email_sent.pop((username, email))
        else:
            self.server.send(addr, "ERROR")
        self.server.close(addr)

    def opt3(self, rmessage: dict, addr: tuple):
        """登录时的服务器操作
        :参数: rmessage：传入的各种信息元组，addr：地址元组
        :返回: 无返回
        """
        username = rmessage["user"]
        password = rmessage["password"]
        self.all_reg_acc = database_operate.get_all_reg_acc() # 每次调用前完成一次获取操作
        if username in self.all_reg_acc:
            if password == self.all_reg_acc[username][0]:
                database_operate.insert_login_data([username, time.ctime()])
            else:
                self.server.send(addr, "ERROR")
        else:
            self.server.send(addr, "ERROR")
        self.server.close(addr)

    def start(self):
        while True:
            messages = self.server.get_message()
            for message in messages:
                print(f"[Msg In]{time.ctime()} : {message}")
                addr = message[0]  # addr : client's address
                rmessage = message[1]
                user_list.append({rmessage["user"]: message[0]})
                all_reg_acc = database_operate.get_all_reg_acc()
                if rmessage["opt"] != 3:
                    username, email = rmessage["user"], rmessage["email"]
                    if database_operate.check_duplicate(username):
                        self.server.send(addr, "DUPLICATE")
                    else:
                        if rmessage["opt"] == 1:
                            self.opt1(username, email, addr)
                        elif rmessage["opt"] == 2:
                            self.opt2(username, email, rmessage, addr)
                        else:
                            print("[Error] unexpected opt")
                else:
                    self.opt3(rmessage, addr)


if __name__ == "__main__":
    ip = ""
    port = 25555
    debug = True
    server = IdentifyServer(ip, port, debug=debug)
    while True:
        try:
            server.start()
        except Exception as e:
            print(f"[Error] {time.ctime()} : {e}")