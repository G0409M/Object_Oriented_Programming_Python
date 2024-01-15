import pandas as pd
from tabulate import tabulate as tab
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

class DataFrame:
    def __init__(self, data, columns):
        self.dframe = pd.DataFrame(data, columns=columns)


    def __str__(self):
        if not self.dframe.empty:
            return tab(self.dframe, headers='keys', tablefmt='pretty')
        else:
            return "DataFrame is empty."
class CountryDataFrame(DataFrame):
    def __init__(self, api_url, country_codes):
        try:
            all_countries_data = []

            for country_code in country_codes:
                url = f'{api_url}/{country_code}'
                response = requests.get(url)

                # Obsługa błędów
                if response.status_code != 200:
                    print(f"Failed to retrieve data for {country_code}. Status code: {response.status_code}")
                    continue

                data = response.json()

                # Obsługa braku danych dla danego kraju
                if not data:
                    print(f"No data available for {country_code}")
                    continue

                country_data = data[0]
                all_countries_data.append(country_data)

            country_info_list = []
            for country_data in all_countries_data:
                country_name = country_data.get('name', {}).get('common', '')
                country_population = country_data.get('population', '')
                country_region = country_data.get('region', '')
                country_subregion = country_data.get('subregion', '')
                country_area = country_data.get('area', '')
                country_capital = country_data.get('capital', [''])[0]
                country_gini = country_data.get('gini', {}).get('2018', '')
                country_info_list.append(
                    [country_name, country_population, country_region, country_subregion, country_area, country_capital,
                    country_gini])

            columns = ['Country', 'Population', 'Region', 'Subregion', 'Area', 'Capital', 'Gini']
            super().__init__(country_info_list, columns)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            self.dframe = pd.DataFrame()  # Jeśli wystąpił błąd, przypisz pustą ramkę danych

    @staticmethod
    def sort_dataframe_by_population(self):
        sorted_df = self.sort_values(by='Population', ascending=False)
        return sorted_df


    @staticmethod
    def group_dataframe_by_subregion(self):
        grouped_df = self.groupby('Subregion').agg({
            'Country': 'count',
            'Population': 'sum',
            'Area': 'sum'
        }).reset_index()
        return grouped_df

    def filter_dataframe_by_region(self):
        self.dframe = self.dframe[self.dframe['Region'].isin(['Europe', 'Americas', 'Asia'])]

    def filter_dataframe_by_letter_a(self):
        self.dframe = self.dframe[self.dframe['Country'].str.lower().str.contains('a')]

    def run(self):
        self.dframe = CountryDataFrame.sort_dataframe_by_population(self.dframe)
        print("Sorted DataFrame:")
        self.filter_dataframe_by_region()
        print("\nFiltered DataFrame by Regions:")
        self.filter_dataframe_by_letter_a()
        print("\nFiltered DataFrame by choosing letter a:")
        self.dframe = CountryDataFrame.group_dataframe_by_subregion(self.dframe)
        print("\nGrouped DataFrame by Subregion:")

    def visualize_data(self, output_path='output_plot.png'):
        sns.set(style="whitegrid")
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

        def format_large_numbers(value, _):
            if value >= 1e6:
                return f'{value / 1e6:.1f}M'
            elif value >= 1e3:
                return f'{value / 1e3:.1f}K'
            else:
                return str(int(value))

        summed_population = self.dframe.groupby('Subregion')['Population'].sum().reset_index()
        summed_area = self.dframe.groupby('Subregion')['Area'].sum().reset_index()

        axes[0].bar(summed_population['Subregion'], summed_population['Population'], color='skyblue')
        axes[0].set_title('Summed Population by Subregion')
        axes[0].set_xlabel('Subregion')
        axes[0].set_ylabel('Summed Population')
        axes[0].yaxis.set_major_formatter(FuncFormatter(format_large_numbers))

        axes[1].bar(summed_area['Subregion'], summed_area['Area'], color='lightcoral')
        axes[1].set_title('Summed Area by Subregion')
        axes[1].set_xlabel('Subregion')
        axes[1].set_ylabel('Summed Area')
        axes[1].yaxis.set_major_formatter(FuncFormatter(format_large_numbers))
        fig.set_facecolor('#f0f0f0')

        plt.tight_layout()
        plt.savefig(output_path, dpi=300)
        plt.show()
