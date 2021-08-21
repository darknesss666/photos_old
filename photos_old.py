import vk_api
import time
import datetime
from vk_api import VkUpload

token = ('токен kate mobile')
vk_session = vk_api.VkApi(token = token, api_version = '5.135')
vk_session._auth_token()
upload = VkUpload(vk_session)

all_photos = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg'] #это картинки, загрузи в папку со скриптом 5 картинок, которые и будут накручиваться, можно 5 разных, но красивее будет, если все будут одинаковыми

while True:
    photo_list = upload.photo(all_photos, album_id = 'айди альбома', caption = f"первое описание\nвторое описание") #если описание не нужно, то сотри строку с "caption"
    time.sleep(3)
    print(time.strftime("\033[35m[%d.%m.%Y|%H:%M:%S]", time.localtime()), "Залил 5 фото на твою стору.")
    time.sleep(30)
print(f'''\033[0m\033[1;32m Накрутка завершена.
Скрипт написал Кирилл Элатов.
ВКонтакте создателя скрипта: https://vk.com/i____hate____my____life''')