import re, string

def main():
    feature_data = open('feature.txt','r')
    for line in feature_data:
        message = re.sub('https?:\/\/.*[\r\n]*','',line)
        print message

if __name__ == '__main__':
    main()
