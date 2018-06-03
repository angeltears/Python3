# 首字母大写title 去尾空格rstrip 数转化为string 　str
name   = "ada lovelace"
print(name.title());
print(name.upper());
print(name.lower());

first_name = "ada"
last_name = 'lovelace'
full_name = first_name + " " + last_name;
print("\tHello, " + full_name.title() + '!'+ "\n");

language = "phthon                           "
print(language.rstrip() + ", hello");
language = language.rstrip()
print(language  + " , hello");

age = 23
message = "Heppy " + str(age) + "rd Birthday"
print(message)
