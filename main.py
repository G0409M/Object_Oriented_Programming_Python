from CountryDate import CountryDataFrame

if __name__ == '__main__':
    api_url = 'https://restcountries.com/v3/alpha'
    country_codes = ['PL', 'US', 'CA', 'DE', 'FR', 'GB', 'IT', 'JP', 'AU', 'BR', 'IN', 'CN', 'RU', 'ZA', 'KR', 'MX',
                             'ES', 'ID', 'NG', 'EG', 'SA', 'AR', 'TR', 'IR', 'TH', 'IT', 'VN', 'PH', 'GB', 'FR',
                             'EG', 'GR', 'NL', 'PT', 'BE', 'SE', 'CH', 'AT', 'NO', 'DK', 'FI', 'IE', 'CL', 'CO', 'VE', 'PE',
                             'MY', 'SG', 'NZ']
    Country_data = CountryDataFrame(api_url, country_codes)
    print(Country_data)
    Country_data.run()
    print(Country_data)
    Country_data.visualize_data()
