# 1. 找数据请求地址
import requests

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
data = {
    'from': 'zh',
    'to': 'en',
    'query': '你好',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '232427.485594',
    'token': '29393d4cb49253d48d82066cf4824d95',
    'domain': 'common',
}
headers = {
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

cookies = {
    #'BAIDUID': 'D4B444FE78CBB3678CAE11C526796E68:FG=1',
    #'BAIDUID_BFESS': 'D4B444FE78CBB3678CAE11C526796E68:FG=1',
    '__yjs_duid': '1_0a8d75cb5648c564de71ed2e03d94b0b1618921552610',
    'REALTIME_TRANS_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'PSTM': '1618925144',
    'BIDUPSID': '50AE456C4D0161AF2C9CFC1C0156FB10',
    'MCITY': '-158%3A',
    'BDUSS': 'mNIVzFHZ3JEZ1k5NnBmTkpFdk03VW56dmRaR1Z-ZEVoNmQzcGprSllOWVdzSWRoRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYjYGEWI2Bhb',
    'BDUSS_BFESS': 'mNIVzFHZ3JEZ1k5NnBmTkpFdk03VW56dmRaR1Z-ZEVoNmQzcGprSllOWVdzSWRoRVFBQUFBJCQAAAAAAAAAAAEAAAD9hL2nuti-~M~oMzEzNjQxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYjYGEWI2Bhb',
    'H_WISE_SIDS': '110085_127969_132548_164325_178384_178637_179345_179380_179449_181133_181135_181482_181588_182000_182273_182529_183030_183330_183630_183976_184012_184321_184655_184735_184794_184811_185029_185036_185306_185517_185635_185879_185924_186039_186319_186411_186597_186643_186716_186743_186831_186844_186894_187019_187084_187121_187206_187215_187287_187418_187485_187532_187562_187605_187668_187726_187789_187815_187877_187929_188181_188294_188426_188521_188733_188754_188832_188846_188898_189056_189096_189097_189143',
    'BDRCVFR[feWj1Vr5u3D]': 'I67x6TjHwwYf0',
    'delPer': '0',
    'PSINO': '7',
    'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
    'H_PS_PSSID': '34837_34067_31254_34657_34584_34518_34830_1996_26350_34627_34473_34700',
    'BA_HECTOR': '0004258hah84a52l5o1gmdojm0q',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1632641112,1632987239,1632987320,1634132601',
    'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1634132601',
    'ab_sr': '1.0.1_MzFjZWQzYzgwZTRkNGUyYWUwZmZjYjIxNTdhZWI3OTczNWM5MmIwYjdhOGJjMDBmZTA3N2VlMDQ2NWQ4Y2I2ODcwZGNmODZmNDk3NjE0ZDU1YzNiNzEwMDFmZTg1OTM5N2VlNjJkNTk5NTI1MmQ2NDZkMTI0NDEwMjJlYzMzZDA3NTBmNmQyZmRjZGEzZDQ5YWFkZGNmNjkxYTlhOWI0MTUwNDA3ZjZkNGM1Njk1NmJmZjQ2YzlhYmI0NGJjZWNm',
}

response = requests.post(url=url, headers=headers, data=data, cookies=cookies)
json_data = response.json()
print(json_data)

"""
当请求不到数据的时候:
    自己的问题:
        headers: User-Agent, Host, Referer, Cookies, Origin
            header, 请求头不全, headers少参数, 没有带cookie, 
            
        参数问题: params 查询参数;  data 请求参数
        
        请求有没有加密?
        
        是不是你的权限没有?<用户权限>
            需要登录的session
        
        代码错误
        
        动态地址
        
        不兼容
        
        封ip: 自己爬取多了, 服务器封锁你的ip, 代理池项目
        
        出现验证码: 人机验证, 应对不正常的请求, 过滤大部分恶意攻击, 
    
    别人的问题
        网站已经蹦了

"""

