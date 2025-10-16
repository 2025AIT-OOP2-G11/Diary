from diaries.AbstractDiary import AbstractDiary

class YonekuraDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return "二日だった"
    def get_author(self):
        return "yonekura"