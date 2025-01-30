import sys
import json
import joblib
import pandas as pd

def main():
    if len(sys.argv) !=2:
        print(sys.argv[1])
        raise IndexError('Give proper argument:\n Length not equal to two')
## load dataframe:
    try:
        json_data = sys.argv[1]

        data = json.loads(json_data)

        df = pd.DataFrame(data)
    except Exception as e:
        print(e)
        raise ValueError('Give a proper dataframe')

## if dataframe:

    if isinstance(df, pd.DataFrame):
        try:
            model = joblib.load('model/saved_svm_model.joblib')
            result = model.predict(df)
            # result = df.shape
            # print(result[0])
            return {'data_shape':df.shape, 'result':result[0]}
        except Exception as e:
            print(e)
    else:
        raise ValueError('Not a dataframe')

if __name__ == "__main__":
    res = main()
    # Convert numpy types to standard python types
    res['result'] = int(res['result'])
    res['data_shape'] = tuple(res['data_shape'])

    json_string = json.dumps(res)  # Convert to JSON string
    print(json_string)

sys.stdout.flush()