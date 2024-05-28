from flask import Flask, request, abort
from courses_schedule_solution import Solution
from werkzeug import exceptions

app = Flask(__name__)
sut = Solution()


@app.get('/')
def get_form():
    return '''
            <html>
            <body>
            <h1>Check if courses can be finished</h1>
            <form action="/" method="POST">
                Количество курсов: <input type="number" name="numCourses"><br>
                Требования (простое разделение, e.g. 1,0;2,1(; ставится если есть еще зависимости): <input type="text" name="prerequisites"><br>
                <input type="submit" value="Submit">
            </form>
            </body>
            </html>
        '''


@app.post('/')
def can_finish():
    try:
        numCourses = int(request.form['numCourses'])
        prerequisites_str = request.form['prerequisites']
        prerequisites = [list(map(int, pair.split(','))) for pair in prerequisites_str.split(';')]
        return {'result': sut.canFinish(numCourses, prerequisites)}
    except TypeError:
        abort(400)
    except ValueError:
        abort(400)
    except exceptions.BadRequestKeyError:
        abort(400)