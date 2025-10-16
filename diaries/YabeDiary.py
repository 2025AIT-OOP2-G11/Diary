from diaries.AbstractDiary import AbstractDiary

class YabeDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "今日もいい天気!"
    def get_author(self):
        return "Yabe"