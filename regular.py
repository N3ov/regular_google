import re

def main():
    # numRegex = re.compile(r'(\d{3},*?)')
    numRegex = re.compile(r'\d{1,3}(,\d{3})*')
    mo = numRegex.findall('num1:42 num2:1,234 num3:6,368,745')
    print(mo)



if __name__ == '__main__':
    main()