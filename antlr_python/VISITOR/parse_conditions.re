# re2py $INPUT -o $OUTPUT -c
%{conditions %}

def parse_conditions(yyinput):
    yycursor = 0
    yycond = YYC_INIT
    integer = -1
    word = ''
    index=0
    while True: %{
        re2c:yyfill:enable = 0;
        re2c:indent:top = 2;
        
        <INIT>  "t" :=> DEC
        <INIT>  "as" :=> WORD
        <INIT> * { return None }
        <DEC> [0-9]+  {
            index=1
            print(yystate)
            match = yyinput[index:yycursor]
            integer  = int(match.decode('utf-8'))
            index += len(match)
            break
        } 
        <DEC> * :=> WORD

        <WORD> [a-z]+ {
            match = yyinput[index:yycursor]
            word += match.decode('utf-8')
            break
        }
        <WORD> * {
            return integer,word
        }
        
    %}

out = parse_conditions(b"t43asdf\0")
print(out)
