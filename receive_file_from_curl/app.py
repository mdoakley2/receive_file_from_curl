#!/home/mark/work/Flask/flask/bin/python

# Program to receive one or more files from a "curl" command
# and save the contents to a local file.

from flask                   import Flask, request
from werkzeug.datastructures import FileStorage

# FileStorage is described in:
#     https://werkzeug.palletsprojects.com/en/3.0.x/datastructures/
    
app = Flask(__name__)

@app.route("/", methods=['POST'])
def receive_and_save():

    target_dir = '/tmp/'

    print('\n\n*************************************')
    n = 0
    for i in request.files:
        n += 1
        filename = request.files[i].filename
        print('file number   :  ', n)
        print('curl file id  :  ', i)
        print('file name     :  ', filename)
        print('\nSaving file to ', target_dir + filename + '\n')
        request.files[i].save(target_dir + filename)
        print (target_dir + filename, ' now saved')
          
        print('*************************************')
    
    print('\n\n')

    return "\n  --- File(s) now saved ---\n\n"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
