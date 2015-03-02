from flask import Flask, render_template

navbar = [{'href': '/', 'caption': 'Home'},
          {'href': '/about', 'caption': 'About'},
          {'href': '/shop', 'caption': 'Shop'},
          {'href': '/FAQ', 'caption': 'FAQ'},
          {'href': '/contact', 'caption': 'Contact'},
          ]

social_icons = [{'icon': 'social/flurl-48x48.png', 'alt': 'fb'},
                {'icon': 'social/reddit-48x48.png', 'alt': 'reddit'},
                {'icon': 'social/mixx-48x48.png', 'alt': 'mixx'},
                {'icon': 'social/stumble-48x48.png', 'alt': 'stumble'},
                {'icon': 'social/digg-48x48.png', 'alt': 'digg'},
                ]

app = Flask(__name__)


@app.route('/', defaults={'page': 'index'})
@app.route('/<page>')
def hello_world(page):
    page += '.html'
    if page != 'index.html' and page != 'about.html':
        page = 'base.html'

    print 'Log: page - ' + page
    return render_template(page, navbar=navbar, social=social_icons)


if __name__ == '__main__':
    app.run()
