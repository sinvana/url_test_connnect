import requests

def get_url(file_name):
    with open(file_name,"r")as f:
        s = f.readlines()
        lt = [i.strip() for i in s]
    return lt

def process_data(lt):
    p_lt = []
    num = 0
    for i in lt:
        num += 1
        print("正在测试第{}个url".format(num))
        try:
            r = requests.get(i,timeout = 3) #可自行更改timeout,默认为3s
            if r.status_code == 200:
                p_lt.append(i)
                print("{}可成功访问".format(i))
            else:
                print("{}不能成功访问,响应码为{}".format(i,r.status_code))
        except:
            print("访问超时")
    return p_lt

def output_data(data,save_name):
    with open(save_name,"a") as f:
        for i in data:
            f.write(i+"\n")
    print("可成功访问的url已保存在{}文件中.".format(save_name))

if __name__ == "__main__":
    url = get_url("url_in.txt")
    p_data = process_data(url)
    output_data(p_data,"url_out.txt")
    input("输入任何字符退出...")
