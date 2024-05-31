from flask import Flask, request, abort
from courses_schedule_solution import Solution
from werkzeug import exceptions

app = Flask(__name__)
sut = Solution()


@app.get('/')
def get_form():
    return '''
            <html>
            <head>
                <title>This is demo app</title>
            </head>
            <body>
            <h1>Check if courses can be finished</h1>
            <form action="/" method="POST">
                Количество курсов: <input type="number" name="numCourses"><br>
                Требования (простое разделение, e.g. 1,0;2,1(; ставится если есть еще зависимости): <input type="text" name="prerequisites"><br>
                <input id="go" type="submit" value="Отправить">
            </form>
            </body>
            </html>
        '''


@app.post('/')
def can_finish():
    try:
        numCourses = int(request.form['numCourses'])
        prerequisites_str = request.form['prerequisites']
        if prerequisites_str == '':
            return {'result': sut.canFinish(numCourses, [])}
        else:
            prerequisites = [list(map(int, pair.split(','))) for pair in prerequisites_str.split(';')]
            return {'result': sut.canFinish(numCourses, prerequisites)}
    except TypeError:
        abort(400)
    except ValueError:
        abort(400)
    except exceptions.BadRequestKeyError:
        abort(400)