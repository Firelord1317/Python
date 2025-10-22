import calendar

print('\n'.join(f"{i}: {m}" for i, m in enumerate(calendar.month_name) if i))