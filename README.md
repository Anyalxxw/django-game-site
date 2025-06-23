# 🎮 Django Game Site

A full-featured gaming website built with Django. This project is inspired by a [Figma design](https://www.figma.com/design/KMmztaxSQD4N8VhxIadSid/Gaming-Website-Design--Community-?node-id=0-1&p=f&t=hhBspBCSBIHh1TBA-0) and includes features for game listings, reviews, blogs, ratings, and admin content management.

## 🌐 Live Preview (Coming Soon)

> You can preview the design idea here:  
[Figma Design – Gaming Website](https://www.figma.com/design/KMmztaxSQD4N8VhxIadSid/Gaming-Website-Design--Community-?node-id=0-1&p=f&t=hhBspBCSBIHh1TBA-0)

---

## 🚀 Features

- Game list with genre and platform filtering
- Detailed game pages with ratings and cover images
- Blog section for articles or news
- Review system with comments and stars
- "Game of the Month" highlight
- Admin panel for content management
- Responsive UI design inspired by Figma template

---

## 🛠 Tech Stack

- Python 3.13+
- Django 5.x
- SQLite (default DB)
- HTML5, CSS3, JavaScript
- Pillow (image processing)

---

## ⚙️ Installation

1. **Clone the repository:** <br/>
  git clone https://github.com/Anyalxxw/django-game-site.git <br/>
  cd django-game-site <br/>
2. **Create and activate a virtual environment:** <br/>
  python -m venv venv <br/>
  source venv/bin/activate    # macOS / Linux <br/>
  venv\Scripts\activate       # Windows <br/>
3. **Install dependencies:** <br/>
  pip install -r requirements.txt<br/>
4. **Apply migrations:** <br/>
   python manage.py migrate<br/>
5. **Run the development server:** <br/>
   python manage.py runserver<br/>
6. **Open in browser:**

---

## Project Structure
  django-game-site/<br/>
  ├── blog/                # Blog app<br/>
  ├── reviews/             # Game reviews<br/>
  ├── library/             # Game catalog<br/>
  ├── game_of_the_month/   # Featured game module<br/>
  ├── store/               # (optional) game store<br/>
  ├── static/              # Static files<br/>
  ├── media/               # Uploaded images<br/>
  ├── templates/           # HTML templates<br/>
  └── game_site/           # Project config<br/>

---

## Sample Admin Login
   You can create a superuser with:<br/>
   python manage.py createsuperuser<br/>

---

## Author

Anna Alekseeva

## 📝 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this software with proper attribution.  
© 2025 Anna Alekseeva
