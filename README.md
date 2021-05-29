# Shoptastic

# Customer Passwords and Details

1. Swati_Customer
        First Name: Swati_Customer
        Last Name: Srivastava
        Email: swati.btech16@gmail.com
        Username: Swati_Customer
        Password: Shoptastic
        Customer ID: 2
        
2. Pulkit Gulati
        First Name: Pulkit
        Last Name: Gulati
        Email: pulkit.gulati@gmail.com
        Username: pulkit009
        Password: Shop@1234
        Customer ID: 3
        
3. Aqib Mughal
        First Name: Aqib
        Last Name: Mughal
        Email: aqib.mughal@gmail.com
        Username: aqib007
        Password: Shop@5678
        Customer ID: 4
        
# Authentication Features

1. E-Mail field during registration must be of the form abc@pqr.xyz
2. Username field accepts alphanumeric, '_', '@', '+', '.', and '-' characters, and the maximum length allowed is 150 characters
3. Passwords of Users are encrypted using 5 hashing algorithms - Argon2PasswordHasher, BCryptSHA256PasswordHasher, BCryptPasswordHasher, PBKDF2PasswordHasher, PBKDF2SHA1PasswordHasher
4. User IDs are of the form - CUS1, CUS2, and so on, where CUS stands for Customers. This user list consists of the superusers also.
5. In case a non-registered user attempts to login, his/her username and password (with which he tried to login) will be notified in the server console, and the access will be denied

# API endpoints

1. localhost/register_login/register      # Register User
2. localhost/register_login/login         # Login User
3. localhost                              # Home page
4. localhost/mobiles/oneplus
5. localhost/mobiles/redmi9power
6. localhost/mobiles/samsunggalaxym51
7. localhost/mobiles/iphone12mini
8. localhost/mobiles/nokia3.4
9. localhost/mobiles/vivoy20
10. localhost/furniture/mdfwalldecor
11. localhost/furniture/furniturecafestool
12. localhost/furniture/woodkeyholder
13. localhost/furniture/storagecase
14. localhost/furniture/wallmirror
15. localhost/furniture/entunit
16. localhost/clothing/zeellehenga
17. localhost/clothing/bandhejsaree
18. localhost/clothing/babyjumpsuit
19. localhost/clothing/babyromper
20. localhost/clothing/mensweatshirt
21. localhost/clothing/menshirt

# Mobiles

Databases - Mobiles, Features (foreign key to Mobiles), Comments (foreign key to Mobiles and Users)
Mobiles presented - One Plus 8 Pro, Redim 9 Power, Samsung Galaxy M51, IPhone 12 Mini, Nokia 3.4, Vivo Y20

# Furniture

Databases - Furnitures, Features (foreign key to Furnitures), Comments (foreign key to Furnitures and Users)
Furniture presented - MDF Wall Decor, FurnitureCafe Stool, A10 Wood Key Holder, Hosley Wall Mirror, UniArt TV Entertainment Unit, Desire Hub Storage Case

# Clothing

Databases - Clothing, Features (foreign key to Clothing), Comments (foreign key to Clothing and Users)
Clothing presented - Zeel Lehenga, Bandhej Saree, Baby Jumpsuit, Baby Romper, Men Sweatshirt, Men shirt

# Technologies used

1. Django
2. HTML
3. CSS
4. JavaScript
5. Bootstrap
6. SQL Databases
7. REST APIs
8. Jinja
9. Cryptography
10. Github - for Project Management
