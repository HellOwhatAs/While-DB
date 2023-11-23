import WhileDB as wd

print("sample_src00 :")
wd.load_program("""
n = read_int();
m = n + 1;
write_int(m + 2);
write_char(10)
""")
wd.Globals().clear()

print("sample_src01 :")
wd.load_program("""
n = read_int();
i = 2;
flag = 1;
while (flag && i * i <= n) do {
  if (n % i == 0)
  then { flag = 0 }
  else { flag = 1 };
  i = i + 1
};
if (flag)
then {
  write_char(80);
  write_char(82);
  write_char(73);
  write_char(77);
  write_char(69);
  write_char(10)
}
else {
  write_char(78);
  write_char(79);
  write_char(78);
  write_char(80);
  write_char(82);
  write_char(73);
  write_char(77);
  write_char(69);
  write_char(10)
}
""")
wd.Globals().clear()

print("sample_src02 :")
wd.load_program("""
n = read_int();
i = 0;
s = 0;
while (i < n) do {
  s = s + read_int();
  i = i + 1
};
write_int(s);
write_char(10)
""")
wd.Globals().clear()

print("sample_src03 :")
wd.load_program("""
n = read_int();
if (n >= 0)
then {
  write_int(n)
}
else {
  write_int(- n)
};
write_char(10)
""")
wd.Globals().clear()

print("Well Done !")
