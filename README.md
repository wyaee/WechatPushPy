# WechatPushPy
Wechat Push Python Version Easy Use.


## 0x00 Preparation

- Python >= 3.0
- Sign up for WeChat public number or [WeChat testing platform](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)
- Feature API
  - [TianAPI](https://www.tianapi.com/)
  - Weather API)：I am using the [Caiyunapp](https://dashboard.caiyunapp.com/user/sign_up/) weather API
  
 ## 0x01 How to use
 
 1. Fill in the relevant parameters in config.ini<br>
 2. Type `pip install -r requirements.txt` and run in the terminal to install the necessary dependencies.<br>
 3. Run the program use `python main.py`<br>
 
4. Template Reference
 ```
 早上好鸭，{target nickname or username}~

天气 : {{skycon_nl_day.DATA}}(白天), {{skycon_nl_night.DATA}} (夜间)
温度 : {{temp_min.DATA}}℃ - {{temp_max.DATA}}℃
空气质量 : {{aqi.DATA}} (US)
{{birth_msg.DATA}}
这是我们相恋的第{{date_msg.DATA}}天
我们已经结婚{{wedding_msg.DATA}}天了
今天是小芝麻出生的第{{born_msg.DATA}}天
{{precipitation.DATA}}

{{pretty_girl.DATA}}

{{daily_english_en.DATA}}
{{daily_english_cn.DATA}}
 ```
 
 ## 0x02 Cautions
 
 The recipient needs to follow the test number or public number to receive the message.
 
 ## 0x03 TODO
 - [ ] Log <br>
 - [ ] JavaScript version 
