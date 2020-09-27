from flask import Flask,render_template,request
import os
import moviepy.editor as mp
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/convert',methods=['POST'])
def convert():
    path1=request.form['path']
    videoclip=mp4.VideoFileClip(path1)
    audioclip=videoclip.audio
    audioclip.write_audiofile("{}"".wav".format(path1))
    return render_template('home2.html')
if __name__ == '__main__':
    app.run()
