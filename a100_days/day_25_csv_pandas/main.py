import csv
import pandas


def read_data(name):
    with open(name) as file:
        data_list = file.readlines()
    return data_list


def read_csv(name):
    with open(name) as data_file:
        data = csv.reader(data_file)
        temperatures = []
        for row in data:
            if row[1] != 'temp':
                temperatures.append(int(row[1]))
    return temperatures


def working_with_pandas():
    data = pandas.read_csv("weather_data.csv")

    data_dict = data.to_dict()
    print(data_dict)

    temp_list = data["temp"].to_list()
    print(temp_list)

    avg_temp = data["temp"].mean()
    print(avg_temp)

    max_temp = data["temp"].max()
    print(max_temp)

    # Get data in columns
    print(data["condition"])
    print(data.condition)

    print()
    # Get data in row
    print(data[data.day == "Monday"])

    print(data[data.temp == data.temp.max()])
    print()

    monday = data[data.day == "Monday"]
    monday_temp_c = int(monday.temp)
    monday_temp_f = (monday_temp_c * 1.8) + 32
    print(monday_temp_f)

    # Create dataframe from scratch
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    print(data)
    data.to_csv("new_data.csv")


def create_squirrel_csv():
    all_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    grey_squirrels_count = len(all_data[all_data["Primary Fur Color"] == "Gray"])
    cinnamon_squirrels_count = len(all_data[all_data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels_count = len(all_data[all_data["Primary Fur Color"] == "Black"])

    data_dict = {
        "Fur color": ["Gray", "Cinnamon", "Black"],
        "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
    }

    df = pandas.DataFrame(data_dict)
    df.to_csv("squirrel_count.csv")

    # squirrel_count = all_data.groupby(["Primary Fur Color"])["Primary Fur Color"].count()
    # new_data = pandas.DataFrame(data=squirrel_count, columns=["Fur color", "Count"])
    # new_data.to_csv("squirrel_count.csv")


if __name__ == "__main__":
    create_squirrel_csv()
