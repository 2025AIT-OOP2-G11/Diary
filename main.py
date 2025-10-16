from diaries.DiarySample import DiarySample
from diaries.ShimodaDiary import ShimodaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

diaries = [ShimodaDiary(), ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()