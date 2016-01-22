# markdown
import markdown

# markdown file の読み込み
f = open('input.md', 'r', encoding='utf-8')
text_md = f.read()
f.close()

# markdown file -> html file
md = markdown.Markdown()
html = md.convert(text_md)

print(html)

fw = open('output1.html', 'w', encoding='utf-8')
fw.write('<html><head><meta charset="utf-8"></head>' + html + '</html>')
fw.close()

# http://tototoshi.hatenablog.com/entry/2014/05/17/020241