html = """<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="./css/project.css">
        <title>Project </title>
    </head>
    <body>

        <header>
            <h1>Project Re:build</h1>
        </header>

        <nav>
            <a href="./index.html">ホーム</a>
            <a href="#">カテゴリ1</a>
            <a href="#">カテゴリ2</a>
            <a href="#">カテゴリ3</a>
        </nav>

        

        <section>
            <article>
                <h2>Project Re:buildとは？</h2>
                <p>Project Re:buildとは本来捨てられるハズの端材などの廃棄物からまた新しくものを作るプロジェクトです。</p>
                <p>年間で木材だけでも約８００万トンを超える量が発生していますがその大部分が再利用されずに焼却・埋め立て処分されています。</p>
                <p>私はそれを使って新たな形をビルドできないか考え、その結果がこの"Project Re:BUILD"なのです。</p>
            </article>

            <article>
                <h2><a href=""></a>Project1 3Dプリンターのフィラメントを利用したキーホルダー</h2>
                <p>ここに別の記事の本文が入ります。</p>
            </article>
        </section>

        <footer>
            <p>&copy; 2023 Project Re:build</p>
        </footer>

    </body>
</html>
"""

CSS= """ body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
     }

            header {
                background-color: #0000ff;
                color: #000000;
                padding: 10px;
                text-align: center;
            }

            nav {
                background-color: #555;
                color: #fff;
                padding: 10px;
                text-align: center;
            }

            nav a {
                color: #fff;
                text-decoration: none;
                margin: 0 10px;
            }

            section {
                padding: 20px;
            }

            article {
                background-color: #fff;
                padding: 20px;
                margin-bottom: 20px;
            }

            footer {
                background-color: #333;
                color: #fff;
                padding: 10px;
                text-align: center;
            }


"""

#my-page.(拡張子)を作るよって指示。これでHTMLとCSSが自動で生成される。
with open("project.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("project.css", "w", encoding="utf=8") as f:
    f.write(CSS)
