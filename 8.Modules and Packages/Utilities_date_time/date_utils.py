from datetime import datetime

def date(f_date,s_date):
    first_date=datetime.strptime(f_date,"%Y-%m-%d")
    second_date=datetime.strptime(s_date,"%Y-%m-%d")
    print(first_date)
    print(second_date)

    # diffrent=first_date-second_date
    # print(f"Diffrent is: {diffrent}")
