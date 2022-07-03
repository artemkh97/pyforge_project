import requests, json
import pandas as pd
import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db.engine)
session = Session()

def write_data(compound):
    api_endpoint = 'https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/{}'.format(compound)
    data = requests.get(api_endpoint)
    df = pd.read_json(data.text)
    df.to_sql('compounds', con=db.engine, if_exists='append')
    return df

print(write_data('ADP'))

tr = db.transactions(df)
session.add(tr)

session.commit()
