import unittest
import pandas as pd
from CountryDate import CountryDataFrame


class TestCountryDataFrameMethods(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        sample_data = [
            ['Poland', 38000000, 'Europe', 'Eastern Europe', 312696, 'Warsaw', 32.0],
            ['United States', 328000000, 'Americas', 'Northern America', 9833517, 'Washington, D.C.', 41.5],
            ['Canada', 37590000, 'Americas', 'Northern America', 9976140, 'Ottawa', 32.6]
        ]
        self.columns = ['Country', 'Population', 'Region', 'Subregion', 'Area', 'Capital', 'Gini']

        # Create a CountryDataFrame instance with the sample data
        api_url = 'https://restcountries.com/v3/alpha'
        country_codes = ['PL', 'US', 'CA']
        self.country_df = CountryDataFrame(api_url=api_url, country_codes=country_codes)
        self.country_df.dframe = pd.DataFrame(sample_data, columns=self.columns)


    def test_filter_dataframe_by_region(self):
        # Call the method to filter the DataFrame by specified regions
        self.country_df.filter_dataframe_by_region()

        # Assertions to check if the filtering is done correctly
        expected_result = pd.DataFrame([
            ['Poland', 38000000, 'Europe', 'Eastern Europe', 312696, 'Warsaw', 32.0],
            ['United States', 328000000, 'Americas', 'Northern America', 9833517, 'Washington, D.C.', 41.5],
            ['Canada', 37590000, 'Americas', 'Northern America', 9976140, 'Ottawa', 32.6]
        ], columns=self.columns)

        pd.testing.assert_frame_equal(self.country_df.dframe, expected_result)

    def test_sort_dataframe_by_population(self):
        # Call the static method to sort the DataFrame by Population
        sorted_df = CountryDataFrame.sort_dataframe_by_population(self.country_df.dframe)

        # Sort both dataframes by the "Country" column for comparison
        sorted_df = sorted_df.sort_values(by='Country').reset_index(drop=True)
        expected_result = pd.DataFrame([
            ['Canada', 37590000, 'Americas', 'Northern America', 9976140, 'Ottawa', 32.6],
            ['Poland', 38000000, 'Europe', 'Eastern Europe', 312696, 'Warsaw', 32.0],
            ['United States', 328000000, 'Americas', 'Northern America', 9833517, 'Washington, D.C.', 41.5]
        ], columns=self.columns).sort_values(by='Country').reset_index(drop=True)

        # Assertions to check if the sorting is done correctly
        pd.testing.assert_frame_equal(sorted_df, expected_result)

    def test_group_dataframe_by_subregion(self):
        # Call the static method to group the DataFrame by Subregion
        grouped_df = CountryDataFrame.group_dataframe_by_subregion(self.country_df.dframe)

        # Define the expected result after grouping by 'Subregion'
        expected_result = pd.DataFrame([
            ['Eastern Europe', 1, 38000000, 312696],
            ['Northern America', 2, 365590000, 19809657]
        ], columns=['Subregion', 'Country', 'Population', 'Area'])

        # Assertions to check if the grouping is done correctly
        pd.testing.assert_frame_equal(grouped_df, expected_result)

    def test_filter_dataframe_by_letter_a(self):
        # Call the method to filter the DataFrame by letter 'a'
        self.country_df.filter_dataframe_by_letter_a()

        # Assertions to check if the filtering is done correctly
        expected_result = pd.DataFrame([
            ['Poland', 38000000, 'Europe', 'Eastern Europe', 312696, 'Warsaw', 32.0],
            ['United States', 328000000, 'Americas', 'Northern America', 9833517, 'Washington, D.C.', 41.5],
            ['Canada', 37590000, 'Americas', 'Northern America', 9976140, 'Ottawa', 32.6]
        ], columns=self.columns).reset_index(drop=True)

        pd.testing.assert_frame_equal(self.country_df.dframe, expected_result)


class TestCountryDataFrame(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        sample_data = [
            ['Germany', 83240525, 'Europe', 'Western Europe', 357114, 'Berlin', None],
            ['United Kingdom', 67215293, 'Europe', 'Northern Europe', 242900, 'London', None],
            ['Australia', 25687041, 'Oceania', 'Australia and New Zealand', 7692024, 'Canberra', None]
        ]
        self.columns = ['Country', 'Population', 'Region', 'Subregion', 'Area', 'Capital', 'Gini']

        # Create a CountryDataFrame instance with the sample data
        api_url = 'https://restcountries.com/v3/alpha'
        country_codes = ['DE', 'GB', 'AU']
        self.country_df = CountryDataFrame(api_url=api_url, country_codes=country_codes)
        self.country_df.dframe = pd.DataFrame(sample_data, columns=self.columns)

    def test_filter_dataframe_by_region(self):
        # Call the method to filter the DataFrame by specified regions
        self.country_df.filter_dataframe_by_region()

        # Expected result after filtering by specified regions
        expected_result = pd.DataFrame([
            ['Germany', 83240525, 'Europe', 'Western Europe', 357114, 'Berlin', None],
            ['United Kingdom', 67215293, 'Europe', 'Northern Europe', 242900, 'London', None],
        ], columns=self.columns)

        # Assertions to check if the filtering is done correctly
        pd.testing.assert_frame_equal(self.country_df.dframe, expected_result)

    def test_group_dataframe_by_subregion(self):
        # Call the static method to group the DataFrame by Subregion
        grouped_df = CountryDataFrame.group_dataframe_by_subregion(self.country_df.dframe)

        # Expected result after grouping by 'Subregion'
        expected_result = pd.DataFrame([

            ['Australia and New Zealand', 1, 25687041, 7692024],
            ['Northern Europe', 1, 67215293, 242900],
            ['Western Europe', 1, 83240525, 357114]
        ], columns=['Subregion', 'Country', 'Population', 'Area'])

        # Assertions to check if the grouping is done correctly
        pd.testing.assert_frame_equal(grouped_df, expected_result)
    def test_sort_dataframe_by_population(self):
        # Call the static method to sort the DataFrame by Population
        sorted_df = CountryDataFrame.sort_dataframe_by_population(self.country_df.dframe)

        # Sort both dataframes by the "Country" column for comparison
        sorted_df = sorted_df.sort_values(by='Country').reset_index(drop=True)
        expected_result = pd.DataFrame([
            ['Australia', 25687041, 'Oceania', 'Australia and New Zealand', 7692024, 'Canberra', None],
            ['Germany', 83240525, 'Europe', 'Western Europe', 357114, 'Berlin', None],
            ['United Kingdom', 67215293, 'Europe', 'Northern Europe', 242900, 'London', None]
        ], columns=self.columns).sort_values(by='Country').reset_index(drop=True)

        # Assertions to check if the sorting is done correctly
        pd.testing.assert_frame_equal(sorted_df, expected_result)

    def test_filter_dataframe_by_letter_a(self):
        # Call the method to filter the DataFrame by letter 'a'
        self.country_df.filter_dataframe_by_letter_a()

        # Expected result after filtering by letter 'a'
        expected_result = pd.DataFrame([
            ['Germany', 83240525, 'Europe', 'Western Europe', 357114, 'Berlin', None],
            ['Australia', 25687041, 'Oceania', 'Australia and New Zealand', 7692024, 'Canberra', None]
        ], columns=self.columns).reset_index(drop=True)

        # Reset index for both DataFrames before comparison
        self.country_df.dframe = self.country_df.dframe.reset_index(drop=True)
        expected_result = expected_result.reset_index(drop=True)

        # Assertions to check if the filtering is done correctly
        pd.testing.assert_frame_equal(self.country_df.dframe, expected_result)

