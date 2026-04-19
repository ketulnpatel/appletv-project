from flask import Flask, render_template

app = Flask(__name__)

shows = [
    {
        "id": 1,
        "title": "Pluribus",
        "genre": "Sci-Fi Drama",
        "year": 2025,
        "seasons": 1,
        "rating": "TV-MA",
        "description": "The most miserable person on Earth must save the world from happiness after a mysterious virus transforms humanity into a peaceful hive mind.",
        "image": "https://m.media-amazon.com/images/M/MV5BOWNlM2E1MDMtYmI5MS00NDQ1LWI3NTctM2VlNjQ5OTAxYTNmXkEyXkFqcGc@._V1_UX500_.jpg",
        "badge": "New"
    },
    {
        "id": 2,
        "title": "Severance",
        "genre": "Sci-Fi Thriller",
        "year": 2022,
        "seasons": 2,
        "rating": "TV-MA",
        "description": "Mark leads a team of office workers whose memories have been surgically divided between their work and personal lives.",
        "image": "https://image.tmdb.org/t/p/w500/tBGuOovTd7FkrmQgtNNEJPyGFzl.jpg",
        "badge": "New Season"
    },
    {
        "id": 3,
        "title": "Ted Lasso",
        "genre": "Comedy Drama",
        "year": 2020,
        "seasons": 3,
        "rating": "TV-MA",
        "description": "An American college football coach is hired to manage an English soccer team, despite having no experience.",
        "image": "https://image.tmdb.org/t/p/w500/5fhZdwP1DVJ0FyVH6vrFdHwpXIn.jpg",
        "badge": "Award Winner"
    },
    {
        "id": 4,
        "title": "The Morning Show",
        "genre": "Drama",
        "year": 2019,
        "seasons": 3,
        "rating": "TV-MA",
        "description": "An inside look at the cutthroat world of morning news and the people who help America wake up.",
        "image": "https://image.tmdb.org/t/p/w500/intvkDMeGgCK3a1BkPa0CIKacBo.jpg",
        "badge": "Season 3"
    },
    {
        "id": 5,
        "title": "Foundation",
        "genre": "Sci-Fi Epic",
        "year": 2021,
        "seasons": 2,
        "rating": "TV-14",
        "description": "A complex saga of humans scattered on planets throughout the galaxy all living under the rule of the Galactic Empire.",
        "image": "https://image.tmdb.org/t/p/w500/vI7pHuxEBsRNdWhijPZ6Q0ZFBEP.jpg",
        "badge": "Epic Series"
    },
    {
        "id": 6,
        "title": "Slow Horses",
        "genre": "Spy Thriller",
        "year": 2022,
        "seasons": 4,
        "rating": "TV-MA",
        "description": "A gripping spy thriller following a team of MI5 agents who serve as a dumping ground for intelligence officers.",
        "image": "https://image.tmdb.org/t/p/w500/3GRHFoEjFKbMIJBxbUEoQ2MkCjg.jpg",
        "badge": "Fan Favourite"
    },
    {
        "id": 7,
        "title": "For All Mankind",
        "genre": "Alternate History",
        "year": 2019,
        "seasons": 4,
        "rating": "TV-MA",
        "description": "An alternate history where the global space race never ended, exploring what might have been.",
        "image": "https://image.tmdb.org/t/p/w500/fKyiGiuLOBmhVhJxzWpEaJIVCjR.jpg",
        "badge": "Season 4"
    },
    {
        "id": 8,
        "title": "Monarch: Legacy of Monsters",
        "genre": "Action Adventure",
        "year": 2023,
        "seasons": 1,
        "rating": "TV-14",
        "description": "Set after Godzilla's battle with other titans, two siblings discover their family's connection to the secret organization Monarch.",
        "image": "https://image.tmdb.org/t/p/w500/ijPm8xpQtMaGitgKjWqFpFKPAqI.jpg",
        "badge": "New"
    },
    {
        "id": 9,
        "title": "Bad Sisters",
        "genre": "Dark Comedy",
        "year": 2022,
        "seasons": 2,
        "rating": "TV-MA",
        "description": "The Garvey sisters are bound together by the premature death of their parents and a promise to always protect each other.",
        "image": "https://image.tmdb.org/t/p/w500/yEFEWHYBFoEQNYMnhNkFxCvQqGq.jpg",
        "badge": "Award Winner"
    },
]

featured = shows[0]

@app.route("/")
def index():
    return render_template("index.html", shows=shows, featured=featured)

@app.route("/show/<int:show_id>")
def show_detail(show_id):
    show = next((s for s in shows if s["id"] == show_id), None)
    if not show:
        return "Show not found", 404
    return render_template("detail.html", show=show)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)