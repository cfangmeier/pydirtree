#!/usr/bin/env python
from sys import argv
from os import listdir
from os.path import join, isdir, expanduser, relpath, abspath

BASE_URL = "http://t3.unl.edu/~cfangmeier/"
BASE_DIR = "/home/dominguez/cfangmeier/public_html/"

IDX=0
def dirtree(path, depth=0, html=""):
    global IDX
    style = 'style="padding-left: 1em"'
    if depth == 0:
        html += "<div id='item-%d' class='collapse show' %s>\n" % (IDX, style)
    else:
        html += "<div id='item-%d' class='collapse' %s>\n" %(IDX, style)
    html += ("  "*depth) + "<div class='list-group'>\n"
    IDX+=1
    for file in listdir(path):
        rel = join(path, file)
        if isdir(rel):
            html += ("<a href='#item-%d' class='list-group-item' data-toggle='collapse'>"
                     "<i class='fas fa-chevron-right'></i>%s</a>\n") % (IDX, file)
            html += dirtree(rel, depth+1)
        else:
            url = BASE_URL + relpath(rel, BASE_DIR)
            html += "<a href='%s' class='list-group-item'>%s</a>\n" % (url, file)
    html += "</div> </div>"
    return html

if __name__ == '__main__':
    with open('index.html', 'w') as f:
        f.write('''\
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Directory Listing</title>
  </head>
<style>
.list-group.list-group-root {
  padding: 0;
  overflow: hidden;
}
.list-group.list-group-root .list-group {
  margin-bottom: 0;
}
.list-group.list-group-root .list-group-item {
  border-radius: 0;
  border-width: 1px 0 0 0;
}
.list-group.list-group-root > .list-group-item:first-child {
  border-top-width: 0;
}
.list-group.list-group-root > .list-group > .list-group-item {
  padding-left: 30px;
}
.list-group.list-group-root > .list-group > .list-group > .list-group-item {
  padding-left: 45px;
}
.list-group-item .glyphicon {
  margin-right: 5px;
}
</style>
<body>
  <div class="container">
    <div class="list-group-root well">
''')
        if len(argv) > 1:
            dir = argv[1]
        else:
            dir = expanduser('~/public_html')
        f.write(dirtree(abspath(dir)))
        f.write('''\
    </div>
  </div>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
<script defer src="https://use.fontawesome.com/releases/v5.4.1/js/all.js" integrity="sha384-L469/ELG4Bg9sDQbl0hvjMq8pOcqFgkSpwhwnslzvVVGpDjYJ6wJJyYjvG3u8XW7" crossorigin="anonymous"></script>

<script>
$(function() {
  $('.list-group-item').on('click', function() {
    $(this)
      .find('[data-fa-i2svg]')
      .toggleClass('fa-chevron-down')
      .toggleClass('fa-chevron-right');
  });

});
</script>

</body>
</html>
''')
