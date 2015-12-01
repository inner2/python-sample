import markdown2

# markdown file の読み込み
f = open('input.md', 'r', encoding='utf-8')
text_md = f.read()
f.close()

html = markdown2.markdown(text_md, extras=['fenced-code-blocks'])

print(html)


fw = open('output2.html', 'w', encoding='utf-8')
# fw = open('output.html', 'w')
fw.write('<html><head><meta charset="utf-8"></head>' + html + '</html>')
# fw.write(html)
fw.close()

# link
# http://papaeye.tumblr.com/post/27705803009/markdown-処理系の比較
# http://www.mnemonic.co.jp/blog/5715999101812736