import numpy as np
import pandas as pd
# import model
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
# import module to calculate model perfomance metrics
from sklearn import metrics
import matplotlib.pyplot as plt


def main():
    data_path = "data.csv"
    data = pd.read_csv(data_path)

    # create a Python list of feature names
    feature_names = ['month', 'new_users_rate_norm', 'avg_session_rate_norm', 'budget normalized',
                     'utm_form normalized']

    # use the list to select a subset of the original DataFrame
    X = data[feature_names]

    # sales
    y = data.was_a_sale

    plot_months_vs_sales(X['month'], X['avg_session_rate_norm'],  y)

    # Splitting X and y into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    # Linear Regression Model
    linreg = LinearRegression()

    # fit the model to the training data (learn the coefficients)
    linreg.fit(X_train, y_train)

    # make predictions on the testing set
    y_pred = linreg.predict(X_test)

    # compute the RMSE of our predictions
    print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


def plot_months_vs_sales(x, x2, y):
    months_data_for_sales = {}
    months_data_for_new_users = {}
    i = 0
    for month in x:
        did_it_sale = int(y[i])
        if did_it_sale == -1:
            did_it_sale = 0

        months_amount = 0
        try:
            months_amount = months_data_for_sales[month]
        except KeyError:
            pass

        months_data_for_sales[month] = months_amount + did_it_sale

        avg_new_users = int(x2[i])
        new_user_amount = 0
        try:
            new_user_amount = months_data_for_new_users[month]
        except KeyError:
            pass
        months_data_for_new_users[month] = new_user_amount + avg_new_users

        i += 1

    a = []
    b = []
    avg_users = []
    for month in months_data_for_sales.keys():
        a.append(month)
        b.append(months_data_for_sales[month])
        avg_users.append(months_data_for_new_users[month])

    # plt.plot(a, b, label='month vs sales qt')
    # plt.plot(a, avg_users, label='month vs avg new users')
    # plt.axis([1, 12, 0, 50])
    # plt.legend()
    # plt.show()


main()
