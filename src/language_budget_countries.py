from mrjob.job import MRJob

class MRLanguageBudgetCountries(MRJob):

    def mapper(self, _, line: str):
        """
        Mapper function to process each line of the input data.

        Args:
            _ (Any): Unused key.
            line (str): A single line of input data.

        Yields:
            Tuple[str, Tuple[str, float]]: Language as the key and a tuple of country and budget as the value.
        """
        try:
            # Definimos los nombres de los campos para mayor claridad
            movie_title, title_year, language, country, budget = line.split('|')

            # Validamos que todos los campos estén presentes y sean válidos
            if all([movie_title, title_year, language, country, budget]):
                yield language, (country, float(budget))
        except ValueError:
            pass  # Ignorar líneas con formato incorrecto

    def reducer(self, language: str, values: list):
        """
        Reducer function to aggregate budgets and countries for each language.

        Args:
            language (str): The language key.
            values (list): List of tuples containing country and budget.

        Yields:
            Tuple[str, Tuple[List[str], float]]: Language as the key and a tuple of sorted country list and total budget as the value.
        """
        countries = set()
        total_budget = 0.0

        for country, budget in values:
            countries.add(country)
            total_budget += budget

        yield language, (sorted(countries), total_budget)

if __name__ == "__main__":
    MRLanguageBudgetCountries.run()
