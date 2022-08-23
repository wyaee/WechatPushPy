import requests
import json
from config import global_config


class Push(object):
    def __init__(self):
        self.appid = global_config.get('WechatConfig', 'appID')
        self.appsecret = global_config.get('WechatConfig', 'appsecret')
        self.template_id = global_config.get('WechatConfig', 'templateID')
        self.target_id = global_config.get('WechatConfig', 'targetID')
        self.access_token = None
        self.json_file = json.load(open('token.json'))
        if not self.appid or not self.appsecret:
            print('请在 config.ini 文件中配置相关参数')

    def get_token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(
            self.appid, self.appsecret)
        data = requests.get(url).json()
        self.access_token = data['access_token']

        return self.access_token

    def push_msg(self, msg):
        msg['touser'] = self.target_id
        msg['template_id'] = self.template_id
        json_data = json.dumps(msg)
        if self.access_token is None:
            self.get_token()
        access_token = self.access_token
        url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % str(access_token)
        response = requests.post(url, json_data)
        print(json.loads(response.text))
