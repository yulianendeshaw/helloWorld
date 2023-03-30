from flask import Flask,render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Yulian Endeshaw! I am adding my first code change'
@app.route('/favorite-course')
def favorite_course():  # put application's code here
    print('Your favorite course name:' + request.args.get('subject'))
    print('Your favorite course number:' + request.args.get('course_number'))
    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():  # put application's code here
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')



if __name__ == '__main__':
    app.run()
@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/homepage')
def homepage():  # put application's code here
    return render_template('homepage.html')