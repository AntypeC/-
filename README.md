# Downloading books from http://www.kdxx.net/ using Download_epub.py

1. Find the index of the book, e.g. ```91818``` from the URL http://www.kdxx.net/txt/91818.html and run ```Download_epub.py``` with the ```book_index``` set to it.

2. Use the edit tool in Calibre to replace the book thumbnail ```cover.png```, modify the chapter title wrapped in ```<h2></h2>``` and remove the scrapped artifact of the site using Find & Replace all, e.g. :
```calibre, version 7.16.0
Searching done: <p>Performed the replacement at 872 occurrences of       &lt;a href="http://www.kdxx.net"&gt;首页&lt;/a&gt; &gt;
      &lt;a href="/class/kehuanchiyuan/1/"&gt;科幻次元&lt;/a&gt; &gt;
```
```calibre, version 7.16.0
Searching done: <p>Performed the replacement at 872 occurrences of &lt;div&gt;&lt;a href="javascript:report()"&gt;章节报错(免登录)&lt;/a&gt;
```
And use the Regex tool to delete all replicating chapter title by entering ```^\s*第\d+章\s+[^\n]*\n``` in the search field. To create a Table of Content, delete the default ```toc.xhtml```, go to Tools > Table of Contents > Edit Table of Contents, Ctrl+A to select all and hit the recycle button to Remove all selected entries. Then, click on "Generate ToC from major headings" and hit OK. Now, to create an appendix, go back to Tools > Table of Contents, select "Insert inline Table of Contents" and place the new ```toc.xhtml``` into the original position of the default.

 3. Next, to make sure the GuanKiapTsingKhai.ttf font applies properly to the text without being too crammed, use the following stylesheet for the text, body and title of the book:

 ```
.p { /* text */
  display: block;
  font-size: 1.2em;
  line-height: 125%;
  orphans: 0;
  text-indent: 0;
  widows: 0;
  margin: 5px 0 0;
}

#booktxt { /* body */
  display: block;
  font-size: 0.83333em;
  orphans: 0;
  widows: 0;
  margin: 0 5pt;
  padding: 0;
}

#toc_1 { /* title */
  display: block;
  font-size: 1.55em;
  font-weight: bold;
  line-height: 125%;
  text-align: center;
  text-shadow: 1px 1px 1px #333;
  margin: 0 0 1.2em;
  padding: 10px 0;
  border-top: #C1CCC0 none 0;
  border-right: #C1CCC0 none 0;
  border-bottom: #C1CCC0 dotted 1px;
  border-left: #C1CCC0 none 0;
}
```

4. Lastly, install and use the Modify ePub plugin, under HTML & Styles, check the options for "Encode HTML in UTF-8", "Remove embedded fonts", "Modify @page and body margin styles" and "Smarten punctuation" and hit apply. Then install and use the plugin "Convert Chinese Text Simplified/Traditional" and apply it for text-type and punctuation (there's also option for converting Horizontal Text to Vertical Text), select the following:
Simplified to Traditional, Output: Taiwan, Update quotes, Entire eBook

If Send to Kindle fails to work for the epub file, use Amazon Kindle EPUB Fix: https://kindle-epub-fix.netlify.app/

# 製作與轉換適合Kindle中文直書直排之Mobi格式電子書

Following the GUIDE from: 
https://wshareit.blogspot.com/2018/06/kindle.html (fonts compatible for Vertical Text)
https://wshareit.blogspot.com/2017/11/kindle-8-for-mac.html (how to edit epub)

1. Convert books > Look & feel > Styling, paste:

```
@page{
margin:5%;
}

body{
-epub-writing-mode: vertical-rl;   /*直式設定 for epub*/
-epub-line-break: normal;          /*斷行設定 for epub*/
-webkit-writing-mode: vertical-rl; /*直式設定*/
-webkit-line-break: normal;        /*斷行設定*/
line-break: strict;                /*斷行設定,參數(normal , auto , strict)*/
writing-mode: vertical-rl;         /*直式設定 for Kindle*/
line-height: 1.4;                  /*控制行間距(可忽略)*/
text-indent: 2em;                  /*首行空兩格*/
margin: 3%;
}
```

2. 在 ```content.opf``` 中要搜尋修改這三個部分，也就是轉換直排中文的關鍵之一
這部分非常重要！非常重要！非常重要！
若有一個部分沒改好或是錯誤就影響繁體中文直排的樣式。

①變更「繁體中文直排與標點」與「Kindle左右邊界留空」
搜尋 ```<dc:language>zh</dc:language>``` 改為
```<dc:language>zh-tw</dc:language>```

②是設定由「左往右的直排格式」
通常是搜尋不到這部份，直接在 ```<dc:language>zh</dc:language>``` 下一列加入即可

```<meta content="vertical-rl" name="primary-writing-mode" />```

③是變更「翻頁方向由右至左」
搜尋 ```<spine toc="ncx">``` 改為
```<spine page-progression-direction="rtl" toc="ncx"> ```

Also, use the find & replace feature in the editor for all the text files as nessesary for any wrong punctuation. Then, format the text-type and punctuation of the book with the plugin "Convert Chinese Text Simplified/Traditional" using the aforementioned specifications.

Download Zhuyin TTF font compatible for Chinese Vertical Text online & install it by dragging it into the "fonts" folder, the default font messes up the punctuation of Chinese Vertical Text.

IMPORTANT NOTE: When uploading to Kindle, Calibre removes Chinese Vertical Text and "Right to Left" when converting epub to mobi therefore it is removed. This process occures automatically when an epub is sent to Kindle. To solve this, convert epub to azw3, and edit the azw3 before sending it to Kindle (remove any mobi conversion that might've been done previously). Alternatively, you can just send the epub directly through https://www.amazon.com/sendtokindle, or by emailing @kindle.com.