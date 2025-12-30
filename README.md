🎬 MOVIE-REVIEW-API
Features
🎥 TMDB Integration - Auto movie posters, ratings, overviews

🔐 JWT Authentication - Secure register/login

📝 Full CRUD
Users can:
- Create reviews
- Read review
- Update reviews
- Delete reviews

🔍 Search & Filter - ?search=moviename

📄 Pagination - 10 reviews per page (?page=2)

QuickStart- Local
git clone https://github.com/Emmanuel047/Movie-Review-API.git
cd movie-review-api
pip install -r requirements.txt
cp .env.example .env  # Add your TMDB_API_KEY
python manage.py migrate
python manage.py runserver

Live API testing at https://movie-review-api-9pdy.onrender.com
Video Demo https://www.loom.com/share/1b844fe88f1745f29b679db1ba9b7efa

API ENDPOINTS

| Method | Endpoint        | Description       | Auth |
| ------ | --------------- | ----------------- | ---- |
| POST   | /api/register/  | Create user       | No   |
| POST   | /api/token/     | Login → JWT token | No   |
| POST   | /api/reviews/   | Create review     | Yes  |
| GET    | /api/reviews/   | List reviews      | Yes  |
| PATCH  | /api/reviews/1/ | Update review     | Yes  |
| DELETE | /api/reviews/1/ | Delete review     | Yes  |

Query Parameters
?page=2           → Page 2 (10/page)
?search=inception → Filter by title/content
?ordering=-rating → Sort by rating DESC
?rating=5         → Exact rating filter

Tech Stack
Backend: Python - Django 4.2 + DRF 3.15
Auth: djangorestframework-simplejwt
Database: SQLite/PostgreSQL
External API: TMDB v3
Search: django-filter
Deployment: Render ready
Frontend: HTML/CSS
Testing - Postman