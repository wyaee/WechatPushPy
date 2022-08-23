from config import global_config
from datetime import datetime, date


class Anniversary(object):
    def __init__(self):
        self._birthday = global_config.get('Anniversary', 'birthday')
        self._zhimaBirthday = global_config.get('Anniversary', 'zhima_birthday')
        self._datingAnniversary = global_config.get('Anniversary', 'dating_anniversary')
        self._weddingAnniversary = global_config.get('Anniversary', 'wedding_anniversary')
        self._colorDanger = global_config.get('Color', 'colorDanger')
        self._colorSecondary = global_config.get('Color', 'colorSecondary')
        self.today = date.today()

    @staticmethod
    def is_date(anniversary):
        """判断日期格式是否正确"""
        try:
            datetime.strptime(anniversary, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_count_days(self, anniversary):
        if not self.is_date(anniversary):
            print(u'日期值应为yyyy-mm-dd形式')
            exit(0)
        else:
            days = date.fromisoformat(anniversary)
            count_days = self.today - days
            return count_days

    def birthday_count(self, birthday):
        birth_msg = {}
        if not self.is_date(birthday):
            print(u'日期值应为yyyy-mm-dd形式')
            exit(0)
        else:
            birthday = date.fromisoformat(birthday)
            birth_month = birthday.month
            birth_day = birthday.day
            this_birth = date(self.today.year, birth_month, birth_day)
            next_years = self.today.year + 1
            next_birth = date(next_years, birth_month, birth_day)
            # 生日当月
            if birth_month == self.today.month:
                # 生日当天
                if birth_day == self.today.day:
                    birth_msg = {
                        "value": '岁岁年年，万喜万般宜\n！！！生日快乐！！！',
                        "color": self._colorDanger
                    }

                elif birth_day > self.today.day:
                    count_days = birth_day - self.today.day
                    birth_msg = {
                        "value": '距离你的生日还有{}天'.format(count_days),
                        "color": self._colorDanger
                    }
                else:
                    count_days = next_birth - self.today
                    birth_msg = {
                        "value": '距离你的生日还有{}天'.format(count_days.days),
                        "color": self._colorSecondary
                    }
            # 生日月之前
            elif birth_month > self.today.month:
                count_days = this_birth - self.today
                birth_msg = {
                    "value": '距离你的生日还有{}天'.format(count_days.days),
                    "color": self._colorSecondary
                }
            else:
                count_days = next_birth - self.today
                birth_msg = {
                    "value": '距离你的生日还有{}天'.format(count_days.days),
                    "color": self._colorSecondary
                }

        return birth_msg

    def get_days(self):
        birth_msg = self.birthday_count(self._birthday)
        born_total = self.get_count_days(self._zhimaBirthday).days
        date_total = self.get_count_days(self._datingAnniversary).days
        date_msg = {
            "value": date_total,
            "color": self._colorSecondary
        }
        wedding_total = self.get_count_days(self._weddingAnniversary).days
        wedding_msg = {
            "value": wedding_total,
            "color": self._colorSecondary
        }
        born_msg = {
            "value": born_total,
            "color": self._colorSecondary
        }

        return birth_msg, date_msg, wedding_msg, born_msg
