total = 0


for i in 0..999 do
    if i % 5 == 0 or i % 3 == 0
        total += i
    end
end

puts total