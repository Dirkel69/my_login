# הגדרת הפונקציה הראשית
def main():
    import hashlib
    import sys

    # פונקציה שמוציאה רווחים ושורות ריקות מהקובץ
    def clear_file(txt):
        for k in range(len(txt)):
            txt[k] = txt[k].replace('\n', '')
            txt[k] = txt[k].replace(' ', '')
        for k in txt:
            if len(k) == 0:
                txt.pop(txt.index(k))
        return txt

    # פונקציית הערבול הנתונה
    def hash_passwd(passwd):
        m = hashlib.sha256()
        m.update((passwd.encode()))
        return m.hexdigest()

    # לבדוק אם התקבלו בשורת הפקודה כמות הארגומנטים שהתוכנית בנויה לעבוד איתם
    if len(sys.argv) != 3:
        print("Wrong number of arguments")
    else:
        # לנסות לבצע את המטלה
        try:
            # מסגרת לעבוד בה עם הקובץ שבו יש את הסיסמאות הלא מוצפנות
            with open(sys.argv[1], "r") as file_from:
                # מסגרת לעבוד בה עם הקובץ שבו יש את הסיסמאות המוצפנות
                with open(sys.argv[2], "w") as file_to:
                    text_from = file_from.readlines()
                    text_from = clear_file(text_from)
                    for pair in text_from:
                        pair = pair.split(':')
                        file_to.write(pair[0] + ':' + hash_passwd(pair[1]) + '\n')
            # ליצור מילון שבו השמות והסיסמאות המוצפנות
            username_password_dictionary = {}
            with open(sys.argv[2], "r") as file_from:
                text_from = file_from.readlines()
                for pair in text_from:
                    pair = pair.split(':')
                    username_password_dictionary[pair[0]] = pair[1].strip('\n')
            # לקבל קלט של שם משתמש וסיסמה מהשמשתמש
            name = input("Please enter name").replace(' ', '')
            passwd = input("Please enter password").replace(' ', '')
            # בודק אם יש שם משתמש כזה ואם יש סיסמה שמתאימה לו ומדפיס הודעה מתאימה
            if ((not username_password_dictionary.get(name) is None) and
                    username_password_dictionary[name] == hash_passwd(passwd)):
                print("Login success")
            else:
                print("Login failed")
        # אם קרתה שגיאה
        except Exception as e:
            print("Something went wrong\n(" + str(e) + ")")


# בדיקה אם הקובץ הזה מורץ כקובץ הראשי
if __name__ == "__main__":
    main()
