import requests
from urllib import parse
from config import global_config


class HandleAPI(object):
    def __init__(self):
        self._url = 'https://api.tianapi.com/'
        self._tianKey = global_config.get('APIS', 'tian_APIKEY')
        self._caiyunKey = global_config.get('APIS', 'caiyun_APIKEY')
        self._colorPrimary = global_config.get("Color", 'colorPrimary')
        self._colorSecondary = global_config.get("Color", 'colorSecondary')
        self._colorSuccess = global_config.get("Color", 'colorSuccess')
        self._colorDanger = global_config.get("Color", 'colorDanger')
        self._colorWarning = global_config.get("Color", 'colorWarning')
        self._caiyunKEY = global_config.get("APIS", 'caiyun_APIKEY')
        self._longitude = global_config.get("APIS", 'longitude')
        self._latitude = global_config.get("APIS", 'latitude')
        if not self._tianKey:
            print("请在config.ini填入tian_APIKEY")
        if not self._caiyunKEY:
            print("请在config.ini填入caiyun_APIKEY")

    def get_tian_data(self, app):
        url = parse.urljoin(self._url, '{}/index?key='.format(app) + self._tianKey)
        response = requests.get(url).json()
        data = {}
        if response['code'] == 200:
            data = response['newslist'][0]
        else:
            print("get tian data error")
            exit(0)
        return data

    def get_caiyun_data(self):
        url = 'https://api.caiyunapp.com/v2.5/{}/{},{}/daily?dailysteps=1'.format(self._caiyunKEY,
                                                                                  self._longitude,
                                                                                  self._latitude)
        response = requests.get(url).json()
        if response['status'] == 'ok':
            data = response['result']['daily']
            temp_max = data['temperature'][0]['max']
            temp_min = data['temperature'][0]['min']
            aqi = data['air_quality']['aqi'][0]['avg']['usa']
            precipitation = data['precipitation'][0]['avg']
            skycon_day = data['skycon_08h_20h'][0]['value']
            skycon_night = data['skycon_20h_32h'][0]['value']
            if precipitation > 0:
                precipitation = {
                    "value": '[Warning]今日将有降雨，请注意带好雨具',
                    "color": self._colorDanger
                }
            else:
                precipitation = {}

            temp_max = {
                "value": int(temp_max),
                "color": self._colorWarning
            }
            temp_min = {
                "value": int(temp_min)
            }
            aqi = {
                "value": aqi
            }
            skycon_nl_day = {
                "value": global_config.get('SkyconNL', skycon_day)
            }
            skycon_nl_night = {
                "value": global_config.get('SkyconNL', skycon_night)
            }
            return temp_min, temp_max, aqi, precipitation, skycon_nl_day, skycon_nl_night
        else:
            print("get caiyun data error")
            exit(0)

    def pretty_girl(self):
        data = self.get_tian_data('caihongpi')
        pretty_girl = {
            "value": data['content'],
            "color": self._colorSuccess
        }

        return pretty_girl

    def daily_english(self):
        data = self.get_tian_data('everyday')
        daily_eng_en = {
            "value": data['content'],
            "color": self._colorPrimary
        }
        daily_eng_cn = {
            "value": data['note']
        }
        return daily_eng_en, daily_eng_cn

    def dialog(self):
        data = self.get_tian_data('dialogue')
        dialog_cn = {
            "value": data['dialogue'],
            # "color":
        }
        dialog_en = {
            "value": data['english'],
            # "color":
        }
        dialog_source = {
            "value": data['source']
        }
        return dialog_cn, dialog_en, dialog_source
