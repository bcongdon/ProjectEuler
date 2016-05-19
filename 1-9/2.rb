$memoize = { 1 => 1, 2 => 1}

def fib (n)
    if $memoize.has_key?(n)
        return n
    else
        $memoize[n] = fib(n-1) + fib(n-2)        
        return $memoize[n]
    end
end

a = 1
b = 1
c = 0
total = 0
while c < 4000000
    c = a + b
    if c % 2 == 0
        total += c
    end
    a = b
    b = c
end

puts total