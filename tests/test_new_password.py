import random
import string
from password.new_password import generate_password,password_length

def test_password_():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

def test_password_length():
    password_test = len(generate_password(password_length))
    assert password_test == password_length
def test_password_diff():
    password1 = generate_password(password_length)
    password2 = generate_password(password_length)
    assert password1 != password2
"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!
Daha fazla test yazabilirseniz harika olur!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin  
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""
