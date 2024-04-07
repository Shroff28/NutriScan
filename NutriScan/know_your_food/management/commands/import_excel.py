from django.core.management.base import BaseCommand
from know_your_food.models import Nutritional_Info
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        excel_file_path = 'know_your_food/management/commands/nutritional_info.xlsx'
        df = pd.read_excel(excel_file_path)
        for index, row in df.iterrows():
            ingredients_detail = {
                "recipe_name": row['Recipe'],
                "serving": row['Serving'],
                "total_fat": row['Total fat(in gm)'],
                "saturated_fat": row['Saturated Fat (in gm)'],
                "cholesterol": row['Cholestrol (in mg)'],
                "sodium": row['Sodium (in mg)'],
                "total_carbohydrates": row['Total Carbohydrates (in gm)'],
                "dietary_fiber": row['Dietery Fibre (in gm)'],
                "sugars": row['Sugars (in gm)'],
                "proteins": row['Protiens (in gm)'],
                "calories": row['Calories(kCal)']
            }
            Nutritional_Info.objects.create(**ingredients_detail)
