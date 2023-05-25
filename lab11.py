
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, restaurant_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_rating = restaurant_rating
    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name}\nТип кухни: {self.cuisine_type}')
    def open_restaurant(self):
        print("Ресторан открыт!")
    def change_rating(self,new_raiting):
        self.restaurant_rating =new_raiting
    def raiting(self):
        print(f'Новый рейтинг:{self.restaurant_rating}')


newRestaurant = Restaurant('Сена','Французская',5)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

restaurant_1 = Restaurant('Макароны','Итальянская',5)
restaurant_1.describe_restaurant()
restaurant_2 = Restaurant('Дэли','Индийская',4)
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('Аграба','Арабская',4)
restaurant_3.describe_restaurant()
restaurant_3.change_rating(input('Введите новый рейтинг:'))
restaurant_3.raiting()
