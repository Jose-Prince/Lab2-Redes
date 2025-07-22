print("Fletcher Cheksum Emisor")
io.write("Insert message: ")
local msg = io.read("*l")
io.write("Insert fletcher type (16|32|64): ")
local f_type = io.read("*n")

local block_size = f_type/2
local mod = 2^(f_type/2) - 1

local sum1 = 0
local sum2 = 0

for i = 1, #msg, block_size do
  local c = msg:sub(i, i + block_size - 1)
  if #c < block_size then
    c = c .. string.rep("0", block_size - #c)
  end
  local value = tonumber(c, 2)
  sum1 = (sum1 + value) % mod
  sum2 = (sum2 + sum1) % mod
end

local checksum = (sum2 << block_size) | sum1

local total_bits = 2 * block_size
local bin = ""
for i = total_bits - 1, 0, -1 do
  bin = bin .. ((checksum >> i) & 1)
end

print(string.format("Checksum: " .. bin))
