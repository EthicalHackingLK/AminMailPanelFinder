import dns.resolver
import os

tex = """
╭━╮╭━╮   ╭╮╭━━━╮ ╭╮    ╭━━━╮     ╭╮
┃┃╰╯┃┃   ┃┃┃╭━╮┃ ┃┃    ┃╭━━╯     ┃┃
┃╭╮╭╮┣━━┳┫┃┃┃ ┃┣━╯┣┳╮╭╮┃╰━━┳┳━╮╭━╯┣━━┳━╮
┃┃┃┃┃┃╭╮┣┫┃┃╰━╯┃╭╮┣┫╰╯┃┃╭━━╋┫╭╮┫╭╮┃┃━┫╭╯
┃┃┃┃┃┃╭╮┃┃╰┫╭━╮┃╰╯┃┃┃┃┃┃┃  ┃┃┃┃┃╰╯┃┃━┫┃
╰╯╰╯╰┻╯╰┻┻━┻╯ ╰┻━━┻┻┻┻╯╰╯  ╰┻╯╰┻━━┻━━┻╯ \n\n"""


os.system('cls' if os.name == 'nt' else 'clear')
print(tex)
domain = input("Input Domain (Ex => example.com)  =  ")
os.system('cls' if os.name == 'nt' else 'clear')
answers = dns.resolver.resolve(domain, 'MX')



for rdata in answers:
    data=open("data.txt",'a')
    data.write(str(rdata.exchange))
    data.write('\n\n')
    print("Mail Server = ",rdata.exchange,'\n')
    data.close()

p=os.getcwd()
print("Youer Data Saved In {p}\data.txt \n")
    