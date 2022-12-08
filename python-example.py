import WhileDB as wd
wd.Globals().update({"n":20,"ret":1})
wd.load_program("""
while n>0 do{
    ret=ret*n;
    n=n-1
}
""")
print(wd.Globals()["ret"])

wd.Globals().update({"n":35,"ret2":1})

wd.load_program("""
write_int(ret);
write_char(10);
while n>0 do{
    if n%2 then {
        ret2=ret2*n
    } else {
        ret2=-ret2*n
    };
    n=n-1
}
""")

print(wd.Globals())
