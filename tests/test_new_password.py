import string
from password.new_password import generate_password,password_length

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters
def test_password_len():
    for length in range (1,21):
        assert length == len(generate_password(length))

def test_password_randomness():
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2,"Arka arkaya oluşturulan 2 şifre aynı olmamalıdır."



"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin  
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""
#1
def test_password_len():
    """Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test eder"""
    for length in range(1,21):
        assert length == len(generate_password(length))
    
#2
def test_password_is_unique():
    """Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test eder"""
    password1 = generate_password(10)
    password2 = generate_password(10)
    assert password1 != password2

