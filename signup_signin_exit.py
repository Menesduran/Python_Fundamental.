users = [
    ("beast", "123456"),
    ("savage", "987654"),
    ("bear", "567890")
]


def is_valid_password(password: str) -> bool:
    """Şifrenin en az 6 karakter uzunluğunda olması gerekiyor."""
    return len(password) >= 6


def sign_in(username: str, password: str) -> str:
    """Kullanıcı adı ve şifre doğruysa giriş yapar."""
    for userName, pwd in users:
        if userName == username and pwd == password:
            return "Hoş geldiniz!"
    return "Bilgiler hatalı, tekrar deneyin."


def sign_up(username: str, password: str) -> str:
    """Yeni kullanıcı kaydı yapar, kullanıcı adı tekrar etmeyecek."""
    for userName, _ in users:
        if userName == username:
            return "Bu kullanıcı adı zaten alınmış!"

    if not is_valid_password(password):
        return "Şifre en az 6 karakter olmalıdır!"

    users.append((username, password))
    print("Üyelik işlemi tamamlandı.")

    # Otomatik giriş yapmayı deniyoruz
    return sign_in(username, password)


# Kullanıcıdan giriş bilgilerini al
while True:
    action = input("Ne yapmak istiyorsunuz? (signup/signin/exit): ").strip().lower()

    if action == "signup":
        username = input("Kullanıcı adı: ").strip()
        password = input("Şifre: ").strip()
        print(sign_up(username, password))

    elif action == "signin":
        username = input("Kullanıcı adı: ").strip()
        password = input("Şifre: ").strip()
        print(sign_in(username, password))

    elif action == "exit":
        print("Çıkış yapıldı.")
        break

    else:
        print("Geçersiz giriş! Lütfen 'signup', 'signin' veya 'exit' yazın.")