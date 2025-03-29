# 🌍 Language Budget Countries

A data processing solution that analyzes movie production budgets by language, providing insights into the financial distribution across different languages and the countries that produce films in each language.

## 📋 Overview

This repository demonstrates the use of [MRJob](https://mrjob.readthedocs.io/en/latest/) for processing movie data. The application aggregates movie budget information by language, presenting:

- Total budget allocated per language
- List of countries producing films in each language
- Average budget per film in each language

## 🔧 Installation

### Prerequisites

- Python 3.6 or higher
- Pip package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/language-budget-countries.git
cd language-budget-countries

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

### Running the Analysis

```bash
python language_budget_countries.py input/movies_data.csv > output/results.json
```

### Input Data Format

The application expects a CSV file with at least the following columns:
- `language`: The primary language of the film
- `budget`: The production budget (in USD)
- `country`: The country of production

### Output Format

The output is a JSON file structured as follows:

```json
{
  "English": {
    "total_budget": 15000000000,
    "countries": ["United States", "United Kingdom", "Canada", "Australia"],
    "average_budget": 35000000
  },
  "Spanish": {
    "total_budget": 2500000000,
    "countries": ["Spain", "Mexico", "Argentina", "Colombia"],
    "average_budget": 12000000
  }
}
```

## 🗂️ Repository Structure

```
language-budget-countries/
├── language_budget_countries.py  # Main MRJob script
├── input/                        # Input data directory
│   └── movies_data.csv           # Sample input data
├── output/                       # Output directory
│   └── results.json              # Sample results
├── tests/                        # Test directory
│   └── test_mrjob.py             # Unit tests
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## 📚 How It Works

The application uses the MapReduce paradigm through MRJob to process large datasets efficiently:

1. **Map Phase**: Each movie record is processed, emitting (language, (budget, country)) key-value pairs
2. **Reduce Phase**: Data is aggregated by language, summing budgets and collecting unique countries
3. **Final Processing**: Calculates averages and formats the output as structured JSON

## 📊 Example Results

| Language | Total Budget ($) | Countries | Avg Budget/Film ($) |
|----------|-----------------|-----------|---------------------|
| English  | 15B             | 25        | 35M                 |
| Spanish  | 2.5B            | 12        | 12M                 |
| French   | 1.8B            | 8         | 15M                 |
| Chinese  | 3.2B            | 5         | 28M                 |

## 🔗 References

- [MRJob Documentation](https://mrjob.readthedocs.io/en/latest/)
- [Hadoop MapReduce](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)
- [Movie Database Source](https://www.example-movie-database.com)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
