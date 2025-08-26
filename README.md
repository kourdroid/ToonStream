# ToonStream 🎬

A modern Django-based streaming platform for animated content, featuring movies, series, and special episodes. ToonStream provides a Netflix-like experience specifically designed for cartoon and animated content.

## 🌟 Features

### Content Management
- **Multi-format Support**: Movies, TV Series, and Special Episodes
- **Season & Episode Organization**: Structured content hierarchy for series
- **Rich Media Support**: Video streaming with poster images and cover art
- **Trailer Integration**: Embedded trailer links for content preview
- **View Tracking**: Monitor content popularity and engagement

### User Experience
- **User Authentication**: Secure login and registration system
- **Responsive Design**: Modern UI built with Tailwind CSS
- **Search Functionality**: Find content quickly across the platform
- **Personal Lists**: Curated content collections for users
- **Streaming Interface**: Dedicated video players for different content types

### Technical Features
- **PostgreSQL Database**: Robust data storage and management
- **Media Handling**: Efficient file upload and serving with Pillow
- **Static File Management**: Optimized with WhiteNoise for production
- **Admin Interface**: Django admin for content management
- **Production Ready**: Configured for deployment with Gunicorn

## 🚀 Installation

### Prerequisites
- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd toonstream
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration**
   - Create a PostgreSQL database
   - Update database credentials in `toon_stream/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432'
       }
   }
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://localhost:8000` to access the application.

## 📖 Usage

### For Users
1. **Registration**: Create an account using the signup page
2. **Browse Content**: Explore movies, series, and specials on the homepage
3. **Watch Content**: Click on any title to view details and start streaming
4. **Search**: Use the search bar to find specific content
5. **Personal Lists**: Save favorite content to your personal list

### For Administrators
1. **Access Admin Panel**: Navigate to `/admin/` and login with superuser credentials
2. **Add Content**: Create new movies, series, seasons, and episodes
3. **Manage Users**: View and manage user accounts
4. **Upload Media**: Add video files, posters, and cover images
5. **Content Organization**: Organize series into seasons and episodes

### Content Types
- **Movies**: Standalone animated films
- **Series**: Multi-season shows with episodes
- **Specials**: One-off episodes or special content

## 🏗️ Project Structure

```
toonstream/
├── core/                   # Main application
│   ├── models.py          # Database models (Movie, Season, Episode)
│   ├── views.py           # View functions and logic
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin interface configuration
│   └── migrations/        # Database migrations
├── templates/             # HTML templates
│   ├── index.html         # Homepage
│   ├── movie_detail.html  # Content details page
│   ├── watch_movie.html   # Movie player
│   ├── watch_serie.html   # Series player
│   └── login.html         # Authentication pages
├── static/                # Static files (CSS, JS, images)
├── media/                 # User-uploaded content
├── toon_stream/           # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
└── manage.py             # Django management script
```

## 🛠️ Technology Stack

- **Backend**: Django 5.0.6
- **Database**: PostgreSQL with psycopg2
- **Frontend**: HTML, CSS, JavaScript with Tailwind CSS
- **Media Processing**: Pillow for image handling
- **Static Files**: WhiteNoise for production serving
- **Deployment**: Gunicorn WSGI server
- **Authentication**: Django's built-in user system

## 🔧 Configuration

### Environment Variables
For production deployment, consider using environment variables for sensitive settings:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` in production
- `DATABASE_URL`: PostgreSQL connection string
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

### Media Files
The application handles two types of media:
- **Static Files**: CSS, JavaScript, images (served via WhiteNoise)
- **Media Files**: User-uploaded content (videos, posters)

## 🚀 Deployment

### Railway/Heroku Deployment
1. Configure environment variables
2. Set up PostgreSQL database
3. Deploy using the provided `Procfile`
4. Run migrations in production
5. Collect static files

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up proper database credentials
- [ ] Configure media file serving
- [ ] Set up HTTPS
- [ ] Configure CSRF trusted origins

## 🤝 Contributing

We welcome contributions to ToonStream! Here's how you can help:

### Getting Started
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write or update tests as needed
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Guidelines
- Follow Django best practices
- Write clear, commented code
- Test your changes thoroughly
- Update documentation as needed
- Follow PEP 8 style guidelines

### Areas for Contribution
- UI/UX improvements
- Performance optimizations
- Additional content management features
- Mobile responsiveness enhancements
- API development
- Testing coverage

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page for existing problems
2. Create a new issue with detailed information
3. Include error messages, screenshots, and steps to reproduce

## 🔮 Future Enhancements

- [ ] User rating and review system
- [ ] Content recommendation engine
- [ ] Mobile application
- [ ] Social features (sharing, comments)
- [ ] Advanced search filters
- [ ] Content categorization by genre
- [ ] Watchlist and progress tracking
- [ ] Multi-language support
- [ ] API for third-party integrations

## 📊 Database Schema

### Models Overview
- **Movie**: Core content model with metadata
- **Season**: Groups episodes for series content
- **Episode**: Individual episodes within seasons
- **User**: Django's built-in user model for authentication

---

**ToonStream** - Bringing animated content to life! 🎭✨