import matplotlib.pyplot as plt


def plot_conversion_by_group(conversion_by_group):
    plt.figure(figsize=(6, 4))
    conversion_by_group.plot(kind="bar", color=["#4C72B0", "#DD8452"])
    plt.title("Conversion Rate by Group")
    plt.ylabel("Conversion Rate")
    plt.xticks(rotation=0)
    plt.show()


def plot_conversion_by_day(conversion_by_day):
    conversion_by_day.plot(kind="bar", figsize=(10, 5))
    plt.title("Conversion Rate by Day and Group")
    plt.ylabel("Conversion Rate")
    plt.xticks(rotation=45)
    plt.legend(title="Test Group")
    plt.show()


def plot_conversion_by_hour(conversion_by_hour):
    conversion_by_hour.plot(kind="bar", figsize=(14, 5))
    plt.title("Conversion Rate by Hour and Group")
    plt.ylabel("Conversion Rate")
    plt.xlabel("Hour of Day")
    plt.legend(title="Test Group")
    plt.show()