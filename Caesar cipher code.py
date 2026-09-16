print("Welcome to the encryption lab. Here, you can encrypt words using the shift or Caesar Cipher.")
word = str(input("What's the original word? "))
key=int(input("What's the key?"))

a=word[0]
b=word[1]
c=word[2]
d=word[3]

ord_a_original=ord(a)
ord_b_original=ord(b)
ord_c_original=ord(c)
ord_d_original=ord(d)

ord_after_key_a = ord_a_original + key
ord_after_key_b = ord_b_original + key
ord_after_key_c = ord_c_original + key
ord_after_key_d = ord_d_original + key

a_after_mod = ord_after_key_a % 122
b_after_mod = ord_after_key_b % 122
c_after_mod = ord_after_key_c % 122
d_after_mod = ord_after_key_d % 122


encrypted_a = chr(a_after_mod)
encrypted_b = chr(b_after_mod)
encrypted_c = chr(c_after_mod)
encrypted_d = chr(d_after_mod)

print("The encrypted word is: ",encrypted_a,encrypted_b,encrypted_c,encrypted_d, sep="")








