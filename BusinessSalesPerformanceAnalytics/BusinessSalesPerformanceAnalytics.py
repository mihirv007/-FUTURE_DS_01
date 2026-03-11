import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("/Users/mihirverma/BusinessSalesPerformanceAnalytics/online_retail.csv")

#features in dataset
features=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']

#check date-time format

expected_format='%Y-%m-%d %H:%M:%S'

validated_dates=pd.to_datetime(dataset['InvoiceDate'],format=expected_format,errors='coerce')

invalid_dates_mask=validated_dates.isna()

if invalid_dates_mask.any():
    print("Found incorrect date formats in the column:")
    # Display rows with incorrect dates
    print(dataset[invalid_dates_mask])
else:
    print("All dates in the column conform to the specified format.")


for featrue in features:
    dataset[featrue]=dataset[featrue].replace('',np.nan)

nan_count=dataset.isna().sum()
#print('nan_count: ',nan_count)
#print('total_rows: ',len(dataset))

dataset['CustomerID']=dataset['CustomerID'].fillna(dataset['CustomerID'].median(),inplace=False)

dataset['Description']=dataset['Description'].fillna(dataset['Description'].mode()[0],inplace=False)

nan_count=dataset.isna().sum()
#print('nan_count: ',nan_count)
#print('total_rows: ',len(dataset))

quantity=dataset[dataset['Quantity']>0]

dataset['Revenue']=(dataset['Quantity']*dataset['UnitPrice']).round(2)


product_Revenue=dataset.groupby(['StockCode','Description'])['Revenue'].sum()

top_product=product_Revenue.sort_values(ascending=False).head(20)

print(dataset['Revenue'].head(20))

#print(top_product)

#StockCode  Description                       
'''DOT        DOTCOM POSTAGE                        206245.48
22423      REGENCY CAKESTAND 3 TIER              164762.19
47566      PARTY BUNTING                          98302.98
85123A     WHITE HANGING HEART T-LIGHT HOLDER     97715.99
85099B     JUMBO BAG RED RETROSPOT                92356.03
23084      RABBIT NIGHT LIGHT                     66756.59
POST       POSTAGE                                66230.64
22086      PAPER CHAIN KIT 50'S CHRISTMAS         63791.94
84879      ASSORTED COLOUR BIRD ORNAMENT          58959.73
79321      CHILLI LIGHTS                          53768.06
23298      SPOTTY BUNTING                         42065.32
22386      JUMBO BAG PINK POLKADOT                41619.66
21137      BLACK RECORD COVER FRAME               40596.96
22502      PICNIC BASKET WICKER 60 PIECES         39619.50
22720      SET OF 3 CAKE TINS PANTRY DESIGN       37413.44
23284      DOORMAT KEEP CALM AND COME IN          36565.39
22960      JAM MAKING SET WITH JARS               36116.09
82484      WOOD BLACK BOARD ANT WHITE FINISH      35859.27
20725      LUNCH BAG RED RETROSPOT                34897.31
22197      POPCORN HOLDER                         33969.46'''

#Description count

'''WHITE HANGING HEART T-LIGHT HOLDER    2369
REGENCY CAKESTAND 3 TIER              2200
JUMBO BAG RED RETROSPOT               2159
PARTY BUNTING                         1727
LUNCH BAG RED RETROSPOT               1638
ASSORTED COLOUR BIRD ORNAMENT         1501
SET OF 3 CAKE TINS PANTRY DESIGN      1473
PACK OF 72 RETROSPOT CAKE CASES       1385
LUNCH BAG  BLACK SKULL.               1350
NATURAL SLATE HEART CHALKBOARD        1280
POSTAGE                               1252
JUMBO BAG PINK POLKADOT               1251
HEART OF WICKER SMALL                 1237
JAM MAKING SET WITH JARS              1229
JUMBO STORAGE BAG SUKI                1214
PAPER CHAIN KIT 50'S CHRISTMAS        1210
JUMBO SHOPPER VINTAGE RED PAISLEY     1202
LUNCH BAG CARS BLUE                   1197
LUNCH BAG SPACEBOY DESIGN             1192
JAM MAKING SET PRINTED                1182'''

#count of customer id 
'''CustomerID
17841.0    7983
14911.0    5903
14096.0    5128
12748.0    4642
14606.0    2782
15311.0    2491
14646.0    2085
13089.0    1857
13263.0    1677
14298.0    1640
15039.0    1508
14156.0    1420
18118.0    1284
14159.0    1212
14796.0    1165
15005.0    1160
16033.0    1152
14056.0    1128
14769.0    1094
17511.0    1076'''

#print(dataset['InvoiceNo'].value_counts()[dataset['InvoiceNo'].value_counts()>500]*dataset['InvoiceNo'])

total_quantity=0
                                       
'''InvoiceNo
573585    1114
581219     749
581492     731
580729     721
558475     705
579777     687
581217     676
537434     675
580730     662
538071     652
580367     650
580115     645
581439     635
580983     629
578344     622
538349     620
578347     606
537638     601
537237     597
536876     593
576617     593
536592     592
537823     591
576837     585
579508     578
577078     572
537240     568
577358     561
576618     552
576840     544
576339     542
579187     541
537666     536
538177     534
579196     533
580727     529
536544     527
578844     527
575930     526
577768     526
578827     520
576329     518
575176     518
539437     518
575477     515
539958     512
579512     503
575875     503
540551     502'''

#print(dataset['StockCode'].value_counts()[dataset['StockCode'].value_counts()>1000])
'''StockCode
85123A    2313
22423     2203
85099B    2159
47566     1727
20725     1639
84879     1502
22720     1477
22197     1476
21212     1385
20727     1350
22383     1348
22457     1280
23203     1267
POST      1256
22386     1251
22469     1239
22960     1229
21931     1214
22086     1210
22411     1202
20728     1197
22382     1192
22961     1182
22666     1180
23298     1179
22699     1138
22384     1137
23209     1135
82482     1129
22993     1111
22727     1107
22697     1085
23206     1084
22178     1072
20724     1068
23084     1067
20726     1061
22726     1026
21080     1015
23199     1009'''

#print(dataset['Quantity'].value_counts())
#all the country's in dataset
'''['United Kingdom' 'France' 'Australia' 'Netherlands' 'Germany' 'Norway'
 'EIRE' 'Switzerland' 'Spain' 'Poland' 'Portugal' 'Italy' 'Belgium'
 'Lithuania' 'Japan' 'Iceland' 'Channel Islands' 'Denmark' 'Cyprus'
 'Sweden' 'Austria' 'Israel' 'Finland' 'Bahrain' 'Greece' 'Hong Kong'
 'Singapore' 'Lebanon' 'United Arab Emirates' 'Saudi Arabia'
 'Czech Republic' 'Canada' 'Unspecified' 'Brazil' 'USA'
 'European Community' 'Malta' 'RSA']'''

#total countrys 32 and most dominate or most profitable region united kingdom

'''
Country             
United Kingdom          495478
Germany                   9495
France                    8557
EIRE                      8196
Spain                     2533
Netherlands               2371
Belgium                   2069
Switzerland               2002
Portugal                  1519
Australia                 1259
Norway                    1086
Italy                      803
Channel Islands            758
Finland                    695
Cyprus                     622
Sweden                     462
Unspecified                446
Austria                    401
Denmark                    389
Japan                      358
Poland                     341
Israel                     297
USA                        291
Hong Kong                  288
Singapore                  229
Iceland                    182
Canada                     151
Greece                     146
Malta                      127
United Arab Emirates        68
European Community          61
RSA                         58
Lebanon                     45
Lithuania                   35
Brazil                      32
Czech Republic              30
Bahrain                     19
Saudi Arabia                10'''

# Step 1: Get value counts
country_counts = dataset['Country'].value_counts()

# Step 2: Find countries with count < 1000
countries_to_replace = country_counts[country_counts < 1000].index

# Step 3: Replace them with "Other_Countries"
dataset['Country'] = dataset['Country'].replace(countries_to_replace, 'Other_Countries')

# Step 4: Check result
#print(dataset['Country'].value_counts())

#dataset rows : 541909

'''Country
United Kingdom     495478
Germany              9495
France               8557
EIRE                 8196
Other_Countries      7344
Spain                2533
Netherlands          2371
Belgium              2069
Switzerland          2002
Portugal             1519
Australia            1259
Norway               1086'''


country_Revenue=dataset.groupby('Country')['Revenue'].sum()

assending_country_revenue=country_Revenue.sort_values(ascending=False)

"""
Country
United Kingdom     8187806.364
Netherlands         284661.540
EIRE                263276.820
Other_Countries     239222.460
Germany             221698.210
France              197403.900
Australia           137077.270
Switzerland          56385.350
Spain                54774.580
Belgium              40910.960
Norway               35163.460
Portugal             29367.020
"""

total_revenue=dataset['Revenue'].sum()

'''for i in range(len(assending_country_revenue)):

    current_Country_Sales=assending_country_revenue.iloc[i]

    country_Name=assending_country_revenue.index[i]

    total_Sales_In_Each_Counrty_Percentage=(current_Country_Sales/total_revenue)*100

    print(f' Total Sales of {country_Name}:{total_Sales_In_Each_Counrty_Percentage:.2f}%')'''


#total sales in each country or region
'''
Total Sales of United Kingdom:84.00%
 Total Sales of Netherlands:2.92%
 Total Sales of EIRE:2.70%
 Total Sales of Other_Countries:2.45%
 Total Sales of Germany:2.27%
 Total Sales of France:2.03%
 Total Sales of Australia:1.41%
 Total Sales of Switzerland:0.58%
 Total Sales of Spain:0.56%
 Total Sales of Belgium:0.42%
 Total Sales of Norway:0.36%
 Total Sales of Portugal:0.30%
'''
''' 
Sale Growth Rate

(Current Period Sales - Prior  Period Sales/Prior  Period Sales)*100

Average Sales Growth Rate

(Total Sales Growth/Number of Years)*100

'''

dataset['InvoiceDate']=pd.to_datetime(dataset['InvoiceDate'],errors='coerce')
dataset['Year']=dataset['InvoiceDate'].dt.year
yearly_Revenue=dataset.groupby('Year')['Revenue'].sum()


perior_year=yearly_Revenue[2010]

current_year=yearly_Revenue[2011]


#sales growth rate

sales_Growth_Rate_Yearly=((current_year-perior_year)/perior_year)*100

print(f'sales_Growth_Rate_Yearly:{sales_Growth_Rate_Yearly:.2f}%')

#sales_Growth_Rate_Yearly:1101.51% from 2010 to 2011

#Monthly sales Revenue

dataset['Month']=dataset['InvoiceDate'].dt.month

monthly_Revenue=dataset.groupby(['Year','Month'])['Revenue'].sum()

monthly_Revenue_Growth=monthly_Revenue.sort_index()

#monthly_Revenue_Growth
'''
Year  Month
2010  12        748957.020
2011  1         560000.260
      2         498062.650
      3         683267.080
      4         493207.121
      5         723333.510
      6         691123.120
      7         681300.111
      8         682680.510
      9        1019687.622
      10       1070704.670
      11       1461756.250
      12        433668.010
'''

#Month growth rate

'''for i in range(len(monthly_Revenue_Growth)-1):
    perior_Month=monthly_Revenue_Growth.iloc[i]
    current_Month=monthly_Revenue_Growth.iloc[i+1]

    sales_Growth_Rate_Monthly=((current_Month-perior_Month)/perior_Month)*100

    year = monthly_Revenue_Growth.index[i][0]
    month = monthly_Revenue_Growth.index[i][1]

    #print(f"Year {year} Month {month} : Growth {sales_Growth_Rate_Monthly:.2f}%")
'''

#sales_Growth_Rate_Yearly
'''sales_Growth_Rate_Yearly:1101.51%
748957.02
Year 2010 Month 12 : Growth -25.23%
560000.26
Year 2011 Month 1 : Growth -11.06%
498062.65
Year 2011 Month 2 : Growth 37.18%
683267.08
Year 2011 Month 3 : Growth -27.82%
493207.121
Year 2011 Month 4 : Growth 46.66%
723333.51
Year 2011 Month 5 : Growth -4.45%
691123.12
Year 2011 Month 6 : Growth -1.42%
681300.111
Year 2011 Month 7 : Growth 0.20%
682680.51
Year 2011 Month 8 : Growth 49.37%
1019687.622
Year 2011 Month 9 : Growth 5.00%
1070704.67
Year 2011 Month 10 : Growth 36.52%
1461756.25
Year 2011 Month 11 : Growth -70.33%'''

#checking if the data is clean or not
print(list(dataset))

print(len(dataset))

dataset=dataset.dropna()

print(len(dataset))

NUN_VALUE=dataset.isna().sum()

print(NUN_VALUE)

#save the dataset

dataset.to_csv('business_sales_performance_analytics.csv')


