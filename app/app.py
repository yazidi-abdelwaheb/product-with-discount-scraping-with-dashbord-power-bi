from app.scrapers.jumia import products_jumia
from app.scrapers.spacenet import products_spacenet
from app.utils.tools import   menu
from app.data_base.select import len_site
from app.data_base.insert import update_dataBase
import json 
from app.utils.tools import loading

def app():
    x=menu()
    while x!=0 :

        match x :
            case 0 : return 
            case 1 :
                jumia = loading('Start scraping in site jumia',products_jumia)
                spacenet= loading('Start scraping in spacenet',products_spacenet)
                data={
                    'jumia':jumia,
                    'spacenet':spacenet
                }
                with open("app/data_json/data.json", "w") as f:
                    json.dump(data, f)
               
               
                print('\nYour data has been updated.\n')
            case 2:
                res=loading('Start update your database',update_dataBase)
              
                print('\nYour data base has been updated.\n')
            case 3 :
                if len_site == 0:
                    print('Your database is empty. scraping data then insert into the database to see the dashboard.')
                    
                
        x=menu()