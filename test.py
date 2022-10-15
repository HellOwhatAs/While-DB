import WhileDB as wd
wd.update_globals({"n":20,"ret":1})
wd.load_program("""
while n>0 do{
    ret=ret*n;
    n=n-1
}
""")
print(wd.get_globals()["ret"])

wd.update_globals({"n":35,"ret2":1})

wd.load_program("""
write_int(ret);
write_char(10);
while n>0 do{
    ret2=ret2*n;
    n=n-1
}
""")

print(wd.get_globals())