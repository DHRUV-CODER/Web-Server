from pathlib import Path
from flask import Flask, render_template, request, render_template_string
import os
app = Flask(__name__)


@app.route('/')
def Home():
    FILENAME = os.listdir()
    return render_template_string('''
                                  <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{FILENAME|length}} Results</title>
    <script src="https://kit.fontawesome.com/61ddec8850.js" crossorigin="anonymous"></script>
    <style>
      body {
        background: #0f0c29;  /* fallback for old browsers */
background: -webkit-linear-gradient(to right, #24243e, #302b63, #0f0c29);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #24243e, #302b63, #0f0c29); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

        color: white;
        font-family: monospace;
        font-size: 35px;
      }
      /* i {
        color: coral;
      } */
      a {
        text-decoration: none;
      }
      /* Works on Firefox */
      * {
        scrollbar-width: thin;
        scrollbar-color: grey black;
      }

      /* Works on Chrome, Edge, and Safari */
      *::-webkit-scrollbar {
        width: 7px;
      }

      *::-webkit-scrollbar-track {
        background: black;
      }

      *::-webkit-scrollbar-thumb {
        background-color: grey;
        border-radius: 20px;
        border: 1px solid black;
      }
    </style>
  </head>
  <body>
      {% for file in FILENAME %}
        {% if os.path.isdir(file) %}
          <a href="/view?file={{file}}">
            <span style="color: coral;"><i class="fas fa-folder-plus fa-small"></i></span>
            </i>
            <span style="color: aquamarine;">{{file}}</span></a>
          <br />
        {% else %}
          <a href="/view?file={{file}}">
            <span style="color:bisque;"><i class="fas fa-file-alt fa-0.5x"></i></span>
            <span style="color: greenyellow;">{{file}}</span></a></a>
            <br />
        {% endif %}
      {% endfor %}
  </body>
</html>

                                  ''', FILENAME=FILENAME, request=request, os=os)


@app.route('/view')
def view():
    filename = request.args.get('file')
    if os.path.isfile(filename):
        try:
            with open(filename) as f:
                in_text = f.read()
                No_of_lines = len(in_text.split("\n"))
                return render_template_string('''
                                       <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{file}}</title>
    <script
      src="https://kit.fontawesome.com/61ddec8850.js"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.1.0/highlight.min.js"
      integrity="sha512-z+/WWfyD5tccCukM4VvONpEtLmbAm5LDu7eKiyMQJ9m7OfPEDL7gENyDRL3Yfe8XAuGsS2fS4xSMnl6d30kqGQ=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.2.0/styles/github-dark.min.css"
      integrity="sha512-rO+olRTkcf304DQBxSWxln8JXCzTHlKnIdnMUwYvQa9/Jd4cQaNkItIUj6Z4nvW1dqK0SKXLbn9h4KwZTNtAyw=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <script>
      hljs.highlightAll();
    </script>
    <style>
      body {
        background-color: #0d1117;
        color: white;
        font-family: monospace;
        margin: 0;
      }
      .wrapper {
        display: flex;
        padding: 1rem 0.5rem;
        font-size: 1rem;
      }
      #code-display {
        padding-top: 0;
        padding-bottom: 0;
      }

      .line-numbers {
        color: #7d7d7d;
        font-family: monospace;
        text-align: end;
      }
      [data-text]::after {
        content: attr(data-text);
      }
      .line-numbers {
        font-family: monospace;
      }
      pre {
        margin: 0;
      }
      a {
        font-size: 45px;
        color: greenyellow;
        text-decoration: none;
      }
      .code {
        display: flex;
        padding: 1rem 0.5rem;
        font-size: 1rem;
      }
      /* Works on Firefox */
      * {
        scrollbar-width: thin;
        scrollbar-color: grey black;
      }

      /* Works on Chrome, Edge, and Safari */
      *::-webkit-scrollbar {
        width: 7px;
      }

      *::-webkit-scrollbar-track {
        background: black;
      }

      *::-webkit-scrollbar-thumb {
        background-color: grey;
        border-radius: 20px;
        border: 1px solid black;
      }
    </style>
  </head>
  <body>
    {% if not in_text %}
    <center>
      <h1>Such Files Can't Be Previwed , You can Download instead.</h1>
      <a
        href="./{{request.args.get('file')}}"
        download="{{request.args.get('file')}}"
      >
        <i class="fas fa-file-download"></i>
        {{request.args.get('file')}}</a
      >
    </center>
    {% else %}
    <div class="wrapper">
      <div class="line-numbers">
        {% for i in range(No_of_lines) %}
        <div><span data-text="{{i}}"></span></div>
        {% endfor%}
      </div>
      <pre><code id="code-display">{{in_text}}</code></pre>
    </div>
    {% endif %}
  </body>
</html>
     
                                  ''', in_text=in_text, os=os, No_of_lines=No_of_lines)
        except:
            return render_template_string('''
                                        <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{file}}</title>
    <script
      src="https://kit.fontawesome.com/61ddec8850.js"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.1.0/highlight.min.js"
      integrity="sha512-z+/WWfyD5tccCukM4VvONpEtLmbAm5LDu7eKiyMQJ9m7OfPEDL7gENyDRL3Yfe8XAuGsS2fS4xSMnl6d30kqGQ=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    ></script>
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.2.0/styles/github-dark.min.css"
      integrity="sha512-rO+olRTkcf304DQBxSWxln8JXCzTHlKnIdnMUwYvQa9/Jd4cQaNkItIUj6Z4nvW1dqK0SKXLbn9h4KwZTNtAyw=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <script>
      hljs.highlightAll();
    </script>
    <style>
      body {
        background-color: #0d1117;
        color: white;
        font-family: monospace;
        margin: 0;
      }
      .wrapper {
        display: flex;
        padding: 1rem 0.5rem;
        font-size: 1rem;
      }
      #code-display {
        padding-top: 0;
        padding-bottom: 0;
      }

      .line-numbers {
        color: #7d7d7d;
        font-family: monospace;
        text-align: end;
      }
      [data-text]::after {
        content: attr(data-text);
      }
      .line-numbers {
        font-family: monospace;
      }
      pre {
        margin: 0;
      }
      a {
        font-size: 45px;
        color: greenyellow;
        text-decoration: none;
      }
      .code {
        display: flex;
        padding: 1rem 0.5rem;
        font-size: 1rem;
      }
      /* Works on Firefox */
      * {
        scrollbar-width: thin;
        scrollbar-color: grey black;
      }

      /* Works on Chrome, Edge, and Safari */
      *::-webkit-scrollbar {
        width: 7px;
      }

      *::-webkit-scrollbar-track {
        background: black;
      }

      *::-webkit-scrollbar-thumb {
        background-color: grey;
        border-radius: 20px;
        border: 1px solid black;
      }
    </style>
  </head>
  <body>
    {% if not in_text %}
    <center>
      <h1>Such Files Can't Be Previwed , You can Download instead.</h1>
      <a
        href="./{{request.args.get('file')}}"
        download="{{request.args.get('file')}}"
      >
        <i class="fas fa-file-download"></i>
        {{request.args.get('file')}}</a
      >
    </center>
    {% else %}
    <div class="wrapper">
      <div class="line-numbers">
        {% for i in range(No_of_lines) %}
        <div><span data-text="{{i}}"></span></div>
        {% endfor%}
      </div>
      <pre><code id="code-display">{{in_text}}</code></pre>
    </div>
    {% endif %}
  </body>
</html>

                                  ''', in_text=None, request=request, os=os)
    elif os.path.isdir(filename):
        FILENAME = os.listdir(filename)
        return render_template_string('''
                                    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{FILENAME|length}} Results</title>
    <script src="https://kit.fontawesome.com/61ddec8850.js" crossorigin="anonymous"></script>
    <style>
      body {
        background: #0f0c29;  /* fallback for old browsers */
        background: -webkit-linear-gradient(to right, #24243e, #302b63, #0f0c29);  /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to right, #24243e, #302b63, #0f0c29); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

        color: white;
        font-family: monospace;
        font-size: 35px;
      }
      a {
        color: white;
        text-decoration: none;
      }
      /* Works on Firefox */
      * {
        scrollbar-width: thin;
        scrollbar-color: grey black;
      }

      /* Works on Chrome, Edge, and Safari */
      *::-webkit-scrollbar {
        width: 7px;
      }

      *::-webkit-scrollbar-track {
        background: black;
      }

      *::-webkit-scrollbar-thumb {
        background-color: grey;
        border-radius: 20px;
        border: 1px solid black;
      }
    </style>
  </head>
  <body>
      {% for file in FILENAME %}      
        {% if "." in file %}
          <a href="/view?file={{request.args.get('file')}}/{{file}}"><span style="color:bisque;"><i class="fas fa-file-alt fa-0.5x"></i></span> 
            <span style="color: greenyellow;">{{file}}</span>
          </a>
          <br />
        {% else %}
        <a href="/view?file={{request.args.get('file')}}/{{file}}"><span style="color: coral;"><i class="fas fa-folder-plus fa-small"></i></span>
        </i> <span style="color: aquamarine;">{{file}}</span></a>
        <br />
        {% endif %}
      {% endfor %}
      {% if not FILENAME %}
      <h1>{{FILENAME|length}} Empty Directory</h1>
      {% endif %}
  </body>
</html>

                                  ''', FILENAME=FILENAME, request=request, os=os)


app.run(port=5000)
