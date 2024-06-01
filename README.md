# 🐑 WoolHub_API 🧶

WoolHub_API is a Django REST framework-based API tailored for wool industry data retrieval. It offers a comprehensive set of filters to access detailed information on wool breeds, colors, prices, and more, ensuring high flexibility and precise data fetching.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) ![DRF](https://img.shields.io/badge/Django%20REST%20Framework-007396?style=for-the-badge&logo=django&logoColor=white)

## 🌟 Features
- **Advanced Filtering**: Utilize exact matches, range selections, and orderings to query wool data precisely.
- **Customizable Data Retrieval**: Tailor the information you fetch to include breed, color, micron count, price, and dates.

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/WoolHub_API.git

# Navigate to the project directory
cd WoolHub_API

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## 📚 API Endpoints and Filters

The API provides detailed filters to refine your data search:

### Endpoint: `/api/wool/data`
| Query Parameter  | Description                            | Example                      |
|------------------|----------------------------------------|------------------------------|
| `breed`          | Exact breed match.                     | `?breed=Merino`              |
| `color`          | Exact color match.                     | `?color=White`               |
| `micron`         | Exact micron range match.              | `?micron=32-36`              |
| `min_price`      | Minimum price filter.                  | `?min_price=100`             |
| `max_price`      | Maximum price filter.                  | `?max_price=200`             |
| `date`           | Exact date match.                      | `?date=2022-03-18`           |
| `breed_contains` | Partial breed match.                   | `?breed_contains=cho`        |
| `color_choice`   | Filter by color choices.               | `?color_choice=white`        |
| `date_range`     | Filter by date range.                  | `?date_range_after=2022-01-01&date_range_before=2022-01-31` |
| `ordering`       | Order results by price or date.        | `?ordering=-price`           |

## 🤖 How to Use
To retrieve data from WoolHub_API, use tools like `curl` or any HTTP client:

```bash
curl -X GET "http://localhost:8000/api/wool/data?breed=Merino&min_price=100"
```

## 📄 Documentation
For more detailed API documentation, visit: [WoolHub_API Docs](http://localhost:8000/docs)

## 🤝 Contributing
Contributions are welcome. Please follow these steps to contribute:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact
Project Link: [https://github.com/dhruvpuri-goswami/WoolHub_API](https://github.com/dhruvpuri-goswami/WoolHub_API)

## 🙏 Acknowledgements
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
