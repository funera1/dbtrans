# dbtrans
文字の打ち込みをちょっとだけ楽にできます。

## 使い方
#### vals.txt
dst=srcを定義します。dstに変更したい文字列、srcに打ち込む文字列を入力してください。
#### seps.txt
文字列を分割する記号を入力してください。



```python3 dbtrans.py```
を実行すると、指定したパスのファイルの文字列がvals.txtで定義した文字列に変換されます。
結果はreturn.txtに出力されます。

## 使用例

#### vals.txt
```
SELECT=sel
FROM=fr
社員=sh
```

#### seps.txt
```
*
;
```
#### input.txt
```
sel * fr sh;
```
#### return.txt
```
SELECT * FROM 社員;
```
