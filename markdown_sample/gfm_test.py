# gfm module
import gfm

# markdown file の読み込み
f = open('input.md', 'r', encoding='utf-8')
text_md = f.read()
f.close()

# html = gfm.gfm(text_md)
html = gfm.markdown(text_md)
print(html)

fw = open('output3.html', 'w', encoding='utf-8')
# fw = open('output.html', 'w')
fw.write('<html><head><meta charset="utf-8"></head>' + html + '</html>')
# fw.write(html)
fw.close()

# https://pypi.python.org/pypi/gfm/