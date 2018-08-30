#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+ pageId,'r').read()
    
else:
    pageId = "GOB"
    description = "hello mother fucker?"

print('''<!doctype html>
<html>
<head>
<title>당신 - test</title>
<meta charset = "utf-8">
</head>

<body>
    <h1><a href="index.py?id"> God of Billiard </a></h1>
    <ul>
      <li><a href="index.py?id=gesipan">Gesipan</a></li>
      <li><a href="index.py?id=gallery" elements title="사진첩">Gallery</a></li>
      <li><a href="index.py?id=member" elements title="회원">Member<a/></li>
      <li><a href="index.py?id=uncleHan" elements title="한준상 dㅇ_ㅇb">한준상<a/></li>
      <li><a href="index.py?id=video" elements title="동영상">Video</a></li>
      <li><a href="index.py?id=system" elements title="System">System</a></li>
    </ul>
  </div>

  <h2>{test}</h2>
  <p>{desc}</p>

  <p>
    <img src="img/cue.jpg" width="100%" height="70%">
    sadasdadadaa
  </p>

</body>
</html>
'''.format(test=pageId, desc=description))
