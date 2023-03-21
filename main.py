from selenium import webdriver
import json
import time

info_f = open('config.json', 'r')
info = json.load(info_f)

driver = webdriver.Chrome()
driver.get('https://thos.tsinghua.edu.cn/fp/view?m=fp#from=hall&serveID=16415057158070272&act=fp/serveapply')

while(True):
    try:
        driver.find_element_by_id('i_user').send_keys(info['username'])
        break
    except:
        time.sleep(1)

driver.find_element_by_id('i_pass').send_keys(info['passwd'])

driver.find_element_by_xpath('//*[@id="theform"]/div[4]/a').click()

while(True):
    try:
        driver.find_element_by_xpath('//*[@id="tabsecond"]/a').click()
        print('main menu entered')
        break
    except:
        print('entering main menu')
        time.sleep(1)

time.sleep(1)

while(True):
    try:
        driver.find_element_by_xpath('//*[@id="formHome_serve_content"]/div/div[3]/p[1]/span').click()
        print('star menu loaded')
        break
    except:
        print('loading star menu')
        time.sleep(1)

while(True):
    try:
        driver.switch_to_frame('formIframe')
        print('form loaded')
        break
    except:
        print('loading form')
        time.sleep(1)

print('application form filling')
driver.find_element_by_name('申请人联系电话').send_keys(info['phone'])
driver.find_element_by_id('XNDD').send_keys(info['destination'])
driver.find_element_by_id('KSSJ').send_keys(info['date'])
driver.find_element_by_id('SY').send_keys(info['reason'])
driver.switch_to.default_content()

for each_guest in info['guests']:
    driver.switch_to_frame('formIframe')

    driver.find_element_by_xpath('//*[@id="body_0"]/div[1]/div[7]/div[2]/div[1]/div[1]/div[1]/div/a[1]').click()

    driver.switch_to.default_content()

    while(True):
        try:
            driver.find_element_by_id('RYXM').send_keys(each_guest['name'])
            print('guest form loaded')
            break
        except:
            print('loading guest form')
            time.sleep(1)

    print('guest form filling')
    driver.find_element_by_id('RYSFZH').send_keys(each_guest['id_num'])
    driver.find_element_by_id('RYSJH').send_keys(each_guest['phone_num'])
    driver.find_element_by_id('RYSSDW').send_keys(each_guest['institution'])
    driver.find_element_by_id('RYXWJZD').send_keys(each_guest['home_addr'])

    print('submit button searching')
    driver.find_element_by_name('ok').click()

driver.switch_to_frame('formIframe')
driver.find_element_by_xpath('//*[@id="CN_vant"]/div/div/div').click()
print('done :-) check the information')