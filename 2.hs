
testdata=")()(({[{(][{}}[{)](}){[({(}]]]]][{[)}[]){{[)]({)[[())[]}{}{{()(}{]]{]{{)]}[({(()]))))){}}}]}([[([])[{[(]]][{(()])[[[(]}{((]}[})][[{){({]}]})}[{]}[{)({{{{[((]{[])}){{)})(}{({((({[({}[}{(]}])}}[(([)([[()}}{)}}{}}]]]]{){}}}))}([])][)]{{}}([]([{}[(}}([]({{((({{{([}[]])))}]))[[{]}))])([){(}]][[])(}][)[){[{{([)(()}((]}{[]{}(([[[}](]}[})}}[]){(}}]{[}({}{[]]]}([}}}{})({[(({[([]][}]{{}[{))}}[)}(]((({}{){[}{(}(]}]()(}()}[{{{}{]([{]([{)})])(})}({]{)]{{{])[}[({]}[[(})}][))[{{[]][[(}({(]})}{])}[{{}}[}}(}}}{{((())([{]{[{]{][()}][{{(()((}]))({){){({]}(]{([]({)([[({{[[})[)()[)]]})[[{(](}({{{([([]{][({][{({[][)}]](])()({[}[()[]{([[(}}})[(([[[()){[}{}])(]((]{{{[}({[})}[{]}[]}}((}{[}]}{])}(])()()][[({[{)}{(}{)}{()(]{})})(])]({){}[(]))}}}[([[)(}[)}}{[[}}([){[}]]({{]{{}{{{})(}}]{]((){])(()}){{(}](}[][]))])]](]{}}))(){}]}][)()))([(){(}[[]([(}]}]))[[(((](]}{{({](]}]}])((]){{{}{]}[[](([{{([{}(}[}))]]}}})]])()[{]][(){})}[)}}][[(}({})(]{]([[[({{}{]]({]})[{()}[}[{)]({{}{]]([)]]}}}]{[[[))({]}](((}{[][]](}]]()(}()){[}}(][()]})][(]](])[]({)])){[{)]}[][]}}}[]{][[{(([][]({[[}((})]()()}{]){]))(){}{{)){{{}[(}]{[{[({}}]{]][]]]({}}{}{([)]}]({])()([{[)()}{{}}]}]{}]{)(([[}}(}]{{{[((}{[[{{[{{){])(]()[{)(}[]]][)}[()})([}}]])}{[(]][]{}[)()()]((}{])}}]]}{({({{]})]]{[()})[()][{})(}]]])}}{{][)[[}}[)])]([([(])([[(]][(][{())})}[]([[()]{({}))}(][)]}]}]}]}[){][]]]{{}(]}{)}{))}}{(]((]]]])())[])[[({(())()({(({(][])]([)[[)((}(([[(}[))([]}(}][}[([})){(]))){(}{][}}[{[]](}({][(])]}][}[})[[}}]][{{]){}({(}([)}[)]]{)))([({})()[(]}{(()[{({{()[[(()))([]){])]]](}{{}([])]]]}[}][](][{{[}]([()((((])][{{([]}{{}(]})(}[](}}{}][)}{)))))[([[[)]]](}({{)]{}[{)}{})[]{[]([]{(}([))]]([()((})}))(}[}({()[{]())]({{][([))[)]({}{){)[)){){)]}]][[(}(){{(])]{}]{[})]})({{)])}}]}}((]]{)}{({[{))]{({]}]})({]){[]{}]))}})(]{(({([}[(][[)({[))())))]}(({(}(]}]))[({[]}}{{[[()(){}](][))(}}{[[{)}[{](]([[}])}(({})(}}())[]{)[]{([[}[])([([}}[}(}{(}{{{[][)}[]]}([(]}(]]](][}(}}){]}}]{[}{{(}{}(}[[{{][]{}[){(}{][[{{((}))}}{]}{){}))})[(()}(]}]}[}[{]][}[(}{})[)}{)[]{}]}]{()){{[{([{)[][][}{])[)(][)]}{})][(]()(()})"

-- make (rl, rr, sl, sr, cl, cr) l [] = replicate rl ')' ++ replicate sl ']' ++ replicate cl '}'
-- make (rl, rr, sl, sr, cl, cr) l (t:testdata)
--  | t==')' = if rl==0 then "()" ++ make (rl, rr, sl, sr, cl, cr) "r" testdata else ")" ++ make (rl-1, rr, sl, sr, cl, cr) "r" testdata
--  | t=='(' = "(" ++ make (rl+1, rr, sl, sr, cl, cr) testdata
--  | t==']' = if sl==0 then "[]" ++ make (rl, rr, sl, sr, cl, cr) "s" testdata else ")" ++ make (rl, rr, sl-1, sr, cl, cr) "s" testdata
--  | t=='[' = "[" ++ make (rl, rr, sl+1, sr, cl, cr) testdata
--  | t=='{' = "{" ++ make (rl, rr, sl, sr, cl+1, cr) testdata
--  | t=='}' = if cl==0 then "{}" ++ make (rl, rr, sl, sr, cl, cr) "c" testdata else ")" ++ make (rl, rr, sl, sr, cl-1, cr) "c" testdata

make2 [] = ""
make2 (t:testdata)
 | t==')' = "()" ++ make2 testdata
 | t=='(' = "()" ++ make2 testdata
 | t==']' = "[]" ++ make2 testdata
 | t=='[' = "[]" ++ make2 testdata
 | t=='{' = "{}" ++ make2 testdata
 | t=='}' = "{}" ++ make2 testdata

-- run = make (0, 0, 0, 0, 0, 0) testdata

run2 = make3 (0,0,0) "" testdata


make3 (rl, sl, cl) l [] = replicate rl ')' ++ replicate sl ']' ++ replicate cl '}'
make3 (rl, sl, cl) l (t:testdata)
  | t==')' = if  rl==0 then "()" ++ make3 (rl, sl, cl) "r" testdata else ")" ++ make3 (rl-1, sl, cl) "r" testdata
  | t=='(' = if any (=='r') l then "(" ++ replicate (rl+1) ')' ++ make3 (0, sl, cl) "r" testdata else "(" ++ make3 (rl+1, sl, cl) "r" testdata
  | t==']' = if  sl==0 then "[]" ++ make3 (rl, sl, cl) "s" testdata else ")" ++ make3 (rl, sl-1, cl) "s" testdata
  | t=='[' = if any (=='s') l then "[]" ++ replicate (sl+1) ']' ++ make3 (rl, 0, cl) "s" testdata else "[" ++ make3 (rl, sl+1, cl) "s" testdata
  | t=='{' = if any (=='c') l then "{}" ++ replicate (cl+1) '}' ++ make3 (rl, sl, 0) "c" testdata else "{" ++ make3 (rl, sl, cl+1) "c" testdata
  | t=='}' = if  cl==0 then "{}" ++ make3 (rl, sl, cl) "c" testdata else ")" ++ make3 (rl, sl, cl-1) "c" testdata