def sha1(message):
    # Инициализация переменных
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    
    # Преобразование сообщения в байты
    message = bytearray(message, 'utf-8')
    
    # Дополнение сообщения до кратности 512 битам
    original_length_bits = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)
    message += original_length_bits.to_bytes(8, byteorder='big')
    
    # Функция циклического сдвига влево
    def left_rotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF
    
    # Функция преобразования блока
    def process_chunk(chunk, h0, h1, h2, h3, h4):
        w = [0] * 80
        
        # Разбиение блока на 16 слов по 32 бита
        for i in range(16):
            w[i] = int.from_bytes(chunk[i*4:i*4+4], byteorder='big')
        
        # Расширение блока до 80 слов
        for i in range(16, 80):
            w[i] = left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)
        
        # Инициализация переменных
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        
        # Основной цикл
        for i in range(80):
            if i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            
            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        
        # Обновление хеш-значений
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF
        
        return h0, h1, h2, h3, h4
    
    # Обработка сообщения блоками
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        h0, h1, h2, h3, h4 = process_chunk(chunk, h0, h1, h2, h3, h4)
    
    # Формирование хеш-значения
    hash_result = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4
    return '%040x' % hash_result

# Пример использования
message = input("Введите текст для хеширования: ")
hashed_message = sha1(message)
print("Хеш SHA-1:", hashed_message)
