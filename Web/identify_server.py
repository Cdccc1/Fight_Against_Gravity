import Web.Modules.safeserver as safeserver
import Web.Modules.database_operate as database_operate
import Web.Modules.send_email as send_email
import time

email_sent = {}
user_list = []  # {"username" : address}


def reg_server(ip: str, port: int, heart_time: int = -1, debug: bool = False) -> None:
    """注册服务器
    :参数: ip: 服务器ip， port: 端口， heart_time: 心跳时间（默认-1）
    :返回: 无返回
    """
    server = safeserver.SocketSever(ip, port, heart_time, debug)
    server.start()
    while True:
        messages = server.get_message()
        for message in messages:
            print(f"[Msg In]{time.ctime()} : {message}")
            addr = message[0]  # addr : client's address
            rmessage = message[1]
            user_list.append({rmessage["user"]: message[0]})
            all_reg_acc = database_operate.get_all_reg_acc()
            if rmessage["opt"] != 3:
                username, email = rmessage["user"], rmessage["email"]
                if username in all_reg_acc.keys():
                    server.send(addr, "DUPLICATE")
                else:
                    if rmessage["opt"] == 1:
                        email_sent[(username, email)] = True
                        id_code = send_email.generate_id_code()
                        send_email.send_email(username, email, id_code)
                        server.send(addr, id_code)
                    elif rmessage["opt"] == 2:
                        if (username, email) in email_sent:
                            password = rmessage["password"]
                            time_n = time.ctime()
                            database_operate.insert_acc_data([username, password, time_n, email])
                            email_sent.pop((username, email))
                        else:
                            server.send(addr, "ERROR")
                        server.close(addr)
                    else:
                        print("unexpected opt")
            else:
                username = rmessage["user"]
                password = rmessage["password"]
                if username in all_reg_acc:
                    if password == all_reg_acc[username][0]:
                        database_operate.insert_login_data([username, time.ctime()])
                    else:
                        server.send(addr, "ERROR")
                else:
                    server.send(addr, "ERROR")
                server.close(addr)


if __name__ == "__main__":
    ip = ""
    port = 25555
    while True:
        try:
            reg_server(ip, port, debug=True)
        except Exception as e:
            print(f"[Error] {e}")
