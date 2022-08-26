from selenium.webdriver import Chrome
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from concurrent.futures import ThreadPoolExecutor

# 利用selenium进行信息填写
# 返回二维码直接扫码捐款，不需要多次信息填写项目
# 利用多线程进行并发

# url_jiujiang_second = "http://wx.fsnh.n.gongyibao.cn/#/donform?accId=e1bd3ed9-b53d-46ac-a578-c94043063584&proId=e5897e5a-f1d9-42ad-8dc3-34a271699b3f&paymethod=1"


def get_single_qrcode(seq):
    option = Options()
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    option.add_argument('--disable-blink-features=AutomationControlled')

    web = Chrome(options=option)

    url_jiujiang = "http://wx.fsnh.n.gongyibao.cn/#/projectdetail?id=e5897e5a-f1d9-42ad-8dc3-34a271699b3f"
    web.get(url_jiujiang)
    time.sleep(1)

    web.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[1]/ul/li[2]/a/button').click()  # click denote directly
    # web.switch_to.window(web.window_handles[-1])
    time.sleep(1)

    # input pre data and click anonymous, protocol
    web.find_element_by_xpath('//*[@id="app"]/div/div[2]/label').click()  # click agree protocol
    web.find_element_by_xpath('//*[@id="app"]/div/form/dl[2]/dd/label').click()  # click anonymous
    time.sleep(0.5)

    web.find_element_by_xpath('//*[@id="app"]/div/form/dl[1]/dd/div/a[4]/div[2]/input').click()  # click input
    time.sleep(0.2)
    web.find_element_by_xpath('//*[@id="app"]/div/form/dl[1]/dd/div/a[4]/div[2]/input').send_keys("1")
    web.find_element_by_xpath('//*[@id="app"]/div/form/a[2]/div[2]/div[2]/input').send_keys("烽哥")
    web.find_element_by_xpath('//*[@id="app"]/div/div[3]/button').click()  # click go to payment
    time.sleep(0.1)
    web.find_element_by_xpath('//*[@id="app"]/div/div[3]/button').click()  # website have some bugs it need double clicks fuckfuckfuck
    time.sleep(1)

    web.find_element_by_xpath('//*[@id="app"]/div/div[3]/button').click()  # click WeChat pay confirm
    time.sleep(0.5)
    web.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div/button[2]').click()  # click confirm tips
    time.sleep(3)

    # http://wx.fsnh.n.gongyibao.cn/#/donform?accId=e1bd3ed9-b53d-46ac-a578-c94043063584&proId=e5897e5a-f1d9-42ad-8dc3-34a271699b3f&paymethod=1
    img = web.find_element_by_xpath('//*[@id="qrcodeTable"]/canvas').screenshot_as_png
    name = "qr_code" + str(seq)
    with open("qr_code_save/" + name + ".png", "wb") as f:
        f.write(img)

    web.close()


if __name__ == '__main__':
    print("++++++++++start++++++++++")
    with ThreadPoolExecutor(4) as t:
        for i in range(4):
            t.submit(get_single_qrcode, seq=i)

    print("----------finish----------")
