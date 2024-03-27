class Car:
    def __init__(self, name, units_sold, customer_reviews):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(units_sold, int) or units_sold < 0:
            raise ValueError("Units sold must be a non-negative integer")
        if not isinstance(customer_reviews, (int, float)) or not 0 <= customer_reviews <= 5:
            raise ValueError("Customer reviews must be a float or integer between 0 and 5")

        self.name = name
        self.units_sold = units_sold
        self.customer_reviews = customer_reviews


def analyze_car_data(cars):
    if not cars:
        return "No cars available"

    total_units_sold = sum(c.units_sold for c in cars)
    highest_sales_car = max(cars, key=lambda x: x.units_sold).name
    above_average_reviews = [c.name for c in cars if c.customer_reviews > 3]
    average_review_score = sum(c.customer_reviews for c in cars) / len(cars)
    average_units_sold = total_units_sold / len(cars)
    below_average_sales = [(c.name, c.units_sold, c.customer_reviews) for c in cars if
                           c.units_sold < average_units_sold]

    return total_units_sold, highest_sales_car, above_average_reviews, average_review_score, below_average_sales


# Provided dataset
product_names = ["GTR R35", "Porsche 911", "Porsche GT3 RS", "Porsche GT2", "Tesla Model 3",
                 "Tesla Plaid", "Tesla Model S", "Tesla Roadster", "BMW M4 Competition", "BMW i8",
                 "Ferrari SF90", "Ferrari LaFerrari", "Ferrari Speedback", "Bugatti Chiron", "Bugatti Divo",
                 "Bugatti Chiron Supersport", "Pagani Zonda R", "Myvi 1.5 X", "Myvi 1.5 AV", "Nissan Sunny"]

units_sold = [150, 200, 100, 75, 250,
              170, 60, 300, 120, 90,
              10, 100, 135, 160, 170,
              70, 90, 15, 75, 98]

customer_reviews = [4.5, 3.8, 2.2, 4.0, 3.5,
                    4.3, 4.8, 4.8, 3.2, 4.8,
                    2.5, 3.0, 4.3, 3.5, 1.6,
                    5.0, 2.8, 2.9, 4.9, 4.9]

cars_data = []

try:
    for name, units, reviews in zip(product_names, units_sold, customer_reviews):
        car = Car(name, units, reviews)
        cars_data.append(car)

    results = analyze_car_data(cars_data)

    print("Total Units Sold:", results[0])
    print("Most Popular Car Model:", results[1])
    print("High Customer Satisfaction Models:", results[2])
    print("Average Customer Review Score:", results[3])
    print("Least Performed Models Identification:", results[4])

except (TypeError, ValueError) as e:
    print("Error:", e)

