from pygments.lexers.ruby import FancyLexer


class InvalidUserNameException(Exception):
    pass

class InvalidPasswordException(Exception):
    pass

class Authenticate:

    def validate_user_name(self, user_name):

        try:
            if len(user_name) < 6 or len(user_name) > 30:
                raise InvalidUserNameException("User name length should be between 6 - 30")

            if not user_name[0].isalpha():
                raise InvalidUserNameException("User name should start with a letter")

            for i in range(0, len(user_name)):
                if (ord('a') <= ord(user_name[i]) <= ord('z')) or (
                        ord('A') <= ord(user_name[i]) <= ord('Z')) or user_name[i] == '_':
                    continue
                else:
                    raise InvalidUserNameException("User Name cannot contain special charaters")
            return True
        except InvalidUserNameException as e:
            print(e)
            return False

    def validate_password(self, password):

        try:
            if len(password) < 8:
                raise InvalidPasswordException("Password Length should be greater than 8")

            have_upper = False
            have_lower = False
            have_special = False
            have_digit = False

            for i in password:
                if i.isupper():
                    have_upper = True
                elif i.islower():
                    have_lower = True
                elif i.isdigit():
                    have_digit = True
                elif i in "!@#$%^&*()-+":
                    have_special = True

            if not have_digit:
                raise InvalidPasswordException("Password Must contain a digit")

            if not have_upper:
                raise InvalidPasswordException("Password must contain a upper case letter")

            if not have_lower:
                raise InvalidPasswordException("Password must contain a lower case letter")

            if not have_special:
                raise InvalidPasswordException("password must contain a special character")

            return True
        except InvalidPasswordException as e:
            print(e)
            return False



    def validate_login(self, username, password):
        if not (self.validate_user_name(username) and self.validate_password(password)):
            print("Authentication Failed")

        else:
            print("Welcome User, {}".format(username))

a = Authenticate()
a.validate_login("barane", "e4D_rktyyjhgr*")