import statsmodels.api as sm
import pandas as pd

def protected_class_pvalue(df: pd.DataFrame):
    if df.empty:
        return 0
    
    df = pd.get_dummies(df, columns=['protected_class'], drop_first=True)
    df['protected_class_reference'] = df['protected_class_reference'].astype(int)


    x = df[['protected_class_reference', 'tenure', 'performance']]
    y = df['compensation']

    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    pvalue = model.pvalues['protected_class_reference']

    return round(pvalue, 3)