s c | c=='z' = 'a'
  | otherwise = succ c
p c | c=='a' = 'z'
  | otherwise = pred c
text = "pnrfne fnynq"
f 0 text= [map (s) text]
f counter text= [newtext] ++ (f (counter-1) newtext)
  where newtext=map (s) text