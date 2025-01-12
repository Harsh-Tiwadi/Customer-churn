import pandas as pd

"""
All machine learning model
"""
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression,LassoCV, LogisticRegression, RidgeCV, ElasticNetCV
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import make_regression


class RegressionModel():
    """
    Pass the clean data and target column and classification/regression to RegressionModel Class for model training
    """
    def __init__(self, df, target:str):
        self._df = df
        self.target = target

    # Getter for the df attribute
    @property
    def df(self):
        if isinstance(self._df, pd.DataFrame):
            return self._df
        else:
            raise ValueError('Not a Dataframe')

    # Setter for the df attribute
    @df.setter
    def df(self, value):
        print('updating')
        if isinstance(value, pd.DataFrame):
            self._df = value
        else:
            raise ValueError("Not a DataFrame.")

    def run_all(self):
        target = self.target
        df = self.df
        x = df.drop(target, axis=1, inplace=True)
        y = df[target]
        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.25,)
        ### Regression models
        """
        'LinearRegression',
        'Ridge',
        'Lasso',
        'ElasticNet',
        'DecisionTreeRegressor',
        'RandomForestRegressor',
        'GradientBoostingRegressor',
        'KNeighborsRegressor'
        """
        # !> LinearRegression
        linear_regression = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=None, positive=False)
        linear_regression.fit(x_train, y_train)
        y_pred_lr = linear_regression.predict(x_test)
        print(f'1. linear_regression r2_score: {r2_score(y_test, y_pred_lr)}')
        print(f'1. linear_regression mean_squared_error: {mean_squared_error(y_test, y_pred_lr)}')

        # !> LassoCV
        alphas=[0.1, 0.7, 0.9, 1, 2, 5, 10, 100]
        lasso_regression = LassoCV(alphas=alphas, cv=5, tol=0.001, random_state=42) # it also take random co-efficient and try to optimize it with each rotation, one co-efficient at a time.
        lasso_regression.fit(x_train, x_test)
        best_alpha_lasso = lasso_regression.alpha_
        print(f'best_alpha fr lasso: {best_alpha_lasso}')
        y_pred_lasso = lasso_regression.predict(x_test)
        print(f'2. lasso_regression r2_score: {r2_score(y_test, y_pred_lasso)}')
        print(f'2. lasso_regression mean_squared_error: {mean_squared_error(y_test, y_pred_lasso)}')

        # !> RidgeCV
        ridge_regression = RidgeCV(alphas=alphas, cv=5, tol=0.001, random_state=42,) # it also take random co-efficient and try to optimize it with each rotation, one co-efficient at a time. also you can give separate alpha to each feature by solver='svd' and scoring="neg_mean_squared_error"
        ridge_regression.fit(x_train, y_train)
        best_alpha_ridge =ridge_regression.alpha_
        print(f'best_alpha fr ridge: {best_alpha_ridge}')
        y_pred_ridge = ridge_regression.predict(x_test)
        print(f'2. ridge_regression r2_score: {r2_score(y_test, y_pred_ridge)}')
        print(f'2. ridge_regression mean_squared_error: {mean_squared_error(y_test, y_pred_ridge)}')

        # !> Elastic_Net
        elastic_net = ElasticNetCV(alphas=alphas, l1_ratio=[.1, .5, .7, .9, .95, .99, 1], tol=0.001, cv=5, random_state=42) # l1_ratio for using both L1 and L2
        elastic_net.fit(x_train, y_train)
        best_alpha_elastic_net =elastic_net.alpha_
        print(f'best_alpha fr elastic_net: {best_alpha_elastic_net}')
        y_pred_elastic_net = elastic_net.predict(x_test)
        print(f'2. elastic_net r2_score: {r2_score(y_test, y_pred_elastic_net)}')
        print(f'2. elastic_net mean_squared_error: {mean_squared_error(y_test, y_pred_elastic_net)}')

        # !> Decision Tree Regressor
        d_tree_param_grid = {
            'criterion': ['squared_error', 'friedman_mse'], # criteria for spiting
            'max_depth': [3,5,10,15], # depth of the tree
            'min_samples_split': [5,7,10], # min samples before split if less then == '' no split
            'min_samples_leaf': [3,5,7], # min samples have to be == '' for leaf node
        }

        decision_tree = DecisionTreeRegressor(splitter='best',
                                              min_weight_fraction_leaf = 0, # % fraction of data that need to be in leaf node
                                              max_features = 'sqrt',
                                              random_state = 42,
                                              max_leaf_nodes = None,
                                              min_impurity_decrease = 0,
                                              ccp_alpha = 0 # cost-complexity pruning
        )

        decision_tree_cv = GridSearchCV(decision_tree, param_grid=d_tree_param_grid, cv=5, scoring='neg_mean_squared_error')
        decision_tree_cv.fit(x_train,y_train)
        print("Best parameters fr decision_tree:", decision_tree_cv.best_params_)
        best_decision_tree = decision_tree_cv.best_estimator_
        y_pred_d_tree = best_decision_tree.predict(x_test)
        print(f'2. decision_tree r2_score: {r2_score(y_test, y_pred_d_tree)}')
        print(f'2. decision_tree mean_squared_error: {mean_squared_error(y_test, y_pred_d_tree)}')

        # !> Random Forest Regressor
        rf_tree_param_grid = {
            'n_estimators': [50,100,200,300,500],
            'criterion': ['squared_error', 'friedman_mse'], # criteria for spiting
            'max_depth': [3,5,10,15], # depth of the tree
            'min_samples_split': [5,7,10], # min samples before split if less then == '' no split
            'min_samples_leaf': [3,5,7], # min samples have to be == '' for leaf node
            'max_samples': [0.8,0.9,1]
        }

        random_forest = RandomForestRegressor(
                                              min_weight_fraction_leaf = 0, # % fraction of data that need to be in leaf node
                                              max_features = 1,
                                              max_leaf_nodes = None,
                                              bootstrap=True,
                                              oob_score=True,
                                              min_impurity_decrease = 0,
                                              ccp_alpha = 0, # cost-complexity pruning
                                              random_state = 42,
        )

        random_forest_cv = GridSearchCV(random_forest, param_grid=rf_tree_param_grid, cv=5, scoring='neg_mean_squared_error')
        random_forest_cv.fit(x_train,y_train)
        print("Best parameters fr random_forest:", random_forest_cv.best_params_)
        best_random_forest = random_forest_cv.best_estimator_
        y_pred_rf_tree = best_random_forest.predict(x_test)
        print(f'2. random_forest r2_score: {r2_score(y_test, y_pred_rf_tree)}')
        print(f'2. random_forest mean_squared_error: {mean_squared_error(y_test, y_pred_rf_tree)}')

        # !> Gradient Boosting regressor













        # fit_intercept==True,
        # copy_X could save memory in large data if ==False,
        # n_jobs no. of cpu,
        # positive where negative
        ### classification models
        """
        'LogisticRegression',
        'KNeighborsClassifier',
        'GradientBoostingClassifier',
        'DecisionTreeClassifier',
        'RandomForestClassifier',
        'GaussianNB'
        """

        self.mode = "C"
        return 'hello'

    def __str__(self):
        return f"{self.df.head(1)}"

# df = pd.DataFrame({'name': ['harsh', 'k', 'l'], 'age': [25, 26, 27]})
# model = ExpModel(df,"hey", "C")
# print(model.direct_run())
