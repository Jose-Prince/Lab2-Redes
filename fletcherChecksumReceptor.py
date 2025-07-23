print("Fletcher Cheksum Receptor")
msg = input("Message received: ")
f_type = int(input("Insert fletcher type (16|32|64): "))

block_size = f_type // 2
mod = 2**(block_size) - 1

data_bits = msg[:-f_type]
checksum_bits = msg[-f_type:]

sum2_bin = checksum_bits[:block_size]
sum1_bin = checksum_bits[block_size:]
sum1_recv = int(sum1_bin, 2)
sum2_recv = int(sum2_bin, 2)

sum1 = 0
sum2 = 0
for i in range(0, len(data_bits), block_size):
  block = data_bits[i:i + block_size]
  if len(block) < block_size:
    block = block.ljust(block_size, '0')
  value = int(block, 2)
  sum1 = (sum1 + value) % mod
  sum2 = (sum2 + sum1) % mod

is_valid = (sum1 == sum1_recv and sum2 == sum2_recv)

if is_valid:
  print("Valid Message")
else:
  print("Invalid Message")
  print("Message received: " + data_bits)
  print("sum1 received: " + str(sum1_recv))
  print("sum1 calculated: " + str(sum1))
  print("sum1 received: " + str(sum2_recv))
  print("sum1 calculated: " + str(sum2))
  
