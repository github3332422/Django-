from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '17255034'
API_KEY = '7D9lKyIhdW22ay8trhnbTcX8'
SECRET_KEY = '7RaXVAhPS5bvygIaQI9YErxOdwx9UCkE'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('F:\Python\dj02\shop\img\zq.jpg')

""" 调用通用物体识别 """
client.advancedGeneral(image);

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用通用物体识别 """
result = client.advancedGeneral(image, options)
print(result)

