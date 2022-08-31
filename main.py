from handleAPI import HandleAPI
from anniversary import Anniversary
from push import Push

if __name__ == '__main__':
    # 能获取到到参数全部获取，按模板需求推送至微信
    get_data = HandleAPI()
    get_days = Anniversary()
    pretty_girl = get_data.pretty_girl()
    daily_english_en, daily_english_cn = get_data.daily_english()
    temp_min, temp_max, aqi, precipitation,skycon_nl_day, skycon_nl_night = get_data.get_caiyun_data()
    birth_msg, date_msg, wedding_msg, born_msg = get_days.get_days()
    msg = {
        'touser': '',
        'template_id': '',
        'data': {
            "skycon_nl_day": skycon_nl_day,
            "skycon_nl_night": skycon_nl_night,
            "temp_min": temp_min,
            "temp_max": temp_max,
            "aqi": aqi,
            "birth_msg": birth_msg,
            "date_msg": date_msg,
            "wedding_msg": wedding_msg,
            "born_msg": born_msg,
            "precipitation": precipitation,
            "pretty_girl": pretty_girl,
            "daily_english_en": daily_english_en,
            "daily_english_cn": daily_english_cn
        }
    }

    Push().push_msg(msg)
