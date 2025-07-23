print("Fletcher Cheksum Emisor")
io.write("Insert message: ")
local msg = io.read("*l")
io.write("Insert fletcher type (16|32|64): ")
local f_type = io.read("*n")

local block_size = f_type/2
local mod = 2^(f_type/2) - 1

local padded_msg = msg
local padding_needed = block_size - (#msg % block_size)
if padding_needed ~= block_size then
  padded_msg = padded_msg .. string.rep("0", padding_needed)
end

local sum1 = 0
local sum2 = 0

for i = 1, #padded_msg, block_size do
  local c = padded_msg:sub(i, i + block_size - 1)
  local value = tonumber(c, 2)
  sum1 = (sum1 + value) % mod
  sum2 = (sum2 + sum1) % mod
end

local checksum = (sum2 << block_size) | sum1

local total_bits = 2 * block_size
local bin_checksum = ""
for i = total_bits - 1, 0, -1 do
  bin_checksum = bin_checksum .. ((checksum >> i) & 1)
end

local complete_msg = padded_msg .. bin_checksum

print(string.format("Checksum: " .. complete_msg))
