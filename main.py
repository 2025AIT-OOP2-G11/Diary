from diaries.DiarySample import DiarySample
from diaries.YabeDiary import YabeDiary
from diaries.YonekuraDiary import YonekuraDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), YabeDiary(), YonekuraDiary(),　]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()