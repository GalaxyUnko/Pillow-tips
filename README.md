# Pillow-tips
tips for Pillow

http://snowman-88888.hatenablog.com/entry/2016/03/08/115918

## PILで画像をロードできないときに確認すること

解決法としては、

from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

を追加するだけで良いらしい。

どうやらPILは極端に大きな画像など高速にロードできない画像はロードしないで見過ごす仕様になっているらしい。
デフォルトでFalseになっているLOAD_TRUNCATED_IMAGESをTrueにすることできちんとロードするようになった。
