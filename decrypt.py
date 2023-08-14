# a função lasso_letter chama uma letra e a posição para qual ela "andará"
def lasso_letter(letter, shift_amount):
    # a variável lasso_letter guardará a letra em sua forma minúscula usando o "ord" 
    lasso_letter = ord(letter.lower())
    # a variável decode_letter_code codificará para qual posição a letra andou
    decode_letter_code = lasso_letter + shift_amount
    # e decod_letter mostrará o valor codificado 
    decod_letter = chr(decode_letter_code)
    return decod_letter
print(lasso_letter('a', 3))