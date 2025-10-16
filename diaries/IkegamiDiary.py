from diaries.AbstractDiary import AbstractDiary

class IkegamiDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-15"
    def get_summary(self):
        return "アルバイトが忙しかった"
    def get_author(self):
        return "池上"